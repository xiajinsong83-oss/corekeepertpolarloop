---
title: "Core Keeper Armor Guide — Set Bonuses and Damage Reduction"
description: "How armor works in Core Keeper — the damage reduction formula, three-piece set bonuses, progression tiers and when stacking armor stops helping."
icon: "/img/app-icons/wiki-mechanics.png"
updated: "2026-10-19"
related:
  - { title: "Mechanics", url: "/wiki/mechanics/" }
  - { title: "Accessories", url: "/wiki/accessories/" }
  - { title: "Crafting", url: "/wiki/crafting/" }
  - { title: "Bosses", url: "/wiki/bosses-mechanics/" }
---

{{< ad >}}

**Armor** is the three-piece defensive layer you wear on your head, chest and legs. Each piece adds a flat armor score plus a small sprinkling of offensive stats — max health, % damage, critical chance, attack speed — and matching pieces from the same set unlock set bonuses at 2, 3 or (rarely) 5 pieces. The trap for new players is treating armor as a raw number: the real defense math caps the benefit, which means piling more and more armor past a soft plateau buys almost nothing.

*Source: [Core Keeper Wiki — Armor](https://corekeeper.atma.gg/en/Armor).*

## How much armor actually reduces

Incoming damage runs through a fixed formula:

`(Base damage − Armour × 0.75) × (1 − boss reduction) × (1 − shield reduction) × random 0.9–1.1`

The limits worth memorising:

- Only **three-quarters** of your armor score is subtracted from the hit.
- The armor subtraction can never remove more than **75% of the incoming damage** — against a 100-damage strike, 20 armor shaves 15 (leaving 85), while 200 armor is capped at shaving 75 (leaving 25).
- **Boss-specific reduction** and **shield reduction** sit *outside* the armor cap, so they bypass the ceiling armor itself cannot cross.
- The final number is randomized by **±10%**.
- **Damage over time** (burning, acid, poison ticks) skips armor entirely — resist it before you rely on a fat health pool.

Practical takeaway: once you are sitting around the mid-30s armor per piece, another 10 armor buys less than a piece that grants boss damage reduction, dodge, or an immunity.

## The armor tier ladder

Each tier is crafted at the matching anvil and, like workbenches, a higher anvil inherits the recipes of the tiers below. Early sets are pure stat sticks; late sets trade raw armor for thematic set bonuses.

| Tier | Example set | Piece armor (helm/chest/legs) | Signature set bonus |
|---|---|---|---||
| Early | Peasant / Copper / Tin | +2 to +8 | None (stat-only) |
| Early | Iron | +10 / +12 / +12 | 3-set: +19% armor while at low health |
| Early | Hivebone | +12 / — / +14 | 3-set: immune to acid damage |
| Mid | Scarlet | — / +19 / — | 3-set: killing an enemy stacks +3% crit chance (up to 5) |
| Mid | Octarine | +15 / +22 / — | 3-set: attack speed +0.2% per % of missing health |
| Mid | Omoroth's | +17 / +20 / +20 | 3-set: +23.1% armor while adjacent to water |
| Late | Galaxite | +18 / +26 / — | 3-set: +12.7% damage while at max health |
| Late | Sentry / Stone | +19 / — / +40 | 2-set: +20% damage against bosses |
| Late | Solarite | +20 / — / — | 3-set: +23.6% damage while at max health |
| Late | Hazmat | +21 / +25 / +26 | 3-set: immune to radioactive damage |
| Late | Magma Horn | +25 / +36 / — | 3-set: immune to burning |
| Endgame | Void-Fused | +25 / +29 / +27 | 3-set: stores 300% of damage taken (up to +800), then detonates it after 2 sec |
| Endgame | Shadow | +25 / +36 / — | 2-set: +31.3% damage dealt by you and nearby allies |
| Endgame | Core Commander | +25 / — / +24 | 3-set: nearby enemies take 67 radioactive damage every other second |

*Exact per-piece values scale with item level (base vs. level-20 variants); the numbers above are representative base-tier figures from the wiki.*

## Thematic immunity sets

A handful of endgame sets do not chase damage at all — they grant status immunities that let you ignore entire biomes or boss mechanics:

| Set | Immunity | Where it matters |
|---|---|---|
| Hivebone | Acid damage | Larva Hive, acid pools |
| Slime | Slippery movement (2-set); melee attackers become slippery (3-set) | Sunken Sea, Morpha arena |
| Moldweb | Mold infection | Mold biome |
| Hazmat | Radioactive damage | Late radioactive zones |
| Magma Horn | Burning | Molten Quarry, Pyrdra, Welder builds |
| Remedaisy necklace + Poison resists | Poison | Ivy arena |

Mixing and matching: you do **not** have to run a full three-piece set. A 2-set bonus (such as Sentry's +20% boss damage or Shadow's +31.3% ally damage) is often worth slotting as two pieces while the other slot wears an accessory or a piece from a different set.

{{< ad >}}

## Passive armor from the crafting skill

Your **Crafting** skill grants a small permanent defensive bonus: **+0.5% armor per skill level**, stacking up to **+50% at level 100**. This is a multiplier on whatever armor score you are already wearing, which is why min-maxers keep crafting even after their gear is finished — the bonus scales with every future upgrade.

Reinforcement at the Salvage and Repair Station adds a separate **+15% to item stats** (including armor) while the boosted durability lasts; that is a temporary buff, not a permanent upgrade, and fades as the item wears down.

## FAQ

**Is it worth swapping to a lower-armor set for a set bonus?** Almost always, once you are past Iron tier. The armor cap means the difference between +25 and +35 armor per piece is small, while a 3-set immunity or +20% boss damage changes entire fights.

**Does armor help against DoT like burning?** No. Burning, acid and poison ticks bypass the armor subtraction entirely. Either wear an immunity set, bring resistance consumables, or out-heal the tick.

**What is the best set for boss fights?** Sentry/Stone (2-set: +20% damage against bosses) and Ancient Guardian accessories stack boss-specific reduction. Combine with a shield in the off-hand — shield reduction sits outside the armor cap.

**Can I mix pieces from different sets?** Yes. Only pieces that share a set name count toward its bonus. Two-piece bonuses are the sweet spot for hybrid builds because they leave a slot open for a third piece from another set.

**Does the crafting skill bonus stack with reinforcement?** Yes. The +0.5%/level crafting bonus is a permanent multiplier on your total armor score; reinforcement's +15% item stats is a separate temporary multiplier applied on top.

{{< version-note >}}
