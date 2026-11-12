# SPDX-License-Identifier: GPL-3.0-only
"""Publish attributed AI reading entries, with one commit per new source URL."""
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import html
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import parse_qsl, quote, urlencode, urlsplit, urlunsplit

HOSTS = {
    'OpenAI': 'openai.com', 'Anthropic / Claude': 'anthropic.com',
    'n8n': 'blog.n8n.io', 'Google AI': 'blog.google',
    'Google Developers': 'developers.googleblog.com', 'Google Research': 'research.google',
    'Hugging Face': 'huggingface.co', 'Cloudflare': 'blog.cloudflare.com',
    'NVIDIA': 'developer.nvidia.com',
}
START, END = '<!-- articles:start -->', '<!-- articles:end -->'


def clean(value, limit=260):
    return ' '.join(html.unescape(re.sub(r'<[^>]*>', '', str(value or ''))).split())[:limit]


def markdown(value):
    value = html.escape(clean(value, 1000), quote=False)
    for character in '\\`*_[]|':
        value = value.replace(character, '\\' + character)
    return value


def canonical_url(value, source):
    parts = urlsplit(str(value))
    host = (parts.hostname or '').lower().removeprefix('www.')
    if parts.scheme != 'https' or parts.username or parts.password or parts.port not in (None, 443):
        raise ValueError('Source URL must be HTTPS without credentials or a custom port')
    if host != HOSTS.get(source):
        raise ValueError('Article URL must belong to its official publisher')
    query = [(key, value) for key, value in parse_qsl(parts.query)
             if not key.lower().startswith('utm_') and key.lower() not in {'ref', 'fbclid', 'gclid'}]
    path = quote(parts.path.rstrip('/') or '/', safe='/%:@-._~!$&+,;=')
    return urlunsplit(('https', host, path, urlencode(sorted(query)), ''))


def iso(value):
    return value.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


def candidates(report, existing, now, *, limit=20, lookback_days=14):
    fresh = {value['name'] for value in report.get('sources', {}).values()
             if not value.get('stale', True) and not value.get('error')}
    if not fresh:
        raise ValueError('No fresh publishers available; cached articles will not be presented as new')
    known = {entry['id'] for entry in existing}
    result = []
    for item in report.get('items', []):
        if item.get('kind') != 'article' or item.get('source') not in fresh:
            continue
        try:
            published = datetime.fromisoformat(item['published_at'].replace('Z', '+00:00'))
            if published.tzinfo is None or not now - timedelta(days=lookback_days) <= published <= now:
                continue
            url = canonical_url(item['url'], item['source'])
            title = clean(item['title'], 220)
            if not title:
                continue
        except (KeyError, TypeError, ValueError, AttributeError):
            continue
        identity = hashlib.sha256(url.encode()).hexdigest()[:24]
        if identity in known:
            continue
        known.add(identity)
        topics = sorted({topic for topic in item.get('topics', []) if topic in {'cost', 'latency', 'build'}})
        excerpt_words = clean(item.get('summary'), 2000).split()
        excerpt = ' '.join(excerpt_words[:25]) + (' …' if len(excerpt_words) > 25 else '')
        result.append({
            'id': identity, 'title': title, 'url': url, 'source': item['source'],
            'published_at': iso(published), 'added_at': iso(now), 'topics': topics,
            'excerpt': excerpt, 'practice': clean(item.get('action'), 400),
            'path': f'articles/{published:%Y-%m}/{identity}.md', 'automated': True,
        })
    # A first run starts with recent articles, rather than a large historical import.
    return sorted(result, key=lambda item: (item['published_at'], item['id']), reverse=True)[:limit]


def render_article(entry):
    lines = [f"# {markdown(entry['title'])}", '',
             f"**Publisher:** {markdown(entry['source'])}  ",
             f"**Published:** {entry['published_at'][:10]}  ",
             f"**Added to this reading list:** {entry['added_at']}  ",
             f"**Topics:** {', '.join(entry['topics']) or 'AI engineering'}", '',
             f"[Read the original article]({entry['url']})", '']
    if entry['excerpt']:
        lines += ['Publisher excerpt (up to 25 words):', '', f"> {markdown(entry['excerpt'])}", '']
    if entry['practice']:
        lines += ['## Practice idea', '', markdown(entry['practice']), '',
                  '*This is a keyword-based suggestion, not evidence that the experiment has been completed.*', '']
    lines += ['---', '', 'Automatically collected from an official publisher. '
              'The article and excerpt belong to their original publisher; this repository provides an attributed reading entry.', '']
    return '\n'.join(lines)


