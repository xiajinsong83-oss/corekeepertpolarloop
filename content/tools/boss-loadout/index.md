---
title: "Boss Loadout Generator"
description: "Core Keeper boss loadout generator — recommended weapon, armor, accessories, food and potions for every main boss, matched to its biome tier."
icon: "/img/app-icons/tool-boss-loadout.png"
keywords: ["Core Keeper boss loadout", "Core Keeper boss gear", "Core Keeper boss guide", "Core Keeper recommended armor", "Core Keeper boss potions"]
related:
  - { title: "Boss Drop Finder", url: "/tools/boss-drop-finder/" }
  - { title: "Combat & Bosses Guides", url: "/guides/combat-bosses/" }
  - { title: "Bosses Database", url: "/database/bosses/" }
---

The Core Keeper **boss loadout generator** pairs every main boss (Glurch, Ghorm, Hive Mother, Malugaz, Azeos, Omoroth, Ra-Akar) with a ready-made gear plan — weapon, armor set, accessory, food and potion — matched to the ore tier of its biome. Recommendations are pulled from the official wiki's per-boss "Recommended gear" sections and cross-checked against our own crafting data, so every item listed is something you can actually craft or farm in that stage of the game.

## How to use

1. Pick a boss card from the row above.
2. Read the five recommendation cards — **Weapon / Armor / Accessory / Food / Potion** — each with a short note on *why* this slot is chosen.
3. Below the cards you'll find a 1–2 sentence tactics summary and the source wiki pages.
4. Hit **Copy loadout** to grab the full plan as plain text for Discord, notes or your next play session.

{{< boss-loadout >}}

## Data notes

Loadout recommendations are cross-checked against each boss's official wiki page on corekeeper.atma.gg and the in-game 1.3.0.6 crafting data in our local items database — per-boss source URLs are listed in the `sources` field of `data/boss-loadouts.yaml`, and any item not yet verifiable locally is flagged as "数据待核" rather than guessed.

{{< ad >}}

## FAQ

- **Why is the recommendation always one tier behind the boss's own drops?** You fight each boss with the gear available *before* you kill it — e.g. Glurch is fought in the copper/tin stage, Omoroth in octarine gear. The boss's own unique drops (Omoroth's Chestplate, Scarab set, etc.) are post-farm upgrades, not pre-fight loadout.
- **Some slots say "data待核 / data pending".** A few wiki-recommended items (Swift Ring, Carapace Armor, Puffungi, Scarlet armor set) are not yet in our local crafting database. They're flagged in the note rather than invented — check the linked wiki page for the exact recipe.
- **Do potions stack with food?** Yes — wiki confirms potions stack with cooked-food buffs, so Stoneskin/Guardian potions on top of a Carrock+Bomb Pepper dish is the optimal combo.
- **Which bosses are optional?** Malugaz is optional (Forgotten Ruins, scarlet tier). The other six are required to power up The Core / advance the titan chain.

## Related tools

- [Boss Drop Finder](/tools/boss-drop-finder/) — every boss's drop table, chance and unlock condition
- [Combat & Bosses Guides](/guides/combat-bosses/) — mechanics, arena setup and cheese strategies
- [Bosses Database](/database/bosses/) — full boss list with biome and tier metadata
