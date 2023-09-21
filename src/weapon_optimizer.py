<<<<<<< Updated upstream
weapon_name = "Clayman's Keen Harpoon +25"
weapon_id = 16030200
reinforce_type_id = 225
base_phys_weapon = 95
base_magic_weapon = 51
base_fire_weapon = 0
base_lightning_weapon = 0
base_holy_weapon = 0
base_str_scaling = 19
base_dex_scaling = 45
base_int_scaling = 19
base_fai_scaling = 0
base_arc_scaling = 0
reinforce_param_weapon_phys = 2.35
reinforce_param_weapon_magic = 2.35
reinforce_param_weapon_fire = 2.35
reinforce_param_weapon_lightning = 2.35
reinforce_param_weapon_holy = 2.35
reinforce_param_scaling_str = 1.3
reinforce_param_scaling_dex = 2.8
reinforce_param_scaling_int = 1.8
reinforce_param_scaling_fai = 1.8
reinforce_param_scaling_arc = 1.8
calc_correct_id_phys = 2
calc_correct_id_magic = 4
calc_correct_id_fire = 0
calc_correct_id_lightning = 0
calc_correct_id_holy = 0
attack_element_correct_id = 10000

PLAYER_STATS = ['str', 'dex', 'int', 'fai', 'arc']
DMG_TYPES = ['phys', 'magic', 'fire', 'lightning', 'holy']

player_stats = {
    'str': None,
    'dex': None,
    'int': None,
    'fai': None,
    'arc': None,
} # TODO: Get user input and make these not be None anymore



CalcCorrectGraph = {
    '0': {'stat': [1, 18, 60, 80, 150],
          'grow': [0, 25, 75, 90, 110],
          'exponent': [1.2, -1.2, 1, 1, 1]}, #weapon scaling default
    '1': {'stat': [1, 20, 60, 80, 150],
          'grow': [0, 35, 75, 90, 110],
          'exponent': [1.2, -1.2, 1, 1, 1]}, #weapon scaling heavy
    '2': {'stat': [1, 20, 60, 80, 150],
          'grow': [0, 35, 75, 90, 110],
          'exponent': [1.2, -1.2, 1, 1, 1]}, #weapon scaling keen
    '4': {'stat': [1, 20, 50, 80, 99],
          'grow': [0, 40, 80, 95, 100],
          'exponent': [1, 1, 1, 1, 1]}, #weapon scaling elemental (magic, fire, lightning, holy)
    '7': {'stat': [1, 20, 60, 80, 150],
          'grow': [0, 35, 75, 90, 110],
          'exponent': [1.2, -1.2, 1, 1, 1]}, #weapon scaling occult
    '8': {'stat': [1, 16, 60, 80, 150],
          'grow': [0, 25, 75, 90, 110],
          'exponent': [1.2, -1.2, 1, 1, 1]} #weapon scaling quality
          }

