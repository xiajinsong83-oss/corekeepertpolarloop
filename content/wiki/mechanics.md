---
title: "Core Keeper Mechanics"
description: "Core Keeper mechanics explained — game systems, world rules, tool tiers, boss progression and how systems interact."
icon: "/img/app-icons/wiki-mechanics.png"
updated: "2026-10-18"
related:
  - { title: "Tools", url: "/tools/" }
  - { title: "Database", url: "/database/" }
  - { title: "Guides", url: "/guides/" }
---

{{< ad >}}

**Mechanics** is the set of hidden formulas behind every number in Core Keeper: how your attacks scale, how much punishment your armour actually soaks, how power-ups wear off, and why bosses suddenly feel twice as scary with a friend online. Most players beat the early game by feel, but once you start min-maxing around Scarlet, Octarine and legendary gear, the order these bonuses apply decides whether a build is strong or merely okay.

## How outgoing damage is stacked

The game layers your damage boosts in a fixed order, and understanding that order prevents wasted investment.

- **Generic damage bonuses add together.** A helmet granting +10% damage and an accessory granting +25% damage combine into a flat +35% total — they are not multiplied against each other.
- **Conversion bonuses multiply that result.** Skills written as "+X% of Y added as Z damage" (for example mining strength or well-trained aim) first turn a secondary stat into flat damage, and only then is that flat number multiplied by your generic damage bonuses. A ranged build with 100 fishing power and a level-5 aim skill adds 30 flat ranged damage, which your percentage boosts then inflate. Because these are flat values rather than percentages, they reward fast-attack weapons more than slow, heavy hits.
- **Critical hits land last.** A critical strike rolls off your critical chance and multiplies the already-finished total, and can itself be inflated by critical-damage bonuses.

A practical takeaway: stacking a dozen identical "+% damage" pieces gives diminishing returns, while mixing in a good conversion stat (such as fishing power on a ranged build) often outperforms more of the same.

## Minions, pets and explosives have their own rules

Not every attack uses the generic damage pipeline.

- **Minions and pets roll their own stats.** They carry independent damage, attack speed, critical chance and debuff chance, and listen only to bonuses explicitly tagged for minions or pets. A minion-focused helmet helps them, but an ordinary +% damage helmet with no minion tag does nothing for your summons.
- **Explosives live in a separate bucket.** They cannot score critical hits, ignore generic +% damage, and cannot apply debuffs like poison or burn. Only explosive-specific bonuses and ranged attack speed touch them.
- **Split-damage weapons split their bonuses too.** A mortar dealing 100 ranged and 200 explosive base damage, with +50% non-explosive damage, ends at 350 rather than 450 — only the ranged portion receives the bonus. Explosive bonuses likewise never boost wall or mining damage.

## How much armour actually protects you

The damage you take follows a compact formula:

`(Base damage − Armour × 0.75) × (1 − boss reduction) × (1 − shield reduction) × random 0.9–1.1`

The important limits to know:

- Only three-quarters of your armour score is subtracted, and the resulting reduction can never remove more than 75% of the hit. Against a 100-damage strike, 20 armour shaves 15 (leaving 85), while 200 armour is capped at shaving 75 (leaving 25).
- Boss-specific reduction and shield reduction sit *outside* that armour cap, so they bypass the ceiling armour itself cannot cross.
- The final number is randomly varied by ±10%.
- Damage over time, such as being set alight, skips armour entirely — resist it before you rely on a fat health pool.

For players, this means piling armour past a soft plateau gives almost nothing; a shield and boss-reduction gear do more against endgame fights.

## Reinforcing your gear

Reinforcement is a temporary power-up applied at the Salvage and Repair Station, and it consumes a slice of the item's own base materials. Only equipment that has durability can be boosted.

- Reinforced tools and armour gain **+15% to their damage and relevant stats** (attack speed is deliberately left untouched), with the bonus numbers shown in green.
- Current durability is doubled up front, which means a broken or worn item is fully repaired in the process.
- The boost is not permanent: once the extra durability burns down to the base value, the +15% vanishes. You can reinforce again afterward.

**What this means for you:** reinforce right before a boss fight or a long mining push, not at your base for the day. The buff fades as you use the item, so save it for the moments it matters.

## Liquids and their priority order

Water flows freely into empty pits and spreads without limit. You can bridge over it, sail across it in boats, fish in it once your rod is high enough, or move it with a bucket. Where it gets clever is how different liquids interact.

| Priority | Liquid | Where it is found |
|---|---|---|
| 1 | Normal water | Undergrounds, Clay Caves, Forgotten Ruins, Azeos' Wilderness, Desert of Beginnings |
| 2 | Lava | Molten Quarry, Desert of Beginnings, Breaker's Reach |
| 3 | Acid water | Larva Hive |
| 4 | Mold water | Mold biome |
| 5 | Shimmering water | Shimmering Frontier |
| 6 | Grimy water | The Passage, Breaker's Reach |
| 7 | Sea water | Sunken Sea |

When two ordinary liquids touch, the higher priority slowly converts the lower one. Sea water sits at the top on purpose, so you cannot flood the whole ocean from a single bucket. Lava is the exception: on contact with weaker water it hardens both sides into Lava Rock Block, rather than spreading.

## Hard mode and multiplayer

- **Hard mode** is chosen when the world is created and is then locked to that save. Enemies lose twice their health and twice their base damage, but boss drop rolls are multiplied by 1.5 (rounded). It trades a tougher run for noticeably richer boss loot.
- **Co-op** does not inflate ordinary enemies at all, but every player independently triggers the same local spawn rate two players standing together roughly double. Bosses, however, scale their health to the number of people connected, with a different multiplier per boss.

Team-up friends to clear content faster, but expect boss arenas to demand that extra party member rather than trivialising them.

## Your off-hand slot

The off-hand slot (activated with Space on PC) holds one of three active item types:

- **Shields** block indefinitely with no cooldown, but you stand still while doing so. Timing the block just before impact is a parry: you take no damage and stun nearby melee attackers. Shields have durability and can therefore be reinforced.
- **Dashes** grant a short burst of speed or a quick reposition on demand.
- **Detonators** set off your minions or nearby remote explosives for a burst of area damage.

{{< version-note >}}
