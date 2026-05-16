# Free AI Resources — Project Guide

A self-updating directory of free AI tools, served as a static web page driven by a CSV.

## Files

| File | Purpose |
|---|---|
| `resources.csv` | Source of truth — free tools, one row per tool |
| `paid_resources.csv` | Source of truth — paid-only tools (no genuine free tier) |
| `frontier_labs.csv` | One row per major AI lab (overview + URLs) |
| `frontier_models.csv` | One row per frontier model — pricing, context window, free tier |
| `index.html` | Web page; fetches and renders `resources.csv` at load time |
| `history.csv` | Append-only log of every add/remove/edit to `resources.csv` |
| `paid_history.csv` | Append-only log of every add/remove/edit to `paid_resources.csv` |
| `frontier_history.csv` | Field-level change log for frontier labs and models |
| `update.py` | Interactive CLI for manual changes (writes history automatically) |
| `refresh_prompt.md` | Claude prompt for researching and adding free tools |
| `paid_refresh_prompt.md` | Claude prompt for researching and adding paid-only tools |
| `frontier_refresh_prompt.md` | Claude prompt for tracking frontier lab model pricing and changes |

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

`history.csv` / `paid_history.csv` columns:
```
date, action, name, category, url, notes
```

Valid `action` values: `add`, `remove`, `edit`, `init`.

`frontier_labs.csv` columns:
```
name, url, api_platform_url, free_chatbot_url, hq, notes
```

`frontier_models.csv` columns:
```
lab, model, modality, context_window_k, input_per_1M_usd, output_per_1M_usd,
free_tier, free_tier_details, status, last_checked
```

`frontier_history.csv` columns:
```
date, action, lab, model, field, old_value, new_value, notes
```

Valid `action` values: `add-model`, `update`, `deprecate`, `add-lab`, `remove-lab`, `init`.
One row per **changed field** — if three fields changed on one model, log three rows.

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

Run all three in the same session so everything lands in one `refresh/YYYY-MM` PR:

```bash
claude
# 1. paste refresh_prompt.md           → free tools
# 2. paste paid_refresh_prompt.md      → paid tools
# 3. paste frontier_refresh_prompt.md  → frontier labs & models
```

Or trigger the scheduled agent if one is configured (check `claude schedule list`).

## Monthly PR workflow

Each monthly refresh creates a branch `refresh/YYYY-MM`, commits all changes to
`resources.csv`, `paid_resources.csv`, and their history files, then opens a PR
against `main`. Merge the PR to publish the month's updates.

## Maintenance rules

- Never delete rows from any `*history.csv` file — they are append-only
- Keep `requires_signup` as exactly `Yes` or `No` (free tools only)
- `tags` are lowercase, comma-separated, no spaces around commas
- `free_tier` should be specific (e.g. "Free tier with rate limits", "Completely free", "$5 credit on signup") not vague ("Free!")
- `pricing` should be specific (e.g. "$20/month", "from $0.015/1K tokens") not vague ("Paid")
- If a tool's free tier **changes** (tighter or more generous limits), update the row and log an `edit` in `history.csv` with old and new values in the notes
- If a tool's free tier disappears, move it from `resources.csv` to `paid_resources.csv` and log `remove` + `add` in the respective history files
- If a paid tool gains a genuine free tier, move it from `paid_resources.csv` to `resources.csv` and log accordingly
- In `frontier_history.csv`, log one row per changed field (not one row per model)
- Categories must match one of the existing values or be clearly justified as new

## Free-tool categories (current)

Audio / Music, Audio / Voice, Code / UI, Code Assistant, Image Generation,
LLM API, LLM Chatbot, LLM Router, LLM Client, Agent Framework, RAG Framework,
Prompt Optimization, Local / Self-hosted, Productivity, Search / Research,
Video Generation

## Paid-tool categories (current)

Same set — pick the closest match.
