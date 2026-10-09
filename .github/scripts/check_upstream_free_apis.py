#!/usr/bin/env python3
"""Report upstream providers that are missing from our free and paid catalogs."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
UPSTREAM_README = (
    "https://raw.githubusercontent.com/mnfst/awesome-free-llm-apis/main/README.md"
)
API_CATALOGS = ("resources.csv", "paid_resources.csv")
MULTIPART_SUFFIXES = {
    "co.uk", "com.au", "co.nz", "com.cn", "com.br", "com.sg", "co.jp", "co.in"
}
IGNORED_NAME_WORDS = {"ai", "api", "cloud", "inference", "llm", "provider", "providers"}
HEADING_RE = re.compile(r"^### \[([^\]]+)\]\((https?://[^)]+)\)")


@dataclass(frozen=True)
class Provider:
    name: str
    url: str
    section: str


def fetch_readme() -> str:
    request = Request(UPSTREAM_README, headers={"User-Agent": "free-ai-upstream-check"})
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def parse_providers(readme: str) -> list[Provider]:
    providers: list[Provider] = []
    section = ""
    for line in readme.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if section not in {"Provider APIs", "Inference providers"}:
            continue
        match = HEADING_RE.match(line)
        if match:
            providers.append(Provider(match.group(1).strip(), match.group(2).strip(), section))
    return providers


def load_catalog_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for filename in API_CATALOGS:
        with (ROOT / filename).open(newline="", encoding="utf-8") as csv_file:
            for row in csv.DictReader(csv_file):
                row["_catalog"] = filename
                rows.append(row)
    return rows


def registrable_domain(url: str) -> str:
    hostname = (urlparse(url).hostname or "").casefold().rstrip(".")
    hostname = hostname.removeprefix("www.")
    labels = hostname.split(".")
    if len(labels) < 2:
        return hostname
    suffix = ".".join(labels[-2:])
    if suffix in MULTIPART_SUFFIXES and len(labels) >= 3:
        return ".".join(labels[-3:])
    return suffix


def significant_words(value: str) -> set[str]:
    words = set(re.findall(r"[a-z0-9]+", value.casefold()))
    return words - IGNORED_NAME_WORDS


def is_covered(provider: Provider, rows: list[dict[str, str]]) -> bool:
    provider_domain = registrable_domain(provider.url)
    provider_words = significant_words(provider.name)
    for row in rows:
        if provider_domain and provider_domain == registrable_domain(row.get("url", "")):
            return True
        row_words = significant_words(row.get("name", ""))
        if provider_words and row_words and (provider_words <= row_words or row_words <= provider_words):
            return True
    return False


def render_report(providers: list[Provider], missing: list[Provider]) -> str:
    lines = [
        "## Upstream free LLM API review",
        "",
        f"Source: [{UPSTREAM_README}](https://github.com/mnfst/awesome-free-llm-apis).",
        "Compared provider links and names against all entries in `resources.csv` and `paid_resources.csv`.",
        "",
    ]
    if not missing:
        lines.extend([f"All {len(providers)} upstream providers have a corresponding resource entry.", ""])
        return "\n".join(lines)

    lines.extend(
        [
            f"{len(missing)} of {len(providers)} upstream providers do not appear in either resource catalog:",
            "",
        ]
    )
    for provider in missing:
        lines.append(f"- [{provider.name}]({provider.url}) — {provider.section}")
    lines.extend(
        [
            "",
            "Review each provider's current free access and eligibility against the project rules before adding it. If accepted, update the relevant resource CSV and history file, then refresh `README.md` and `CHANGELOG.md`.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="write the Markdown report to this path")
    parser.add_argument("--github-output", type=Path, help="write has_missing to a GitHub Actions output file")
    args = parser.parse_args()

    try:
        providers = parse_providers(fetch_readme())
    except (OSError, UnicodeError, URLError) as error:
        print(f"Could not fetch upstream README: {error}", file=sys.stderr)
        return 2
    if not providers:
        print("No provider headings were found in the upstream README; refusing an empty comparison.", file=sys.stderr)
        return 2

    rows = load_catalog_rows()
    missing = [provider for provider in providers if not is_covered(provider, rows)]
    report = render_report(providers, missing)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as output:
            output.write(f"has_missing={'true' if missing else 'false'}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
