# Tier Watcher — Setup Prompt (one-time)

Use this prompt with a coding agent session to build the **tier-change watcher**: a
local-only cache of vendor pricing/quota pages plus a small differ, so monthly
refreshes research only the tools whose pages actually changed instead of all ~70.

This is a *one-time tooling* prompt, not a recurring refresh prompt. Run it once;
after that the recurring refresh prompts can call `python3 check_tiers.py` first and
treat its output as the research shortlist.

---

## Prompt (copy everything below this line)

You are working in a repository that maintains a CSV-driven directory of free, paid
and local AI tools (`resources.csv`, `paid_resources.csv`, `local_resources.csv`
plus history logs, rendered by `index.html`). Its conventions live in `AGENTS.md` —
**read it first**, along with `sync_activity.py` (the existing cache-based sync
script your new script should complement, not modify) and `quotas.py`.

**Your task:** build a local tier-change watcher consisting of `check_tiers.py`,
`watch_pages.csv` and a gitignored `.cache/` directory, then run a first seed pass.

### Background and goal

Free-tier churn shows up on vendor pricing/quota *pages* before it shows up anywhere
else. Re-researching every tool each month is wasteful; instead we snapshot the
relevant pages locally and diff them between runs. The cache is a local working
copy only — it is **never committed** (`history.csv` already records the outcomes).

### Step 1 — `watch_pages.csv` (committed)

Create `watch_pages.csv` with columns:

```
name,watch_url,notes
```

- `name` — must exactly match the `name` in `resources.csv` / `paid_resources.csv` /
  `local_resources.csv`. File is LF line endings.
- `watch_url` — the vendor page most likely to reveal a tier change (pricing page,
  free-tier docs, rate-limit docs — **not** the marketing homepage).
- Include only tools whose tiers actually move (roughly 25–35 rows): every SaaS API
  (LLM API, LLM Router categories), hosted chatbots, code assistants with hosted
  plans, and media generators from `resources.csv`; every row of `paid_resources.csv`.
  Skip pure open-source frameworks and pure local runners — GitHub metadata for
  those is already covered by `sync_activity.py`.
- `notes` — optional; use `js-rendered` for pages that a plain HTTP fetch cannot
  capture meaningfully (client-side rendered pricing tables), so the differ knows
  to mark them "needs manual check" instead of snapshotting noise. Keep the field
  minimal-quoting compliant (quote only if it contains a comma).

### Step 2 — `check_tiers.py`

A single-file, **stdlib-only** script (match the style of `sync_activity.py` —
no new dependencies, `urllib.request` for fetching, no framework). Behaviour:

```bash
python3 check_tiers.py          # fetch all, diff vs cached snapshots, print report
python3 check_tiers.py --diff "GitHub Copilot"   # unified diff for one tool
python3 check_tiers.py --seed   # write/refresh snapshots without reporting diffs
```

Details:

- For each row of `watch_pages.csv`, GET `watch_url` with a browser-like
  `User-Agent` header, a 20s timeout, and per-URL error isolation (a failed fetch
  must not abort the run — record it under a "fetch errors" section of the report).
- Normalise fetched HTML to plain text: strip `<script>`/`<style>`/comments, tags,
  collapse whitespace. Any stdlib approach (`html.parser`) is fine.
- Snapshot to `.cache/tiers/<slug>.txt` where `<slug>` is a filesystem-safe version
  of `name` (lowercase, non-alphanumeric → `-`). Create `.cache/tiers/` as needed.
- On a plain run, diff each new page against its cached snapshot
  (`difflib.unified_diff`) and print:
  - a "changed" list — tool names whose page changed, with a thin snippet (a few
    diff hunks, ≤20 lines per tool);
  - an "unchanged" name list, one line total;
  - the "fetch errors" list, one line per error;
  - a "js-rendered" list of tools flagged for manual checking.
  Then update the snapshots so tomorrow's diff is relative to today.
- Output ends with a paste-ready line: `Likely changed: <names>`.
- Never write to any CSV or doc — this script is read-only against the repo data.

### Step 3 — Git hygiene

- Add `.cache/` to `.gitignore` (keep any existing contents; line-based edit).
- Do **not** commit the cache. Do **not** modify any existing CSV/doc.
- Before committing, run per-file line-ending checks on `watch_pages.csv`
  (must be LF) and verify it parses: exactly 3 fields per row.
- Validate your script by actually running `--seed` then a plain run twice: the
  second run should report everything unchanged (fetch errors notwithstanding).

### Step 4 — Wire it into this repo's docs

- `AGENTS.md`: add `check_tiers.py` and `watch_pages.csv` to the **Files** table,
  and add a short "Tier-change watching" paragraph under **How to run a refresh**
  instructing future refreshes to run `python3 check_tiers.py` first and prioritise
  the changed list.
- `README.md` (contributing section only, one sentence) — mention the watcher as
  pre-refresh tooling.

### Step 5 — Branch, commit, PR

Land this on the monthly refresh branch per repo convention:

```bash
git checkout -b refresh/$(date +%Y-%m) 2>/dev/null || git checkout refresh/$(date +%Y-%m)
git add check_tiers.py watch_pages.csv .gitignore AGENTS.md README.md
git commit -m "tooling: add tier-change watcher (check_tiers.py + watch_pages.csv)"
git push -u origin refresh/$(date +%Y-%m)
```

If a PR for that branch already exists, the push updates it; otherwise open one
with `gh pr create`. Summarise in the PR body: how many pages are watched, how many
fetched cleanly on the seed run, which are js-rendered/manual, and the first diff
report output.

### What to report back

- Row count of `watch_pages.csv` and how it was derived (which categories included/excluded).
- Seed-run stats: clean fetches, fetch errors (with reasons), js-rendered exclusions.
- Confirmation that a second plain run reports "no changes".
- Paths of every file created/edited and the PR URL.

---

## Running it

Open a coding agent session in this project directory and paste the prompt above.
One shot; no schedule needed. Afterwards, plain `python3 check_tiers.py` is the
pre-refresh gate.
