# Changelog

Every edition of this list is a dated snapshot. Free tiers move fast, so what
changed matters as much as what's on the list.

The machine-readable record lives in [`history.csv`](history.csv),
[`paid_history.csv`](paid_history.csv) and [`local_history.csv`](local_history.csv) — those
files are append-only and are the source of truth. This file is the human-readable summary.

Format loosely follows [Keep a Changelog](https://keepachangelog.com).

## [2026-09] — Evaluation & Benchmark Harnesses addition

44 local tools (was 37). Added dedicated **Evaluation & Harnesses** category tracking standard LLM benchmark frameworks, agent sandboxes, and production unit test harnesses.

### Added
- **lm-evaluation-harness** (EleutherAI) — Standard framework for few-shot evaluation across 60+ benchmarks (MMLU, GSM8K, ARC, HumanEval) powering the Open LLM Leaderboard.
- **SWE-bench** (Princeton) — Industry benchmark and evaluation harness for autonomous coding agents against real GitHub issues in Docker sandboxes.
- **Inspect AI** (UK AI Safety Institute) — Open-source evaluation harness for LLM capabilities, agent tool-use protocols, and sandboxed safety evaluations.
- **Promptfoo** — CLI and CI/CD test harness for testing LLM outputs, prompt assertions, red-teaming, and regression suites.
- **DeepEval** (Confident AI) — Production unit testing framework for LLMs (Pytest for AI) covering hallucination, answer relevancy, and G-Eval.
- **Ragas** — Evaluation harness tailored for Retrieval-Augmented Generation (RAG) pipelines (faithfulness, context recall and precision).
- **Lighteval** (Hugging Face) — Lightweight evaluation toolkit for assessing LLMs across multi-turn chat, math, and custom evaluation suites.

---

## [2026-09] — Paid subscriptions expansion


27 paid resources (was 6). Broadened paid tools tracking across frontier chatbots, AI coding IDEs, generative video, music/voice synthesizers, and enterprise productivity subscriptions.

### Added
- **Frontier LLM Subscriptions**:
  - **ChatGPT Plus / Pro** ($20 / $200/mo) — GPT-4o, o1, o3-mini reasoning, Deep Research, and Advanced Voice.
  - **Claude Pro / Team** ($20 / $25-30/mo) — Claude 3.7 Sonnet hybrid extended thinking, Artifacts, and Projects.
  - **Gemini Advanced** ($19.99/mo) — Google One AI Premium with Gemini 2.0/1.5 Pro (2M context) and Workspace apps.
  - **Grok / X Premium+** ($16-$22/mo) — Real-time X grounding, Grok 3 reasoning, Aurora thinking mode, FLUX image gen.
  - **Perplexity Pro** ($20/mo) — Unlimited Pro Search with multi-model switching (Claude 3.7, GPT-4o, DeepSeek R1).
- **Code Assistants & IDEs**:
  - **Cursor Pro** ($20/mo) — 500 fast requests/mo, Agent Composer, and predictive Cursor Tab.
  - **Windsurf Pro** ($15-$20/mo) — Unlimited Cascade Flow actions with daily/weekly quotas and Claude 3.7.
  - **GitHub Copilot Pro** ($10/mo) — Multi-model switching across Claude 3.7 Sonnet, GPT-4o, and Gemini 2.0 Flash.
  - **Augment Code** ($20/user/mo) — Enterprise codebase instant context understanding and pair programming.
- **Media Generation (Video, Music, Voice, Image)**:
  - **Runway** ($12-$76/mo) — Gen-3 Alpha, Act-One motion capture, and camera control.
  - **Luma Dream Machine** ($29.99-$99.99/mo) — High-fidelity text/image-to-video with camera keyframes.
  - **Pika Pro** ($10-$60/mo) — Pikaffects (melt, inflate, crush), lip sync, and sound effects.
  - **ElevenLabs** ($5-$99/mo) — Ultra-realistic voice cloning, multilingual dubbing, and speech-to-speech.
  - **Suno** ($10-$30/mo) — Radio-ready vocal song generation with full commercial terms.
  - **Udio** ($10-$30/mo) — High-fidelity music generation with stem separation and audio inpainting.
  - **Magnific AI** ($39-$299/mo) — AI image upscaler and hallucination enhancer for photorealistic detail.
- **Enterprise & Productivity**:
  - **Microsoft Copilot Pro** ($20/mo) — GPT-4o integration inside Word, Excel, PowerPoint, and Outlook.
  - **Descript** ($12-$24/user/mo) — Text-based audio and video editing with Studio Sound.
  - **Granola** ($10/user/mo) — AI notepad for meetings with automated transcription and template summaries.
  - **Glean** (~$30-$50/user/mo) — Enterprise work search across Google Workspace, Slack, Jira, and GitHub.
  - **Gamma** ($10-$20/user/mo) — Generative AI canvas for presentations, documents, and webpages.

---

## [2026-08] — Local LLM tools refresh


18 local/self-hosted tools (was 12).

### Added

Fills four previously-empty local categories:

- **OpenHands** (Code Assistant) — self-hosted autonomous coding agent (formerly OpenDevin), MIT, sandboxed Docker execution via CLI or web GUI.
- **AnythingLLM** (Web UI) — all-in-one self-hosted RAG + no-code agents + multi-model chat, MIT.
- **Unsloth** (Fine-tuning / Quant) — fast local LoRA/QLoRA fine-tuning with a no-code Studio UI, Apache-2.0 core.
- **Text Embeddings Inference** (Embeddings / RAG) — Hugging Face's self-hosted embedding/reranking server, Apache-2.0.
- **ComfyUI** (Image / Audio / Video) — node-based local diffusion UI for Stable Diffusion/Flux, GPL-3.0.
- **LocalAGI** (Agent Framework) — self-hostable agent orchestration platform from the LocalAI team, MIT.

### Changed (drift)

- **ExLlamaV2 → ExLlamaV3** — ExLlamaV2 was archived by its maintainer in March 2026; development continues on ExLlamaV3 (new EXL3 quant format, same MIT license).
- **Text Generation WebUI → TextGen (oobabooga)** — project renamed and repo moved to `oobabooga/textgen` in 2026, now ships a native Electron desktop app and an OpenAI/Anthropic-compatible API; license unchanged (AGPL-3.0).

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

**Local LLMs pathway** — created `local_resources.csv` (12 seed tools: Ollama, llama.cpp, LM Studio, Jan, vLLM, SGLang, Open WebUI, Kobold.cpp, ExLlamaV2, Text Generation WebUI, LocalAI, Tabby), tracked via `local_history.csv` and refreshed via `local_refresh_prompt.md`. The web page gained a dedicated "Run It Yourself" section below the main grid, showing each tool's category, hardware requirements, and licence. Local tools are counted separately and stay out of the Free/Paid/All totals so month-on-month counts remain comparable. The refresh scope also covers local embeddings/RAG, image/audio/video runners, and hardware/benchmarking tools.

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

- **ChatGPT policy** — logged OpenAI's commitment that the core ChatGPT chat tier remains permanently free (with rate limits on new frontier models).
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