def render_index(entries):
    if not entries:
        return 'The first collection will appear here after the publisher runs.\n'
    lines = [f"**{len(entries)} reading entries** · Latest 30 below · [Full catalog](data/articles.json)", '']
    for entry in sorted(entries, key=lambda item: (item['published_at'], item['id']), reverse=True)[:30]:
        lines.append(f"- **{entry['published_at'][:10]} · {markdown(entry['source'])}** — "
                     f"[{markdown(entry['title'])}]({entry['path']})")
    return '\n'.join(lines) + '\n'


def git(root, *arguments, env=None):
    return subprocess.run(['git', '-C', str(root), *arguments], check=True,
                          text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env).stdout.strip()


def publish(root, report, *, now=None, limit=20, lookback_days=14, commit=False):
    root = Path(root).resolve()
    now = now or datetime.now(timezone.utc)
    catalog_path = root / 'data/articles.json'
    entries = json.loads(catalog_path.read_text()) if catalog_path.exists() else []
    if not isinstance(entries, list):
        raise ValueError('The article catalog is invalid')
    selected = candidates(report, entries, now, limit=limit, lookback_days=lookback_days)
    if not selected:
        return []
    readme = (root / 'README.md').read_text()
    if readme.count(START) != 1 or readme.count(END) != 1 or readme.index(START) >= readme.index(END):
        raise ValueError('README index markers are missing or malformed')
    if commit and git(root, 'status', '--porcelain', '--untracked-files=normal'):
        raise ValueError('The checkout must be clean before publishing')
    commit_env = dict(os.environ)
    for key in ('GIT_AUTHOR_DATE', 'GIT_COMMITTER_DATE'):
        commit_env.pop(key, None)  # Commit dates always reflect the real run.
    added = []
    for entry in selected:
        target = root / entry['path']
        if target.exists():
            raise ValueError('An article file exists outside the catalog; inspect it before continuing')
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_article(entry), encoding='utf-8')
        entries.append(entry)
        catalog_path.parent.mkdir(parents=True, exist_ok=True)
        catalog_path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        before, rest = readme.split(START)
        _, after = rest.split(END)
        (root / 'README.md').write_text(before + START + '\n\n' + render_index(entries) + '\n' + END + after, encoding='utf-8')
        if commit:
            git(root, 'add', '--', entry['path'], 'data/articles.json', 'README.md')
            git(root, 'commit', '-m', f"content: add {entry['source']} reading — {entry['title']}",
                '-m', f"Source: {entry['url']}\nAutomated feed import; original article credited to its publisher.", env=commit_env)
        added.append(entry)
    return added


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).parent)
    parser.add_argument('--report', type=Path, help='Use a saved feed report instead of fetching')
    parser.add_argument('--cache', type=Path, default=Path('.cache/feed.json'))
    parser.add_argument('--limit', type=int, default=20)
    parser.add_argument('--lookback-days', type=int, default=14)
    parser.add_argument('--commit', action='store_true', help='Make one local commit per new article; does not push')
    args = parser.parse_args(argv)
    if not 1 <= args.limit <= 60 or not 1 <= args.lookback_days <= 90:
        parser.error('limit must be 1–60 and lookback-days must be 1–90')
    try:
        if args.report:
            report = json.loads(args.report.read_text())
        else:
            from ai_learning_feed.cli import collect
            report, code = collect(args.cache, limit=60)
            if code:
                raise ValueError('All live sources failed; no articles were published')
        added = publish(args.root, report, limit=args.limit, lookback_days=args.lookback_days, commit=args.commit)
        print(json.dumps({'added': len(added), 'articles': [{'title': entry['title'], 'path': entry['path']} for entry in added]}))
        if os.environ.get('GITHUB_STEP_SUMMARY'):
            with open(os.environ['GITHUB_STEP_SUMMARY'], 'a', encoding='utf-8') as summary:
                summary.write(f"Published {len(added)} new attributed reading entries. No duplicate or filler commits.\n")
                for source in report.get('sources', {}).values():
                    if source.get('error') or source.get('stale'):
                        summary.write(f"- {markdown(source['name'])}: unavailable or stale; skipped.\n")
        return 0
    except (OSError, ValueError, ImportError, subprocess.CalledProcessError) as error:
        print(f'Publisher failed: {error}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
