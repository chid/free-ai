# Changelog

Notable changes to this directory, newest first. Dates are the date of the refresh.

`history.csv` and `paid_history.csv` are the machine-readable record of every
individual add/remove/edit; this file is the human-readable summary of each
refresh. Format loosely follows [Keep a Changelog](https://keepachangelog.com).

---

## 2026-08-01 — August refresh

**76 free resources** (was 65) across 16 categories, plus the first 3 entries in
the paid list.

### Added — free tools (13)

**LLM APIs** — the free-inference field widened considerably since May:

- **Cloudflare Workers AI** — 10,000 neurons/day free on the edge, resets 00:00 UTC
- **NVIDIA NIM** — 100+ open models at ~40 RPM through the Developer Program, no expiry
- **SambaNova** — permanent free tier (20 RPM / 20 RPD / 200K TPD per model) plus $5 credits
- **SiliconFlow** — some small models free forever, plus ¥14 signup credits
- **Z.ai (GLM)** — 1,000 requests/day on GLM-5.1

**Everything else:**

- **Vercel AI Gateway** *(LLM Router)* — recurring $5/month of credits, provider list price with no markup
- **Qwen Chat** *(LLM Chatbot)* — Alibaba's free, rate-limited assistant
- **Manus** *(Productivity)* — autonomous task agent, 300 credits refreshed daily
- **Cline**, **Kilo Code**, **Goose** *(Code Assistants)* — open-source BYOK coding agents; free tooling, you pay only your model provider
- **Leonardo AI** (150 fast tokens/day) and **Krea** (100 compute units/day) *(Image Generation)*

### Added — paid tools (3)

`paid_resources.csv` had been empty since it was created in May. Seeded with three
market leaders that have no genuine free tier:

- **Midjourney** — $10/mo Basic through $120/mo Mega; no free trial
- **Superhuman** — $30/mo Starter, $40/mo Business; trial only
- **Sora** — consumer app discontinued, now API-only at $0.10–$0.50 per second

### Removed (2)

- **Phind** — shut down 16 January 2026; the site 404s and signups are closed
- **Gemini CLI** — stopped serving free, AI Pro and Ultra personal accounts on
  18 June 2026. Superseded by **Antigravity**, which is already listed

### Changed

Free tiers tightened noticeably this quarter. Every entry below had its
`free_tier` corrected against current published limits:

| Tool | Change |
|---|---|
| Groq | 30 RPM; daily cap is **per-model** — 14.4K RPD on `llama-3.1-8b-instant`, 1K on `llama-3.3-70b-versatile` |
| OpenRouter | **50** `:free` requests/day at 20 RPM; the 1,000/day cap now requires a $10 lifetime top-up |
| Cohere | Restated as **1,000 API calls/month**, 20 req/min for chat |
| Playground AI | Tightened late July: 10 → **5** images per rolling window, 10 → **2** downloads/day |
| Suno | Free songs are **no longer downloadable** — stream and share only (Warner settlement) |
| Udio | **All downloads suspended** platform-wide since 30 Oct 2025, pending the UMG licensed relaunch |
| ElevenLabs | Restated as 10,000 credits/month (~10 min of TTS); **no commercial licence** below Starter |
| Cursor | Softened — Cursor no longer publishes exact free-tier allowances |
| Google AI Studio | Softened — Google no longer publishes fixed free-tier RPM/RPD; limits are shown per account in AI Studio |

Renames and corrections:

- **Windsurf → Devin Desktop.** Cognition rebranded Windsurf on 2 June 2026;
  Cascade was replaced by Devin Local. Free tier keeps unlimited Tab completions
  and inline edits, but cloud agents now start at the $20 Pro plan
- **Antigravity** updated for Antigravity 2.0 (Google I/O 2026) — desktop app,
  CLI and SDK, and the supported successor to Gemini CLI
- **Google AI Studio** — dropped the now-past 17 June 2026 deprecation notice and
  recorded the current quota (5–15 RPM, up to 1,500 requests/day)

### Fixed

- **Three rows in `resources.csv` were silently corrupt.** MetaGPT, models.dev and
  Freebuff had unquoted commas in their `description` field, so they parsed as 9–10
  columns instead of 7. The web view rendered their descriptions truncated and their
  `free_tier`/`tags` shifted into the wrong columns. All three are re-quoted
- `README.md` is now **generated** from the CSVs by `generate_readme.py` rather than
  hand-maintained. It had drifted to claiming 63 resources across 13 categories while
  omitting 14 listed tools (Chutes.ai, Puter.js, Freebuff, OpenCode, Lovable, Muse
  Spark, Antigravity, LiteLLM, LlamaIndex, DSPy, aisuite, models.dev, and others) and
  4 whole categories

### Validation

Every entry added or changed in this refresh was re-checked against the vendor's own
docs or pricing page where reachable. That pass caught eight claims that came from
secondary sources and did not survive contact with the primary one:

| Entry | Corrected to |
|---|---|
| **Groq** | Daily cap is per-model (14.4K RPD on the 8B model), not a blanket 1,000/day |
| **Z.ai (GLM)** | No documented "1,000 req/day on GLM-5.1" tier — the free offering is the zero-cost **Flash** models |
| **Vercel AI Gateway** | Docs confirm a recurring monthly credit but not the "$5" figure, and it covers only a **subset of models** at reduced rate limits |
| **SambaNova** | Free tier applies when no payment method is linked; the "$5 starter credits" and "permanent" claims aren't in the docs |
| **ElevenLabs** | 10k credits ≈ **10 minutes of TTS**; the "~20,000 characters" and attribution claims weren't supported |
| **Cohere** | 1,000 calls/month and 20 req/min confirmed; the **non-commercial** restriction is not stated in the docs |
| **Goose** | Docs moved to `goose-docs.ai`; governance moved from Block to the **Agentic AI Foundation** |
| **Leonardo AI** | 150 daily tokens is ~10–15 images, not 15–30 |

Confirmed exactly as published: Cloudflare Workers AI (10,000 neurons/day, resets
00:00 UTC), OpenRouter (20 RPM / 50 RPD / 1,000 after a $10 lifetime top-up),
SambaNova's 20 RPM / 20 RPD / 200K TPD, Cohere's call cap, Manus (300 daily credits,
plus a 1,500/month ceiling and Lite-model-only that we now record), Krea (100 compute
units/day), and NVIDIA NIM (~40 RPM, no card).

Two entries were softened rather than corrected because the vendor no longer publishes
exact figures at all: **Cursor** and **Google AI Studio**. Better a vaguer true claim
than a precise false one.

### Not added

- **GitHub Models** was a strong free-API candidate — but it was retired on
  30 July 2026 (playground, catalogue, inference API and BYOK all withdrawn), so it
  never made it into the list

---

## 2026-05-23 — May research refresh

- Added agent frameworks: **CrewAI**, **AutoGen**, **MetaGPT**, **AgentScope**
- Added **Muse Spark** (Meta Superintelligence Labs) and **Antigravity** (Google)
- Added **Chutes.ai** and **Puter.js** for free DeepSeek access
- Added **Freebuff**, **OpenCode**, **Lovable**
- Corrected the **OpenRouter** description — `:free` is a rate-limited community
  tier, not a set of permanently free models
- Flagged the June 2026 **Gemini CLI** and **Gemini 2.5 API** deprecations

## 2026-05-16 — Tooling and scope

- Added the paid-tools pathway: `paid_resources.csv`, `paid_history.csv`,
  `paid_refresh_prompt.md`, and the monthly `refresh/YYYY-MM` PR workflow
- Added developer tooling entries: **LiteLLM**, **LangChain**, **LlamaIndex**,
  **DSPy**, **aisuite**; expanded refresh-prompt category coverage
- Replaced hand-tracked frontier model pricing with a link to
  [models.dev](https://models.dev)
- Fixed tier-change history logging

## 2026-05-15 — Initial release

- Seeded `resources.csv` with 40 free AI tools
- Added `index.html` (CSV-driven filterable web view), `update.py`,
  `history.csv`, `refresh_prompt.md`, and the README
