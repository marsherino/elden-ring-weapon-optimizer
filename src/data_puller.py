import os
from os.path import normpath
import csv
### define a function that opens up the two csv files, one function for each dictionary, and they parse stuff
### goal: get data in the same format that it's in in the weapon_optimizer file lns. 608-656
### rename the csv files to something normal - this saves a lot of effort

def get_weapon_damage():
  WeaponDamage = {}
  path = normpath(os.path.join(os.getcwd(), "static/elden_ring_raw_data.csv"))
  with open(path, 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for row in csvreader:
      WeaponDamage[row[0]] = {
        'phys': int(row[3]),
        'magic': int(row[4]),
        'fire': int(row[5]),
        'lightning': int(row[6]),
        'holy': int(row[7])
        }
  return WeaponDamage

def get_weapon_names_map():
  ret = {}
  path = normpath(os.path.join(os.getcwd(), "static/elden_ring_raw_data.csv"))
  with open(path, 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for row in csvreader:
      ret[row[0]] = row[1]
  return ret

def get_weapon_scaling():
  WeaponScaling = {}
  path = normpath(os.path.join(os.getcwd(), "static/elden_ring_raw_data.csv"))
  with open(path, 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for row in csvreader:
      WeaponScaling[row[0]] = {
        'str': float(row[9]),
        'dex': float(row[10]),
        'int': float(row[11]),
        'fai': float(row[12]),
        'arc': float(row[13])
        }
  return WeaponScaling

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

def get_reinforce_param_weapon_damage():
  ReinforceParamWeaponDamage = {}
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
        if 1999 < int(row[2]) < 3000:
          ParamRow = int(row[2])+10
        else:
          ParamRow = int(row[2])+25
        for param_row in params_list:
          if int(param_row[0]) == ParamRow:
            ReinforceParamWeaponDamage[str(ParamRow)] = {
              'weapon_phys': float(param_row[1]),
              'weapon_magic': float(param_row[2]),
              'weapon_fire': float(param_row[3]),
              'weapon_lightning': float(param_row[4]),
              'weapon_holy': float(param_row[5]),
            }

    return ReinforceParamWeaponDamage

def get_reinforce_param_weapon_scaling():
  ReinforceParamWeaponScaling = {}
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
        if 1999 < int(row[2]) < 3000:
          ParamRow = int(row[2])+10
        else:
          ParamRow = int(row[2])+25
        for param_row in params_list:
          if int(param_row[0]) == ParamRow:
            ReinforceParamWeaponScaling[str(ParamRow)] = {
              'scaling_str': float(param_row[7]),
              'scaling_dex': float(param_row[8]),
              'scaling_int': float(param_row[9]),
              'scaling_fai': float(param_row[10]),
              'scaling_arc': float(param_row[11]),
            }
    return ReinforceParamWeaponScaling

def get_weapon_id_to_reinforce_type_id():
  ret = {}
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
        if 1999 < int(row[2]) < 3000:
          ParamRow = int(row[2])+10
        else:
          ParamRow = int(row[2])+25
        ret[row[0]] = ParamRow
  return ret

def get_attack_element_correct_id():
  attack_element_correct_id = {}
  path = normpath(os.path.join(os.getcwd(), "static/elden_ring_raw_data.csv"))
  with open(path, 'r') as f:
    csvreader = csv.reader(f)
    next(csvreader)
    for row in csvreader:
      attack_element_correct_id[row[0]] = row[26]
  return attack_element_correct_id
