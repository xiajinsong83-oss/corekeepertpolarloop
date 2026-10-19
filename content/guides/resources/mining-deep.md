---
title: "Core Keeper Mining Guide — Wall Hardness, Drill Efficiency and the Best Digging Routes"
description: "Deep Core Keeper mining guide — how wall damage deduction works, which pickaxe breaks which wall, ore boulder drill math, AFK mining skill farming, and efficient tunnel routes."
keywords: ["Core Keeper mining guide", "Core Keeper drill ore boulder", "Core Keeper wall hardness", "Core Keeper mining route", "Core Keeper mining skill farm"]
tags: [guide, resources, mining, drills]
canonical: "https://www.polarloop.cn/guides/resources/mining-deep/"
updated: "2026-10-19"
related:
  - { title: "Ore Tier Guide", url: "/guides/resources/ore-tier-guide/" }
  - { title: "Mining Matrix Tool", url: "/tools/mining-matrix/" }
  - { title: "Resource Efficiency Calculator", url: "/tools/resource-efficiency/" }
faq:
  - q: "Why does my pickaxe bounce off walls?"
    a: "Each wall type subtracts a flat amount of mining damage from every hit. If your mining damage is at or below that deduction, you deal zero damage and hear a gong-like knockback. You need to clear the deduction — and 12 above it to earn experience."
  - q: "How much ore does one boulder give?"
    a: "Every ore boulder yields exactly 1800 ore of its metal. Drills extract it at a diminishing rate: 1 drill = 27 ore/hour, 8 drills = 116 ore/hour."
  - q: "What do I need for my first drill?"
    a: "A Drill costs 10 Scarlet Bar and 10 Iron Bar at the Automation Table — about 43 Scarlet Ore minimum before smelting. Mine Scarlet by hand in Azeos' Wilderness first."
---

The [ore tier guide](/guides/resources/ore-tier-guide/) tells you *which ore lives in which ring*. This guide goes deeper: how mining damage actually resolves against walls, how to plan tunnels so you never waste swings, and how drills turn ore boulders into an infinite late-game ore supply.

## How wall damage really works

A wall does not have a simple health bar. Every hit first **deducts a flat resistance**, and only the leftover damage bites into wall health. That changes your whole tool check:

- A Tin Pickaxe (83 damage) comfortably breaks Stone walls (67 resistance) but cannot touch Grass walls (147 resistance).
- To *damage* a Grass wall you need mining damage above ~166; to *earn experience* you need it 12 higher still (~178).
- **Melee punches ignore the resistance deduction**, so you can always punch through any breakable wall eventually — just slowly.
- Unattended walls **self-heal 5 seconds** after the last hit, so stop-and-go tunneling wastes progress.

| Wall type | Resistance (min mining damage) | Pickaxe that clears it |
|---|---|---|
| Straw-bale / Paintable / Eerie | 13 | Any early tool |
| Stone, Dark Stone, Stone Bricks | 67 | Tin Pickaxe (83) |
| Grass Block / Scarlet Wall | 147 | Iron Pickaxe (167) |
| Coral Wall | 254 | Scarlet / Ancient Pickaxe |
| Galaxite Wall | 367 | Octarine Pickaxe (403) |
| Gleam Wood Wall | 547 | Galaxite Pickaxe (556) |

Mining skill adds +1 mining damage per level (up to +100), so a high-skill character can punch through walls a tier above their pickaxe — useful for squeezing through before the next workbench.

## Efficient digging routes

- **Branch mining off a main tunnel.** Dig a long horizontal spine, then send short branches every few tiles. It covers wall area without the confusion of a random cave-in maze.
- **Follow the glitter.** Rising sparkles mark rooms and plants; the larger, static sparkles mark ore veins embedded in walls. Aim your tunnel at them.
- **Smelt while you dig.** Ore waits in a chest, but furnaces process in parallel — line up several so smelting never becomes your bottleneck.
- **Bridge over water on long trips.** Water cuts your movement; carrying dirt blocks to bridge across keeps mining routes fast.

## Ore boulders and drill efficiency

Once the Automation Table and Drills are unlocked, the 2×2 **ore boulders** scattered through each biome become your real ore economy. Pickaxes cannot break them — only drills, powered by generators or levers. Each boulder is a fixed 1800 ore.

Adding more drills to one boulder has **diminishing returns**:

| Drills on one boulder | Ore per hour | Hours to deplete |
|---|---|---|
| 1 | 27 | 67.5 |
| 2 | 49 | 37 |
| 3 | 64 | 28 |
| 4 | 82 | 22 |
| 5 | 95 | 19 |
| 6 | 103 | 17.5 |
| 7 | 109 | 16.5 |
| 8 | 116 | 15.5 |

The practical lesson: if your drills are scarce, **spread them across several boulders** rather than stacking them on one. Prioritize Scarlet boulders first — more drills need more Scarlet to build, and the Wilderness is infinite, so you will never run out.

## AFK mining skill farming

Because you gain 1 XP per *hit* (not per break), two setups let you level mining hands-free:

- **Punching on the spot:** surround yourself with a wall type your unarmed mining damage just barely can't one-break, face sideways, and hold use + attack. New blocks place automatically as old ones break.
- **Minecart loop:** lay an 80+ tile rail loop with a one-tile wall gap you can punch from the cart. The loop length keeps the 5-second self-heal resetting, so the walls never break and you never replace them.

Data sourced from the [Core Keeper Wiki — Mining](https://corekeeper.atma.gg/en/Mining), cross-checked against our verified local mining data.

{{< ad >}}


## FAQ

**Why does my pickaxe bounce off walls?** Each wall type subtracts a flat amount of mining damage from every hit. If your mining damage is at or below that deduction, you deal zero damage and hear a gong-like knockback. You need to clear the deduction — and 12 above it to earn experience.

**How much ore does one boulder give?** Every ore boulder yields exactly 1800 ore of its metal. Drills extract it at a diminishing rate: 1 drill = 27 ore/hour, 8 drills = 116 ore/hour.

**What do I need for my first drill?** A Drill costs 10 Scarlet Bar and 10 Iron Bar at the Automation Table — about 43 Scarlet Ore minimum before smelting. Mine Scarlet by hand in Azeos' Wilderness first.

## Related

- [Ore Tier Guide](/guides/resources/ore-tier-guide/)
- [Mining Matrix Tool](/tools/mining-matrix/)
- [Resource Efficiency Calculator](/tools/resource-efficiency/)
- [Biomes database](/database/biomes/)
