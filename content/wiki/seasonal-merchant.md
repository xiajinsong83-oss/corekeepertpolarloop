---
title: "Core Keeper Seasonal Merchant — How to Summon and What They Sell"
description: "How the Seasonal Merchant works in Core Keeper — crafting the Calendar, seasonal currency, event-exclusive stock and when the merchant leaves."
icon: "/img/app-icons/wiki-seasonal.png"
updated: "2026-10-18"
related:
  - { title: "Seasonal Events", url: "/wiki/seasonal/" }
  - { title: "Seasonal Workbenches", url: "/wiki/seasonal-workbenches/" }
  - { title: "News", url: "/news/" }
  - { title: "Carpenter's Table (Crafting)", url: "/wiki/crafting/" }
---

{{< ad >}}

The **Seasonal Merchant** is the travelling vendor who shows up only during real-world celebrations — Halloween, Christmas, Easter and the rest. They do not wander in on their own; you have to invite them with a specific crafting item. Their stock is event-exclusive and is bought with event-specific currency, not ordinary coins, so missing the window means waiting a full year for the same items to return.

## How to summon the merchant

Unlike the regular NPC merchants who move into your base once you meet their room requirements, the Seasonal Merchant is triggered by a placeable object:

1. **Craft a Seasonal Calendar** at the **Carpenter's Table**. This is the invite item.
2. **Hang the Calendar on a wall** inside a suitable room — the same kind of enclosed, lit room that other NPCs require.
3. **Make sure an event is actually running.** The merchant only moves in during the active celebration. Outside event dates, the Calendar does nothing.

In multiplayer, the merchant appears in the host's world (or the dedicated server's world), and everyone connected trades with them there. On a dedicated server, the `-season` launch property overrides the calendar, so you can lock a season permanently even off-calendar.

## Seasonal currency

The merchant does not take gold. Every event has its own drop currency that you farm from themed enemies during the celebration:

| Event | Currency | How to get it |
|---|---|---|
| Christmas | Cookies & Milk | Drop from seasonal-themed enemies during the event window |
| Halloween, Easter, Valentine, Lunar New Year, Cherry Blossom, Anniversary | Event-specific drops | From event-themed mobs during that window |

The practical loop is: **kill themed mobs → collect currency → trade with the merchant.** Because the enemies themselves are reskinned versions of existing types, you can farm in any biome you already know.

{{< ad >}}

## What the merchant sells

Stock rotates with the event, but the pattern is consistent:

- **The event's own workbench.** For Christmas that is the Festive Workbench (5 Cookies & Milk); for Halloween it is the Samhain Workbench; for Easter the Easter Workbench; for Valentine the Valentine Crafting Table. Buying the bench unlocks the event's full craftable set.
- **Decorative blocks and furniture.** Snow blocks, festive walls, themed tables, stools, fireplaces and similar build pieces.
- **Vanity items.** The Pumpkin Head cosmetic for Halloween, festive hats and outfits for Christmas, cherry-blossom décor in spring.
- **Themed food and comfort items.** Christmas brings Cookies & Milk itself, Hot Chocolate, Hot Punch, Fruit Bread and a full Winter Dinner.
- **Wrapped presents.** Regular Winter Presents and the rarer Luxury Winter Present are opened for random festive loot.
- **Boss figurines and trinkets.** Halloween sells the Spookaveling, Pumpking Caveling and Haunted Hive Mother figurines as display pieces.

Once the event ends, the merchant packs up and the stock disappears. Items you have already bought or crafted stay in your storage forever.

## Little Helperlings

During Christmas specifically, the merchant's arrival is paired with **Little Helperlings** — small companions that you feed cooked food. In return, they craft presents for you. They are part of the Christmas window and leave when the event does.

## Practical tips

- **Craft the Calendar early, even before the event.** It is a Carpenter's Table recipe, so it costs nothing to have it ready on a wall the moment the dates roll over.
- **Farm currency in familiar biomes.** Themed mobs are reskins, not new AI — bring your usual AoE weapon and work through areas you already know.
- **Buy the workbench first.** It costs only a handful of Cookies & Milk (5 for Christmas) and unlocks the entire craftable set. Everything else should come after.
- **Keep storage space clear.** Event food, décor and presents pile up fast. A dedicated chest labelled with the event name makes post-event sorting painless.
- **Use the season override for catch-up.** If you missed Valentine's four-day window, flip the override in Settings → Gameplay and farm the merchant on demand. See [Seasonal Events](/wiki/seasonal/) for the full override list.

## FAQ

**Do I need to be online for the Seasonal Merchant to arrive?** The event is driven by the real-world date, but the merchant lives in your world. You must load a world where the Calendar is hung in a suitable room — an offline title screen will not work.

**What happens to the merchant when the event ends?** They leave and take their stock with them. The Calendar remains on your wall, but it does nothing until the next celebration or an override.

**Can I buy event items with gold?** No. Every purchase costs event-specific drops (Cookies & Milk for Christmas, etc.). Gold spent during the window is irrelevant to the merchant.

**Do the event currency items expire?** Cookies & Milk and similar drops stay in your inventory after the event ends, but the merchant that accepts them is gone. Hold onto them until the next Christmas — they will be valid again.

**Is the Seasonal Merchant different on a dedicated server?** Mechanically no, but the host's server decides which event is active. Passing `-season Christmas` (or Halloween, Easter, Valentine, None) overrides the calendar and lets you run any celebration year-round.

{{< version-note >}}
