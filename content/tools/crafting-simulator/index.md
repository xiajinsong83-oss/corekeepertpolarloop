---
title: "Crafting Simulator"
description: "Core Keeper crafting simulator — enter your inventory, find out how many items you can craft right now, what is the bottleneck and what to gather next."
icon: "/img/app-icons/tool-crafting-simulator.png"
keywords: ["Core Keeper crafting simulator", "Core Keeper inventory calculator", "Core Keeper bottleneck", "Core Keeper what can I craft", "Core Keeper materials needed"]
related:
  - { title: "Items Database", url: "/database/items/" }
  - { title: "Item Crafting Calculator", url: "/tools/item-calculator/" }
  - { title: "Crafting Guide", url: "/wiki/crafting/" }
---

The Core Keeper **crafting simulator** turns your backpack into a bottleneck analysis. Pick a target item, type in what you are already carrying — raw ore, smelted bars, wood, fiber — and it computes **how many copies you can actually craft right now**, which step of the chain stalls first, and exactly how much more of each material you must gather.

Where the item crafting calculator answers *"what do I need to craft N of this?"*, the simulator answers *"given the stack in my chests, what can I finish today?"*

## How to use

1. **Choose the target item** (search the dropdown — every craftable recipe in the wiki dataset is listed).
2. **Set your goal quantity** — how many you want to walk away with.
3. **Enter your current stock** for every material in the chain: raw ore/wood count directly, and so do bars or intermediate products you already smelted or crafted.
4. Read the result:
   - **Craftable now** — the maximum copies your stock supports (intermediates are re-smelted automatically in the math).
   - **Bottleneck** — the single ingredient that limits production, and how far short you are.
   - **Gap to reach your goal** — sortable table of every material you still need, tagged *gather* (mine / chop / dig) or *craft* (needs a station first).
   - **Full crafting chain** — the multi-level tree with per-node status: `ok`, `short N`, or your stock on the target itself.
5. **Copy plan** exports the whole simulation as plain text for your notes or discord.

{{< crafting-simulator >}}

{{< ad >}}

## Data notes

- Recipes verified against the community wiki (corekeeper.atma.gg) for game version 1.3.0.6; the extra station recipes (Furnace, Cooking Pot, Copper Anvil, Tin Workbench, Wood Chest and more) were appended 2026-10-19 from the wiki Crafting page.
- Stock of an intermediate product counts **as itself first**: if you have Copper Bars in the chest, they cover bar demand before the simulator burns Copper Ore.
- The simulator assumes full focus on one target — it does not split materials between parallel craftings.

## FAQ

- **How is this different from the Item Crafting Calculator?** The calculator expands the recipe tree for a fixed quantity and lists raw ingredients. The simulator layers your inventory on top, runs bottom-up capacity math, and reports the max craftable count and the bottleneck step.
- **Do I need to smelt everything first?** No — type your ore stack in the ore field and your bar stack in the bar field; the simulator combines both automatically.
- **What counts as a "gather" gap vs a "craft" gap?** Raw materials (ore, wood, fiber, dirt block) are gathered in the world; anything with its own recipe (bars, stations, gear) must be crafted at the matching workbench or furnace.
- **Can I simulate bulk goals like 100 bars?** Yes — goal quantity runs up to 999 and every gap scales with it.

## Related tools

- [Item Crafting Calculator](/tools/item-calculator/) — expand any recipe into its full material tree
- [Items Database](/database/items/) — stats, rarity and sources for every item
- [Resource Efficiency Calculator](/tools/resource-efficiency/) — estimate how long the gathering will take
