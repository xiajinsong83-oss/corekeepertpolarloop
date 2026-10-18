---
title: "Core Keeper World"
description: "Core Keeper world guide — world generation, rings, biomes, the Core, dirt and stone layers, and how seeds shape your map."
icon: "/img/app-icons/wiki-world.png"
updated: "2026-10-18"
related:
  - { title: "Seed Finder", url: "/tools/seed-finder/" }
  - { title: "Database Biomes", url: "/database/biomes/" }
  - { title: "Seeds", url: "/seeds/" }
---

{{< ad >}}

**World** generation in Core Keeper is radial and deterministic. Every map is an underground layer that starts at The Core in the middle and spreads outward in rings; beyond a certain distance the plane is effectively endless. A hidden seed value baked into your save decides how those rings rotate, where each boss sits, and the exact shape of every chasm. Once you understand the ring layout, "where do I go next?" stops being guesswork.

## The center: dirt, clay and stone

You always spawn beside The Core in the middle of the map.

- **The Undergrounds** — the brown "dirt" biome — fills the central circle, roughly 140 tiles out. It is also the default biome that fills the gaps between other zones, which is why it is never named on the in-game map.
- **The Clay Caves** and **The Forgotten Ruins** (the grey stone biome) occupy most of the band from about 150 to 450 tiles out, split by a small angular gap. Their orientation around the circle is different on every seed. The Larva Hive structures you dig into are dungeons *inside* the Clay Caves, not a separate ring.
- **The Great Wall** is the wavy barrier between 450 and 520 tiles out. It physically gates the outer biomes, so it doubles as a natural progression wall — you cross it when your gear is ready.

## The outer rings and beyond

Past 520 tiles the three major outer biomes begin, laid out counter-clockwise with small gaps between them:

- **Azeos' Wilderness** (green)
- **The Sunken Sea** (blue, mostly water)
- **The Desert of Beginnings** (tan/orange)

Their starting angles are randomized per seed. The so-called sub-biomes — Mold, Forlorn Metropolis, Molten Quarry and Oasis — are not separate rings at all; they are large dungeon structures embedded inside their parent outer biome. Push about 1200 tiles from the center and you reach The Passage, the furthest edge of normal world generation.

| Zone | Distance from Core | Notes |
|---|---|---|
| Undergrounds (dirt) | 0 – ~140 | Starting area, default gap filler |
| Clay Caves / Forgotten Ruins | ~150 – 450 | Larva Hive lives inside Clay Caves |
| Great Wall | ~450 – 520 | Progression barrier |
| Outer biomes | ~520 + | Wilderness, Sunken Sea, Desert |
| The Passage | ~1200 + | Far outer region |

## What the seed actually controls

Two very different things are decided up front, and mixing them up is the most common cause of confusion:

- **Fixed by the seed at creation:** biome rotation, every main and optional boss arena, and the points of interest tied to fixed radii — including the parts needed for the Phantom Spark bow, the Soul Seeker pickaxe and the Godsent armor set. These sit at set distances from The Core and only vary by angle.
- **Spawned dynamically as you explore:** most scenes. Notable exceptions are the medium maze (holding the Clear Gemstone), the tiny unlit Chipped Blade temples, and the eye-shaped Thread of Fate scene. Because these are rolled as chunks generate, a Rune Song ingredient can appear in the Forgotten Ruins on one seed and deep in the Wilderness on another.

This is why a seed-finder tool is so useful: fixed-radius targets can be predicted, while dynamic scenes always demand careful perimeter searching.

## How the map grows as you play

The world is not fully built when you create it. Generation unfolds in stages:

- Empty tiles start as solid Obsidian Blocks. The moment a player enters, the fixed scenes (The Core, the first three boss spawns, the merchant rooms) are stamped down.
- Terrain is rendered in 64×64-tile chunks, and only for chunks that already contain a placed scene.
- Walking to within roughly 30 tiles of an un-generated chunk border triggers that chunk's terrain and scenery — this is why the explored area creeps outward rather than appearing all at once.
- Chasms and gorge shapes use a Voronoi noise pattern, while wavy biome borders use a convolution pass. Both are deterministic, so the same seed regenerates an identical map on a dedicated server.
- Each generated chunk rolls a chance to place a biome-specific dungeon or a random scene (up to two per chunk in the central dirt). Structures can push into a neighboring chunk and trigger it too — a domino effect that explains odd clusters of ruins.
- Ghorm looping around its ring lays down terrain and scenes in its wake, even before you walk there.

## Traversal tools by progression tier

Movement tech unlocks in lockstep with how far you can dig, which is part of the intended progression:

- **Early:** break soft walls, level mining and running, lay wooden bridges over gaps.
- **Tin Workbench:** minecarts and rails let you run a fast shuttle line from your base at The Core out to boss arenas.
- **Recall Idols:** channel to teleport straight back to The Core. They are rare and pricey to craft, so treat them as emergency returns rather than a commute.
- **Scarlet Workbench:** boats make the water-heavy Sunken Sea painless to cross.
- **Octarine Workbench:** portals — but they need to be powered for 20 minutes before they link up, and their recipes are expensive, so they only pay off well into Sunken Sea exploration.
- **Go-Karts:** fast across the open Desert, but you cannot see obstacles far ahead or attack while driving, so their exploration value is limited.

## Smart exploration strategy

- Glurch and Ghorm are nearly impossible to miss when you first strike outward from the center. Hive Mother sits further out, so craft the Hive Mother Scanner at Glurch's statue rather than digging blind.
- Outer-biome bosses can be found with scanners bought from the Spirit Merchant, or by sweeping the fixed-distance arcs. Note that Malugaz's throne room has no scanner — distance rings or a careful sweep are your only options.
- For dynamic scenes like the Rune Song pieces, enter each new outer biome by expanding an ever-widening spiral or a back-and-forth band along its inner edge, so you leave no dark gap where a tiny temple could hide. Only then make beelines to known bosses, and backtrack along your route later.

{{< version-note >}}
