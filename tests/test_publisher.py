from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

import publisher

NOW = datetime(2026, 11, 12, 6, 0, tzinfo=timezone.utc)


def article(slug='prompt-caching', **changes):
    return {'title': 'Reduce latency with prompt caching', 'source': 'OpenAI',
            'url': f'https://openai.com/news/{slug}/', 'kind': 'article',
            'published_at': '2026-11-11T12:00:00Z', 'topics': ['cost', 'latency'],
            'summary': ' '.join(f'word{index}' for index in range(40)),
            'action': 'Benchmark repeated prompts and compare latency.', **changes}


def report(*items):
    return {'sources': {'openai': {'name': 'OpenAI', 'stale': False, 'error': None}}, 'items': list(items)}


class SelectionTests(unittest.TestCase):
    def test_records_credit_dates_and_short_excerpt(self):
        entry, = publisher.candidates(report(article()), [], NOW)
        self.assertEqual(entry['published_at'], '2026-11-11T12:00:00Z')
        self.assertEqual(entry['added_at'], '2026-11-12T06:00:00Z')
        self.assertTrue(entry['automated'])
        self.assertEqual(len(entry['excerpt'].removesuffix(' …').split()), 25)
        self.assertIn('https://openai.com/news/prompt-caching', publisher.render_article(entry))

    def test_tracking_links_and_fragments_do_not_create_duplicates(self):
        items = report(article(), article(url='https://www.openai.com/news/prompt-caching?utm_source=mail#section'))
        selected = publisher.candidates(items, [], NOW)
        self.assertEqual(len(selected), 1)
        self.assertEqual(publisher.candidates(items, selected, NOW), [])

    def test_old_future_and_reference_items_are_excluded(self):
        items = report(article(published_at='2026-01-01T00:00:00Z'), article(published_at='2027-01-01T00:00:00Z'), article(kind='guide'))
        self.assertEqual(publisher.candidates(items, [], NOW), [])

    def test_unknown_hosts_credentials_and_unsafe_schemes_are_excluded(self):
        items = report(*(article(url=url) for url in ['https://evil.example/post', 'https://name:password@openai.com/post', 'javascript:alert(1)', 'https://openai.com:8443/post']))
        self.assertEqual(publisher.candidates(items, [], NOW), [])

    def test_stale_source_fails_instead_of_importing_cached_articles(self):
        data = report(article())
        data['sources']['openai']['stale'] = True
        with self.assertRaisesRegex(ValueError, 'No fresh publishers'):
            publisher.candidates(data, [], NOW)

    def test_partial_failure_keeps_only_articles_from_live_publishers(self):
        data = report(article(), article(source='NVIDIA', url='https://developer.nvidia.com/blog/example'))
        data['sources']['nvidia'] = {'name': 'NVIDIA', 'stale': True, 'error': 'unavailable'}
        self.assertEqual([entry['source'] for entry in publisher.candidates(data, [], NOW)], ['OpenAI'])

    def test_limits_recent_imports_and_does_not_invent_entries(self):
        data = report(article('first'), article('second'))
        self.assertEqual(len(publisher.candidates(data, [], NOW, limit=1)), 1)
        self.assertEqual(publisher.candidates(report(), [], NOW), [])

    def test_untrusted_titles_cannot_insert_html_or_markdown_links(self):
        entry, = publisher.candidates(report(article(title='<script>bad()</script>[click](https://evil.example)')), [], NOW)
        rendered = publisher.render_article(entry)
        self.assertNotIn('<script>', rendered)
        self.assertIn('\\[click\\]', rendered)


class PublishingTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / 'README.md').write_text('# Readings\n\n' + publisher.START + '\n\nEmpty\n\n' + publisher.END + '\n')
        publisher.git(self.root, 'init', '-b', 'main')
        publisher.git(self.root, 'config', 'user.name', 'Publisher Test')
        publisher.git(self.root, 'config', 'user.email', 'publisher@example.test')
        publisher.git(self.root, 'add', 'README.md')
        publisher.git(self.root, 'commit', '-m', 'Initialize reading list')

    def test_one_commit_per_article_and_repeat_run_changes_nothing(self):
        data = report(article('first'), article('second'))
        added = publisher.publish(self.root, data, now=NOW, commit=True)
        self.assertEqual(len(added), 2)
        self.assertEqual(publisher.git(self.root, 'rev-list', '--count', 'HEAD'), '3')
        for revision in ['HEAD', 'HEAD~1']:
            names = publisher.git(self.root, 'diff-tree', '--no-commit-id', '--name-only', '-r', revision).splitlines()
            self.assertEqual(len([name for name in names if name.startswith('articles/')]), 1)
            self.assertIn('README.md', names)
            self.assertIn('data/articles.json', names)
            self.assertIn('Automated feed import', publisher.git(self.root, 'show', '-s', '--format=%B', revision))
        previous = publisher.git(self.root, 'rev-parse', 'HEAD')
        self.assertEqual(publisher.publish(self.root, data, now=NOW, commit=True), [])
        self.assertEqual(publisher.git(self.root, 'rev-parse', 'HEAD'), previous)
        self.assertEqual(publisher.git(self.root, 'status', '--porcelain'), '')

    def test_no_articles_create_no_files_or_commits(self):
        self.assertEqual(publisher.publish(self.root, report(), now=NOW, commit=True), [])
        self.assertFalse((self.root / 'data/articles.json').exists())
        self.assertEqual(publisher.git(self.root, 'rev-list', '--count', 'HEAD'), '1')

    def test_commit_mode_rejects_a_dirty_checkout(self):
        (self.root / 'personal.txt').write_text('Do not accidentally commit this file')
        with self.assertRaisesRegex(ValueError, 'clean'):
            publisher.publish(self.root, report(article()), now=NOW, commit=True)
        self.assertFalse((self.root / 'articles').exists())

    def test_missing_readme_markers_fail_before_writing_entries(self):
        (self.root / 'README.md').write_text('Missing markers')
        with self.assertRaisesRegex(ValueError, 'markers'):
            publisher.publish(self.root, report(article()), now=NOW)
        self.assertFalse((self.root / 'articles').exists())


if __name__ == '__main__':
    unittest.main()
