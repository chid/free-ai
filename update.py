#!/usr/bin/env python3
"""
Interactive CLI to add, remove, or update entries in resources.csv and paid_resources.csv.
All changes are appended to history.csv or paid_history.csv with a timestamp.
Usage: python3 update.py
"""

import csv
import os
import sys
from datetime import datetime, timezone

BASE = os.path.dirname(os.path.abspath(__file__))
FREE_CSV = os.path.join(BASE, "resources.csv")
FREE_HISTORY = os.path.join(BASE, "history.csv")
PAID_CSV = os.path.join(BASE, "paid_resources.csv")
PAID_HISTORY = os.path.join(BASE, "paid_history.csv")

FREE_FIELDS = ["name", "category", "url", "description", "free_tier", "requires_signup", "tags"]
PAID_FIELDS = ["name", "category", "url", "description", "pricing", "tags"]
HISTORY_FIELDS = ["date", "action", "name", "category", "url", "notes"]

CATEGORIES = [
    "Agent Framework",
    "Audio / Music",
    "Audio / Voice",
    "Code / UI",
    "Code Assistant",
    "Image Generation",
    "LLM API",
    "LLM Chatbot",
    "LLM Client",
    "LLM Router",
    "Local / Self-hosted",
    "Productivity",
    "Prompt Optimization",
    "RAG Framework",
    "Search / Research",
    "Video Generation",
]


# ── persistence ──────────────────────────────────────────────────────────────

