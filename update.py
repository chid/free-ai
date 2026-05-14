#!/usr/bin/env python3
"""
Interactive CLI to add, remove, or update entries in resources.csv.
All changes are appended to history.csv with a timestamp.
Usage: python3 update.py
"""

import csv
import os
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE, "resources.csv")
HISTORY_PATH = os.path.join(BASE, "history.csv")
FIELDS = ["name", "category", "url", "description", "free_tier", "requires_signup", "tags"]
HISTORY_FIELDS = ["date", "action", "name", "category", "url", "notes"]

CATEGORIES = [
    "Audio / Music",
    "Audio / Voice",
    "Code / UI",
    "Code Assistant",
    "Image Generation",
    "LLM API",
    "LLM Chatbot",
    "Local / Self-hosted",
    "Productivity",
    "Search / Research",
    "Video Generation",
]


# ── persistence ──────────────────────────────────────────────────────────────

def load() -> list[dict]:
    if not os.path.exists(CSV_PATH):
        return []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save(rows: list[dict]) -> None:
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)


def log_history(action: str, name: str, category: str = "", url: str = "", notes: str = "") -> None:
    exists = os.path.exists(HISTORY_PATH)
    with open(HISTORY_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HISTORY_FIELDS, quoting=csv.QUOTE_MINIMAL)
        if not exists:
            writer.writeheader()
        writer.writerow({
            "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "action": action,
            "name": name,
            "category": category,
            "url": url,
            "notes": notes,
        })


# ── helpers ───────────────────────────────────────────────────────────────────

def ask(label: str, default: str = "") -> str:
    hint = f" [{default}]" if default else ""
    val = input(f"  {label}{hint}: ").strip()
    return val if val else default


def pick_category() -> str:
    print("\n  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i:2}. {cat}")
    print("     0. Enter custom category")
    while True:
        choice = input("  Pick number (or 0 for custom): ").strip()
        if choice == "0":
            return input("  Custom category: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("  Invalid choice, try again.")


# ── actions ───────────────────────────────────────────────────────────────────

def add(rows: list[dict]) -> list[dict]:
    print("\n--- Add a new resource ---")
    name = ask("Name")
    if not name:
        print("  Name is required.")
        return rows
    if any(r["name"].lower() == name.lower() for r in rows):
        print(f"  '{name}' already exists.")
        return rows

    category = pick_category()
    url = ask("URL")
    description = ask("Description")
    free_tier = ask("Free tier details", "Free tier available")
    requires_signup = ""
    while requires_signup not in ("Yes", "No"):
        requires_signup = ask("Requires signup? (Yes/No)", "Yes")
    tags = ask("Tags (comma-separated, e.g. coding,api,chat)")

    rows.append({
        "name": name,
        "category": category,
        "url": url,
        "description": description,
        "free_tier": free_tier,
        "requires_signup": requires_signup,
        "tags": tags,
    })
    save(rows)
    log_history("add", name, category, url)
    print(f"\n  Added '{name}'. Refresh index.html to see it.")
    return rows


def remove(rows: list[dict]) -> list[dict]:
    print("\n--- Remove a resource ---")
    query = input("  Name to remove (partial match): ").strip().lower()
    matches = [(i, r) for i, r in enumerate(rows) if query in r["name"].lower()]
    if not matches:
        print("  No matches found.")
        return rows

    for i, (_, r) in enumerate(matches, 1):
        print(f"  {i}. {r['name']} ({r['category']})")

    choice = input("  Pick number to delete (Enter to cancel): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(matches)):
        print("  Cancelled.")
        return rows

    idx, r = matches[int(choice) - 1]
    confirm = input(f"  Delete '{r['name']}'? (y/N): ").strip().lower()
    if confirm == "y":
        rows.pop(idx)
        save(rows)
        log_history("remove", r["name"], r["category"], r["url"])
        print(f"  Removed '{r['name']}'.")
    else:
        print("  Cancelled.")
    return rows


def edit(rows: list[dict]) -> list[dict]:
    print("\n--- Edit a resource ---")
    query = input("  Name to edit (partial match): ").strip().lower()
    matches = [(i, r) for i, r in enumerate(rows) if query in r["name"].lower()]
    if not matches:
        print("  No matches found.")
        return rows

    for i, (_, r) in enumerate(matches, 1):
        print(f"  {i}. {r['name']} ({r['category']})")

    choice = input("  Pick number (Enter to cancel): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(matches)):
        print("  Cancelled.")
        return rows

    idx, r = matches[int(choice) - 1]
    print(f"\n  Editing '{r['name']}' — press Enter to keep current value\n")
    updated = {
        "name":            ask("Name", r["name"]),
        "category":        ask("Category (Enter to keep, 'pick' to choose)", r["category"]),
        "url":             ask("URL", r["url"]),
        "description":     ask("Description", r["description"]),
        "free_tier":       ask("Free tier details", r["free_tier"]),
        "requires_signup": ask("Requires signup? (Yes/No)", r["requires_signup"]),
        "tags":            ask("Tags", r["tags"]),
    }
    if updated["category"].strip().lower() == "pick":
        updated["category"] = pick_category()

    changes = [f for f in FIELDS if updated[f] != r[f]]
    if not changes:
        print("  No changes made.")
        return rows

    rows[idx] = updated
    save(rows)
    log_history("edit", updated["name"], updated["category"], updated["url"],
                f"changed: {', '.join(changes)}")
    print(f"\n  Updated '{updated['name']}'.")
    return rows


def show_history() -> None:
    if not os.path.exists(HISTORY_PATH):
        print("  No history yet.")
        return
    with open(HISTORY_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("  History is empty.")
        return
    print(f"\n  {'Date':<12} {'Action':<8} {'Name'}")
    print("  " + "-" * 50)
    for r in reversed(rows[-50:]):
        print(f"  {r['date']:<12} {r['action']:<8} {r['name']}")
    if len(rows) > 50:
        print(f"\n  … {len(rows) - 50} older entries in history.csv")


def list_resources(rows: list[dict]) -> None:
    if not rows:
        print("  No resources found.")
        return
    by_cat: dict[str, list] = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(r["name"])
    for cat in sorted(by_cat):
        print(f"\n  {cat}")
        for name in sorted(by_cat[cat]):
            print(f"    • {name}")
    print(f"\n  Total: {len(rows)}")


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    rows = load()
    while True:
        print(f"\nFree AI Resources — {len(rows)} entries")
        print("  1. Add resource")
        print("  2. Remove resource")
        print("  3. Edit resource")
        print("  4. List all")
        print("  5. Show history")
        print("  6. Quit")
        choice = input("Choice: ").strip()
        if choice == "1":
            rows = add(rows)
        elif choice == "2":
            rows = remove(rows)
        elif choice == "3":
            rows = edit(rows)
        elif choice == "4":
            list_resources(rows)
        elif choice == "5":
            show_history()
        elif choice == "6":
            break
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit(0)
