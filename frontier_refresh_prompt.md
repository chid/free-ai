# Frontier Labs — Refresh Prompt

Tracks pricing, context windows, free-tier limits, and model releases for
the major AI labs. Run monthly alongside the free and paid refresh prompts
so all changes land in the same `refresh/YYYY-MM` PR.

---

## Prompt (copy everything below this line)

You are maintaining a model-level pricing and capability tracker for frontier
AI labs. The project root is your current working directory.

**Your task:** Research the current state of every lab and model in the tracker,
update any changed values, add new models, deprecate retired ones, and log
every change with old and new values so the history is a full audit trail.

### Step 0 — Create or switch to the monthly branch

```bash
git checkout -b refresh/$(date +%Y-%m) 2>/dev/null || git checkout refresh/$(date +%Y-%m)
```

### Step 1 — Read current state

Read `frontier_labs.csv` — the list of labs being tracked.
Read `frontier_models.csv` — current model rows with their last-known values.
Read `frontier_history.csv` — recent changes so you know what already moved.

### Step 2 — Research each lab

For each lab in `frontier_labs.csv`, search for:
- Current flagship and recent models
- Official API pricing page (input + output cost per million tokens)
- Context window for each model
- Whether a free API tier exists and its limits
- Any models released or deprecated since the last refresh

Good search queries per lab (substitute lab name):
- `"<lab> API pricing 2026"`
- `"<lab> new model 2026"`
- `site:<api_platform_url> pricing`

Also run a broad sweep:
- `"frontier AI model pricing comparison 2026"`
- `"LLM pricing per million tokens 2026"`

### Step 3 — Update frontier_models.csv

For each model currently in `frontier_models.csv`:
- Check every tracked field against your research.
- If a value has changed, update the row AND log it in `frontier_history.csv`
  (see Step 5 for the log format).

Fields to check and update:
- `input_per_1M_usd` — cost per million input tokens (USD)
- `output_per_1M_usd` — cost per million output tokens (USD)
- `context_window_k` — context window in thousands of tokens
- `free_tier` — Yes or No
- `free_tier_details` — specific rate-limit details (e.g. "1500 req/day via AI Studio")
- `status` — one of: `active`, `preview`, `deprecated`
- `last_checked` — update to today's date whenever you verify a row

For any **new** model not yet in the file, append a row with all fields populated.

For any **deprecated** model, set `status` to `deprecated` (do not delete the row).

### Step 4 — Update frontier_labs.csv

If a lab has a new API platform URL, chatbot URL, or notable structural change
(acquisition, rename, shutdown), update the row and log an `update` entry in
`frontier_history.csv` with `model` = `—`.

### Step 5 — Log every change in frontier_history.csv

Append one row per changed field. Schema:

```
date,action,lab,model,field,old_value,new_value,notes
```

Valid `action` values:
- `add-model` — new model added
- `update` — existing field value changed
- `deprecate` — model status set to deprecated
- `add-lab` — new lab added to frontier_labs.csv
- `remove-lab` — lab removed (shutdown or out of scope)

Example rows:
```
2026-06-01,update,Anthropic,claude-opus-5,input_per_1M_usd,15.00,12.00,price cut announced on blog
2026-06-01,update,OpenAI,gpt-5,context_window_k,128,200,increased context per release notes
2026-06-01,add-model,xAI,grok-3-mini,—,—,—,new lightweight model released
2026-06-01,deprecate,OpenAI,gpt-4,status,active,deprecated,removed from API as of 2026-06-01
```

If a value is unchanged, do NOT log it — only log actual changes.

### Step 6 — Commit and push

```bash
git add frontier_labs.csv frontier_models.csv frontier_history.csv
git commit -m "refresh(YYYY-MM): frontier — N models updated, M added, K deprecated"
git push -u origin refresh/$(date +%Y-%m)
```

If a PR for this branch already exists (from the free or paid refresh), do not
open a second one — the commit will appear automatically in the existing PR.
If no PR exists yet, open one:

```bash
gh pr create \
  --title "Monthly refresh: $(date +%B\ %Y)" \
  --body "## Frontier changes
<!-- paste Step 7 summary here -->" \
  2>/dev/null || echo "PR already open for this branch"
```

### Step 7 — Report

- How many models were tracked before this refresh
- How many models were added (list lab + model name)
- How many models were deprecated
- How many field-level changes were logged (pricing, context, free tier)
- Notable pricing trends or capability jumps you observed

---

## Running it

Run in the same Claude Code session as `refresh_prompt.md` and
`paid_refresh_prompt.md` so all three land in one `refresh/YYYY-MM` PR:

```bash
claude
# 1. paste refresh_prompt.md        → free tools
# 2. paste paid_refresh_prompt.md   → paid tools
# 3. paste frontier_refresh_prompt.md → labs & models
```

## frontier_models.csv column reference

| Column | Format | Example |
|---|---|---|
| `lab` | Lab name matching frontier_labs.csv | `Anthropic` |
| `model` | Official model identifier | `claude-opus-4-5` |
| `modality` | `text`, `multimodal`, `image`, `audio`, `video` | `multimodal` |
| `context_window_k` | Integer, thousands of tokens | `200` |
| `input_per_1M_usd` | Decimal USD, blank if not API-available | `15.00` |
| `output_per_1M_usd` | Decimal USD, blank if not API-available | `75.00` |
| `free_tier` | `Yes` or `No` | `Yes` |
| `free_tier_details` | Specific limits or blank | `1500 req/day via AI Studio` |
| `status` | `active`, `preview`, or `deprecated` | `active` |
| `last_checked` | ISO date | `2026-05-16` |
