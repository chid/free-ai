# Free AI Resources — Refresh Prompt

Use this prompt with Claude Code (or paste into Claude) to research and update the resources list.

---

## Prompt (copy everything below this line)

You are maintaining a curated list of free AI resources. The project root is your current working directory.

**Your task:** Research new free AI tools and services, then add any that are not already in the list, and open a pull request with your changes.

### Step 0 — Create a monthly branch

Before making any changes, create and switch to a branch named `refresh/YYYY-MM` using today's date (e.g. `refresh/2026-05`). If the branch already exists, switch to it.

```bash
git checkout -b refresh/$(date +%Y-%m) 2>/dev/null || git checkout refresh/$(date +%Y-%m)
```

### Step 1 — Read current state

Read `resources.csv` to see what's already listed. Note every `name` so you don't add duplicates.

Read `history.csv` to see what was recently added or removed.

### Step 2 — Research new resources

Search the web for recent free AI tools across these categories. Focus on tools released or updated in the last 6 months:

- LLM Chatbots and assistants (free tier)
- LLM APIs with free quotas
- Image generation (free or free tier)
- Code assistants (free for individuals)
- Local / self-hosted models and runners
- Audio, voice, music generation (free tier)
- Video generation (free tier)
- AI productivity tools (free tier)
- Search and research AI tools
- LLM routing, proxy, and orchestration tools (open-source or free — tools that expose a unified API across providers, wrap CLI/OAuth sessions, or handle fallback/load-balancing between models)
- LLM frameworks and agent libraries (open-source — for building pipelines, RAG systems, or optimizing prompts)

Good search queries to use:
- "free AI tools 2025"
- "free LLM API no credit card"
- "free AI image generator 2025"
- "best free AI coding assistant"
- site:reddit.com "free AI" new tools
- "free LLM proxy open source" OR "OpenAI compatible API wrapper"
- "open source LLM framework" OR "open source AI agent framework"

### Step 3 — Evaluate each candidate

Only add a resource if ALL of these are true:
- Has a genuine free tier (not just a trial with a credit card requirement)
- Is publicly accessible (not invite-only or waitlisted)
- Is not already in resources.csv (check by name and URL)
- Is a real, functioning product (not vaporware)

For each resource determine:
- `name` — short product name
- `category` — pick the closest from: LLM Chatbot, LLM API, Image Generation, Code Assistant, Local / Self-hosted, Audio / Voice, Audio / Music, Video Generation, Productivity, Search / Research, Code / UI, LLM Router, Agent Framework, RAG Framework, Prompt Optimization, LLM Client
- `url` — canonical homepage or signup URL
- `description` — one sentence, what it does, no hype
- `free_tier` — specific details (e.g. "Free tier with 100 requests/day", "Completely free", "$5 credit on signup")
- `requires_signup` — Yes or No
- `tags` — 3–6 lowercase comma-separated keywords

### Step 4 — Write changes

For each new resource to add, append a row to `resources.csv`.

Also append a row to `history.csv` for each addition:
```
date,action,name,category,url,notes
YYYY-MM-DD,add,<name>,<category>,<url>,found via refresh
```

### Step 5 — Check for stale entries

For each resource currently in `resources.csv`, consider whether it is likely to still be free and active. If you have strong evidence a tool has removed its free tier or shut down, remove it from `resources.csv` and log a `remove` entry in `history.csv` with a note explaining why.

### Step 6 — Open a pull request

Commit all changes to the `refresh/YYYY-MM` branch and push it, then open a PR against `main`:

```bash
git add resources.csv history.csv
git commit -m "refresh(YYYY-MM): add N tools, remove M stale entries"
git push -u origin refresh/$(date +%Y-%m)
gh pr create \
  --title "Monthly refresh: $(date +%B\ %Y)" \
  --body "$(cat <<'EOF'
## Changes
<!-- paste your Step 7 summary here -->

## Checklist
- [ ] No duplicate names or URLs
- [ ] All new entries have specific free_tier descriptions
- [ ] requires_signup is exactly Yes or No
- [ ] history.csv updated for every add/remove/edit
- [ ] Stale entries reviewed
EOF
)"
```

### Step 7 — Report

Output a summary (also paste it into the PR body above):
- How many resources were in the list before
- How many were added (list them)
- How many were removed (list them with reason)
- How many are in the list now
- Any notable changes in the AI landscape you noticed

---

## Running it

Open a Claude Code session in this project directory and paste the prompt above.

Or use the scheduled agent (see `CLAUDE.md`) which runs this automatically.
