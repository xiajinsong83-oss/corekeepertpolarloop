#!/usr/bin/env python3
"""
Idempotent generator for creatures/biomes detail pages.

Reads data/creatures.yaml and data/biomes.yaml, then writes a Hugo leaf page
under content/database/<creatures|biomes>/<slug>.md for every entry whose page
does NOT already exist. Existing hand-written pages are never overwritten, so
re-running this script is safe (idempotent).

Frontmatter `key` must match the YAML `name` character-for-character because the
layouts match on that key. Icons must already exist under static/img/app-icons/.
"""

import os
import re

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
CONTENT_DIR = os.path.join(ROOT, "content", "database")
UPDATED = "2026-10-18"

# Explicit slug overrides (auto-derivation would otherwise append "Biome" or
# keep "The" in some cases). Only new entries are listed here.
SLUG_OVERRIDES = {
    "Caveling Skirmisher": "caveling-skirmisher",
    "Caveling Gardener": "caveling-gardener",
    "Caveling Assassin": "caveling-assassin",
    "Caveling Scholar": "caveling-scholar",
    "Core Sentry": "core-sentry",
    "Red Slime": "red-slime",
    "Purple Slime": "purple-slime",
    "Larva Hive Biome": "larva-hive",
    "Mold Biome": "mold",
    "Forlorn Metropolis": "forlorn-metropolis",
    "Molten Quarry": "molten-quarry",
    "The Shimmering Frontier": "shimmering-frontier",
    "Breaker's Reach": "breakers-reach",
}

# Entries that already existed in the YAML before this expansion. Their pages
# are either hand-written (caveling.md, clay-caves.md, the-undergrounds.md, ...)
# — never auto-generate stubs for them. The remaining original ring biomes
# (forgotten-ruins.md, great-wall.md, ...) now get pages via this script.
NO_AUTOGEN = {
    # original 6 creatures (hand-written pages exist)
    "Caveling", "Caveling Brute", "Caveling Shaman", "Larva", "Mold Slime",
    "Geobot Miner",
    # ring biomes that already have hand-written pages
    "The Undergrounds", "The Clay Caves",
}

# Icon overrides: these YAML entries reference legacy biome-*.png files that do
# not exist in the repo. Point their generated pages at a safe, existing icon.
ICON_OVERRIDES = {
    "The Forgotten Ruins": "/img/app-icons/biomes.png",
    "The Great Wall": "/img/app-icons/biomes.png",
    "Azeos' Wilderness": "/img/app-icons/biomes.png",
    "The Sunken Sea": "/img/app-icons/biomes.png",
    "The Desert of Beginnings": "/img/app-icons/biomes.png",
    "The Passage": "/img/app-icons/biomes.png",
}

