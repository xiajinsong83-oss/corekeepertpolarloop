---
title: "Core Keeper Cooking"
description: "Core Keeper cooking guide — recipes, meals, buffs, ingredients and cooking stations."
icon: "/img/app-icons/wiki-cooking.png"
updated: "2026-10-18"
related:
  - { title: "Database Items", url: "/database/items/" }
  - { title: "Tools", url: "/tools/" }
  - { title: "Guides", url: "/guides/" }
---

{{< ad >}}

**Cooking** is how you turn raw foraged ingredients into dishes that punch far above their weight. Dropping two ingredients into a Cooking Pot produces a meal with stronger buffs, longer duration, and hidden stat combinations you'd never see from eating them raw. Understanding the hidden math behind the pot is what separates a good survivor from an endgame-ready one.

## How the Cooking Pot works

Set a Cooking Pot down on any flat surface, walk up to it, and interact to open its interface. You'll see two ingredient slots:

- Move any compatible food from your inventory into either slot.
- **Order doesn't matter** — berry-plus-fish is the same dish as fish-plus-berry.
- Each slot needs at least one item; you can't cook a single ingredient on its own.
- **Robot Arms** can be wired to automatically feed ingredients into the pot for a self-running kitchen.

The pot processes each pair over **10 seconds**, then drops one finished dish into the output slot. Two quirks catch people out:

- A dish is identified entirely by the **combination** of ingredients used. Cooked food only stacks with identical recipes, so don't expect random leftovers to merge into one pile.
- Dishes can come in up to **three rarities** (regular, rare, epic), and rarity changes the actual buff numbers.

## The hidden ingredient math

Every edible item carries **hidden cooking effects** that are different from what happens when you eat it raw — and the game never shows them. When two ingredients meet in the pot:

- Both ingredients' effects are combined into the dish.
- **Permanent max-health boosts are additive** — cooking can never erase a permanent health gain, and they stack.
- **Everything else picks the higher value.** If one ingredient gives +2.8 health/sec and the other gives +2.2, you get +2.8; you do not get both.

Worked example — cooking a Heart Berry with a Blue Cave Guppy:

| Effect | Heart Berry | Blue Cave Guppy | Dish result |
|---|---|---|---|
| Food points | +19 | +21 | **+21** (higher wins) |
| Regen (20 sec) | +2.8 hp/sec | +2.2 hp/sec | **+2.8 hp/sec** (higher wins) |
| Dodge (5 min) | — | +5% | **+5% dodge** |
| Max health (5 min) | +25 | — | **+25 max health** |

The rule of thumb: stack the ingredient with the stronger version of each stat you want, and let anything extra come along for free.

## Rarity, golden ingredients and bonus rolls

A few layered systems decide how strong a finished dish is:

- **Extra food rolls**: every cooking level adds +0.2% chance to produce a bonus dish, up to +20% at level 100. This roll is made independently each time you pull food out of the pot.
- **Master Chef talent**: can bump each bonus dish up a rarity tier.
- **Base rarity by input**:
  - Both ingredients non-golden/legendary → dish is **regular**, with a chance to roll rare.
  - At least one ingredient golden/legendary → dish is **rare**, with a chance to roll epic.
- **Stat scaling**: rare dishes get +25% stats versus regular (before rounding); epic dishes get +50%.
- **Double golden bonus**: if **both** ingredients are golden or legendary, another multiplicative +15% is added on top.

Three fine-print notes worth remembering:

- Rare or epic dishes do **not** get written into your recipe book.
- Permanent max-health boosts are **not** scaled by rarity or the golden bonus.
- **Shiny Larva Meat** looks golden but does not count as a golden ingredient for cooking.

## Leveling and talents

Cooking experience is awarded when you **take a finished dish out of the pot**, not while it simmers. As with gardening, each level feeds a small +0.2% bonus-dish chance (up to 20% at level 100).

The most useful cooking talents:

- **Utilizing Every Nutrient** — +5% to +25% food from cooked dishes.
- **Healthy Diet** — your well-fed buffs become +20% to +100% stronger.
- **Not So Picky** — well-fed buffs trigger at +2% to +10% lower food intake.
- **Long-Lasting Food** — +6% to +30% longer buff durations on cooked dishes.
- **Fast Food** — +1% to +5% melee attack speed for 30 seconds after eating cooked food.
- **Power of Omega-3!** — +3% to +15% damage against bosses when eating fish or fish-based dishes.
- **The Smell of Food** — +4% to +20% damage for you and nearby allies.
- **Sharing Is Caring** — +0.1 to +0.5 health per second to you and nearby allies.
- **Master Chef** — +5% to +25% chance that bonus dishes roll rare.

## Example ingredient effects

To make the hidden system concrete, here are the regular/rare/epic values for a few early ingredients:

| Ingredient | Regular | Rare | Epic |
|---|---|---|---|
| Mushroom | +19 food; +4.2 hp/sec for 20s | +24 food; +5.2 hp/sec | +28 food; +6.3 hp/sec |
| Giant Mushroom | +31 food; +25 max health (permanent, once); +24 max health for 10 min | +39 food; +30 max health for 10 min | +46 food; +36 max health for 10 min |
| Moorshroom | +20 food; +6.6 hp/sec for 20s; +4 glow for 10 min | +25 food; +8.2 hp/sec; +5 glow | +30 food; +9.9 hp/sec; +6 glow |
| Glowing Mushroom | +20 food; +4 purple glow; +34% explosion damage for 10 min | +25 food; +5 glow; +42% explosion damage | +30 food; +6 glow; +51% explosion damage |
| Heart Berry | +19 food; +25 max health for 10 min; +2.8 hp/sec for 20s | +24 food; +31 max health; +3.5 hp/sec | +28 food; +38 max health; +4.2 hp/sec |

## Tips for new chefs

- **Cook almost everything** — eating raw food is almost always weaker than the cooked version of the same ingredient.
- **Pair high-value stats deliberately**: want regen? Match two regen sources and let the higher one win. Want a permanent health bump? Giant Mushroom-style ingredients are worth cooking early and often.
- **Keep Golden crops / Golden fish for special dishes** — they're the only route into epic-tier food.
- **Set up a Robot Arm-fed pot** once you have the parts; bulk-cooking while you explore is the real endgame quality-of-life move.
- **Don't chase recipe-book completion for rare/epic dishes** — by design they won't be saved, so keep a manual note of your favorite combos.

{{< version-note >}}
