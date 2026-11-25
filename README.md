# AI Learning Daily

An automatically maintained reading list for practical AI engineering: **lower costs, faster inference, and better systems**.

Each entry links to the original publisher, keeps its publication date, includes a short attributed excerpt, and offers a keyword-based practice idea. These are reading resources, not claims that the linked work or suggested experiments were completed by this repository's maintainer.

<!-- articles:start -->

**80 reading entries** · Latest 30 below · [Full catalog](data/articles.json)

- **2026-11-24 · n8n** — [Production AI Playbook: Audit &amp; trace for AI agents](articles/2026-11/99c35c1258d2ddc6e299fee8.md)
- **2026-11-24 · OpenAI** — [GPT-6 models demonstrate intrinsic protein-design capabilities](articles/2026-11/ac2f786b30f6d45772c42167.md)
- **2026-11-24 · OpenAI** — [Clay helps sales teams win with Codex and ChatGPT](articles/2026-11/a3c9028eefd69cfd15ff27f4.md)
- **2026-11-24 · OpenAI** — [How iFood scales coding agents across 15,000 repositories](articles/2026-11/89a905d5eae9fa3ef5a8af6c.md)
- **2026-11-23 · OpenAI** — [Richpanel helps companies automate 50% of support in 30 days](articles/2026-11/1259b534687dd8b3171199ff.md)
- **2026-11-23 · Google Developers** — [Did the user ask for this? Securing AI agents against intent hijacking with Semantic governance policies](articles/2026-11/d0ed4d1f645598f142c1c13a.md)
- **2026-11-23 · Hugging Face** — [How to build and maintain an agentic evaluation](articles/2026-11/00d52199bef25f9eda98fa79.md)
- **2026-11-22 · OpenAI** — [Perplexity and Intelligence](articles/2026-11/1a10f1676d46fc01a909d8ea.md)
- **2026-11-20 · OpenAI** — [Combatting adversarial distillation](articles/2026-11/7ad44f990f0c53ef2e2a5377.md)
- **2026-11-20 · OpenAI** — [Can AI help scientists identify promising drug candidates?](articles/2026-11/c1a2af93db54bfcf7c217cb7.md)
- **2026-11-20 · Google Developers** — [How to securely connect internal Cloud Run MCP servers to Gemini Enterprise](articles/2026-11/bc55ae1ae5897f87c15f207c.md)
- **2026-11-20 · OpenAI** — [Hebbia sees improvements in financial research with GPT-6 Astra](articles/2026-11/8145fefb47ff1ca9fa5560e6.md)
- **2026-11-20 · Google Developers** — [How to handle user, connector, and agent auth in Gemini Enterprise with a custom UI](articles/2026-11/1dcdfb995f83a35a1a02115c.md)
- **2026-11-20 · Google Developers** — [Agent Anomaly Detection: Safeguarding agents across other clouds](articles/2026-11/18462794d5c944865ca3c5f0.md)
- **2026-11-19 · NVIDIA** — [Reducing Rollout Bottlenecks in Reinforcement Learning with NVIDIA Dynamo](articles/2026-11/fdf247289ced7fca8c814c4b.md)
- **2026-11-19 · Google AI** — [Introducing Tool Retrieval in the Gemini API](articles/2026-11/056cf0b58a3dbace68332c5e.md)
- **2026-11-19 · NVIDIA** — [Build Tool-Calling Parsers in Rust with AI Agents](articles/2026-11/2d01b6350c2d3fb2cb0f094e.md)
- **2026-11-19 · Google Developers** — [Multi-Turn Agentic Reinforcement Learning with Tunix and Gemma 4 on Google TPUs](articles/2026-11/e6f9d601449ae6856b74bcb7.md)
- **2026-11-19 · Google Developers** — [Distributed LLM Training Across Metros: Streaming DiLoCo in MaxText](articles/2026-11/ddc3aaf2a01e995425ca8f4d.md)
- **2026-11-18 · Hugging Face** — [Why your fine-tuning job takes longer than the FLOPs say](articles/2026-11/e55c8f2df06c07ffc92b5ea2.md)
- **2026-11-18 · NVIDIA** — [Build Training-Ready Physical AI Datasets with Two Prompts in NVIDIA Cosmos](articles/2026-11/e0a5680da648bf1e9f0c1f68.md)
- **2026-11-18 · OpenAI** — [Research acceleration: The jagged frontier](articles/2026-11/58da586369f33999eb920dc2.md)
- **2026-11-18 · OpenAI** — [Managing frontier AI risk: From training to deployment](articles/2026-11/99be0c0a7e074380d1a5d6cd.md)
- **2026-11-18 · Hugging Face** — [180B Parameters, 32GB of RAM: Pushing MoE Inference to the Limit with Transformers](articles/2026-11/ec56b5eff9affb1c339e466c.md)
- **2026-11-17 · OpenAI** — [Introducing GPT-6.2 Astra and Sol](articles/2026-11/8f6af8c44a4a1bfb5de31585.md)
- **2026-11-17 · NVIDIA** — [Co-Designing Sparse Attention for Efficient Long-Context Inference](articles/2026-11/ef0668bcb4a436fa3ea78ed7.md)
- **2026-11-17 · OpenAI** — [Astra for Law leads in legal intelligence](articles/2026-11/b43ef08ac3ed4f7af6f4fa4f.md)
- **2026-11-17 · Google Developers** — [Gemini 4 Hydrogen: a faster model for general purpose robotics](articles/2026-11/7c3a077a80825638365ff213.md)
- **2026-11-17 · Google Developers** — [Build full-stack Android apps with Gemini in Google AI Studio](articles/2026-11/3d0957b329c2f381935ad1f1.md)
- **2026-11-16 · NVIDIA** — [Post-Training NVIDIA Nemotron to Increase Accuracy in Your Scientific Domain](articles/2026-11/e5e272e7744c80be5ffb799c.md)

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
