#!/usr/bin/env python3
"""Regenerate README.md from resources.csv and paid_resources.csv.

The README used to be hand-maintained and drifted out of sync with the CSVs
(missing rows, stale counts, missing categories). Run this after any change:

    python3 generate_readme.py
"""
import csv
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.abspath(__file__))

# Category -> (section heading, blurb). Order here is the order in the README.
SECTIONS = [
    ("LLM Chatbot", "LLM Chatbots",
     "Full-featured AI chat interfaces with free tiers."),
    ("LLM API", "LLM APIs",
     "Programmatic access to large language models with free quotas."),
    ("LLM Router", "LLM Routers & Gateways",
     "Route one request across many providers, with fallback and rate-limit handling."),
    ("LLM Client", "LLM Clients",
     "Thin libraries for talking to several model providers through one interface."),
    ("Code Assistant", "Code Assistants",
     "AI tools that live in your editor or terminal."),
    ("Code / UI", "Code & UI Builders",
     "Generate full UIs and apps from a prompt in the browser."),
    ("Image Generation", "Image Generation",
     "Text-to-image tools that are free or have a meaningful free tier."),
    ("Video Generation", "Video Generation",
     "AI tools for generating or editing video."),
    ("Audio / Voice", "Audio & Voice",
     "Text-to-speech, voice cloning, and speech recognition."),
    ("Audio / Music", "Music Generation",
     "Generate original music from text prompts."),
    ("Local / Self-hosted", "Local & Self-hosted",
     "Run models on your own hardware — no API keys, no data leaving your machine."),
    ("Search / Research", "Search & Research",
     "AI-powered search engines and research tools."),
    ("Productivity", "Productivity",
     "AI tools for writing, notes, diagrams, presentations, and task automation."),
    ("Agent Framework", "Agent Frameworks",
     "Open-source libraries for building single and multi-agent LLM systems. "
     "All are free to use — costs come only from the models you connect."),
    ("RAG Framework", "RAG Frameworks",
     "Connect models to your own data for retrieval-augmented generation."),
    ("Prompt Optimization", "Prompt Optimization",
     "Optimise prompts and pipelines programmatically instead of by hand."),
]

PREAMBLE = """# Awesome Free AI

> A snapshot of genuinely free (or free-tier) AI tools, APIs, and platforms **as \
they existed in {month}**.

Free tiers change fast — tools get paywalled, rebranded, or shut down. This list \
captures what was on offer at the time of each update, with every change tracked in \
[`history.csv`](history.csv) and summarised in [`CHANGELOG.md`](CHANGELOG.md). Think \
of it less as a permanent directory and more as a dated edition: accurate when \
written, audited on refresh.

**{count} free resources** across {n_cats} categories, plus \
[{paid_count} notable paid-only tools](paid_resources.csv). Browse the \
[web view](index.html) for a filterable, searchable UI, or read on.
"""

OUTRO = """---

## Contributing

The list is driven by [`resources.csv`](resources.csv) — edit that file to add or \
change entries. This README is generated from it, so regenerate after any change:

```bash
python3 generate_readme.py
```

**Quick add via CLI:**
```bash
python3 update.py
```

**Manual CSV edit** — append a row with these columns:
```
name, category, url, description, free_tier, requires_signup, tags
```

**Criteria for inclusion:**
- Has a genuine free tier (no credit card required to start, unless noted)
- Publicly accessible — not waitlisted or invite-only
- Active and functional product
- AI is a core part of the product, not a minor feature

Tools with no genuine free tier belong in [`paid_resources.csv`](paid_resources.csv) \
instead.

All changes are logged to [`history.csv`](history.csv) / \
[`paid_history.csv`](paid_history.csv), which are append-only.

**Automated refresh:** Open a Claude Code session here and paste \
[`refresh_prompt.md`](refresh_prompt.md) (free tools) or \
[`paid_refresh_prompt.md`](paid_refresh_prompt.md) (paid tools) to have Claude \
research new tools and update the list.
"""


def slug(heading):
    """GitHub-flavoured anchor for a heading."""
    s = heading.lower().replace(" ", "-")
    return re.sub(r"[^a-z0-9\-]", "", s)


def read(path):
    with open(os.path.join(ROOT, path), newline="") as fh:
        return [r for r in csv.DictReader(fh) if r.get("name")]


def entry(row):
    desc = row["description"].rstrip(". ")
    line = f'- **[{row["name"]}]({row["url"]})** — {desc}. *{row["free_tier"].rstrip(". ")}.*'
    if row["requires_signup"] == "No":
        line += " *No signup required.*"
    return line


def main():
    resources = read("resources.csv")
    paid = read("paid_resources.csv")

    known = {cat for cat, _, _ in SECTIONS}
    unknown = sorted({r["category"] for r in resources} - known)
    if unknown:
        sys.exit(f"error: category not mapped to a README section: {unknown}\n"
                 f"add it to SECTIONS in generate_readme.py")

    used = [(cat, head, blurb) for cat, head, blurb in SECTIONS
            if any(r["category"] == cat for r in resources)]

    out = [PREAMBLE.format(month=date.today().strftime("%B %Y"),
                           count=len(resources), n_cats=len(used),
                           paid_count=len(paid)),
           "---\n", "## Contents\n"]
    out += [f"- [{head}](#{slug(head)})" for _, head, _ in used]
    out += ["- [Contributing](#contributing)", "", "---", ""]

    for cat, head, blurb in used:
        out += [f"## {head}", "", blurb, ""]
        out += [entry(r) for r in resources if r["category"] == cat]
        out.append("")

    out.append(OUTRO)

    with open(os.path.join(ROOT, "README.md"), "w") as fh:
        fh.write("\n".join(out))

    print(f"README.md: {len(resources)} resources across {len(used)} categories")


if __name__ == "__main__":
    main()
