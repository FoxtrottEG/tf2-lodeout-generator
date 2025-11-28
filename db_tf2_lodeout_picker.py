SCOPES = [
    "Holographic Sight",
    "HCOG Sight",
    "Threat Scope (Digital/Thermal)",
    "AOG Scope (Mid-range)",
    "Default Iron Sights"
]

SNIPER_SCOPES = [
    "Variable Zoom Scope",
    "HCOG Sight",
    "Threat Scope (Digital/Thermal)",
    "Default Iron Sights"
]

UPGRADES = [
    "Extended Magazine",
    "Speedloader",
    "Gunrunner",
    "Quick Swap",
    "Extra Ammo"
]

SECONDARY_UPGRADES = [
    "Extended Magazine",
    "Speedloader",
    "Quick Swap",
    "Extra Ammo"
]

AT_UPGRADES = [
    "Extra Ammo",
    "Speedloader",
    "Quick Swap"
]

TITANFALL_KIT = [
    "Dome Shield",
    "Warpfall"
]

TITAN_KIT = [
    "Assault Chip",
    "Stealth Auto-Eject",
    "Turbo Engine",
    "Overcore",
    "Nuclear Eject",
    "Counter Ready"
]

PR_WEAPON = {
    # ar
    "R-201 Carbine": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "Hemlok BF-R": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "G2A5": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },

    # smgs
    "C.A.R. SMG": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "Volt SMG": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "R-97 Compact SMG": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "Alternator SMG": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },

    # lmgs
    "Spitfire": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "L-STAR": {
        "scopes": SCOPES,
        "upgrades": ["Extended Magazine", "Speedloader", "Gunrunner", "Fast Reload"]
    },
    "Devotion": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },

    # shotguns
    "EVA-8 Auto": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "Mastiff Shotgun": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },

    # snipers
    "Kraber-AP": {
        "scopes": SNIPER_SCOPES,
        "upgrades": ["Extended Magazine", "Speedloader", "Extra Ammo", "Ricochet"]
    },
    "Double Take": {
        "scopes": SNIPER_SCOPES,
        "upgrades": ["Extended Magazine", "Speedloader", "Extra Ammo", "Ablative Rounds"]
    },
    "Longbow-DMR": {
        "scopes": SCOPES + ["Variable Zoom Scope"],
        "upgrades": UPGRADES
    },

    # grens
    "SMR (Sidewinder)": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "Cold War": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "Softball": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    "Epg-1": {
        "scopes": SCOPES,
        "upgrades": UPGRADES
    },
    #pistols
    #"Mozambique Shotgun": {
    #    "upgrades": SECONDARY_UPGRADES
    #},
    #"Wingman": {
    #    "upgrades": SECONDARY_UPGRADES
    #}
}

SA_WEAPON = {
    "RE-45 Auto Pistol": {
        "upgrades": SECONDARY_UPGRADES
    },
    "P2016": {
        "upgrades": SECONDARY_UPGRADES
    },
    "B3 Wingman Elite": {
        "upgrades": SECONDARY_UPGRADES
    }
}

AT_WEAPON = {
    "MGL Mag Launcher": {
        "upgrades": AT_UPGRADES + ["Extended Magazine"]
    },
    "Thunderbolt": {
        "upgrades": AT_UPGRADES
    },
    "Charge Rifle": {
        "upgrades": AT_UPGRADES + ["Extended Battery", "Charge Hack"]
    },
    "Archer Heavy Rocket": {
        "upgrades": AT_UPGRADES
    }
}

TACTICAL = [
    "Grapple",
    "Cloak",
    "Stim",
    "Holo",
    "A-Wall",
    "Pulse Blade"
]

BOOSTS = [
    "Amped Weapons",
    "Ticks",
    "Smart Pistol MK6",
    "Pilot Sentry",
    "Titan Sentry",
    "Battery Back-up",
    "Map Hack",
    "Radar Jammer",
    "Phase Rewind",
    "Hard Cover",
    "Holo Pilot Nova",
    "Dice Roll"
]

ORDINANCE = [
    "Frag Granade",
    "ARC Granade",
    "Satchel",
    "Fire Star",
    "Gravity Star"
]

KIT1 = [
    "Power Cell",
    "Phase Embark",
    "Ordinance Expert",
    "Fast Heal"
]
KIT2 = [
    "Wallhang",
    "Kill report",
    "Low Profile",
    "Hover",
    "Titan Hunter"
]

TITANS = {
    "Ion": {
        "titanfall_kit": TITANFALL_KIT,
        "titan_kit": TITAN_KIT,
        "special_kit": ["Entangled Energy", "Zero-Point Tripwire", "Vortex", "Amplifier", "Grand Cannon", "Refraction Lens"]
        },
    "Scorch": {
        "titanfall_kit": TITANFALL_KIT,
        "titan_kit": TITAN_KIT,
        "special_kit": ["Wildfire Laucher", "Tempted Plating", "Inferno shield", "Fuel the Fire", "Scorched Earth"],
        },
    "Northstar": {
        "titanfall_kit": TITANFALL_KIT,
        "titan_kit": TITAN_KIT,
        "special_kit": ["Piercing Shot", "Enhanced Payload", "Twin Traps", "Viper Thrusters", "Threat Optics"],
        },
    "Ronin": {
        "titanfall_kit": TITANFALL_KIT,
        "titan_kit": TITAN_KIT,
        "special_kit": ["Ricochet Rounds", "Thunderstorm", "Temporal Anomaly", "Highlander", "Phase Reflex"],
        },
    "Tone": {
        "titanfall_kit": TITANFALL_KIT,
        "titan_kit": TITAN_KIT,
        "special_kit": ["Enhanced Tracker Rounds", "Reinforced Partical Wall", "Pulse-Echo", "Rocket Barrage", "Burst Loader"],
        },
    "Legion": {
        "titanfall_kit": TITANFALL_KIT,
        "titan_kit": TITAN_KIT,
        "special_kit": ["Enhanced Ammo Capacity", "Sensor Array", "Bulwark", "Light-Weight Alloys", "Hidden Compartment"],
        },
    "Monarch": {
        "titanfall_kit": TITANFALL_KIT,
        "titan_kit": TITAN_KIT,
        "special_kit": ["Shield Amplifier", "Energy Thief", "Survival of the Fittest", "Rapid Rearm"],
        "monarch_core1": ["Arc Rounds", "Missile Racks", "Energy Transfer"],
        "monarch_core2": ["Rearm and Reload", "Maelstron", "Energy Field"],
        "monarch_core3": ["Multi-Target Missile System", "Superior Chassis", "XO-16 Accelerator"],
    }
}
