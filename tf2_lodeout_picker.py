import random
from db_tf2_lodeout_picker import (PR_WEAPON, SE_WEAPON, AT_WEAPON,)

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

print(f"This is your primary weapon {prw} using the {prw_sc} scope and these two upgrades {prw_up1}, {prw_up2}!!!")
