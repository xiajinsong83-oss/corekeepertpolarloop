---
title: "Core Keeper Map Structure — The Core, Distance Arcs and Fixed Landmarks"
description: "How to read a Core Keeper world map — The Core at the centre, fixed-distance arcs, which landmarks are stamped at world creation versus rolled dynamically, and how to use distance rings to locate bosses."
canonical: "https://www.polarloop.cn/wiki/world-map/"
icon: "/img/app-icons/wiki-world.png"
updated: "2026-10-19"
related:
  - { title: "World", url: "/wiki/world/" }
  - { title: "World Generation", url: "/wiki/world-generation/" }
  - { title: "Biomes", url: "/wiki/biomes/" }
  - { title: "Seed Finder", url: "/tools/seed-finder/" }
---

*Source: [World — Core Keeper Wiki (atma.gg)](https://corekeeper.atma.gg/en/World), especially the "Set distance locations" and generation-algorithm sections. Distances are approximate tile counts from The Core.*

{{< ad >}}

A Core Keeper map is a **radial coordinate system**, not a random blob. Everything important sits on a circle around The Core: only the *angle* is randomised by the seed, while the *distance* is fixed. Once you stop thinking "which direction?" and start thinking "which arc?", finding bosses and legendary gear stops being blind digging. This page explains the map's anatomy — distinct from [World Generation](/wiki/world-generation/), which covers the chunk-by-chunk terrain pipeline.

## The centre: The Core and the origin

Every world spawns you beside **The Core**, the single fixed scene at the map's heart. Two map facts hang off it:

- The Undergrounds (dirt) fills the central circle to a radius of about **140 tiles**, and it is also the default biome that fills the gaps between every other zone — which is why the in-game map never names it.
- The chunk grid has its origin at the bottom-left corner of your default spawn tile, just below The Core statue. Every chunk coordinate in the world is measured from that point.

## The distance arcs

Biome bands and major landmarks sit at set radii. The seed rotates the whole layout, but it never moves these distances.

| Arc (distance from Core) | What lives on it |
|---|---|
| ~0 – 140 | The Undergrounds; Glurch's arena; Ghorm's looping track |
| ~150 – 450 | Clay Caves and Forgotten Ruins; Larva Hive (Hive Mother); Malugaz's throne room |
| ~450 – 520 | The Great Wall gate |
| ~520 + | Outer biomes; Azeos', Omoroth's and Ra-Akar's arenas |
| ~1200 + | The Passage; the Shimmering Frontier ring |

Because the angles are randomised, a seed-finder tool can predict *which direction* each arc landmark sits — see the [Seed Finder](/tools/seed-finder/).

## Fixed at creation vs. rolled as you explore

The single most useful thing to understand about the map: not every landmark behaves the same way.

| Behaviour | What it includes | How to find it |
|---|---|---|
| **Fixed radius, random angle** | All bosses (main and optional), the Phantom Spark bow parts, the Soul Seeker pickaxe parts, the Godsent armour set | Sweep the known arc; or use a seed tool |
| **Stamped on first entry** | The Core, the first three boss spawns, the NPC merchant rooms | Walk out — they are already placed |
| **Dynamic (rolled per chunk)** | Most scenes, the medium maze (Clear Gemstone), the tiny Chipped Blade temples, the Thread of Fate eye scene | Perimeter-spiral search; see below |

The practical split: **fixed-radius targets can be predicted, dynamic scenes always demand careful perimeter searching.**

{{< ad >}}

## Landmarks you will recognise

- **Merchant rooms** — the Fishing Merchant, the Cloaked Merchant and others spawn as pre-placed cells. They are stamped when you first enter the world, so they exist even before you have their summoning item.
- **Ghorm's track** — Ghorm loops around its ring early in the game. As it runs, it lays down tiles in its wake, triggering terrain and scenes around its path *before* you walk there. Sitting at The Core for a few minutes lets Ghorm pre-generate a surprising amount of the inner map.
- **Boss arenas** — their locations are preset by the seed, but the scene is only stamped down once terrain generates inside its footprint. If you stand on un-generated Obsidian where a boss "should" be, walk a little further and the arena appears.
- **The Main Mold Dungeon** and other named points of interest have fixed locations; their dungeon shape is set by the seed.

## How to actually sweep a new biome

Dynamic scenes (the Rune Song ingredients, the Thread of Fate) can land in unexpected biomes — the medium maze might roll in the Forgotten Ruins on one seed and deep in the Wilderness on another. To leave no dark gap:

1. On first entering a new outer biome, map an **expanding spiral** or a **back-and-forth band** along its inner edge.
2. Only then beeline to known bosses.
3. Backtrack along your route later — small, dim temples are easy to skate past.

For outer-biome bosses, craft scanners at the Spirit Merchant using items from their native biome. Note there is **no scanner for Malugaz's throne room** — distance rings or a careful sweep are your only options.

## FAQ

**Is the map the same shape on every seed?** The ring distances (0–140, 150–450, 450–520, 520–1200+) are identical. Only the angles of each biome and landmark rotate.

**Why is there nothing where my boss should be?** Boss scenes only stamp down after terrain generates in their footprint. If you are standing on Obsidian, step further — the chunk renders and the arena appears.

**Can I just dig straight outward to find everything?** No. Fixed-radius bosses are on arcs, so a straight line may cross their ring at the wrong angle. Sweep the arc or use a seed tool.

**Do merchant rooms move?** No. They are pre-placed on world entry and exist even before you unlock their summoning item — you can stumble onto them by exploration.

{{< version-note >}}
