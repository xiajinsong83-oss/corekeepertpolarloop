---
title: "Item Crafting Calculator"
description: "Core Keeper crafting calculator — pick an item and get the full material list, quantities and workbench required."
icon: "/img/app-icons/item-calculator.png"
keywords: ["Core Keeper crafting calculator", "Core Keeper recipe calculator", "Core Keeper materials", "Core Keeper recipes"]
related:
  - { title: "Items Database", url: "/database/items/" }
  - { title: "Resource Efficiency Calculator", url: "/tools/resource-efficiency/" }
  - { title: "Creature Lookup", url: "/tools/creature-lookup/" }
---

The Core Keeper **item crafting calculator** expands any recipe into its **full crafting tree**. Pick a target item and a quantity, and it recursively breaks every intermediate material down to raw ingredients — ore, bars and wood all the way to what you actually need to mine or gather.

## How to use

1. Choose the item you want to craft.
2. Set the target quantity.
3. Read the **raw ingredient summary** (total ore / wood needed) and the **crafting tree** showing each intermediate step with its station (Furnace, Smelter Kiln, Anvil, Workbench).

{{< crafting-calculator >}}

{{< ad >}}

## Data notes

- **Recipes**: verified against the official wiki (corekeeper.atma.gg) for game version 1.3.0.6, 2026-10-18. Intermediate smelting is 1:1 — 1 ore → 1 bar (Furnace: Copper 7s, Tin 12s, Iron 17s; Smelter Kiln: Gold 22s, Scarlet 27s).
- A few niche recipes (exact Gold Bar counts on Iron-tier tools) are flagged for a second wiki pass; the tree still expands them using the wiki-listed materials.
- Raw materials (Ore, Wood, Fiber, Dirt Block) are gathering endpoints — they have no recipe.

## FAQ

- **Does it include all recipes?** Recipe data is synced from the community wiki and updated after each major patch.
- **Can I plan bulk crafting?** Yes — set a target quantity and the whole tree scales automatically.
- **Why do I see raw ore instead of bars?** The tree expands every bar back to its ore; the raw summary tells you exactly what to mine.

## Related tools

- [Items Database](/database/items/) — stats and sources for every item
- [Resource Efficiency Calculator](/tools/resource-efficiency/) — estimate gathering rates for the materials you need
