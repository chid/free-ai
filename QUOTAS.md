# Quota Notes -- Paid AI, 2026

*Last reviewed: 28 August 2026.*

This file tracks **how paid AI tools meter usage**, not what they cost. Headline
prices have barely moved in 2026 -- $20/month is still the anchor for a pro plan.
What changed is the unit underneath it.

It exists because the free/paid boundary this repo tracks is no longer drawn by
price. Several tools on the free list are free in the sense that matters (you can
start without a card) while quietly metering the part you actually want, and the
`free_tier` column can't carry that nuance on its own.

---

## The shift, in one paragraph

Flat-rate ended in 2026. Through 2025 a subscription bought an unlimited-ish
allowance of *requests*; by August 2026 nearly every major vendor meters either
**dollars of inference** or **time-windowed compute**, and most run two limits at
once -- a short rolling window to smooth load, plus a weekly or monthly cap to
bound cost. The second consequence matters more than the first: cheap,
high-volume features (inline completions, autocomplete) are being kept free and
unlimited, while *agentic* work -- chat, agents, code review, headless runs -- is
what gets metered. The meter moved from "how often do you ask" to "how much
compute did you consume".

---

## Timeline

| Date | Change |
|---|---|
| **14 May 2024** | Google AI Studio introduces Gemini 1.5 Flash free tier: 15 RPM, 1M TPM, 1,500 RPD, and 1M context. |
| **Mar 2026** | Anthropic reduces Claude Code 5-hour limits during weekday peak hours (5-11 AM PT). |
| **19 Mar 2026** | Windsurf retires credits entirely, moving to daily + weekly quotas. Pro goes $15 -> $20. |
| **Apr 2026** | GitHub pauses new individual Copilot signups; reopens gradually from 17 June. |
| **6 May 2026** | Anthropic permanently doubles Claude Code's 5-hour limits (weekly cap unchanged). |
| **13 May 2026** | Claude Code weekly limits run 50% above published standard -- extended three times, most recently on 19 Aug through 31 Aug 2026, with Anthropic saying it hopes to make it permanent. |
| **1 Jun 2026** | GitHub Copilot replaces premium-request quotas with token-based **AI Credits** on all plans. Inline completions and next-edit suggestions stay free and never touch the balance. |
| **15 Jun 2026** | Anthropic splits programmatic use off the subscription: Agent SDK calls, `claude -p` headless mode and third-party Agent-SDK tools draw from a **separate monthly credit pool** ($20 Pro / $100 Max 5x / $200 Max 20x). |
| **17 Jun 2026** | Google AI Studio deprecates legacy Gemini 2.5 Pro and Flash endpoints; active Flash models (3.6 Flash, 2.5 Flash-Lite) standardize at 15 RPM, 1M TPM, 1,500 RPD with up to 2M context. |
| **Mid-Jul 2026** | OpenAI drops the 5-hour Codex cap alongside GPT-5.6 Sol, leaving a single weekly quota. |
| **25 Aug 2026** | OpenAI restores the 5-hour cap for Codex and ChatGPT Work on **Plus only**; Pro ($100/$200) keeps it disabled. |

---

## How each tool meters, as of August 2026

| Tool | Plans | Metered by | Notes |
|---|---|---|---|
| **Google AI Studio (Gemini)** | Free API key (per-project) / Pay-as-you-go | **Tri-metered**: RPM (15), TPM (1M), RPD (1,500) | Limits apply at the **Google Cloud project level** across all keys. Flash models get 1,500 requests/day, up to 2M tokens context, and free 2GB temporary file uploads. Pro models are tightly throttled (2 RPM, 50 RPD). **Privacy tradeoff**: on the free tier, prompts and responses may be human-reviewed and used to train Google products; attaching billing removes training use but converts calls to pay-as-you-go. |
| **Claude Code** | Pro $20 / Max 5x $100 / Max 20x $200 | 5-hour rolling window **and** a weekly cap on active compute hours | Window starts on your first prompt, not a fixed clock. The bucket is **shared** across Claude Code, claude.ai and Cowork. Roughly 10-45 prompts per window on Pro, up to ~900 on Max 20x. Programmatic use is a separate pool (see 15 Jun). |
| **ChatGPT / Codex** | Plus $20 / Pro $100 / $200 | Rolling window + weekly quota, per surface | Plus: ~160 GPT-5.5 messages/3h, ~3,000 GPT-5.5 Thinking/week. Codex 5-hour cap is back on Plus as of 25 Aug; Pro is exempt. Overflow is buyable as credits. |
| **GitHub Copilot** | Free / Pro $10 / Pro+ $39 / Max $100 | Token-based **AI Credits** | Pro includes $10/mo of credits, Pro+ $70. Chat, agent mode, code review and Copilot CLI draw down; **completions do not**. Free plan still 2,000 completions + 50 chats/month. |
| **Cursor** | Free (Hobby) / Hobby $10 / Pro $20 / Pro+ $60 / Business $40/seat / Ultra $200 | Monthly credit pool | Replaced the old "fast requests" count -- the change that caused the most confusion. Frontier models sit behind Max Mode multipliers, which accelerates burn. Hobby limits are account-specific and not published as fixed numbers. |
| **Windsurf** | Free / Pro $20 / Max $200 / Teams $40/user | Daily + weekly quotas | Credits gone since 19 Mar. Free keeps unlimited Tab autocomplete and inline edits plus ~25 Cascade Flow Actions/month. |
| **OpenCode Go** | $5 first month, then $10/mo | **Dollar-denominated**: $12 per 5 hours, $30/week, $60/month | The clearest example of the shift -- the quota is literally priced in dollars of inference. One key, 18 open models via OpenCode Zen. Overflow falls back to your Zen balance if "Use balance" is on. Current model agreement runs through 31 Aug 2026. |

