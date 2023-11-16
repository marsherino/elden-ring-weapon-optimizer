import csv
### define a function that opens up the two csv files, one function for each dictionary, and they parse stuff
### goal: get data in the same format that it's in in the weapon_optimizer file lns. 608-656
### rename the csv files to something normal - this saves a lot of effort

def get_weapon_damage():
  WeaponDamage = {}
  with open('elden_ring_raw_data.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
      WeaponDamage[row[0]] = {
        'phys': int(row[3]),
        'magic': int(row[4]),
        'fire': int(row[5]),
        'lightning': int(row[6]),
        'holy': int(row[7])
        }
  return WeaponDamage

def get_weapon_scaling():
  WeaponScaling = {}
  with open('elden_ring_reinforce_param_weapon.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
      WeaponScaling[row[0]] = {
        'str': int(row[9]),
        'dex': int(row[10]),
        'int': int(row[11]),
        'fai': int(row[12]),
        'arc': int(row[13])
        }
  return WeaponScaling

def get_weapon_calc_correct_id():
  CALC_CORRECT_DICT = {}
  with open('elden_ring_calc_correct_id.csv', 'r') as f:
    csvreader = csv.reader(f)
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
  with open('elden_ring_raw_data.csv', 'r') as f:
    with open('elden_ring_reinforce_param_weapon.csv', 'r') as g:
      csvreader = csv.reader(f)
      paramreader = csv.reader(g)
      for row in csvreader:
        if 1999 < int(row[2]) < 3000:
          ParamRow = int(row[2])+10
          paramreader = list(paramreader)
          ReinforceParamWeaponDamage[ParamRow] = {
            'weapon_phys': int(paramreader[ParamRow][1]),
            'weapon_magic': int(paramreader[ParamRow][2]),
            'weapon_fire': int(paramreader[ParamRow][3]),
            'weapon_lightning': int(paramreader[ParamRow][4]),
            'weapon_holy': int(paramreader[ParamRow][5]),
            }
        else:
          ParamRow = int(row[2])+25
          paramreader = list(paramreader)
          ReinforceParamWeaponDamage[ParamRow] = {
            'weapon_phys': int(paramreader[ParamRow][1]),
            'weapon_magic': int(paramreader[ParamRow][2]),
            'weapon_fire': int(paramreader[ParamRow][3]),
            'weapon_lightning': int(paramreader[ParamRow][4]),
            'weapon_holy': int(paramreader[ParamRow][5]),
            }
    return ReinforceParamWeaponDamage

def get_reinforce_param_weapon_scaling():
  ReinforceParamWeaponScaling = {}
  with open('elden_ring_raw_data.csv', 'r') as f:
    with open('elden_ring_reinforce_param_weapon.csv', 'r') as g:
      csvreader = csv.reader(f)
      paramreader = csv.reader(g)
      for row in csvreader:
        if 1999 < int(row[2]) < 3000:
          ParamRow = int(row[2])+10
          paramreader = list(paramreader)
          ReinforceParamWeaponScaling[ParamRow] = {
            'weapon_phys': int(paramreader[ParamRow][1]),
            'weapon_magic': int(paramreader[ParamRow][2]),
            'weapon_fire': int(paramreader[ParamRow][3]),
            'weapon_lightning': int(paramreader[ParamRow][4]),
            'weapon_holy': int(paramreader[ParamRow][5]),
            }
        else:
          ParamRow = int(row[2])+25
          paramreader = list(paramreader)
          ReinforceParamWeaponScaling[ParamRow] = {
            'weapon_phys': int(paramreader[ParamRow][7]),
            'weapon_magic': int(paramreader[ParamRow][8]),
            'weapon_fire': int(paramreader[ParamRow][9]),
            'weapon_lightning': int(paramreader[ParamRow][10]),
            'weapon_holy': int(paramreader[ParamRow][11]),
            }
    return ReinforceParamWeaponScaling
          
def get_attack_element_correct_id():
  attack_element_correct_id = {}
  with open('elden_ring_raw_data.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
      attack_element_correct_id[row[0]] = row[26]
  return attack_element_correct_id
