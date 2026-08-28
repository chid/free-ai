#!/usr/bin/env python3
"""
Interactive CLI to manage entries in resources.csv, paid_resources.csv, and local_resources.csv.
All changes are appended to the respective history files with a timestamp.
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
LOCAL_CSV = os.path.join(BASE, "local_resources.csv")
LOCAL_HISTORY = os.path.join(BASE, "local_history.csv")

FREE_FIELDS = ["name", "category", "url", "description", "free_tier", "requires_signup", "tags"]
PAID_FIELDS = ["name", "category", "url", "description", "pricing", "tags"]
LOCAL_FIELDS = ["name", "category", "url", "description", "hardware_reqs", "license", "tags"]
HISTORY_FIELDS = ["date", "action", "name", "category", "url", "notes"]

FREE_CATEGORIES = [
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

LOCAL_CATEGORIES = [
    "Local Runner",
    "Desktop Client",
    "Serving Engine",
    "Web UI",
    "Code Assistant",
    "Agent Framework",
    "Fine-tuning / Quant",
    "Embeddings / RAG",
    "Image / Audio / Video",
    "Hardware / Benchmarking",
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


def pick_category(categories: list[str], current: str = "") -> str:
    print("\n  Categories:")
    for i, cat in enumerate(categories, 1):
        mark = " (current)" if cat == current else ""
        print(f"    {i:2}. {cat}{mark}")
    print("     0. Enter custom category")
    while True:
        choice = input("  Pick number (or 0 for custom): ").strip()
        if choice == "0":
            return input("  Custom category: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
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

    category = pick_category(FREE_CATEGORIES)
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
        category = pick_category(FREE_CATEGORIES, r["category"])

    requires_signup = r["requires_signup"]
    signup_input = ask(f"Requires signup? (Yes/No)", r["requires_signup"])
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

    category = pick_category(FREE_CATEGORIES)
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
        category = pick_category(FREE_CATEGORIES, r["category"])

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


# ── actions: local llm tools ──────────────────────────────────────────────────

def add_local(rows: list[dict]) -> list[dict]:
    print("\n--- Add a new local LLM resource ---")
    name = ask("Name")
    if not name:
        print("  Name is required.")
        return rows
    if any(r["name"].lower() == name.lower() for r in rows):
        print(f"  '{name}' already exists in local resources.")
        return rows

    category = pick_category(LOCAL_CATEGORIES)
    url = ask("URL")
    description = ask("Description")
    hardware_reqs = ask("Hardware requirements (e.g. Mac Apple Silicon, NVIDIA CUDA, CPU)")
    license = ask("License (e.g. MIT, Apache-2.0, Open Source)", "MIT")
    tags = clean_tags(ask("Tags (comma-separated, e.g. local,cli,gguf,cuda)"))

    rows.append({
        "name": name,
        "category": category,
        "url": url,
        "description": description,
        "hardware_reqs": hardware_reqs,
        "license": license,
        "tags": tags,
    })
    save_csv(LOCAL_CSV, LOCAL_FIELDS, rows)
    log_history(LOCAL_HISTORY, "add", name, category, url)
    print(f"\n  Added '{name}' to local_resources.csv and logged to local_history.csv.")
    return rows


def remove_local(rows: list[dict]) -> list[dict]:
    print("\n--- Remove a local LLM resource ---")
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
        reason = ask("Reason/Notes (for local_history.csv)")
        rows.pop(idx)
        save_csv(LOCAL_CSV, LOCAL_FIELDS, rows)
        log_history(LOCAL_HISTORY, "remove", r["name"], r["category"], r["url"], reason)
        print(f"  Removed '{r['name']}'.")
    else:
        print("  Cancelled.")
    return rows


def edit_local(rows: list[dict]) -> list[dict]:
    print("\n--- Edit a local LLM resource ---")
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
        category = pick_category(LOCAL_CATEGORIES, r["category"])

    updated = {
        "name":          ask("Name", r["name"]),
        "category":      category,
        "url":           ask("URL", r["url"]),
        "description":   ask("Description", r["description"]),
        "hardware_reqs": ask("Hardware requirements", r.get("hardware_reqs", "")),
        "license":       ask("License", r.get("license", "MIT")),
        "tags":          clean_tags(ask("Tags", r["tags"])),
    }

    changes = [f for f in LOCAL_FIELDS if updated[f] != r.get(f, "")]
    if not changes:
        print("  No changes made.")
        return rows

    rows[idx] = updated
    save_csv(LOCAL_CSV, LOCAL_FIELDS, rows)
    notes = ask("History notes (Enter for auto diff)", f"changed: {', '.join(changes)}")
    log_history(LOCAL_HISTORY, "edit", updated["name"], updated["category"], updated["url"], notes)
    print(f"\n  Updated '{updated['name']}'.")
    return rows


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


def list_resources(free_rows: list[dict], paid_rows: list[dict], local_rows: list[dict]) -> None:
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

    if local_rows:
        print(f"\n=== Local LLM Resources ({len(local_rows)}) ===")
        by_cat_local: dict[str, list] = {}
        for r in local_rows:
            by_cat_local.setdefault(r["category"], []).append(r["name"])
        for cat in sorted(by_cat_local):
            print(f"\n  {cat}:")
            for name in sorted(by_cat_local[cat]):
                print(f"    • {name}")


def audit_repo() -> None:
    print("\n=== Repository Data Audit ===")
    errors = 0
    warnings = 0

    free_rows = load_csv(FREE_CSV)
    paid_rows = load_csv(PAID_CSV)
    local_rows = load_csv(LOCAL_CSV)

    print(f"• Free tools: {len(free_rows)} in resources.csv")
    print(f"• Paid tools: {len(paid_rows)} in paid_resources.csv")
    print(f"• Local tools: {len(local_rows)} in local_resources.csv")

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
        if cat not in FREE_CATEGORIES:
            print(f"  [WARNING] resources.csv row {i} ({name}): Unknown category '{cat}'")
            warnings += 1

        signup = r.get("requires_signup", "").strip()
        if signup not in ("Yes", "No"):
            print(f"  [ERROR] resources.csv row {i} ({name}): Invalid requires_signup '{signup}' (must be Yes or No)")
            errors += 1

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

    # Check local rows
    local_names = set()
    for i, r in enumerate(local_rows, 2):
        name = r.get("name", "").strip()
        if not name:
            print(f"  [ERROR] local_resources.csv row {i}: Empty name")
            errors += 1
        elif name.lower() in local_names:
            print(f"  [ERROR] local_resources.csv row {i}: Duplicate name '{name}'")
            errors += 1
        local_names.add(name.lower())

    if errors == 0 and warnings == 0:
        print("\nAll CSV files passed validation with zero errors and zero warnings! ✓")
    else:
        print(f"\nAudit complete: {errors} error(s), {warnings} warning(s).")


# ── main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    free_rows = load_csv(FREE_CSV)
    paid_rows = load_csv(PAID_CSV)
    local_rows = load_csv(LOCAL_CSV)

    while True:
        print(f"\n============================================================")
        print(f" AI Resources CLI ({len(free_rows)} free, {len(paid_rows)} paid, {len(local_rows)} local)")
        print(f"============================================================")
        print("  1. Add free resource")
        print("  2. Remove free resource")
        print("  3. Edit free resource")
        print("  4. Add paid resource")
        print("  5. Remove paid resource")
        print("  6. Edit paid resource")
        print("  7. Add local LLM resource")
        print("  8. Remove local LLM resource")
        print("  9. Edit local LLM resource")
        print(" 10. List all resources across all pathways")
        print(" 11. Show free history")
        print(" 12. Show paid history")
        print(" 13. Show local history")
        print(" 14. Run repo data audit")
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
            local_rows = add_local(local_rows)
        elif choice == "8":
            local_rows = remove_local(local_rows)
        elif choice == "9":
            local_rows = edit_local(local_rows)
        elif choice == "10":
            list_resources(free_rows, paid_rows, local_rows)
        elif choice == "11":
            show_history(FREE_HISTORY, "Free Tools History")
        elif choice == "12":
            show_history(PAID_HISTORY, "Paid Tools History")
        elif choice == "13":
            show_history(LOCAL_HISTORY, "Local LLM History")
        elif choice == "14":
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

