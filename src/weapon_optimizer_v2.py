from data_puller import *
from AttackElementCorrectParam import AttackElementCorrectParam
from CalcCorrectGraph import CalcCorrectGraph
from player_stats import *

PLAYER_STATS = ['str', 'dex', 'int', 'fai', 'arc']
DMG_TYPES = ['phys', 'magic', 'fire', 'lightning', 'holy']


ReinforceParamWeaponDamage, ReinforceParamWeaponScaling, weapon_id_to_reinforce_type_id = get_reinforce_data()
WeaponDamage, weapon_names_map, WeaponScaling, attack_element_correct_id_dict = get_raw_data()
CALC_CORRECT_DICT = get_weapon_calc_correct_id()

#weapon upgrades component
def base_damage_reinforcement(weapon_id):
    reinforce_base_damage = {}
    reinforce_type_id = weapon_id_to_reinforce_type_id[weapon_id]

    for key in list(WeaponDamage[weapon_id].keys()):
      reinforce_base_damage[key] = WeaponDamage[str(weapon_id)][key] * ReinforceParamWeaponDamage[str(reinforce_type_id)]["weapon_" + key]

    return reinforce_base_damage


#weapon inherent scaling component
def base_scaling_reinforcement(weapon_id):
    reinforce_base_scaling = {}
    reinforce_type_id = weapon_id_to_reinforce_type_id[weapon_id]

    for key in list(WeaponScaling[weapon_id].keys()):
      reinforce_base_scaling[key] = (WeaponScaling[str(weapon_id)][key] * ReinforceParamWeaponScaling[str(reinforce_type_id)]["scaling_" + key]) / 100

    return reinforce_base_scaling


#player scaling / softcap component
def player_scaling_multiplier(weapon_id, player):
    attack_element_correct_id = attack_element_correct_id_dict[weapon_id]
    result = {}

    for char_attr in AttackElementCorrectParam[attack_element_correct_id]:
        result[char_attr] = {}
        for dmg_type, val in AttackElementCorrectParam[attack_element_correct_id][char_attr].items():
            if val:
                # TODO: Instead of calc_correct_id_phys, we need to make some kind of dictionary called something like calc_correct_id that has another nested dict inside it; the nested dict should have keys that are damage types and values that are the numbers for a specific weapon. You might need to essentially parse the whole spreadsheet to get this and then filter in only the relevant numbers
                tmp = CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['stat'].copy()
                orig_len = len(tmp)
                tmp.append(player[char_attr])
                tmp = sorted(tmp)
                # tmp now contains the player attribute, along with all of the values from CalcCorrectGraph's "stat" block for this id
                idx = tmp.index(player[char_attr])
                
                # In case our player's value is the largest thing in this array, its index will be out of range when we check after my weird sort maneuver
                # So therefore just pick the biggest value
                if idx == orig_len:
                    idx -= 1
                
                ratio = (player[char_attr] - CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['stat'][idx - 1]) / (CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['stat'][idx] - CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['stat'][idx - 1])

                if CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['exponent'][idx - 1] > 0:
                    growth = ratio ** CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['exponent'][idx - 1]
                else:
                    growth = 1 - ((1 - ratio) ** abs(CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['exponent'][idx - 1]))

                output = CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['grow'][idx - 1] + ((CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['grow'][idx] - CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['grow'][idx - 1]) * growth)

                if dmg_type in list(result[char_attr].keys()):
                    result[char_attr][dmg_type] += output
                else:
                    result[char_attr][dmg_type] = output
            else:
                if dmg_type not in list(result[char_attr].keys()):
                    result[char_attr][dmg_type] = 0

    for _k, v in result.items():
        for subk in list(v.keys()):
            v[subk] = v[subk]/100

    return result

"""
output_values will look like this when it's full:
{
  'str': {
    'phys': 0,
    'magic': 30,
    ...
  },
  'dex': {
    'phys': 14,
    'magic': 108,
    ...
  }
  ...
}
"""


def combined_calc(base_damage_reinforcement, base_scaling_reinforcement, player_scaling_multiplier):
    result = []
    for dmg_type in DMG_TYPES:
        for char_attr in PLAYER_STATS:
            dmg_type_val = (base_damage_reinforcement[dmg_type] * base_scaling_reinforcement[char_attr] * player_scaling_multiplier[char_attr][dmg_type])
            result.append(dmg_type_val)
        result.append(base_damage_reinforcement[dmg_type])
    return int(sum(result))

def main():
    player_stats = get_player_stats()

    comp = {}
    for weapon_id in WeaponDamage.keys():
        # Skip weapons whose CalcCorrectGraph values are greater than 8
        if any([(int(x) > 8) for x in CALC_CORRECT_DICT[str(weapon_id)].values()]):
            continue
        bdr = base_damage_reinforcement(weapon_id)
        bsr = base_scaling_reinforcement(weapon_id)
        psm = player_scaling_multiplier(weapon_id, player_stats)
        ar = combined_calc(bdr, bsr, psm)
        comp[weapon_id] = ar

    highest_dmg = max(comp.values())
    
    best_weapons = []
    for k,v in comp.items():
        if v == highest_dmg:
            best_weapons.append(k)

    for weapon in best_weapons:
        print(weapon_names_map[str(weapon)])
        
if __name__ == '__main__':
    main()