# Short 1-3 sentence intro blurbs per entry name.
BLURBS = {
    "Caveling Skirmisher": (
        "The **Caveling Skirmisher** is a ranged mob of The Clay Caves that hurls "
        "spears on sight from Clay Moss tiles. Weaker than melee cavelings but "
        "annoying at range, it drops Larva Meat and Fiber when farmed."
    ),
    "Caveling Gardener": (
        "The **Caveling Gardener** patrols Azeos' Wilderness on Lush Moss, circling "
        "players before striking. While standing on grass it can sprout up to five "
        "Snare Plants that trap you in place."
    ),
    "Caveling Assassin": (
        "The **Caveling Assassin** is a fast Desert caveling that fires a spread of "
        "three daggers and then dashes straight through its target. Its high speed "
        "and pass-through movement make it hard to pin down."
    ),
    "Caveling Scholar": (
        "The **Caveling Scholar** appears in Forlorn Metropolis dungeons, firing a "
        "Scholar's Staff at range and beaming heals onto nearby Scholars and Core "
        "Sentries. Take them out first or the whole room will sustain itself."
    ),
    "Core Sentry": (
        "The **Core Sentry** is a large Forlorn Metropolis construct that stays "
        "dormant until you approach, then powers up and stomps a three-way fork of "
        "bright projectiles. Very high health makes it a priority target."
    ),
    "Red Slime": (
        "The **Red Slime** is the always-aggressive early slime of The Undergrounds "
        "and The Clay Caves. Unlike the passive Orange Slime it shares Ground Slime "
        "with, it will hop onto you on sight and is immune to slow and acid."
    ),
    "Purple Slime": (
        "The **Purple Slime** is the poison slime of Azeos' Wilderness, spawning on "
        "Ground Poison Slime. Its jumps apply poison that cuts healing received by "
        "75%, so keep antidotes or a Remedaisy Necklace ready."
    ),
    "Larva Hive Biome": (
        "The **Larva Hive Biome** is a maze-like dungeon inside The Clay Caves, its "
        "walls made of tough organic Larva Hive Block. Slimes do not spawn here; "
        "instead Chrysalis and acid-laying larvae are everywhere, and The Hive "
        "Mother waits at its heart."
    ),
    "Mold Biome": (
        "The **Mold Biome** is a fungus-overrun dungeon embedded in Azeos' "
        "Wilderness. Mold Ground slows you by up to 75% at ten stacks, and the "
        "zombie-like Infected Cavelings plus stunning Mold Tentacles make it one of "
        "the hardest areas in the game."
    ),
    "Forlorn Metropolis": (
        "The **Forlorn Metropolis** is a ruined hi-tech dungeon scattered through "
        "The Sunken Sea. Caveling Scholars support the heavier Core Sentries here, "
        "and the ruins hold Octarine Ore and materials for the Phantom Spark."
    ),
    "Molten Quarry": (
        "The **Molten Quarry** is a volcanic sub-biome of The Desert of Beginnings, "
        "its blackened terrain split by lava and burning Ground Magma Slime. It is "
        "home to Igneous the Molten Mass and the Ancient Forge needed for the Soul "
        "Seeker Pickaxe."
    ),
    "The Shimmering Frontier": (
        "The **Shimmering Frontier** is a bright blue crystal ring wrapped around "
        "the outer biomes. It is the source of Solarite Ore, Gleam Wood and the "
        "colored gems, patrolled by Crystal Snails, Mimites and Orbital Turrets."
    ),
    "Breaker's Reach": (
        "**Breaker's Reach** is the mechanical, void-tainted late-game biome found "
        "far north past The Passage, added in the Void & Voltage update. It yields "
        "Relucite Ore and Corrupted Alloy and is overrun by Geobots and void "
        "cavelings."
    ),
    "The Forgotten Ruins": (
        "**The Forgotten Ruins** is the stone inner-ring biome opposite The Clay "
        "Caves, mined for Iron Ore and Gold Ore. Cavelings defend their settlements "
        "here on Stone Moss, and Malugaz the Corrupted is summoned in the throne "
        "room around 350 tiles from The Core."
    ),
    "The Great Wall": (
        "**The Great Wall** is an unbreakable wavy barrier spanning 450–520 tiles "
        "around the inner biomes. It gates access to the outer biomes until you "
        "have powered up The Core and unlocked the ability to break it down."
    ),
    "Azeos' Wilderness": (
        "**Azeos' Wilderness** is the lush forest outer-ring biome, mined for "
        "Scarlet Ore. Caveling Gardeners and Bush-disguised Caveling Hunters roam "
        "with Purple Slimes, Azeos the Sky Titan awaits ~600 tiles out, and Mold "
        "dungeons infect parts of it."
    ),
    "The Sunken Sea": (
        "**The Sunken Sea** is the water-filled outer biome of Beach Sand islands "
        "and glowing crystal water, mined for Octarine Ore. Tentacles, Blue Slimes "
        "and Bubble Crabs apply a slippery debuff, Omoroth lurks ~1100 tiles out, "
        "and Forlorn Metropolis dungeons sit among the islands."
    ),
    "The Desert of Beginnings": (
        "**The Desert of Beginnings** is the hot sandy outer-ring biome, mined for "
        "Galaxite Ore. Explosive Bomb Scarabs and swift Caveling Assassins patrol, "
        "Ra-Akar the Sand Titan waits ~1000 tiles out, and Molten Quarry and Oasis "
        "sub-biomes are hidden among the sandstone."
    ),
    "The Passage": (
        "**The Passage** is the outermost biome beyond the three outer rings, its "
        "fossil-block walls needing late-game mining gear. It yields Pandorium Ore "
        "and is home to Sulfur Worms and Urschleim, the optional late-game slime "
        "boss circling ~1250 tiles out."
    ),
}


def slugify(name: str) -> str:
    if name in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[name]
    s = name.lower().replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    s = re.sub(r"^the-", "", s)
    return s


def render(entry: dict, kind: str) -> str:
    name = entry["name"]
    icon = ICON_OVERRIDES.get(name, entry["icon"])
    blurb = BLURBS.get(
        name,
        f"The **{name}** is documented on the Core Keeper wiki. "
        f"{entry.get('note', '')}",
    )
    desc = f"Core Keeper {name} — stats, drops, spawn and tips."
    fm = (
        f'---\n'
        f'title: "{name}"\n'
        f'description: "{desc}"\n'
        f'icon: "{icon}"\n'
        f'key: "{name}"\n'
        f'updated: "{UPDATED}"\n'
        f'---\n\n'
        f'{blurb}\n\n'
        f'## Tips\n\n'
        f'- Data sourced from the Core Keeper wiki (atma.gg); numbers shift with patches\n'
        f'- Bring appropriate resistance gear before farming this area\n\n'
        f'{{{{< ad >}}}}\n'
    )
    return fm


def process(rel_data: str, rel_out: str, kind: str) -> list:
    with open(os.path.join(DATA_DIR, rel_data), "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    items = data[kind]
    out_dir = os.path.join(CONTENT_DIR, rel_out)
    created = []
    for entry in items:
        if entry["name"] in NO_AUTOGEN:
            continue
        slug = slugify(entry["name"])
        path = os.path.join(out_dir, f"{slug}.md")
        if os.path.exists(path):
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(render(entry, kind))
        created.append(f"{rel_out}/{slug}.md")
    return created


def main():
    creatures = process("creatures.yaml", "creatures", "creatures")
    biomes = process("biomes.yaml", "biomes", "biomes")
    print("Created creature pages:")
    for p in creatures:
        print("  ", p)
    print("Created biome pages:")
    for p in biomes:
        print("  ", p)
    if not creatures and not biomes:
        print("Nothing to do — all pages already exist.")


if __name__ == "__main__":
    main()
