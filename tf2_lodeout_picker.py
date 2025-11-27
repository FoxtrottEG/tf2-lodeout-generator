import random
from db_tf2_lodeout_picker import (TACTICAL, PR_WEAPON, SA_WEAPON, AT_WEAPON, BOOSTS, ORDINANCE, KIT1, KIT2)

# select pilot kit
tact = random.choice(TACTICAL)

# selection primary
PR_WEAPONS_NAMES = list(PR_WEAPON.keys())
prw = random.choice(PR_WEAPONS_NAMES)

PR_WEAPONS_DETAILS = (PR_WEAPON[prw])
SCOPE_List = PR_WEAPONS_DETAILS['scopes']
prw_sc = random.choice(SCOPE_List)

PR_WEAPONS_DETAILS = (PR_WEAPON[prw])
UPGRADES_List = PR_WEAPONS_DETAILS['upgrades']
prw_up1 = random.choice(UPGRADES_List)
UPGRADES_List.remove(prw_up1)

UPGRADES_List = PR_WEAPONS_DETAILS['upgrades']
prw_up2 = random.choice(UPGRADES_List)

# selection secoundary
SA_WEAPONS_NAMES = list(SA_WEAPON.keys())
saw = random.choice(SA_WEAPONS_NAMES)

SA_WEAPONS_DETAILS = (SA_WEAPON[saw])
UPGRADES_List = SA_WEAPONS_DETAILS['upgrades']
saw_up1 = random.choice(UPGRADES_List)
UPGRADES_List.remove(saw_up1)

UPGRADES_List = SA_WEAPONS_DETAILS['upgrades']
saw_up2 = random.choice(UPGRADES_List)

# selection anti-titan
AT_WEAPON_NAMES = list(AT_WEAPON.keys())
atw = random.choice(AT_WEAPON_NAMES)

AT_WEAPONS_DETAILS = (AT_WEAPON[atw])
UPGRADES_List = AT_WEAPONS_DETAILS['upgrades']
atw_up1 = random.choice(UPGRADES_List)
UPGRADES_List.remove(atw_up1)

UPGRADES_List = AT_WEAPONS_DETAILS['upgrades']
atw_up2 = random.choice(UPGRADES_List)

# selects ordinance
ord = random.choice(ORDINANCE)

# select boost
boost = random.choice(BOOSTS)

# select kits
kit1 = random.choice(KIT1)
kit2 = random.choice(KIT2)

print(f"  === Tactical ===")
print(f"Pilot-Tactical: {tact}")

print(f"  === Primary ===")
print(F"Gun: {prw}")
print(f"Scope: {prw_sc}")
print(f"Upgrade-1: {prw_up1}")
print(f"Upgrade-2: {prw_up2}")

print(f"  === Secoundary ===")
print(f"Gun: {saw}")
print(f"Upgrade-1: {saw_up1}")
print(f"Upgrade-2: {saw_up2}")

print(f"  === Anti-Titan ===")
print(f"Gun: {atw}")
print(f"Upgrade-1: {atw_up1}")
print(f"Upgrade-2: {atw_up2}")

print(f"  === Ordinance ===")
print(f"Ordinance: {ord}")

print(f"  === Boost ===")
print(f"Boost: {boost}")

print(f"  === Kits ===")
print(f"Kit-1: {kit1}")
print(f"Kit-2:{kit2}")
