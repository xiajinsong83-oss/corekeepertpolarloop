---
title: "Core Keeper World Generation — Chunks, Seeds and Terrain Pipeline"
description: "How Core Keeper generates its map — 64x64 chunks, Voronoi noise, on-demand terrain, Ghorm's wake, and why the same seed always produces the same world."
icon: "/img/app-icons/wiki-world.png"
updated: "2026-10-18"
related:
  - { title: "World", url: "/wiki/world/" }
  - { title: "The Great Wall", url: "/wiki/great-wall/" }
  - { title: "Seeds Guide", url: "/seeds/seed-guide/" }
  - { title: "Seed Finder", url: "/tools/seed-finder/" }
---

{{< ad >}}

**World generation** in Core Keeper is layered rather than instant. When you create a world, the game bakes a deterministic seed value into the save, but the map itself is not built all at once. Empty tiles start as solid Obsidian Blocks and only turn into dirt, stone, water and dungeons as players trigger them. This page explains the pipeline: what is fixed at creation, what is rolled as you explore, and why two players on the same seed always see the same map.

## The chunk system

The world is rendered as a grid of **64×64-tile chunks**. A chunk stays invisible — and full of Obsidian — until something forces it to generate.

- The trigger radius is roughly **30 tiles** from an empty chunk's border. Walk past the halfway point of an adjacent chunk and the next chunk over renders its terrain.
- The very centre of the grid is special: the corner where four chunks meet sits at the bottom-left corner of your default spawn tile, just below The Core statue. Every chunk coordinate in the world is measured from this origin.
- Terrain generation is normally processed on the GPU. On a dedicated server with no GPU, or launched with `-nographics`, only the pre-placed scenes are stamped down — chunks appear as a sea of solid Obsidian with rooms sitting on top.

## What is fixed at creation vs. what rolls on exploration

The seed decides two very different sets of things, and mixing them up is the most common reason players get confused about "where is my boss?":

| Aspect | Fixed by the seed | Rolled as chunks generate |
|---|---|---|
| Biome angular rotation | Yes | — |
| Main and optional boss arenas | Yes (at fixed radii) | — |
| Fixed-radius points of interest (Phantom Spark parts, Soul Seeker pickaxe, Godsent armour) | Yes | — |
| Merchant rooms and The Core | Yes, stamped on first entry | — |
| Most scenes | — | Yes, rolled per chunk |
| Medium maze (Clear Gemstone), Chipped Blade temples, Thread of Fate eye scene | — | Yes, can land in different biomes across seeds |
| Chasm shapes and gorge layout | Deterministic from seed | — |
| Random dungeon placements | — | Yes, weighted per biome |

The practical upshot: **fixed-radius targets can be predicted with a seed tool, but dynamic scenes always demand careful perimeter searching.**

## The noise algorithms behind the terrain

Two deterministic algorithms shape the natural look of the map:

- **Voronoi noise** generates chasms and gorges. It produces irregular, cell-like gaps that look like natural cracks in the rock.
- **A convolution pass** generates the wavy, undulating borders between biomes. This is why the edge between dirt and stone, or between the inner biomes and The Great Wall, looks like a coastline rather than a straight line.

Both are seeded, so running the same seed on a dedicated server reproduces an identical map. The ring bands themselves (0–140, 150–450, 450–520, 520–1200+) are the same on every world; only the angles and the undulation details move.

{{< ad >}}

## What happens when a chunk generates

When a chunk finally renders, the game runs through a short pipeline:

1. **Terrain is laid down** — dirt, stone, water, chasms, the biome's natural features.
2. **A structure roll happens.** Each chunk has a chance to place either a biome-specific dungeon or one random scene from that biome's weighted scene list.
3. **In the central dirt biome, up to two scenes can spawn per chunk.** Outer biomes are generally more restricted.
4. **The domino effect.** If a new structure is pushed out of the centre of its chunk by neighbouring structures, it can spill across a chunk border — triggering the adjacent chunk to generate its own terrain and roll another scene. This is why clusters of ruins sometimes appear in odd places.
5. **Boss arenas wait for terrain.** A boss's spawn scene is only stamped down once terrain has been generated inside its footprint. Even though the arena's location is pre-set by the seed, walking near it is what makes it appear.

## Ghorm pre-generates terrain

Ghorm the Devourer loops around its ring early in the game. As it runs, it lays down tiles in its wake — which triggers terrain generation and scene placement around its track *before* a player ever walks there. This can include the medium maze holding the Clear Gemstone, which is one of the few "dynamic" scenes that can appear closer than expected because Ghorm rolled it for you.

## Dungeons as a generation type

Procedurally generated dungeons are large structures made of several rooms connected together. They are biome-specific and usually occupy either a single chunk or a **2×2 chunk** area.

| Dungeon type | Parent biome | Notes |
|---|---|---|
| Larva Hive | Clay Caves (inner) | Dungeon inside the Clay Caves, not a separate ring |
| Mold | Azeos' Wilderness | Always takes 2×2 chunks |
| Forlorn Metropolis | Sunken Sea | 2×2 chunk dungeon |
| Molten Quarry | Desert of Beginnings | 2×2 chunk dungeon |
| Caveling cities | Forgotten Ruins | No walls; large overlapping blob areas, not a sub-biome |
| Boss arenas | Various | Up to ~3×3 chunks, centred on fixed-radius scenes |

Scenes inside dungeons can be mirrored, flipped or embellished with smaller structures, which is why no two Mold dungeons look identical even on the same seed.

## Why this matters for exploration

- **Use a seed finder for fixed targets.** Boss arenas and fixed-radius gear pieces sit at predictable angles; a seed tool saves you hours of blind digging.
- **Search perimeter-first for dynamic scenes.** When you first enter a new outer biome, map an expanding spiral or a back-and-forth band along its inner edge. Only after the whole perimeter is revealed should you beeline to known bosses.
- **Walk further than you think you need to.** The 30-tile trigger radius means you can stand just outside a chunk and see nothing; a few more steps in either direction will reveal it.
- **Dedicated-server players on `-nographics`** will see scenes stamped into Obsidian. This is not a bug, it is the expected behaviour of headless generation.

## FAQ

**Does the seed change the shape of the rings?** No. The ring distances (0–140, 150–450, 450–520, 520–1200+) are the same on every world. The seed changes *where* each biome sits around the circle and *how* the wavy borders undulate.

**Why does my map look half-finished when I know a boss should be nearby?** Boss scenes are only stamped down after terrain generates within their footprint. If you are standing on un-generated Obsidian, walk a little further — the chunk will render and the arena will appear.

**Can I share a seed with a friend and get the same world?** Yes. The ring layout, biome angles, boss arenas and fixed-radius items will match. Dynamic scenes may differ if one of you explored into new chunks before the other, but the deterministic structures will be identical.

**Do seeds work across game versions?** Generation can shift between major updates. Always note the game version a seed was tested on — patch notes list version numbers, and a seed from 0.5.x may not reproduce the same map on 1.3.x.

**Why do I see clusters of ruins far from where I expected them?** The domino effect: a structure pushed against a chunk border triggers the neighbouring chunk, which rolls its own scene. Clusters are normal, not a bug.

{{< version-note >}}
