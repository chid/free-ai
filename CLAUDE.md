# Free AI Resources — Project Guide

A self-updating directory of free AI tools, served as a static web page driven by a CSV.

## Files

| File | Purpose |
|---|---|
| `resources.csv` | Source of truth — free tools, one row per tool |
| `paid_resources.csv` | Source of truth — paid-only tools (no genuine free tier) |
| `local_resources.csv` | Source of truth — local/self-hosted LLM runners, UIs, and engines |
| `index.html` | Web page; fetches and renders CSV data at load time |
| `history.csv` | Append-only log of every add/remove/edit to `resources.csv` |
| `paid_history.csv` | Append-only log of every add/remove/edit to `paid_resources.csv` |
| `local_history.csv` | Append-only log of every add/remove/edit to `local_resources.csv` |
| `CHANGELOG.md` | Human-readable summary of each refresh, newest first |
| `QUOTAS.md` | Notes on how paid AI plans meter usage — quota models, not prices |
| `quota_history.csv` | Append-only log of quantitative rate limits, credit pools, and quota transitions over time |
| `quotas.py` | CLI/library to query, filter, and compare quantitative quota histories |
| `README.md` | Markdown rendering of `resources.csv`, regenerated each refresh |
| `update.py` | Interactive CLI for manual changes (writes history automatically) |
| `sync_activity.py` | Syncs latest commit dates, stars, and model updates from GitHub/HuggingFace |
| `activity.json` | Cached metadata and live activity timestamps for GitHub/HuggingFace resources |
| `refresh_prompt.md` | Claude prompt for researching and adding free tools |
| `paid_refresh_prompt.md` | Claude prompt for researching and adding paid-only tools |
| `local_refresh_prompt.md` | Claude prompt for researching and adding local LLM tools |


> **Frontier model pricing & context windows:** see [models.dev](https://models.dev) — no need to track this ourselves.

## CSV schemas

`resources.csv` columns:
```
name, category, url, description, free_tier, requires_signup, tags
```

`paid_resources.csv` columns:
```
name, category, url, description, pricing, tags
```
(`pricing` replaces `free_tier`/`requires_signup` — paid tools are always paid and require accounts.)

`local_resources.csv` columns:
```
name, category, url, description, hardware_reqs, license, tags
```

`history.csv` / `paid_history.csv` / `local_history.csv` columns:
```
date, action, name, category, url, notes
```

`quota_history.csv` columns:
```
date, vendor, product, tier, feature_or_model, metric, limit_value, unit, window, change_type, notes
```


Valid `action` values: `add`, `remove`, `edit`, `init`.

## How to serve locally

```bash
python3 -m http.server 8080
# open http://localhost:8080
```

The page uses `fetch('resources.csv')` so it needs a server (not file://).

## How to update

**Manually via CLI:**
```bash
python3 update.py
```
Supports add, remove, edit, list, and history view. All writes also log to `history.csv`.

**Manually via CSV editor:**
Edit `resources.csv` directly, then append a row to `history.csv` yourself.

**Via Claude (research refresh):**
Open a Claude Code session in this directory and paste the contents of `refresh_prompt.md` (free tools) or `paid_refresh_prompt.md` (paid-only tools). Claude will web-search for new tools, add any not already listed, and open a PR.

## How to run a refresh

Run both in the same session so everything lands in one `refresh/YYYY-MM` PR:

```bash
claude
# 1. paste refresh_prompt.md        → free tools
# 2. paste paid_refresh_prompt.md   → paid tools
```

Or trigger the scheduled agent if one is configured (check `claude schedule list`).

## Monthly PR workflow

Each monthly refresh creates a branch `refresh/YYYY-MM`, commits all changes to
`resources.csv`, `paid_resources.csv`, their history files, `CHANGELOG.md`,
`QUOTAS.md` and `README.md`, then opens a PR against `main`. Merge the PR to publish the month's
updates.

## Maintenance rules

- Never delete rows from any `*history.csv` file — they are append-only
- Every refresh adds a dated section at the top of `CHANGELOG.md` summarising adds, removes, tier changes, and fixes
- When a vendor changes *how* it meters (credits, rolling windows, shared pools) rather than what it charges, record it in `QUOTAS.md` and date it — temporary boosts must never be written into a `free_tier` or `pricing` value undated
- `README.md` mirrors `resources.csv` — regenerate its resource sections when rows change, and update the snapshot month and count in the header
- Keep `requires_signup` as exactly `Yes` or `No` (free tools only)
- `tags` are lowercase, comma-separated, no spaces around commas
- `free_tier` should be specific (e.g. "Free tier with rate limits", "Completely free", "$5 credit on signup") not vague ("Free!")
- `pricing` should be specific (e.g. "$20/month", "from $0.015/1K tokens") not vague ("Paid")
- If a tool's free tier **changes** (tighter or more generous limits), update the row and log an `edit` in `history.csv` with old and new values in the notes
- If a tool's free tier disappears, move it from `resources.csv` to `paid_resources.csv` and log `remove` + `add` in the respective history files
- If a paid tool gains a genuine free tier, move it from `paid_resources.csv` to `resources.csv` and log accordingly
- Categories must match one of the existing values or be clearly justified as new

## Free-tool categories (current)

Audio / Music, Audio / Voice, Code / UI, Code Assistant, Image Generation,
LLM API, LLM Chatbot, LLM Router, LLM Client, Agent Framework, RAG Framework,
Prompt Optimization, Productivity, Search / Research,
Video Generation

### One tool, one pathway

`Local / Self-hosted` was retired from `resources.csv` on 2026-09-05. Anything that
runs on the reader's own hardware belongs in `local_resources.csv` — it has the
`hardware_reqs` and `license` columns that make a local tool useful, which the free
schema does not. Before adding a row to any pathway, check the other two for the same
name or URL.

Freemium tools are the deliberate exception: a genuinely free tier in `resources.csv`
alongside a separately-named paid plan in `paid_resources.csv` (e.g. `Claude (Anthropic)`
and `Claude Pro / Team / Max`) is correct and intended.

## Paid-tool categories (current)

Same set — pick the closest match.

## Local-tool categories (current)

Local Runner, Desktop Client, Serving Engine, Web UI, Code Assistant,
Agent Framework, Fine-tuning / Quant, Embeddings / RAG,
Image / Audio / Video, Hardware / Benchmarking

Local tools render in their own "Run It Yourself" section at the bottom of
`index.html` — they are deliberately excluded from the Free/Paid/All tier counts
and from the header total, so month-on-month resource counts stay comparable.
The page search filters both the main grid and the local section; the category
chips apply to the main grid only.