---

## OpenCode Go -- why it's worth a note

OpenCode is on the free list and stays there: the agent is open source, BYOK, and
costs nothing to run. **OpenCode Go** is a separate, optional paid plan from the
same team -- $10/month for one key covering 18 open coding models (GPT 5.6 Luna,
Kimi K3, DeepSeek V4 Pro, Grok 4.5, GLM-5.2, Qwen3.8 Max and others) through
OpenCode Zen.

It's listed in [`paid_resources.csv`](paid_resources.csv) because it's a genuine
paid subscription, and it's the cleanest illustration of where metering has
landed: no request counts, no credits with an invented exchange rate -- just
$12 per 5 hours, $30 per week, $60 per month of actual inference spend, with the
option to spill over onto a prepaid balance instead of hard-stopping. A user can
read that limit and know exactly what they're getting, which is more than can be
said for most credit systems.

---

## Google AI Studio -- why it's worth a note

Google AI Studio represents the opposite extreme of the subscription clampdown:
while developer coding subscriptions moved to restrictive 5-hour rolling windows
or token credit burn-downs, Google continues to offer one of the most generous
free developer tiers in the industry.

Current Flash models (such as 3.6 Flash and 2.5 Flash-Lite) provide **15 RPM**,
**1,000,000 TPM**, and **1,500 requests per day** with up to a **2M token context window**,
free multimodal ingestion (audio and up to 1h video), structured JSON output,
function calling, and a free 2GB temporary **Files API** (48h retention).

However, two architectural nuances are essential to understand:
1. **Limits are per Google Cloud Project, not per key.** Creating 5 API keys
   in the same project still draws from the single shared 1,500 RPD bucket.
2. **The Data Privacy Trade-off.** On the Free tier, prompts and responses
   **may be reviewed by human reviewers and used by Google to train and improve models**.
   Attaching billing removes the training clause, but immediately removes the free tier
   allowance, switching all calls to pay-as-you-go. For clean separation, keep separate
   free prototyping projects and paid production projects.

---

## Quantitative Quota Tracking (`quota_history.csv`)

To quantitatively explore how quotas, rate limits, credit pools, and token buckets have shifted across vendors over time, this repository maintains an append-only time-series dataset in [`quota_history.csv`](quota_history.csv).

### Using the CLI (`quotas.py`)

You can inspect, query, and compare historical and active quotas using `quotas.py`:

```bash
# 1. View current active quotas across all providers and tiers:
python3 quotas.py summary

# 2. View full timeline of changes for a specific vendor or tool:
python3 quotas.py history --product "Google"
python3 quotas.py history --product "Claude"

# 3. Filter by metric type (requests, tokens, credits_usd, compute_hours):
python3 quotas.py history --metric requests

# 4. Compare free-tier vs paid-tier rate limits side-by-side:
python3 quotas.py compare

# 5. Output structured JSON for graphing or analysis:
python3 quotas.py history --product "Google" --json
```

---

## What this means for the free list

- **"Free tier" increasingly means "free completions."** Copilot and Windsurf
  both give away the cheap, high-frequency feature and meter the agent. When
  reading a `free_tier` value, check *which* capability is free.
- **Shared pools are easy to miss.** Claude's quota spans three products; using
  one silently drains the others. Free tiers built on the same infrastructure
  tend to inherit this.
- **Dollar-denominated limits are the honest ones.** Where a vendor publishes a
  dollar figure (OpenCode Go, Copilot's AI Credits), the tier is legible.
  Where it publishes "credits" without a rate, or nothing at all (Cursor Hobby),
  it isn't -- and those are the rows most likely to need an `edit` next refresh.
- **Boosts are temporary until stated otherwise.** Claude Code's +50% weekly
  limit has been extended three times and is still, formally, an extension. Don't
  write a temporary allowance into a `free_tier` or `pricing` value without
  dating it.

---

## Sources

Reviewed August 2026. These change often -- re-verify before relying on a number.

- [Claude Code rate limits & usage quotas](https://www.truefoundry.com/blog/claude-code-limits-explained) | [Claude usage limits, dated timeline](https://explainx.ai/blog/claude-usage-limits-2026-timeline-explained)
- [The flat-rate AI coding subscription era is ending](https://medium.com/activated-thinker/the-flat-rate-ai-coding-subscription-era-is-ending-what-github-copilot-claude-code-and-cursor-9763e043a63a)
- [GitHub Copilot pricing 2026: credits explained](https://questloops.com/blog/github-copilot-pricing-2026-free-pro-pro-and-the-new-ai-credits-system)
- [OpenAI restores 5-hour Codex limits for Plus](https://9to5mac.com/2026/08/24/openai-restores-5-hour-codex-and-work-limits-for-chatgpt-plus-users/) | [ChatGPT Plus limits 2026](https://customgpt.ai/chatgpt-plus-limits-2026/)
- [Cursor pricing 2026](https://www.nxcode.io/resources/news/cursor-ai-pricing-plans-guide-2026) | [Windsurf pricing 2026](https://www.nocode.mba/articles/windsurf-pricing)
- [OpenCode Go docs](https://opencode.ai/go) | [OpenCode Go pricing, limits & models](https://hackup.ai/ai-plans/opencode/)