AttackElementCorrectParam = {
    '10000': {'str': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': True,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': True,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': False,
                'magic': False,
                'fire': True,
                'lightning': False,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '10005': {'str': {
                'phys': True,
                'magic': False,
                'fire': True,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': True,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': True,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '10013': {'str': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': True,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': True,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': False,
                'magic': False,
                'fire': True,
                'lightning': False,
                'holy': True,
              },
              'arc': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '10100': {'str': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': True,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': True,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': False,
                'magic': False,
                'fire': True,
                'lightning': False,
                'holy': True,
              },
              'arc': {
                'phys': True,
                'magic': True,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '12000': {'str': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': True,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': True,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': False,
                'magic': False,
                'fire': True,
                'lightning': False,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '12005': {'str': {
                'phys': True,
                'magic': False,
                'fire': True,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': True,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': True,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '20000': {'str': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'int': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'fai': {
                'phys': True,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '20010': {'str': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'int': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'fai': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '20020': {'str': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '20030': {'str': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'int': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'fai': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'arc': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
            },
    '30000': {'str': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '30010': {'str': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'int': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'fai': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '30020': {'str': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
                },
              'dex': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            },
    '30030': {'str': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
                },
              'dex': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'int': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
              'fai': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'arc': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
            },
    '30040': {'str': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
                },
              'dex': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'int': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'fai': {
                'phys': True,
                'magic': True,
                'fire': True,
                'lightning': True,
                'holy': True,
              },
              'arc': {
                'phys': False,
                'magic': False,
                'fire': False,
                'lightning': False,
                'holy': False,
              },
            }#Frenzied Flame Seal
        }

CALC_CORRECT_DICT = {
    '16030200': {
        'phys': 2,
        'magic': 4,
        'fire': 0,
        'lightning': 0,
        'holy': 0,
    }
}

WeaponDamage = {
    '16030200': {
        'phys': 95,
        'magic': 51,
        'fire': 0,
        'lightning': 0,
        'holy': 0,
    }
}

WeaponScaling = {
    '16030200': {
        'str': 19,
        'dex': 45,
        'int': 19,
        'fai': 0,
        'arc': 0,
    }
}

ReinforceParamWeaponDamage = {
    '225': {
        'weapon_phys': 2.35,
        'weapon_magic': 2.35,
        'weapon_fire': 2.35,
        'weapon_lightning': 2.35,
        'weapon_holy': 2.35,
    }
}

ReinforceParamWeaponScaling = {
    '225': {
        'scaling_str': 1.3,
        'scaling_dex': 2.8,
        'scaling_int': 1.8,
        'scaling_fai': 1.8,
        'scaling_arc': 1.8,
    }
}


#weapon upgrades component
def base_damage_reinforcement(weapon_id, reinforce_type_id):
    reinforce_base_damage = {}

    for key in list(WeaponDamage[weapon_id].keys()):
      reinforce_base_damage[key] = WeaponDamage[weapon_id][key] * ReinforceParamWeaponDamage[reinforce_type_id]["weapon_" + key]

    return reinforce_base_damage


#weapon inherent scaling component
def base_scaling_reinforcement(weapon_id, reinforce_type_id):
    reinforce_base_scaling = {}

    for key in list(WeaponScaling[weapon_id].keys()):
      reinforce_base_scaling[key] = (WeaponScaling[weapon_id][key] * ReinforceParamWeaponScaling[reinforce_type_id]["scaling_" + key]) / 100

    return reinforce_base_scaling


#player scaling / softcap component
def player_scaling_multiplier(attack_element_correct_id, weapon_id, player):
    result = {}

    for char_attr in AttackElementCorrectParam[attack_element_correct_id]:
        result[char_attr] = {}
        for dmg_type, val in AttackElementCorrectParam[attack_element_correct_id][char_attr].items():
            if val:
                # TODO: Instead of calc_correct_id_phys, we need to make some kind of dictionary called something like calc_correct_id that has another nested dict inside it; the nested dict should have keys that are damage types and values that are the numbers for a specific weapon. You might need to essentially parse the whole spreadsheet to get this and then filter in only the relevant numbers
                tmp = CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['stat'].copy()
                tmp.append(player[char_attr])
                tmp = sorted(tmp)
                # tmp now contains the player attribute, along with all of the values from CalcCorrectGraph's "stat" block for this id
                idx = tmp.index(player[char_attr])
                ratio = (player[char_attr] - CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['stat'][idx - 1]) / (CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['stat'][idx] - CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['stat'][idx - 1])

                if CalcCorrectGraph[str(CALC_CORRECT_DICT[str(weapon_id)][dmg_type])]['exponent'][idx - 1] < 0:
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


    # and then multiply them by the weapon dmg

###

def combined_calc(base_damage_reinforcement, base_scaling_reinforcement, player_scaling_multiplier):
    result = {}
    for dmg_type in DMG_TYPES:
        dmg_type_val = 0
        for char_attr in PLAYER_STATS:
            dmg_type_val += (base_damage_reinforcement[dmg_type] * base_scaling_reinforcement[char_attr] * player_scaling_multiplier[char_attr][dmg_type])
        result[dmg_type] = dmg_type_val
    return result

#Putting it together
def main():
  damage_type_ar = {}

  for dmg_type, val in AttackElementCorrectParam[attack_element_correct_id][char_attr].items():
      if val:
        final_damage = reinforce_base_damage[dmg_type] * (reinforce_base_scaling[char_attr] / 100) * player_scaling_multiplier[char_attr]
      else:
          damage_type_ar[dmg_type] = 0




      final_magic_damage = scaled_magic_weapon
      final_fire_damage = scaled_fire_weapon
      final_lightning_damage = scaled_lightning_weapon
      final_holy_damage = scaled_holy_weapon




      attack_rating = final_phys_damage + final_magic_damage + final_fire_damage + final_lightning_damage + final_holy_damage
      return attack_rating

if __name__ == '__main__':
    main()
