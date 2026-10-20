---
title: "Core Keeper Recipe Backtracker — Total Materials Calculator"
description: "Core Keeper recipe backtracker — pick any craftable item and quantity, and it expands every intermediate ingredient down to the raw materials you need to gather. Total material calculator for crafting runs."
icon: "/img/app-icons/tool-recipe-backtracker.png"
keywords: ["Core Keeper recipe backtracker", "Core Keeper materials calculator", "Core Keeper crafting calculator", "Core Keeper how much materials", "Core Keeper crafting requirements"]
tags: [tools, calculator, crafting, materials]
relatedTools:
  - { title: "Item Crafting Calculator", url: "/tools/item-calculator/" }
  - { title: "Crafting Simulator", url: "/tools/crafting-simulator/" }
  - { title: "Resource Efficiency Calculator", url: "/tools/resource-efficiency/" }
updated: "2026-10-20"
---

Need 5 Iron Bows but don't know how much raw ore to mine? This **Core Keeper recipe backtracker** takes any craftable item and quantity, walks every recipe level and tells you the exact total of each raw material to gather — bars, planks, glass and beyond.

{{< recipe-backtracker >}}

## How the backtracker works

Recipes in Core Keeper are nested: an Iron Bow needs Iron Bars, which need Iron Ore. The calculator recursively expands every intermediate ingredient until nothing left can be crafted further, then sums the totals:

- **Intermediates to craft** — the mid-tier items you must make first, each with the workbench required
- **Raw materials to gather** — the final totals of ore, wood, fiber and other base resources

## Example: Copper Pickaxe ×2

| Intermediate | Total | Workbench |
|---|---|---|
| Copper Bar | 4 | Copper Furnace |
| — | — | — |
| **Raw material** | **Total** | |
| Copper Ore | 4 | |
| Wood | 8 | |

## Tips for big crafting runs

- **Multiply before you mine** — work out the full requirement once, then do one mining trip instead of five.
- **Check the workbench** — some intermediates (like glass or bars) need their own furnace or table; queue them first.
- **Reinforced versions cost more** — the calculator uses the base recipe; reinforced upgrades add extra materials.

## FAQ

**Is the recipe data accurate?** Yes — recipes come from our verified item database (atma.gg), including every craftable item with published materials.

**What if an item has no recipe listed?** Items without a published recipe are treated as raw materials and simply added to the gather list.

**Can it handle quantities above 1?** Yes — enter any quantity and every intermediate and raw total scales accordingly.

{{< ad >}}
