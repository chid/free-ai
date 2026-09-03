#!/usr/bin/env python3
"""
CLI and Python library to explore and review how AI quotas, rate limits,
and credit pools have quantitatively changed over time.

Usage:
    python3 quotas.py summary                     # Show latest active quotas
    python3 quotas.py history                     # Show all quota change events
    python3 quotas.py history --product "Google"  # Filter by product or vendor
    python3 quotas.py history --metric requests   # Filter by metric (requests, tokens, credits_usd)
    python3 quotas.py compare                     # Compare current limits across tools
    python3 quotas.py history --json              # Output matching records as JSON
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))
QUOTAS_CSV = os.path.join(BASE, "quota_history.csv")


def load_quota_history():
    if not os.path.exists(QUOTAS_CSV):
        print(f"Error: {QUOTAS_CSV} not found.", file=sys.stderr)
        sys.exit(1)

    rows = []
    with open(QUOTAS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    return rows


def filter_rows(rows, args):
    filtered = rows
    if getattr(args, "vendor", None):
        filtered = [r for r in filtered if args.vendor.lower() in r["vendor"].lower()]
    if getattr(args, "product", None):
        filtered = [r for r in filtered if args.product.lower() in r["product"].lower()]
    if getattr(args, "tier", None):
        filtered = [r for r in filtered if args.tier.lower() in r["tier"].lower()]
    if getattr(args, "metric", None):
        filtered = [r for r in filtered if args.metric.lower() in r["metric"].lower()]
    return filtered


def cmd_history(args, rows):
    filtered = filter_rows(rows, args)

    if getattr(args, "json", False):
        print(json.dumps(filtered, indent=2))
        return

    if not filtered:
        print("No matching quota records found.")
        return

    print(f"\n{'DATE':<12} {'VENDOR / PRODUCT':<28} {'TIER':<14} {'FEATURE / MODEL':<26} {'LIMIT':<20} {'ACTION':<12} NOTES")
    print("-" * 135)
    for r in filtered:
        prod_str = f"{r['vendor']} ({r['product']})" if r['vendor'] != r['product'] else r['vendor']
        limit_str = f"{r['limit_value']} {r['unit']}"
        print(f"{r['date']:<12} {prod_str[:26]:<28} {r['tier'][:12]:<14} {r['feature_or_model'][:24]:<26} {limit_str:<20} {r['change_type']:<12} {r['notes']}")
    print("-" * 135)
    print(f"Total events: {len(filtered)}\n")


def cmd_summary(args, rows):
    filtered = filter_rows(rows, args)
    latest = {}
    for r in sorted(filtered, key=lambda x: x["date"]):
        key = (r["vendor"], r["product"], r["tier"], r["feature_or_model"], r["metric"])
        latest[key] = r

    if getattr(args, "json", False):
        print(json.dumps(list(latest.values()), indent=2))
        return

    grouped = defaultdict(list)
    for (vendor, product, tier, feature, metric), r in latest.items():
        if r["limit_value"] == "0" or r["change_type"] == "deprecation":
            continue
        grouped[(vendor, product, tier)].append(r)

    print(f"\n{'VENDOR / PRODUCT':<30} {'TIER':<16} {'FEATURE / MODEL':<26} {'ACTIVE LIMIT':<20} {'SINCE':<12} NOTES")
    print("=" * 135)
    for (vendor, product, tier), items in sorted(grouped.items()):
        prod_str = f"{vendor} / {product}" if vendor != product else vendor
        for i, item in enumerate(items):
            p_display = prod_str if i == 0 else ""
            t_display = tier if i == 0 else ""
            limit_str = f"{item['limit_value']} {item['unit']}"
            print(f"{p_display[:28]:<30} {t_display[:14]:<16} {item['feature_or_model'][:24]:<26} {limit_str:<20} {item['date']:<12} {item['notes']}")
        print("-" * 135)
    print()


def cmd_compare(args, rows):
    filtered = filter_rows(rows, args)

    print("\n--- FREE TIER RATE LIMIT COMPARISON ---")
    free_items = [r for r in filtered if r["tier"].lower() == "free" and r["limit_value"] not in ("0", "unlimited")]
    latest_free = {}
    for r in sorted(free_items, key=lambda x: x["date"]):
        latest_free[(r["product"], r["feature_or_model"], r["metric"])] = r

    for (product, feature, metric), r in sorted(latest_free.items()):
        print(f"• {product:<20} | {feature:<24} | {r['limit_value']} {r['unit']:<10} (Window: {r['window']}) — {r['notes']}")

    print("\n--- PAID SUBSCRIPTION COMPUTE / CREDIT LIMITS ---")
    paid_items = [r for r in filtered if r["tier"].lower() != "free"]
    latest_paid = {}
    for r in sorted(paid_items, key=lambda x: x["date"]):
        latest_paid[(r["product"], r["tier"], r["metric"])] = r

    for (product, tier, metric), r in sorted(latest_paid.items()):
        print(f"• {product:<20} [{tier:<12}] | {r['limit_value']} {r['unit']:<15} (Window: {r['window']}) — {r['notes']}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Explore and track AI quotas and rate limits quantitatively over time.")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    for p in [subparsers.add_parser("history", help="List chronological quota events"),
              subparsers.add_parser("summary", help="Show current active quotas per product and tier"),
              subparsers.add_parser("compare", help="Compare current quotas across tools")]:
        p.add_argument("--vendor", help="Filter by vendor (Google, Anthropic, etc.)")
        p.add_argument("--product", help="Filter by product name")
        p.add_argument("--tier", help="Filter by tier (Free, Pro, etc.)")
        p.add_argument("--metric", help="Filter by metric (requests, tokens, credits_usd)")
        p.add_argument("--json", action="store_true", help="Output results as JSON")

    args = parser.parse_args()
    rows = load_quota_history()

    if args.command == "history":
        cmd_history(args, rows)
    elif args.command == "compare":
        cmd_compare(args, rows)
    else:
        cmd_summary(args, rows)


if __name__ == "__main__":
    main()
