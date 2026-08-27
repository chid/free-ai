# Changelog

Every edition of this list is a dated snapshot. Free tiers move fast, so what
changed matters as much as what's on the list.

The machine-readable record lives in [`history.csv`](history.csv) and
[`paid_history.csv`](paid_history.csv) — those files are append-only and are the
source of truth. This file is the human-readable summary.

Format loosely follows [Keep a Changelog](https://keepachangelog.com).

---

## [2026-08] — August 2026 refresh

71 free resources (was 65), 6 paid (was 0).

### Added

**LLM APIs** — the free-inference field widened considerably since May.

- **Cloudflare Workers AI** — serverless GPU inference at the edge; 10,000 Neurons/day, resetting at 00:00 UTC.
- **SambaNova Cloud** — 200,000 tokens/day per model on RDU hardware.
- **NVIDIA NIM** — OpenAI-compatible endpoints for 120+ open-weight models; 1,000 free credits at ~40 req/min.

**Routers & Clients**

- **Vercel AI Gateway** — one endpoint to 200+ models across 40+ providers; $5 of credit per month, refreshing.

**Code Assistants** — the BYOK agent category consolidated around a few open-source projects.

- **Cline** — MIT-licensed VS Code agent; the project most other VS Code agents were forked from.
- **Kilo Code** — VS Code / JetBrains / CLI / Slack agent with 500+ models at zero inference markup. Now on `kilo.ai`.
- **Zed** — Rust editor with native AI and MCP support; free Personal plan includes 2,000 edit predictions/month.

**Video Generation**

- **Dreamina (Seedance 2.0)** — ByteDance's video model with native audio; daily free credits, up to 1080p, watermark-free.

**Paid list** — `paid_resources.csv` was empty at the start of the month; it now holds 6 entries.

- **Midjourney** — $10/mo Basic through $120/mo Mega. No free tier or trial since March 2023.
- **OpenCode Go** — $5 first month then $10/mo for 18 hosted open coding models via OpenCode Zen. The
  open-source OpenCode agent itself is unaffected and stays on the free list.
- **Tabnine** — $39/user/mo Code Assistant, $59/user/mo Agentic Platform, billed annually. The Basic plan was
  retired in 2025; only a 14-day trial remains. Sells privacy, not price — self-hosted, VPC and air-gapped
  deployment, no training or retention on your code.
- **Superhuman** — from $25/user/mo annually ($30 monthly), Business $40. No free tier. Acquired by Grammarly
  in 2025.
- **Sudowrite** — $10–$44/mo annually ($19–$59 monthly). One-time ~10,000-credit trial, no ongoing free plan.

### Moved — free list to paid list

- **Notion AI** — the Free plan gets a capped AI *trial*, not the assistant. Real access starts at Notion Plus
  ($10/user/mo, basic writing) or Business ($20/user/mo, agents). It was carrying a vague
  `Free trial; requires Notion plan` tier value that the inclusion criteria don't allow, so it moved to
  `paid_resources.csv` — logged as `remove` in `history.csv` and `add` in `paid_history.csv`.

**Notes**

- **[`QUOTAS.md`](QUOTAS.md)** — new. Tracks how paid AI plans meter usage rather than what they charge:
  the 2026 move off flat-rate, a dated timeline of every limit change, and a per-tool table of Claude Code,
  ChatGPT/Codex, Copilot, Cursor, Windsurf and OpenCode Go. Prices barely moved this year; the unit
  underneath them changed completely.

### Removed

- **Gemini CLI** — stopped serving requests for free, AI Pro and Ultra personal accounts on **18 June 2026**.
  Google's replacement is Antigravity CLI (`agy`), covered by the existing **Antigravity** entry. Enterprise
  licences via Gemini Code Assist Standard/Enterprise are unaffected.

### Changed — free tiers that moved

- **Windsurf** — retired the credit system on 19 March 2026. Free plan is now unlimited Tab autocomplete and
  inline edits plus ~25 Cascade Flow Actions/month, on daily/weekly quotas rather than a monthly credit pool.
- **Cursor** — free plan is now branded **Hobby**: limited Agent requests and Tab completions, no credit card.
  The one-year free student Pro program ended in 2026.
- **Suno** — audio downloads were removed from the free tier in January 2026 after the Warner Music settlement.
  Free tracks stream and share on Suno but can't be downloaded or monetised. Still 50 credits/day (~10 songs).
- **Udio** — settled with Universal Music on similar terms; free tier is now 10 songs/month.
- **OpenRouter** — free tier pinned down: 14 models at ~50 requests/day, up to 1M context.
- **Cohere** — trial key is 1,000 calls/month and **non-commercial use only**.
- **Groq** — free tier is ~30 requests/min on open models.
- **Google AI Studio** — the Gemini 2.5 Pro/Flash endpoint retirement (17 June 2026) has taken effect. Current
  Flash models remain free with no credit card.
- **Antigravity** — now the official Gemini CLI replacement, shipping both the IDE and the `agy` CLI.
- **GitHub Copilot** — free tier is unchanged at 2,000 completions + 50 chats/month, but paid plans moved to
  token-based **AI Credits** on 1 June 2026. Inline completions and next-edit suggestions never draw down the
  balance; chat, agent mode, code review and the CLI do.
- **OpenCode** — description now mentions the optional paid Go plan. The agent stays free, open-source and BYOK.

### Fixed

- Three rows (`MetaGPT`, `models.dev`, `Freebuff`) had descriptions containing unquoted commas, which shifted
  every field after the description and rendered the wrong text as `free_tier` and `requires_signup` in both the
  web view and any CSV reader. Descriptions are now quoted.
- `README.md` was several refreshes behind `resources.csv` — it listed 63 tools and was missing every entry added
  on 16 and 23 May. It is now regenerated from the CSV and covers all 72, with new **Routers & Clients** and
  **Frameworks** sections for the categories that had no home.

---

## [2026-05] — May 2026

Initial release and two follow-up passes. 65 free resources at close of month.

### Added

- **15 May** — initial 40-resource seed, then a research refresh adding Cerebras, Le Chat, DeepSeek, Gemini CLI,
  Amazon Q Developer, Kling AI and Pika.
- **16 May** — developer tooling: LiteLLM, LangChain, LlamaIndex, DSPy, aisuite. Paid-tools tracking initialised.
- **23 May** — agent frameworks (CrewAI, AutoGen, MetaGPT, AgentScope), free DeepSeek access (Chutes.ai,
  Puter.js), terminal agents (Freebuff, OpenCode), Lovable, and Muse Spark — Meta Superintelligence Labs' first
  natively multimodal model, free via meta.ai. Antigravity added as Google's incoming Gemini CLI replacement.

### Changed

- **GitHub Copilot** — free for all users (2,000 completions + 50 chats/month), no longer students-only.
- **Codeium → Windsurf** — rebranded; name, URL, description and tier all updated.
- **OpenRouter** — corrected: the `:free` suffix is a rate-limited community tier, not permanently free models.
- **Gemini CLI / Google AI Studio** — flagged the June 2026 deprecations ahead of time.

### Removed

- Frontier model pricing and context-window tracking, in favour of linking to [models.dev](https://models.dev).
