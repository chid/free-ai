#!/usr/bin/env python3
"""Report new models.fyi model pages for review in the release timeline."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[2]
SITEMAP_URL = "https://models.fyi/sitemap.xml"
BASELINE_PATH = ROOT / ".github" / "upstreams" / "models-fyi-slugs.txt"


def fetch_model_slugs() -> set[str]:
    request = Request(SITEMAP_URL, headers={"User-Agent": "free-ai-upstream-check"})
    with urlopen(request, timeout=30) as response:
        sitemap = ElementTree.fromstring(response.read())

    slugs: set[str] = set()
    for element in sitemap.iter():
        if not element.tag.endswith("loc") or not element.text:
            continue
        parsed = urlparse(element.text.strip())
        if parsed.netloc.casefold() == "models.fyi" and parsed.path.startswith("/models/"):
            slug = parsed.path.rstrip("/").rsplit("/", 1)[-1]
            if slug:
                slugs.add(slug)
    return slugs


def load_release_names() -> set[str]:
    with (ROOT / "model_releases.csv").open(newline="", encoding="utf-8") as csv_file:
        return {normalize(row.get("name", "")) for row in csv.DictReader(csv_file)}


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def render_report(new_slugs: list[str]) -> str:
    lines = [
        "## New models.fyi model pages",
        "",
        f"Source: [models.fyi sitemap]({SITEMAP_URL}).",
        "Compared new model page slugs against the baseline recorded when this check was added and names in `model_releases.csv`.",
        "",
    ]
    if not new_slugs:
        lines.extend(["No new model pages need review.", ""])
        return "\n".join(lines)

    lines.extend([f"{len(new_slugs)} new model page(s) need review:", ""])
    for slug in new_slugs:
        lines.append(f"- [{slug}](https://models.fyi/models/{slug})")
    lines.extend(
        [
            "",
            "Check whether each page represents a notable release for the timeline. If accepted, add the verified release to `model_releases.csv` and append its change to `model_releases_history.csv`. If intentionally skipped, add its slug to `.github/upstreams/models-fyi-slugs.txt` so it is acknowledged and does not keep reappearing.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the Markdown report to this path")
    parser.add_argument("--github-output", type=Path, help="write has_new_models to a GitHub Actions output file")
    args = parser.parse_args()

    try:
        slugs = fetch_model_slugs()
    except (OSError, UnicodeError, ElementTree.ParseError, URLError) as error:
        print(f"Could not fetch or parse models.fyi sitemap: {error}", file=sys.stderr)
        return 2
    if not slugs:
        print("No model pages were found in the models.fyi sitemap; refusing an empty comparison.", file=sys.stderr)
        return 2
    if not BASELINE_PATH.is_file():
        print(f"Missing models.fyi baseline: {BASELINE_PATH}", file=sys.stderr)
        return 2

    baseline = {
        line.strip()
        for line in BASELINE_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }
    release_names = load_release_names()
    new_slugs = sorted(
        slug for slug in slugs if slug not in baseline and normalize(slug) not in release_names
    )
    report = render_report(new_slugs)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as output:
            output.write(f"has_new_models={'true' if new_slugs else 'false'}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
