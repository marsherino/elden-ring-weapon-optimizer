import os
from os.path import normpath
import csv
### define a function that opens up the two csv files, one function for each dictionary, and they parse stuff
### goal: get data in the same format that it's in in the weapon_optimizer file lns. 608-656
### rename the csv files to something normal - this saves a lot of effort

DOES_NOT_SCALE_UP = [3000]
ONLY_GOES_TO_FIVE = [4500, 4600]
ONLY_GOES_TO_TEN = [2200, 2400, 2500, 2600, 2700, 2800, 3200, 3300, 4000, 4100, 6100, 6200, 6300, 7000, 8300, 8500, 9000]

def get_raw_data():
  weapon_damage = {}
  weapon_names_map = {}
  weapon_scaling = {}
  attack_element_correct_id = {}
  weapon_minimums = {}
  weapon_weight = {}
  path = normpath(os.path.join(os.getcwd(), "static/elden_ring_raw_data.csv"))
  with open(path, 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for row in csvreader:
      weapon_damage[row[0]] = {
        'phys': int(row[3]),
        'magic': int(row[4]),
        'fire': int(row[5]),
        'lightning': int(row[6]),
        'holy': int(row[7])
        }
      weapon_scaling[row[0]] = {
        'str': float(row[9]),
        'dex': float(row[10]),
        'int': float(row[11]),
        'fai': float(row[12]),
        'arc': float(row[13])
        }
      weapon_minimums[row[0]] = {
        'str': int(row[29]),
        'dex': int(row[30]),
        'int': int(row[31]),
        'fai': int(row[32]),
        'arc': int(row[33]),
      }
      weapon_names_map[row[0]] = row[1]
      attack_element_correct_id[row[0]] = row[26]
      weapon_weight[row[0]] = int(row[37])
  return weapon_damage, weapon_names_map, weapon_scaling, attack_element_correct_id, weapon_weight, weapon_minimums

def get_weapon_calc_correct_id():
  CALC_CORRECT_DICT = {}
  path = normpath(os.path.join(os.getcwd(), "static/elden_ring_calc_correct_id.csv"))
  with open(path, 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for row in csvreader:
      CALC_CORRECT_DICT[row[0]] = {
        'phys': int(row[2]),
        'magic': int(row[3]),
        'fire': int(row[4]),
        'lightning': int(row[5]),
        'holy': int(row[6])
        }
    return CALC_CORRECT_DICT

def get_reinforce_data():
  ReinforceParamWeaponDamage = {}
  ReinforceParamWeaponScaling = {}
  reinforce_type_id = {}
  fpath = normpath(os.path.join(os.getcwd(), "static/elden_ring_raw_data.csv"))
  gpath = normpath(os.path.join(os.getcwd(), "static/elden_ring_reinforce_param_weapon.csv"))
  with open(fpath, 'r') as f:
    with open(gpath, 'r') as g:
      csvreader = csv.reader(f)
      next(csvreader)
      paramreader = csv.reader(g)
      params_list = list(paramreader)
      params_list = params_list[1:]
      for row in csvreader:
        if int(row[2]) in ONLY_GOES_TO_TEN:
          ParamRow = int(row[2])+10
        elif int(row[2]) in ONLY_GOES_TO_FIVE:
          ParamRow = int(row[2])+5
        elif int(row[2]) in DOES_NOT_SCALE_UP:
          ParamRow = int(row[2])
        else:
          ParamRow = int(row[2])+25

        reinforce_type_id[row[0]] = ParamRow

        for param_row in params_list:
          if int(param_row[0]) == ParamRow:
            ReinforceParamWeaponDamage[str(ParamRow)] = {
              'weapon_phys': float(param_row[1]),
              'weapon_magic': float(param_row[2]),
              'weapon_fire': float(param_row[3]),
              'weapon_lightning': float(param_row[4]),
              'weapon_holy': float(param_row[5]),
            }
            ReinforceParamWeaponScaling[str(ParamRow)] = {
              'scaling_str': float(param_row[7]),
              'scaling_dex': float(param_row[8]),
              'scaling_int': float(param_row[9]),
              'scaling_fai': float(param_row[10]),
              'scaling_arc': float(param_row[11]),
            }

    return ReinforceParamWeaponDamage, ReinforceParamWeaponScaling, reinforce_type_id

