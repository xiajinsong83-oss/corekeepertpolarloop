---
title: "Core Keeper World Seeds Guide — How Seeds Shape Your World"
description: "How world seeds work in Core Keeper — seed generation, ring biomes, boss placement angles and how to share seeds with other players."
icon: "/img/app-icons/seeds.png"
keywords: ["Core Keeper seeds", "Core Keeper world seed guide", "Core Keeper seed generation", "Core Keeper how seeds work"]
tags: [guide, seeds, world generation]
canonical: "https://www.polarloop.cn/seeds/seed-guide/"
updated: "2026-10-18"
related:
  - { title: "Seed Finder tool", url: "/tools/seed-finder/" }
  - { title: "Ore and resource guide", url: "/guides/resources/ore-tier-guide/" }
  - { title: "Boss guide", url: "/guides/combat-bosses/boss-guide/" }
---

Every Core Keeper world is generated from a **seed** — the number you pick at world creation. The seed decides where each biome ring sits, which direction you find the Clay Caves, and roughly where the early bosses spawn. This guide explains how seed generation works and how to use seeds with friends.

## What a seed controls

| Aspect | Seed-dependent |
|---|---|
| Biome angles | Yes — Clay Caves / Forgotten Ruins each occupy half of the world beyond the chasm; the exact angle varies by seed |
| Outer biome order | Yes — the three outer biomes (Azeos' Wilderness, Sunken Sea, Mold) rotate counter-clockwise per seed |
| Boss placement | Partly — Glurch spawns ~65 tiles in a random angle; boss arc segments shift with the seed |
| World shape / ring distances | No — the ring band structure (0–140, 150–450, 450–520, 520–1200+) is the same for every world |

In short: the seed is a **rotation and placement** key, not a terrain generator. Terrain detail chunks generate on demand, so two seeds with the same ring layout still explore differently.

## Ring bands (same in every seed)

- **0–140 tiles**: The Undergrounds (starting area, copper/tin, first bosses)
- **150–450**: Clay Caves + Forgotten Ruins (tin / iron, Larva Hive)
- **450–520**: The Great Wall (gate barrier)
- **520–1200+**: Azeos' Wilderness, Sunken Sea, Mold (gold + endgame content)
- **~1200+**: The Passage (endgame)

## Why share seeds

Seeds are the fastest way to start a co-op world with known geography: a seed where Clay Caves is close saves an hour of wandering, and a seed with an early Hive Mother spawn accelerates the boss loop. When you find a good one, share the **seed number** (visible at world creation / world select) with friends — the world layout will be identical.

## Seed library

We're building a curated seed library on this page — seed entries are added from **community-submitted, verified worlds only** (never invented). Each entry records the seed code, game version it was tested on, what makes it interesting (nearby Clay Caves, early boss arc, rich ore ring) and a map note. Check the [Seed Finder tool](/tools/seed-finder/) to preview terrain before committing.

**Got a seed worth sharing?** Submit the seed number plus the version and what you found — verified entries get added to the library with your name attached.

## FAQ

**Does the seed change the map shape?** The ring bands are fixed; the seed changes where biomes and bosses sit within them.

**Can I see my world's seed after creating it?** The seed is shown at world creation; keep it noted for sharing or re-creating the world.

**Do seeds work across versions?** Generation can shift between major updates — always note the game version a seed was tested on (check [Patch Notes](/patches/) for version numbers).

## Related

- [Seed Finder tool](/tools/seed-finder/)
- [Ore and resource guide](/guides/resources/ore-tier-guide/)
- [Boss guide](/guides/combat-bosses/boss-guide/)
