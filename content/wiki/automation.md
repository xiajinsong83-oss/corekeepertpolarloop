---
title: "Core Keeper Automation — Electricity, Wires and Auto Farms"
description: "How automation works in Core Keeper — power transmission range, generators, circuits, drills, conveyor belts and the standard mob/wood/food farm layouts."
icon: "/img/app-icons/wiki-mechanics.png"
updated: "2026-10-19"
related:
  - { title: "Mechanics", url: "/wiki/mechanics/" }
  - { title: "Crafting", url: "/wiki/crafting/" }
  - { title: "Mining", url: "/wiki/mining/" }
  - { title: "Gardening", url: "/wiki/gardening/" }
---

{{< ad >}}

**Automation** is the set of powered machines that turn a base into a self-running factory: drills chew through Ore Boulders while you are off fighting, conveyor belts ferry dropped loot into chests, and Robot Arms pull items between inventories so you never have to walk back. Every electrical machine runs on a simple two-wire logic — a power source, a length of conducting wire, and whatever you want switched on the other end. Once the Electronics Table and Automation Table are unlocked, almost any manual loop can be wired up.

*Source: [Core Keeper Wiki — Automation](https://corekeeper.atma.gg/en/Automation).*

## How electricity actually travels

Power is not infinite — it is a level that drops as it crosses tiles, and every machine you run through it costs one level, the same as a tile of wire.

- An **Electricity Generator** transmits full power over **18 conducting tiles**.
- A **Lever** or **Pressure Plate** only transmits over **6 tiles**.
- After that full-power range, power decays over a further **5 tiles**, so connected lamps visibly dim along the tail of the run.
- Each machine on the circuit subtracts one power level, exactly as a wire tile would.
- **Drills, Robot Arms and doors work at any power level**, even the dimmest — only lamps care about brightness.

When a machine is powered, the notches on the four sides of its base glow yellow. That is the only built-in signal tracer, so when a circuit fails, walk along it and watch for the first notch that stays dark.

## Power sources and powered machines

Everything electronic is crafted at the **Electronics Table** (unlocked from the Copper Workbench tier), with the heavy-duty farming machines moving to the **Automation Table** and then the **Advanced Automation Table**.

| Type | Item | Crafted at |
|---|---|---|
| Power source | Electricity Generator | Electronics Table |
| Power source | Lowered Electricity Generator | Electronics Table |
| Power source | Kinematic Dynamo | Electronics Table |
| Switch | Lever | Electronics Table |
| Pressure trigger | Pressure Plate | Electronics Table |
| Motion trigger | Explorer Proximity Sensor | Electronics Table |
| Motion trigger | Enemy Proximity Sensor | Electronics Table |
| Digging | Crude Drill / Drill | Automation Table |
| Item handling | Robot Arm | Automation Table |
| Farming | Robot Farm Arm | Advanced Automation Table |
| Item handling | Item Collector | Advanced Automation Table |
| Processing | Seed Extractor, Shredder, Incinerator | Advanced Automation Table |
| Defence | Galaxite Turret, Flame Turret | Galaxite / Relucite tier |
| Decoration / utility | Lamp, Electrical Door, Electrical Drop Gate, Siren Lamp, Table Saw, Egg Incubator | Various |

## Circuit shapes and logic

Circuit pieces let you bend, split and delay a wire run without splicing wires by hand. Every shape is cheap — a Copper Bar each — so there is no reason to build an L-bend out of long straight runs.

| Circuit | Cost | What it does |
|---|---|---|
| I Circuit | 1 Copper Bar | Straight pass-through |
| L Circuit | 1 Copper Bar | Right-angle bend |
| T Circuit | 1 Copper Bar | Splits a run into three directions |
| Cross Circuit | 1 Copper Bar | Four-way crossing |
| Delay Circuit | 1 Copper Bar | Passes a lower-powered signal after a short hold |
| Logic Circuit | 2 Copper Bar | Truth-gate block; boosts a weak signal when a second input is present |

Levers are player-activated switches: they pass through the generator's higher power *and* generate their own small power, which makes them the simplest way to toggle a distant machine on and off.

{{< ad >}}

## The four standard farm layouts

### Automatic door

Lay a pair of **Pressure Plates** on both sides of an **Electrical Door** and it opens from whichever side you approach. Swap in an **Explorer Proximity Sensor** plus an **Electrical Drop Gate** if you want the door to trigger only for the player, not for slimes wandering through.

### Ore Boulder excavation

Ring an Ore Boulder with a ring of **Crude Drill** or **Drill** blocks, run wire from an **Electricity Generator**, and let the drills chip the boulder automatically. Add **Conveyor Belts**, **Robot Arms** and Furnaces to ferry ore straight into smelters — an eight-drill ring around a Scarlet Ore Boulder smelts its own output into bars while you explore.

### Wood farm

**Root Seeds** grow wood in a random adjacent direction every 2–3 minutes. Place drills facing a tile that the root can grow into (never touching the Root Seed itself, or you destroy the plant), and the drills harvest each new wood tile as it appears. A straight-line root pattern yields far more than a scattered planting — frame the growth path with a single starter root so the next root never grows directly beside an existing one.

### Mob farm

Enclose a roughly **16×16** chamber, floor it with the block that spawns the mob you want (for example Fungal Soil for Shrooman), and line the walls with **Spike Traps**, **Galaxite Turrets** or **Radiation Crystals**. Robot Arms, Conveyor Belts and Chests collect the drops. Orange Slimes are the easiest auto-kill target: they aggro onto whatever trap hits them and jump on it repeatedly.

### Food farm

Combine **Sprinkler**, **Robot Farm Arm**, **Seed Extractor**, **Conveyor Belt** and **Conveyor Belt Splitter** into a loop: the farm arm plants and harvests, half the crop goes to a seed extractor to replenish seeds, and the other half is funnelled into storage.

## FAQ

**Why are my lamps dim at the end of a long wire run?** Power decays after 18 tiles from a generator (6 from a lever/pressure plate). Add a **Logic Circuit** as a relay on the run, or move the generator closer — drills and arms do not care, but brightness does.

**Can machines run off a lever all by themselves?** Yes, but only over 6 tiles. Anything farther needs a generator on the circuit, with the lever wired in as a switch rather than as the sole source.

**Do drills hurt the Root Seed in a wood farm?** Only if a drill face touches the seed tile itself. Keep one tile of gap between the drill heads and the Root Seed, and the root will keep sprouting into the drill-facing tile.

**What is the difference between a Robot Arm and an Item Collector?** Robot Arm pulls or pushes items between adjacent inventories on a timer. Item Collector vacuums up loose drops on the floor around it — use Collectors at the bottom of mob traps and Arms on conveyor-belt junctions.

**Where do I unlock the best automation parts?** **Automation Table** arrives at the Tin Workbench tier; the **Advanced Automation Table** (Robot Farm Arm, Seed Extractor, Shredder, Incinerator, Item Collector) comes online with the **Octarine Workbench**.

{{< version-note >}}
