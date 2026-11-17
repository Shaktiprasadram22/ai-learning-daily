# AI Learning Daily

An automatically maintained reading list for practical AI engineering: **lower costs, faster inference, and better systems**.

Each entry links to the original publisher, keeps its publication date, includes a short attributed excerpt, and offers a keyword-based practice idea. These are reading resources, not claims that the linked work or suggested experiments were completed by this repository's maintainer.

<!-- articles:start -->

**50 reading entries** · Latest 30 below · [Full catalog](data/articles.json)

- **2026-11-16 · NVIDIA** — [Post-Training NVIDIA Nemotron to Increase Accuracy in Your Scientific Domain](articles/2026-11/e5e272e7744c80be5ffb799c.md)
- **2026-11-16 · NVIDIA** — [NVIDIA Vera Rubin NVL72 Leads Agentic Inference Performance on MLPerf Endpoints v1.0](articles/2026-11/bd4930e0839976d3ed7ae4ae.md)
- **2026-11-16 · NVIDIA** — [NVIDIA Vera Rubin NVL72 Achieves up to 2x Blackwell Ultra Performance in MLPerf Training v6.1](articles/2026-11/7ec90737528b7237217e7205.md)
- **2026-11-16 · n8n** — [AI made integrations the vendor’s problem](articles/2026-11/3f55c7d30161021585230a4b.md)
- **2026-11-16 · OpenAI** — [Our first phase of embedded assessments](articles/2026-11/9fe6d2ae73e55f52b8078f18.md)
- **2026-11-16 · OpenAI** — [More ways to move care forward with ChatGPT for Healthcare](articles/2026-11/21e886491b30cfff0403f0b9.md)
- **2026-11-16 · OpenAI** — [Advancing computer-use agents for healthcare teams](articles/2026-11/21b4758ab52123ac78ffa3db.md)
- **2026-11-16 · Google Developers** — [Agents are sessions, not requests: size GKE node pools for AI agent sessions](articles/2026-11/d4dd27aa4150d5d5e7ff227e.md)
- **2026-11-16 · Google Developers** — [Securing Your Agents: A Hands-On Guide to Agent Anomaly Detection](articles/2026-11/8b718dabaac7aeb3b971360f.md)
- **2026-11-13 · Cloudflare** — [Kitesurf is now open source](articles/2026-11/a443b3b05538516102c1262d.md)
- **2026-11-13 · NVIDIA** — [Run Native DLA Inference in Python on NVIDIA Jetson AGX Orin Using cuDLA](articles/2026-11/b46b6bb43e745acd7c60d611.md)
- **2026-11-13 · OpenAI** — [Introducing ChatGPT Wallet](articles/2026-11/7d4d71d056da02862d0b2ec1.md)
- **2026-11-13 · OpenAI** — [Shield helps technicians hand off legacy portal work with OpenAI](articles/2026-11/a99dfdd20d85acbbb850aa77.md)
- **2026-11-13 · Anthropic / Claude** — [Building strong safety evaluations](articles/2026-11/43af641572cb998c4f69a130.md)
- **2026-11-12 · OpenAI** — [How Amplitude ships product improvements in 1–2 days with OpenAI](articles/2026-11/67672a694e389b29af5588bf.md)
- **2026-11-12 · Google Developers** — [How Agent Anomaly Detection scores on benchmarks we didn't write](articles/2026-11/d99b7127f7fd99e6149610b8.md)
- **2026-11-12 · Hugging Face** — [The Definitive Fine-Tuning Guide for 3D Generation Models](articles/2026-11/cbda9238a3684b28e47a3f03.md)
- **2026-11-11 · NVIDIA** — [Validating GPU Platforms with Runtime AI Inventory via the NVIDIA DSX AI Factory](articles/2026-11/4b30bf9e8a4d0303bec665cd.md)
- **2026-11-11 · Hugging Face** — [BotPsy: On-Device Personal Assistant with a Sub-Billion-Parameter Agentic Language Model](articles/2026-11/19b4fcb1faac9c9bdbccd358.md)
- **2026-11-11 · Google Developers** — [A2UI 1.0: Build delightful, fast, reliable, agentic experiences](articles/2026-11/740de2548ad8f4689ad7f676.md)
- **2026-11-11 · OpenAI** — [JioStar’s chief architect on AI discovery at 500M-user scale](articles/2026-11/55ff14dc4213127df72a8039.md)
- **2026-11-10 · n8n** — [Build Safer n8n Agents and Workflows with Google Gemini 4 Carbon](articles/2026-11/26a090d137e1aeb75b70910d.md)
- **2026-11-10 · NVIDIA** — [Agent Substrate: Advancing Kubernetes for Agents at Scale](articles/2026-11/a8c416e2c7748124802b5f5d.md)
- **2026-11-10 · NVIDIA** — [Start and Restore GPU Workloads in Seconds with NVIDIA Snapshot](articles/2026-11/25d05ca668539a6649120826.md)
- **2026-11-10 · n8n** — [Meet Nod: a standalone personal agent from n8n Labs that runs on your computer](articles/2026-11/5460776ef92cacf5d941db2b.md)
- **2026-11-10 · OpenAI** — [Cogent and OpenAI build cyber defense factories for enterprises](articles/2026-11/37e4452e64c861cffe83ba46.md)
- **2026-11-09 · OpenAI** — [CodeRabbit scales agentic software development and ships 20x more](articles/2026-11/02e9abf47eaf3fa01f98fe0d.md)
- **2026-11-06 · NVIDIA** — [Speed Up Image Generation with FLUX 3 Image Klein on NVIDIA Blackwell GPUs](articles/2026-11/4e0aa3919fe104e56d23bd7a.md)
- **2026-11-06 · NVIDIA** — [Accelerating Reinforcement Learning Weight Refit with the Reshard Collective](articles/2026-11/581dcf5cabc7cf1758ba78bb.md)
- **2026-11-06 · Anthropic / Claude** — [The components of agent memory](articles/2026-11/9bd43ba4c2466855b9f0d164.md)

<!-- articles:end -->

## How it works

A daily external scheduler starts the GitHub Actions publisher at **10:00 AM Asia/Kolkata**. The publisher uses [AI Learning Feed](https://github.com/Shaktiprasadram22/ai-learning-feed), pinned to a specific source revision, to read official feeds and article indexes.

- Sources: OpenAI, Anthropic / Claude, n8n, Google AI, Google Developers, Google Research, Hugging Face, Cloudflare, and NVIDIA Developer.
- Each previously unseen article creates **one commit** containing its entry and updated reading index.
- URL-based duplicate detection survives repeated runs and tracking-link variations.
- Up to 20 new entries per run, published within the last 14 days. The first run imports recent articles; publication dates remain distinct from collection dates.
- Unavailable publishers are skipped. A complete source outage fails the run. A day without new articles creates no empty or filler commits.
- No AI model, paid API, database, or full-text article copying. Descriptions are short publisher excerpts, not AI-written summaries; practice ideas are keyword-based templates.

Open **Actions → Publish AI readings → Run workflow** to collect on demand. The public workflow uses GitHub's temporary repository token; no personal credential is stored in this repository.

## Run locally

Requires Python 3.10+ and Git. Clone this project and its feed engine into adjacent directories:

```sh
git clone https://github.com/Shaktiprasadram22/ai-learning-daily.git
git clone https://github.com/Shaktiprasadram22/ai-learning-feed.git
git -C ai-learning-feed checkout 1f1acf43366403348eebbb79678e0f3426490de6
cd ai-learning-daily
python3 -m unittest discover -s tests -v
PYTHONPATH=../ai-learning-feed python3 publisher.py
```

The last command writes entries locally without committing. Start from a clean checkout and use `--commit` to create one commit per entry; configure your Git author first. Pushing is a separate action. `--report report.json` accepts a saved AI Learning Feed export for offline testing.

The full machine-readable catalog lives in [data/articles.json](data/articles.json); Markdown entries live under `articles/`. Commit timestamps reflect the actual run, without backdating. Future runs depend on publisher availability, valid scheduler credentials, and GitHub Actions availability.

## License

Publisher code: **GPL-3.0-only**. The feed engine has the same license and is credited in [NOTICE.md](NOTICE.md). Linked articles, titles, and publisher excerpts retain their original owners' rights; this code license does not relicense them. This project is independent of the publishers listed above.
