import random

# list of weapons

pr_weapon = ['kraber',]
se_weapon = ['sweapon1', 'sweapon2', 'sweapon3']
at_weapon = ['atweapon1', 'atweapon2', 'atweapon3']

# common upgrades

COMMON_SCOPES = [
    "Holographic Sight",
    "HCOG Sight",
    "Threat Scope (Digital/Thermal)",
    "AOG Scope (Mid-range)",
    "Default Iron Sights"
]

COMMON_SNIPER_SCOPES = [
    "Variable Zoom Scope",
    "HCOG Sight",
    "Threat Scope (Digital/Thermal)",
    "Default Iron Sights"
]

COMMON_UPGRADES_MODS = [
    "Extended Magazine",
    "Speedloader",
    "Gunrunner (Movement while Aiming)",
    "Quick Swap",
    "Extra Ammo"
]

prw = random.choice(pr_weapon)

if prw == 'kraber':
    prw_sc = random.choice(COMMON_SNIPER_SCOPES)
    prw_up1 = random.choice(COMMON_UPGRADES_MODS)
    COMMON_UPGRADES_MODS.remove(prw_up1)
    prw_up2 = random.choice(COMMON_UPGRADES_MODS)


print(f"This is your primary weapon {prw} using {prw_sc}, {prw_up1} and {prw_up2}")

sew = random.choice(se_weapon)
print(f"This is your secoundary weapon {sew}")

atw = random.choice(at_weapon)
print(f"This is your Anti-titant weapon {atw}")
