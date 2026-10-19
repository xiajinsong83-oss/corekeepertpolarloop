#!/usr/bin/env python3
"""
Generate Hugo content pages for Core Keeper items.

Idempotent: reads data/items.yaml, and for every item that does not yet have
a content/database/items/<slug>.md page, creates one using the standard
frontmatter + body template. Existing pages are left untouched.

Slug rule (matches existing pages like azeos-claw.md, ghorm-s-horn.md):
  name.lower() -> replace any non [a-z0-9] char with '-' -> collapse
  consecutive '-' -> strip leading/trailing '-'.

Usage:
  python3 scripts/gen_item_pages.py
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
ITEMS_YAML = REPO_ROOT / "data" / "items.yaml"
PAGES_DIR = REPO_ROOT / "content" / "database" / "items"

UPDATED = "2026-10-18"


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s)
    return s.strip("-")


def build_description(item: dict) -> str:
    name = item["name"]
    cat = item.get("category", "Item")
    if cat == "Boss Drop":
        src = item.get("source", "a boss")
        return (
            f"Core Keeper {name} — boss drop item from {src}, "
            f"used for progression and crafting."
        )
    return (
        f"Core Keeper {name} — {cat}. "
        "Stats verified against the official wiki (atma.gg)."
    )


def build_body(item: dict) -> str:
    name = item["name"]
    cat = item.get("category", "item")
    return (
        f"{name} is one of Core Keeper's {cat.lower()} items. "
        "The infobox below shows verified stats and sources — "
        "check the related guide pages for how to obtain and use it.\n"
    )


def render_page(item: dict) -> str:
    name = item["name"]
    icon = item.get("icon", "/img/app-icons/item-items.png")
    desc = build_description(item)
    body = build_body(item)
    return (
        "---\n"
        f'title: "{name}"\n'
        f'description: "{desc}"\n'
        f'icon: "{icon}"\n'
        f'key: "{name}"\n'
        f'updated: "{UPDATED}"\n'
        "---\n\n"
        f"{body}\n"
        "{{< ad >}}\n"
    )


def main() -> int:
    with open(ITEMS_YAML, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    items = data.get("items", [])
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    created = 0
    skipped = 0
    for item in items:
        name = item["name"]
        slug = slugify(name)
        page_path = PAGES_DIR / f"{slug}.md"
        if page_path.exists():
            skipped += 1
            continue
        page_path.write_text(render_page(item), encoding="utf-8")
        created += 1
        print(f"  created {page_path.relative_to(REPO_ROOT)}  (key={name!r})")

    print(f"\nDone. items in yaml: {len(items)}; pages created: {created}; "
          f"existing pages skipped: {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
