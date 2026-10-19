---
title: "Core Keeper Boss Mechanics — Summoning, Scanners and Respawns"
description: "How boss progression works in Core Keeper — story versus optional bosses, summoning items, scanner use, multiplayer scaling and hard-mode loot."
icon: "/img/app-icons/wiki-mechanics.png"
updated: "2026-10-19"
related:
  - { title: "Mechanics", url: "/wiki/mechanics/" }
  - { title: "Armor", url: "/wiki/armor/" }
  - { title: "The Great Wall", url: "/wiki/great-wall/" }
  - { title: "World", url: "/wiki/world/" }
---

{{< ad >}}

**Bosses** are the large signature enemies that gate progression and mark biomes. They spawn at fixed distances from The Core at random angles, which means you can triangulate them by how far you have walked rather than memorising a seed. Every boss falls into one of three buckets: **story bosses** that drop the hearts and souls you need to power The Core and open new biomes, **optional side bosses** that farm materials and legendary recipes, and **post-game bosses** that unlock after the main story ends. This page covers the *mechanics* of summoning, locating and respawning them — for per-boss drops see the [boss drop finder](/tools/boss-drop-finder/) and [bosses database](/database/items/).

*Source: [Core Keeper Wiki — Bosses](https://corekeeper.atma.gg/en/Bosses).*

## Story bosses and progression gates

The first three bosses power The Core itself. Each drops a unique heart item that must be emplaced in its boss statue; once all three are in, The Great Wall opens and the mid-game titans become reachable.

| Boss | Biome | Distance from Core | Base HP | Summoning / respawn item |
|---|---|---|---|---|
| Glurch the Abominous Mass | Underground | 65 | 2,459 | Found naturally at 65 tiles; Bearded Merchant freed on kill |
| Ghorm the Devourer | Clay Caves / Forgotten Ruins | ~200 (encircling track) | 8,061 | Ghorm Summoning Idol (Cloaked Merchant) |
| Malugaz the Corrupted | Forgotten Ruins | ~300 | 14,513 | Skull of the Corrupted Shaman (crafted from 3 Crystal Skull Shards from cavelings) |

After the three hearts, six **Titans** drop souls that advance the story. Five of them are summoned at an **Ancient Shrine** craftable item; Omoroth is fished up instead.

| Titan | Biome | Distance | Base HP | Summoning method |
|---|---|---|---|---|
| Azeos the Sky Titan | Azeos' Wilderness | ~550 | 31,813 | Place Large Shiny Glimmering Object in the arena |
| Omoroth the Sea Titan | Sunken Sea | ~650 | 90,772 | Equip Expert Lure in off-hand, fish at a whirlpool |
| Ra-Akar the Sand Titan | Desert of Beginnings | ~600 | 160,799 | Place Thumper in the arena |
| Druidra the Wild Titan | Azeos' Wilderness | roaming ~1000–1200 | 136,992 + 48,028 armor | Place Wind Organ of Wilderness |
| Crydra the Ice Titan | Sunken Sea | roaming | 136,992 + 48,028 armor | Place Wind Organ of Ice; summons an invulnerable Druidra copy |
| Pyrdra the Fire Titan | Desert of Beginnings | roaming | 136,992 + 48,028 armor | Place Wind Organ of Fire; summons invulnerable Druidra + Crydra copies |

Once all six souls are in, the **Core Commander** awakens inside the Crystal Meteorite in the Desert of Beginnings (HP 465,385, ~1200 tiles). Respawn it with a **Core Commander Summoning Idol** on the meteorite rune.

## Post-game and optional bosses

These are not required to finish the story but drop legendary recipes, pets and endgame materials.

| Boss | Bucket | Biome | Summoning item |
|---|---|---|---|
| The Hive Mother | Optional early | Larva Hive | Hive Mother Summoning Idol (Cloaked Merchant) |
| King Slime | Optional crossover | Any slime rune | Crown Summoning Idol |
| Ivy the Poisonous Mass | Optional mid | Azeos' Wilderness (~900) | Giant Slime Summoning Idol |
| Morpha the Aquatic Mass | Optional mid | Sunken Sea (~1400) | Giant Slime Summoning Idol |
| Igneous the Molten Mass | Optional mid | Molten Quarry (~1400) | Giant Slime Summoning Idol (drops Cipher Parchment for Soul Seeker) |
| Atlantean Worm | Optional late | Sunken Sea (roaming) | Place Bait Pillar near it (9,641 HP per segment) |
| Urschleim | Optional late | The Passage (~1250 encircling) | Primeval Slime Cell anywhere in the biome |
| Nimruza, Queen of the Burrowed Sands | Post-game | Oasis (Desert) | Corrupted Sap at Ancient Shrine |
| S.A.H.A.B.A.R. | Post-game | Breaker's Reach (~1450) | Profane Override at the interactable computer |
| Oblidra the Void Lord | Post-game | Void (Breaker's Reach) | Wind Organ of Void (10 Oblivion Fragments) |

Seasonal variants reuse the same arenas with their own summoning idol: **Haunted Hive Mother** (Halloween, from Samhain Goodie Bags) and **Awakened Azeos** (Easter, from Large Golden Egg).

{{< ad >}}

## How scanners work

Every boss has a matching **Scanner** item (for example *Ghorm the Devourer Scanner*, *Azeos the Sky Titan Scanner*). Scanners are crafted or bought after your first kill and then pin the boss's position onto your map, turning the "walk 600 tiles at a random angle" guesswork into a waypoint. Without a scanner, you can still triangulate: Ghorm's track sits about 220 tiles out, the Great Wall sits around 470 tiles, and later bosses are described in the wiki as multiples of that radius.

## Multiplayer and hard-mode rules

- **Co-op does not inflate ordinary enemies**, but every nearby player independently triggers local spawns — two players standing together roughly double the ambient spawn rate.
- **Bosses scale their health to the number of players connected**, with a different multiplier per boss. Bring a friend and expect longer fights, not trivial ones.
- **Hard mode** is locked at world creation: enemies have double health and double base damage, but boss drop rolls are multiplied by **1.5 (rounded)**.

## FAQ

**Do I have to re-fight a boss to farm its drops?** Yes. Place the matching summoning item on its rune circle to respawn it. Cloaked Merchant idols restock over time; Ancient Shrine items are craftable on demand once unlocked.

**Why is Omoroth not biting?** You must equip the **Expert Lure** in your off-hand slot and cast your fishing rod at one of the five whirlpools in its arena. Regular lures do not work.

**What does the "protective armor" number on Druidra/Crydra/Pyrdra mean?** It is a separate shield pool that must be broken before their main HP bar takes damage. The numbers (136,992 main + 48,028 armor) are base values; multiplayer and difficulty scale them.

**Which boss should I fight first?** Glurch at 65 tiles is always your first. Then follow Ghorm's track (the 8-tile-wide swathe of slimes) and push into the Forgotten Ruins for Malugaz. Do not attempt the Hive Mother or Ivy until you have Iron-tier gear.

**Where do I spend the titan souls?** Each soul goes onto its matching boss statue back at The Core. After all six are emplaced, the Crystal Meteorite in the Desert of Beginnings becomes breakable, opening the Core Commander fight.

{{< version-note >}}
