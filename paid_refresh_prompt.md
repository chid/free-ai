# Paid AI Resources — Refresh Prompt

Use this prompt with Claude Code to research and update the paid tools list.
Only tools with **no meaningful free tier** belong here — if a tool has a
genuine free plan, it belongs in `resources.csv` instead.

---

## Prompt (copy everything below this line)

You are maintaining a curated list of notable paid AI tools. The project root is your current working directory.

**Your task:** Research notable paid-only AI tools and services, then add any that are not already in the list, and open a pull request with your changes.

### Step 0 — Create a monthly branch

Before making any changes, create and switch to a branch named `refresh/YYYY-MM` using today's date. If the branch already exists (e.g. a free-tools refresh already created it), switch to it.

```bash
git checkout -b refresh/$(date +%Y-%m) 2>/dev/null || git checkout refresh/$(date +%Y-%m)
```

### Step 1 — Read current state

Read `paid_resources.csv` to see what's already listed. Note every `name` so you don't add duplicates.

Read `resources.csv` to check for overlap — if a tool has a genuine free tier it is already there and should NOT be added to `paid_resources.csv`.

Read `paid_history.csv` to see what was recently added or removed.

### Step 2 — Research new resources

Search the web for notable paid AI tools across these categories. Focus on tools released or significantly updated in the last 6 months:

- LLM APIs (paid tiers only — no meaningful free quota)
- Frontier model access (GPT-5, Claude Pro/Max, Gemini Ultra, etc.)
- AI agents and automation platforms
- Paid code assistants and IDEs
- AI video generation (paid-only or only trivial free tier)
- AI image generation (paid-only)
- Audio / voice synthesis (paid-only)
- Enterprise AI productivity and workflow tools
- AI search and research tools (paid)

Good search queries to use:
- "best paid AI tools 2025 worth it"
- "AI tools worth paying for 2025"
- "best AI API paid tier comparison 2025"
- site:reddit.com "worth paying for" AI tools

### Step 3 — Evaluate each candidate

Only add a resource if ALL of these are true:
- Has **no genuine free tier** (or only a trivial credit/trial not enough for real use)
- Is not already in `paid_resources.csv` (check name and URL)
- Is not already in `resources.csv` with a free tier (check carefully)
- Is a real, functioning product used by a meaningful number of people
- Represents genuinely good value or is a market leader in its category

For each resource determine:
- `name` — short product name
- `category` — pick the closest from: LLM API, LLM Chatbot, Code Assistant, Image Generation, Video Generation, Audio / Voice, Audio / Music, Agent Platform, Productivity, Search / Research, Code / UI
- `url` — canonical homepage or pricing URL
- `description` — one sentence, what it does, no hype
- `pricing` — specific details (e.g. "$20/month Pro plan", "from $0.015/1K tokens", "starts at $25/month")
- `tags` — 3–6 lowercase comma-separated keywords

### Step 4 — Write changes

For each new resource to add, append a row to `paid_resources.csv`.

Also append a row to `paid_history.csv` for each addition:
```
date,action,name,category,url,notes
YYYY-MM-DD,add,<name>,<category>,<url>,found via refresh
```

### Step 5 — Check for stale entries, pricing changes, and graduations

For each resource currently in `paid_resources.csv`:

- **Pricing changed**: update the `pricing` field in-place and log an `edit` entry in `paid_history.csv` with a note describing the old and new values. Example note: `pricing changed from "$20/month" to "$25/month"`.
- **Gained a genuine free tier**: remove it from `paid_resources.csv`, add it to `resources.csv`, and log a `remove` in `paid_history.csv` and an `add` in `history.csv` (cross-reference each other in the notes).
- **Shut down or become irrelevant**: remove it and log a `remove` in `paid_history.csv`.

### Step 6 — Open a pull request

Commit all changes to the `refresh/YYYY-MM` branch and push, then open (or update) a PR against `main`:

```bash
git add paid_resources.csv paid_history.csv resources.csv history.csv
git commit -m "refresh(YYYY-MM): paid tools — add N, remove M"
git push -u origin refresh/$(date +%Y-%m)
gh pr create \
  --title "Monthly refresh: $(date +%B\ %Y)" \
  --body "$(cat <<'EOF'
## Changes
<!-- paste your Step 7 summary here -->

## Checklist
- [ ] No tool with a genuine free tier added to paid_resources.csv
- [ ] No overlap with resources.csv
- [ ] pricing field is specific (not vague like "various plans")
- [ ] paid_history.csv updated for every add/remove/edit
- [ ] Graduated tools moved to resources.csv if they gained a free tier
EOF
)" 2>/dev/null || echo "PR may already exist for this branch — push only"
```

### Step 7 — Report

- How many paid resources were in the list before
- How many were added (list them with price points)
- How many were removed or graduated to the free list
- How many are in the list now
- Any notable pricing changes or market shifts observed

---

## Running it

Open a Claude Code session in this project directory and paste the prompt above.

Ideally run this in the same monthly session as `refresh_prompt.md` so both
free and paid tools land in the same `refresh/YYYY-MM` branch and PR.