def load_csv(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_csv(path: str, fields: list[str], rows: list[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(rows)


def log_history(path: str, action: str, name: str, category: str = "", url: str = "", notes: str = "") -> None:
    exists = os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
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


def clean_tags(tags_str: str) -> str:
    parts = [t.strip().lower() for t in tags_str.split(",") if t.strip()]
    return ",".join(parts)


def pick_category(current: str = "") -> str:
    print("\n  Categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        mark = " (current)" if cat == current else ""
        print(f"    {i:2}. {cat}{mark}")
    print("     0. Enter custom category")
    while True:
        choice = input("  Pick number (or 0 for custom): ").strip()
        if choice == "0":
            return input("  Custom category: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("  Invalid choice, try again.")


# ── actions: free tools ───────────────────────────────────────────────────────

def add_free(rows: list[dict]) -> list[dict]:
    print("\n--- Add a new free resource ---")
    name = ask("Name")
    if not name:
        print("  Name is required.")
        return rows
    if any(r["name"].lower() == name.lower() for r in rows):
        print(f"  '{name}' already exists in free resources.")
        return rows

    category = pick_category()
    url = ask("URL")
    description = ask("Description")
    free_tier = ask("Free tier details", "Free tier available")
    requires_signup = ""
    while requires_signup not in ("Yes", "No"):
        requires_signup = ask("Requires signup? (Yes/No)", "Yes")
    tags = clean_tags(ask("Tags (comma-separated, e.g. coding,api,chat)"))

    rows.append({
        "name": name,
        "category": category,
        "url": url,
        "description": description,
        "free_tier": free_tier,
        "requires_signup": requires_signup,
        "tags": tags,
    })
    save_csv(FREE_CSV, FREE_FIELDS, rows)
    log_history(FREE_HISTORY, "add", name, category, url)
    print(f"\n  Added '{name}' to resources.csv and logged to history.csv.")
    return rows


def remove_free(rows: list[dict]) -> list[dict]:
    print("\n--- Remove a free resource ---")
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
        reason = ask("Reason/Notes (for history.csv)")
        rows.pop(idx)
        save_csv(FREE_CSV, FREE_FIELDS, rows)
        log_history(FREE_HISTORY, "remove", r["name"], r["category"], r["url"], reason)
        print(f"  Removed '{r['name']}'.")
    else:
        print("  Cancelled.")
    return rows


def edit_free(rows: list[dict]) -> list[dict]:
    print("\n--- Edit a free resource ---")
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

    category = ask("Category (Enter to keep, 'pick' to choose)", r["category"])
    if category.strip().lower() == "pick":
        category = pick_category(r["category"])

    requires_signup = r["requires_signup"]
    signup_input = ask("Requires signup? (Yes/No)", r["requires_signup"])
    if signup_input in ("Yes", "No"):
        requires_signup = signup_input

    updated = {
        "name":            ask("Name", r["name"]),
        "category":        category,
        "url":             ask("URL", r["url"]),
        "description":     ask("Description", r["description"]),
        "free_tier":       ask("Free tier details", r["free_tier"]),
        "requires_signup": requires_signup,
        "tags":            clean_tags(ask("Tags", r["tags"])),
    }

    changes = [f for f in FREE_FIELDS if updated[f] != r[f]]
    if not changes:
        print("  No changes made.")
        return rows

    rows[idx] = updated
    save_csv(FREE_CSV, FREE_FIELDS, rows)
    notes = ask("History notes (Enter for auto diff)", f"changed: {', '.join(changes)}")
    log_history(FREE_HISTORY, "edit", updated["name"], updated["category"], updated["url"], notes)
    print(f"\n  Updated '{updated['name']}'.")
    return rows


# ── actions: paid tools ───────────────────────────────────────────────────────

def add_paid(rows: list[dict]) -> list[dict]:
    print("\n--- Add a new paid resource ---")
    name = ask("Name")
    if not name:
        print("  Name is required.")
        return rows
    if any(r["name"].lower() == name.lower() for r in rows):
        print(f"  '{name}' already exists in paid resources.")
        return rows

    category = pick_category()
    url = ask("URL")
    description = ask("Description")
    pricing = ask("Pricing details (e.g. $20/month)")
    tags = clean_tags(ask("Tags (comma-separated, e.g. productivity,writing,subscription)"))

    rows.append({
        "name": name,
        "category": category,
        "url": url,
        "description": description,
        "pricing": pricing,
        "tags": tags,
    })
    save_csv(PAID_CSV, PAID_FIELDS, rows)
    log_history(PAID_HISTORY, "add", name, category, url)
    print(f"\n  Added '{name}' to paid_resources.csv and logged to paid_history.csv.")
    return rows


def remove_paid(rows: list[dict]) -> list[dict]:
    print("\n--- Remove a paid resource ---")
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
        reason = ask("Reason/Notes (for paid_history.csv)")
        rows.pop(idx)
        save_csv(PAID_CSV, PAID_FIELDS, rows)
        log_history(PAID_HISTORY, "remove", r["name"], r["category"], r["url"], reason)
        print(f"  Removed '{r['name']}'.")
    else:
        print("  Cancelled.")
    return rows


def edit_paid(rows: list[dict]) -> list[dict]:
    print("\n--- Edit a paid resource ---")
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

    category = ask("Category (Enter to keep, 'pick' to choose)", r["category"])
    if category.strip().lower() == "pick":
        category = pick_category(r["category"])

    updated = {
        "name":        ask("Name", r["name"]),
        "category":    category,
        "url":         ask("URL", r["url"]),
        "description": ask("Description", r["description"]),
        "pricing":     ask("Pricing", r["pricing"]),
        "tags":        clean_tags(ask("Tags", r["tags"])),
    }

    changes = [f for f in PAID_FIELDS if updated[f] != r[f]]
    if not changes:
        print("  No changes made.")
        return rows

    rows[idx] = updated
    save_csv(PAID_CSV, PAID_FIELDS, rows)
    notes = ask("History notes (Enter for auto diff)", f"changed: {', '.join(changes)}")
    log_history(PAID_HISTORY, "edit", updated["name"], updated["category"], updated["url"], notes)
    print(f"\n  Updated '{updated['name']}'.")
    return rows


# ── actions: migrate between lists ───────────────────────────────────────────

def move_free_to_paid(free_rows: list[dict], paid_rows: list[dict]) -> tuple[list[dict], list[dict]]:
    print("\n--- Move Free Tool -> Paid List ---")
    query = input("  Name to move (partial match): ").strip().lower()
    matches = [(i, r) for i, r in enumerate(free_rows) if query in r["name"].lower()]
    if not matches:
        print("  No matches found.")
        return free_rows, paid_rows

    for i, (_, r) in enumerate(matches, 1):
        print(f"  {i}. {r['name']} ({r['category']})")

    choice = input("  Pick number (Enter to cancel): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(matches)):
        print("  Cancelled.")
        return free_rows, paid_rows

    idx, r = matches[int(choice) - 1]
    pricing = ask("Pricing details for paid list")
    notes = ask("Reason/Notes (e.g. Free tier discontinued)")

    # Remove from free
    free_rows.pop(idx)
    save_csv(FREE_CSV, FREE_FIELDS, free_rows)
    log_history(FREE_HISTORY, "remove", r["name"], r["category"], r["url"], f"Moved to paid_resources.csv: {notes}")

    # Add to paid
    paid_item = {
        "name": r["name"],
        "category": r["category"],
        "url": r["url"],
        "description": r["description"],
        "pricing": pricing,
        "tags": clean_tags(r["tags"]),
    }
    paid_rows.append(paid_item)
    save_csv(PAID_CSV, PAID_FIELDS, paid_rows)
    log_history(PAID_HISTORY, "add", r["name"], r["category"], r["url"], f"Moved from resources.csv: {notes}")

    print(f"\n  Moved '{r['name']}' from free to paid list and logged to both histories.")
    return free_rows, paid_rows


def move_paid_to_free(free_rows: list[dict], paid_rows: list[dict]) -> tuple[list[dict], list[dict]]:
    print("\n--- Move Paid Tool -> Free List ---")
    query = input("  Name to move (partial match): ").strip().lower()
    matches = [(i, r) for i, r in enumerate(paid_rows) if query in r["name"].lower()]
    if not matches:
        print("  No matches found.")
        return free_rows, paid_rows

    for i, (_, r) in enumerate(matches, 1):
        print(f"  {i}. {r['name']} ({r['category']})")

    choice = input("  Pick number (Enter to cancel): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(matches)):
        print("  Cancelled.")
        return free_rows, paid_rows

    idx, r = matches[int(choice) - 1]
    free_tier = ask("Free tier details")
    requires_signup = ""
    while requires_signup not in ("Yes", "No"):
        requires_signup = ask("Requires signup? (Yes/No)", "Yes")
    notes = ask("Reason/Notes (e.g. Launched new free plan)")

    # Remove from paid
    paid_rows.pop(idx)
    save_csv(PAID_CSV, PAID_FIELDS, paid_rows)
    log_history(PAID_HISTORY, "remove", r["name"], r["category"], r["url"], f"Moved to resources.csv: {notes}")

    # Add to free
    free_item = {
        "name": r["name"],
        "category": r["category"],
        "url": r["url"],
        "description": r["description"],
        "free_tier": free_tier,
        "requires_signup": requires_signup,
        "tags": clean_tags(r["tags"]),
    }
    free_rows.append(free_item)
    save_csv(FREE_CSV, FREE_FIELDS, free_rows)
    log_history(FREE_HISTORY, "add", r["name"], r["category"], r["url"], f"Moved from paid_resources.csv: {notes}")

    print(f"\n  Moved '{r['name']}' from paid to free list and logged to both histories.")
    return free_rows, paid_rows


# ── reports & validation ──────────────────────────────────────────────────────

def show_history(path: str, title: str) -> None:
    if not os.path.exists(path):
        print(f"  No {title} yet.")
        return
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print(f"  {title} is empty.")
        return
    print(f"\n  === {title} (Last 50 changes) ===")
    print(f"  {'Date':<12} {'Action':<8} {'Name':<24} {'Notes'}")
    print("  " + "-" * 70)
    for r in reversed(rows[-50:]):
        print(f"  {r['date']:<12} {r['action']:<8} {r['name']:<24} {r.get('notes', '')}")
    if len(rows) > 50:
        print(f"\n  … {len(rows) - 50} older entries in {os.path.basename(path)}")


def list_resources(free_rows: list[dict], paid_rows: list[dict]) -> None:
    print(f"\n=== Free Resources ({len(free_rows)}) ===")
    by_cat: dict[str, list] = {}
    for r in free_rows:
        by_cat.setdefault(r["category"], []).append(r["name"])
    for cat in sorted(by_cat):
        print(f"\n  {cat}:")
        for name in sorted(by_cat[cat]):
            print(f"    • {name}")

    if paid_rows:
        print(f"\n=== Paid-Only Resources ({len(paid_rows)}) ===")
        by_cat_paid: dict[str, list] = {}
        for r in paid_rows:
            by_cat_paid.setdefault(r["category"], []).append(r["name"])
        for cat in sorted(by_cat_paid):
            print(f"\n  {cat}:")
            for name in sorted(by_cat_paid[cat]):
                print(f"    • {name}")


def audit_repo() -> None:
    print("\n=== Repository Data Audit ===")
    errors = 0
    warnings = 0

    free_rows = load_csv(FREE_CSV)
    paid_rows = load_csv(PAID_CSV)

    print(f"• Free tools: {len(free_rows)} in resources.csv")
    print(f"• Paid tools: {len(paid_rows)} in paid_resources.csv")

    # Check free rows
    free_names = set()
    for i, r in enumerate(free_rows, 2):
        name = r.get("name", "").strip()
        if not name:
            print(f"  [ERROR] resources.csv row {i}: Empty name")
            errors += 1
        elif name.lower() in free_names:
            print(f"  [ERROR] resources.csv row {i}: Duplicate name '{name}'")
            errors += 1
        free_names.add(name.lower())

        cat = r.get("category", "").strip()
        if cat not in CATEGORIES:
            print(f"  [WARNING] resources.csv row {i} ({name}): Unknown category '{cat}'")
            warnings += 1

        signup = r.get("requires_signup", "").strip()
        if signup not in ("Yes", "No"):
            print(f"  [ERROR] resources.csv row {i} ({name}): Invalid requires_signup '{signup}' (must be Yes or No)")
            errors += 1

        tags = r.get("tags", "").split(",")
        for t in tags:
            if t != t.strip():
                print(f"  [WARNING] resources.csv row {i} ({name}): Tag '{t}' has leading/trailing spaces")
                warnings += 1
            if t != t.lower():
                print(f"  [WARNING] resources.csv row {i} ({name}): Tag '{t}' has uppercase characters")
                warnings += 1

    # Check paid rows
    paid_names = set()
    for i, r in enumerate(paid_rows, 2):
        name = r.get("name", "").strip()
        if not name:
            print(f"  [ERROR] paid_resources.csv row {i}: Empty name")
            errors += 1
        elif name.lower() in paid_names:
            print(f"  [ERROR] paid_resources.csv row {i}: Duplicate name '{name}'")
            errors += 1
        paid_names.add(name.lower())

        cat = r.get("category", "").strip()
        if cat not in CATEGORIES:
            print(f"  [WARNING] paid_resources.csv row {i} ({name}): Unknown category '{cat}'")
            warnings += 1

    # Overlap check
    overlap = free_names.intersection(paid_names)
    if overlap:
        print(f"  [ERROR] Tools listed in both free and paid: {overlap}")
        errors += len(overlap)

    if errors == 0 and warnings == 0:
        print("\nAll CSV files passed validation with zero errors and zero warnings! ✓")
    else:
        print(f"\nAudit complete: {errors} error(s), {warnings} warning(s).")


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    free_rows = load_csv(FREE_CSV)
    paid_rows = load_csv(PAID_CSV)

    while True:
        print(f"\n==========================================")
        print(f" Free AI Resources CLI ({len(free_rows)} free, {len(paid_rows)} paid)")
        print(f"==========================================")
        print("  1. Add free resource")
        print("  2. Remove free resource")
        print("  3. Edit free resource")
        print("  4. Add paid resource")
        print("  5. Remove paid resource")
        print("  6. Edit paid resource")
        print("  7. Move tool (Free <-> Paid)")
        print("  8. List all resources")
        print("  9. Show free history")
        print(" 10. Show paid history")
        print(" 11. Run repo data audit")
        print("  0. Quit")
        choice = input("Choice: ").strip()

        if choice == "1":
            free_rows = add_free(free_rows)
        elif choice == "2":
            free_rows = remove_free(free_rows)
        elif choice == "3":
            free_rows = edit_free(free_rows)
        elif choice == "4":
            paid_rows = add_paid(paid_rows)
        elif choice == "5":
            paid_rows = remove_paid(paid_rows)
        elif choice == "6":
            paid_rows = edit_paid(paid_rows)
        elif choice == "7":
            direction = ask("Direction: 1 for Free -> Paid, 2 for Paid -> Free", "1")
            if direction == "1":
                free_rows, paid_rows = move_free_to_paid(free_rows, paid_rows)
            elif direction == "2":
                free_rows, paid_rows = move_paid_to_free(free_rows, paid_rows)
        elif choice == "8":
            list_resources(free_rows, paid_rows)
        elif choice == "9":
            show_history(FREE_HISTORY, "Free Tools History")
        elif choice == "10":
            show_history(PAID_HISTORY, "Paid Tools History")
        elif choice == "11":
            audit_repo()
        elif choice in ("0", "q", "quit", "exit"):
            break
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye.")
        sys.exit(0)
