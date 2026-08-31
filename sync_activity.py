#!/usr/bin/env python3
"""
Syncs latest commit/release/model update timestamps and stars from GitHub and HuggingFace APIs.
Saves results into activity.json which is loaded by index.html.
Usage: python3 sync_activity.py
"""

import csv
import json
import os
import re
import urllib.request
import urllib.error
import time

BASE = os.path.dirname(os.path.abspath(__file__))
FREE_CSV = os.path.join(BASE, "resources.csv")
PAID_CSV = os.path.join(BASE, "paid_resources.csv")
LOCAL_CSV = os.path.join(BASE, "local_resources.csv")
ACTIVITY_JSON = os.path.join(BASE, "activity.json")


def load_all_urls():
    urls = {}
    for path, tier in [(FREE_CSV, 'free'), (PAID_CSV, 'paid'), (LOCAL_CSV, 'local')]:
        if os.path.exists(path):
            with open(path, newline='', encoding='utf-8') as f:
                for r in csv.DictReader(f):
                    name = r.get('name')
                    url = r.get('url', '')
                    if name and url:
                        urls[name] = {'url': url, 'tier': tier}
    return urls


def fetch_github_info(owner, repo):
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(api_url, headers={
        'User-Agent': 'free-ai-directory-updater',
        'Accept': 'application/vnd.github.v3+json'
    })
    # If GITHUB_TOKEN is available in env, use it for higher rate limits
    token = os.environ.get('GITHUB_TOKEN')
    if token:
        req.add_header('Authorization', f'token {token}')

    try:
        with urllib.request.urlopen(req, timeout=8) as res:
            data = json.loads(res.read().decode('utf-8'))
            return {
                'type': 'github',
                'repo': f"{owner}/{repo}",
                'last_activity': data.get('pushed_at', '')[:10],
                'created_at': data.get('created_at', '')[:10],
                'stars': data.get('stargazers_count', 0),
                'forks': data.get('forks_count', 0),
                'open_issues': data.get('open_issues_count', 0),
                'archived': data.get('archived', False),
                'description': data.get('description', '')
            }
    except urllib.error.HTTPError as e:
        if e.code == 403:
            print(f"  [Rate limited] GitHub API rate limit hit for {owner}/{repo}")
        elif e.code == 404:
            print(f"  [Not found] GitHub repo {owner}/{repo}")
        else:
            print(f"  [HTTP {e.code}] GitHub {owner}/{repo}: {e}")
    except Exception as e:
        print(f"  [Error] GitHub {owner}/{repo}: {e}")
    return None


def fetch_hf_info(model_id):
    api_url = f"https://huggingface.co/api/models/{model_id}"
    req = urllib.request.Request(api_url, headers={'User-Agent': 'free-ai-directory-updater'})
    try:
        with urllib.request.urlopen(req, timeout=8) as res:
            data = json.loads(res.read().decode('utf-8'))
            return {
                'type': 'huggingface',
                'model_id': model_id,
                'last_activity': (data.get('lastModified') or data.get('createdAt') or '')[:10],
                'downloads': data.get('downloads', 0),
                'likes': data.get('likes', 0),
                'pipeline_tag': data.get('pipeline_tag', '')
            }
    except Exception as e:
        print(f"  [Error] HuggingFace {model_id}: {e}")
    return None


def sync_activity():
    print("=== Syncing Model & Repository Activity ===")
    targets = load_all_urls()
    print(f"Loaded {len(targets)} resources from directory CSVs.")

    # Load existing cache if any
    cache = {}
    if os.path.exists(ACTIVITY_JSON):
        try:
            with open(ACTIVITY_JSON, 'r', encoding='utf-8') as f:
                cache = json.load(f)
        except Exception:
            cache = {}

    updated_count = 0

    for name, info in targets.items():
        url = info['url']
        
        # Check GitHub pattern
        gh_match = re.search(r'github\.com/([a-zA-Z0-9_.-]+)/([a-zA-Z0-9_.-]+)', url)
        if gh_match:
            owner, repo = gh_match.group(1), gh_match.group(2).rstrip('/')
            # Avoid special paths
            if owner not in ('features', 'trending', 'topics', 'marketplace', 'settings'):
                print(f"Fetching GitHub repo for '{name}' ({owner}/{repo})...")
                res = fetch_github_info(owner, repo)
                if res:
                    cache[name] = res
                    updated_count += 1
                time.sleep(0.3)
                continue

        # Check Hugging Face pattern
        hf_match = re.search(r'huggingface\.co/([a-zA-Z0-9_.-]+/[a-zA-Z0-9_.-]+)', url)
        if hf_match:
            model_id = hf_match.group(1).rstrip('/')
            if not model_id.startswith('spaces/') and not model_id.startswith('datasets/'):
                print(f"Fetching HuggingFace model for '{name}' ({model_id})...")
                res = fetch_hf_info(model_id)
                if res:
                    cache[name] = res
                    updated_count += 1
                time.sleep(0.3)
                continue

    with open(ACTIVITY_JSON, 'w', encoding='utf-8') as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

    print(f"\nActivity sync complete! Recorded live metadata for {len(cache)} resources in activity.json.")


if __name__ == '__main__':
    sync_activity()
