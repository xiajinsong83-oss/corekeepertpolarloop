---
title: "Seed Finder"
description: "Core Keeper seed finder — browse curated starting, rich ore, boss-near and rare terrain seeds for your world."
icon: "/img/app-icons/seed-finder.png"
keywords: ["Core Keeper seed finder", "Core Keeper seed preview", "Core Keeper starting seed", "Core Keeper world seed"]
related:
  - { title: "Boss Drop Finder", url: "/tools/boss-drop-finder/" }
  - { title: "Seeds Library", url: "/seeds/" }
  - { title: "Biomes Database", url: "/database/biomes/" }
---

The Core Keeper **seed finder** helps you pick a good world seed before you start. Core Keeper worlds are generated deterministically from a hidden seed — biome rotation, boss spawn arcs and fixed scenes all depend on it, while terrain details are generated chunk-by-chunk as you explore.

## How to use

Enter a numeric seed to jump to curated seeds with similar traits, or browse the full seed library by tag (starting / rich ore / boss-near / rare terrain).

{{< seed-finder >}}

## What a seed controls

- **Biome rotation** — which direction Clay Caves / Forgotten Ruins sit, and the counter-clockwise order of the three outer biomes
- **Boss spawn arcs** — fixed-distance arcs with random angles for all main and optional bosses
- **Fixed scenes** — the Core, first-three-boss spawns and NPC merchant scenes

{{< ad >}}

## FAQ

- **Does Core Keeper use seeds?** Yes — every world is created from a hidden random seed that determines biome rotation and boss positions.
- **Are seeds version-dependent?** Yes. Major updates can change generation, so check the version tag on each seed page.
- **Can I preview terrain from a seed?** Not fully — terrain needs the game's generation algorithm. This tool focuses on the deterministic high-level layout.
