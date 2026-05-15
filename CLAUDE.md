# Free AI Resources — Project Guide

A self-updating directory of free AI tools, served as a static web page driven by a CSV.

## Files

| File | Purpose |
|---|---|
| `resources.csv` | Source of truth — one row per tool |
| `index.html` | Web page; fetches and renders `resources.csv` at load time |
| `history.csv` | Append-only log of every add/remove/edit with dates |
| `update.py` | Interactive CLI for manual changes (writes history automatically) |
| `refresh_prompt.md` | Reusable Claude prompt for researching and adding new tools |

## CSV schema

`resources.csv` columns:
```
name, category, url, description, free_tier, requires_signup, tags
```

`history.csv` columns:
```
date, action, name, category, url, notes
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
Open a Claude Code session in this directory and paste the contents of `refresh_prompt.md`. Claude will web-search for new tools, add any not already listed, and log all changes to history.

## How to run a refresh

```bash
claude  # then paste refresh_prompt.md contents
```

Or trigger the scheduled agent if one is configured (check `claude schedule list`).

## Maintenance rules

- Never delete `history.csv` rows — it is append-only
- Keep `requires_signup` as exactly `Yes` or `No`
- `tags` are lowercase, comma-separated, no spaces around commas
- `free_tier` should be specific (e.g. "Free tier with rate limits", "Completely free", "$5 credit on signup") not vague ("Free!")
- If a tool's free tier disappears, log a `remove` in history with a note explaining why
- Categories must match one of the existing values or be clearly justified as new

## Categories (current)

Audio / Music, Audio / Voice, Code / UI, Code Assistant, Image Generation,
LLM API, LLM Chatbot, Local / Self-hosted, Productivity, Search / Research, Video Generation
