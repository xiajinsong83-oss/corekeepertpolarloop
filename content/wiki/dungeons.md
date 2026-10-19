---
title: "Core Keeper Dungeons — Generated Structure Atlas by Biome"
description: "A Core Keeper dungeon atlas — the recurring generated structure types, which biome each appears in, and how big they are on the map, from Larva Hive and Mold to Desert temples and Caveling cities."
canonical: "https://www.polarloop.cn/wiki/dungeons/"
icon: "/img/app-icons/wiki-dungeons.png"
updated: "2026-10-19"
related:
  - { title: "World Generation", url: "/wiki/world-generation/" }
  - { title: "Scenes", url: "/wiki/scenes/" }
  - { title: "Biomes", url: "/wiki/biomes/" }
  - { title: "World", url: "/wiki/world/" }
---

*Source: [World — Core Keeper Wiki (atma.gg)](https://corekeeper.atma.gg/en/World), "Dungeon types (list)". Map-appearance descriptions are qualitative; exact counts per seed vary.*

{{< ad >}}

Beyond the plain terrain, every Core Keeper world is built from a repeating vocabulary of **procedurally generated dungeons** — networks of linked rooms that the generator stamps into a biome. Unlike the hand-placed set pieces covered on [Scenes](/wiki/scenes/), these structure *types* recur in every world, just at different angles and mirrored or flipped layouts. This atlas groups them by biome so you can recognise what you have dug into the moment it comes into view.

## How big generated structures get

Most dungeons occupy either a single chunk or a **2×2 block** of 64×64 chunks. Boss arenas and the sub-biome dungeons are larger still, stretching to roughly **3×3 chunks** — but because their central scene sits on a fixed-distance arc, they are not neatly aligned to the chunk grid.

## The dungeon atlas by biome

| Structure type | Parent biome | Notes |
|---|---|---|
| Slime | The Undergrounds | Small slime-warren structures near the centre |
| House | Clay Caves / Forgotten Ruins | Ordinary ruined houses dotted through the inner stone and clay |
| Larva Hive *(sub-biome)* | Clay Caves | Maze of hive-covered, tougher walls; home of the Hive Mother |
| Clay moss Caveling encampment | Clay Caves | Camp-style Caveling outposts |
| Caveling City | Forgotten Ruins | Wall-less, overlapping "blob" districts — not a tidy dungeon |
| Mold *(sub-biome)* | Azeos' Wilderness | Fungi-infested halls; always takes a 2×2 chunk footprint |
| Islands (enclosed and open) | The Sunken Sea | Beach-sand islands ringed by limestone walls |
| Forlorn Metropolis *(sub-biome)* | The Sunken Sea | Run-down hi-tech dungeon; 2×2 chunk footprint |
| Hidden canyon Caveling village | The Desert of Beginnings | Tucked-away villages in desert canyons |
| Mini temple and maze cluster | The Desert of Beginnings | Small temple-and-maze groups (watch for Chipped Blade temples) |
| Temple | The Desert of Beginnings | Larger intact temple dungeons with loot |
| Molten Quarry *(sub-biome)* | The Desert of Beginnings | Lava-riven volcanic dungeon; holds Igneous and the Ancient Forge |

{{< ad >}}

## Sub-biomes are dungeons, too

The four named sub-biomes — **Larva Hive, Mold, Forlorn Metropolis and Molten Quarry** — are each just a themed dungeon type in generation terms. What sets them apart is scale: they wrap a boss or a critical craft (the Ancient Forge for the Soul Seeker pickaxe) and carry their own ore and loot tables. The Caveling Cities in the Forgotten Ruins look dungeon-like but are the exception — loose wall-less blobs rather than enclosed rooms.

## Why no two look identical

Scenes inside a dungeon can be **mirrored, flipped or embellished** with smaller attached structures, so two Mold dungeons on the same seed still differ in detail. When a new structure is pushed against a chunk border, it can spill into the next chunk and trigger it to generate its own scene — this "domino effect" is why clusters of ruins sometimes appear in odd places. For the full generation pipeline behind this, see [World Generation](/wiki/world-generation/).

## FAQ

**Is a "sub-biome" a separate ring I have to find?** No. It is a themed dungeon embedded inside its parent biome. Mold is inside the Wilderness, Forlorn Metropolis inside the Sunken Sea, and Molten Quarry inside the Desert.

**What is the biggest generated structure?** Boss arenas and the sub-biome dungeons, which can stretch to roughly 3×3 chunks. Most ordinary dungeons are single-chunk or 2×2.

**How do I tell a Caveling City from a regular dungeon?** Caveling Cities in the Forgotten Ruins have no walls and read as large overlapping blobs on the revealed map, rather than a tidy enclosed room network.

**Are dungeon layouts the same on every seed?** The *types* recur, but each instance is mirrored, flipped or embellished, and the domino effect shifts clusters. The same seed reproduces the fixed arenas, but the random dungeons still vary in detail.

{{< version-note >}}
