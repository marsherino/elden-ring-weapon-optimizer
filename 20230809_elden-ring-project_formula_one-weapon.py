weapon_name = "Clayman's Keen Harpoon +25"
weapon_id = 16030200
reinforce_type_id = 225
base_phys_weapon = 95
base_magic_weapon = 51
base_fire_weapon = 0
base_lightning_weapon = 0
base_holy_weapon = 0
reinforce_param_weapon_phys = 2.35
reinforce_param_weapon_magic = 2.35
reinforce_param_weapon_fire = 2.35
reinforce_param_weapon_lightning = 2.35
reinforce_param_weapon_holy = 2.35
calc_correct_id_phys = 2
calc_correct_id_magic = 4
calc_correct_id_fire = 0
calc_correct_id_lightning = 0
calc_correct_id_holy = 0
attack_element_correct_id = 10000

player_str = 
player_dex = 
player_int = 
player_fai = 
player_arc = 

CalcCorrectGraph = {
    '0': {'stat0': 1, 'stat1': 18, 'stat2': 60, 'stat3': 80, 'stat4': 150, 'grow0': 0, 'grow1': 25, 'grow2': 75, 'grow3': 90, 'grow4': 110, 'exponent0': 1.2, 'exponent1': -1.2, 'exponent2': 1, 'exponent3': 1, 'exponent4': 1}, #weapon scaling default
    '1': {'stat0': 1, 'stat1': 20, 'stat2': 60, 'stat3': 80, 'stat4': 150, 'grow0': 0, 'grow1': 35, 'grow2': 75, 'grow3': 90, 'grow4': 110, 'exponent0': 1.2, 'exponent1': -1.2, 'exponent2': 1, 'exponent3': 1, 'exponent4': 1}, #weapon scaling heavy
    '2': {'stat0': 1, 'stat1': 20, 'stat2': 60, 'stat3': 80, 'stat4': 150, 'grow0': 0, 'grow1': 35, 'grow2': 75, 'grow3': 90, 'grow4': 110, 'exponent0': 1.2, 'exponent1': -1.2, 'exponent2': 1, 'exponent3': 1, 'exponent4': 1}, #weapon scaling keen
    '4': {'stat0': 1, 'stat1': 20, 'stat2': 50, 'stat3': 80, 'stat4': 99, 'grow0': 0, 'grow1': 40, 'grow2': 80, 'grow3': 95, 'grow4': 100, 'exponent0': 1, 'exponent1': 1, 'exponent2': 1, 'exponent3': 1, 'exponent4': 1}, #weapon scaling elemental (magic, fire, lightning, holy)
    '7': {'stat0': 1, 'stat1': 20, 'stat2': 60, 'stat3': 80, 'stat4': 150, 'grow0': 0, 'grow1': 35, 'grow2': 75, 'grow3': 90, 'grow4': 110, 'exponent0': 1.2, 'exponent1': -1.2, 'exponent2': 1, 'exponent3': 1, 'exponent4': 1}, #weapon scaling occult
    '8': {'stat0': 1, 'stat1': 16, 'stat2': 60, 'stat3': 80, 'stat4': 150, 'grow0': 0, 'grow1': 25, 'grow2': 75, 'grow3': 90, 'grow4': 110, 'exponent0': 1.2, 'exponent1': -1.2, 'exponent2': 1, 'exponent3': 1, 'exponent4': 1}, #weapon scaling quality
}

AttackElementCorrectParam = {
    '10000': {'phys_str': True, 'phys_dex': True, 'phys_int': False, 'phys_fai': False, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': False, 'magic_arc': False, 'fire_str': False, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': True, 'lightning_int': False, 'lightning_fai': False, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': False},
    '10005': {'phys_str': True, 'phys_dex': True, 'phys_int': False, 'phys_fai': False, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': False, 'magic_arc': False, 'fire_str': True, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': False, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': True, 'lightning_int': False, 'lightning_fai': False, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': False},
    '10013': {'phys_str': True, 'phys_dex': True, 'phys_int': False, 'phys_fai': False, 'phys_arc': True, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': False, 'magic_arc': False, 'fire_str': False, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': True, 'lightning_int': False, 'lightning_fai': False, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': False},
    '10100': {'phys_str': True, 'phys_dex': True, 'phys_int': False, 'phys_fai': False, 'phys_arc': True, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': False, 'magic_arc': True, 'fire_str': False, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': True, 'fire_arc': True, 'lightning_str': False, 'lightning_dex': True, 'lightning_int': False, 'lightning_fai': False, 'lightning_arc': True, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': True},
    '12000': {'phys_str': True, 'phys_dex': True, 'phys_int': False, 'phys_fai': True, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': False, 'magic_arc': False, 'fire_str': False, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': True, 'lightning_int': False, 'lightning_fai': False, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': False},
    '12005': {'phys_str': True, 'phys_dex': True, 'phys_int': False, 'phys_fai': True, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': False, 'magic_arc': False, 'fire_str': True, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': False, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': True, 'lightning_int': False, 'lightning_fai': False, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': False},
    '20000': {'phys_str': False, 'phys_dex': False, 'phys_int': True, 'phys_fai': True, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': False, 'magic_arc': False, 'fire_str': False, 'fire_dex': False, 'fire_int': True, 
              'fire_fai': False, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': False, 'lightning_int': True, 'lightning_fai': False, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': True, 'holy_fai': False, 'holy_arc': False},
    '20010': {'phys_str': False, 'phys_dex': False, 'phys_int': True, 'phys_fai': True, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': True, 'magic_arc': False, 'fire_str': False, 'fire_dex': False, 'fire_int': True, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': False, 'lightning_int': True, 'lightning_fai': True, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': True, 'holy_fai': True, 'holy_arc': False},
    '20020': {'phys_str': False, 'phys_dex': False, 'phys_int': False, 'phys_fai': True, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': False, 'magic_fai': True, 'magic_arc': False, 'fire_str': False, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': False, 'lightning_int': False, 'lightning_fai': True, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': False},
    '20030': {'phys_str': False, 'phys_dex': False, 'phys_int': True, 'phys_fai': False, 'phys_arc': True, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': False, 'magic_arc': True, 'fire_str': False, 'fire_dex': False, 'fire_int': True, 
              'fire_fai': False, 'fire_arc': True, 'lightning_str': False, 'lightning_dex': False, 'lightning_int': True, 'lightning_fai': False, 'lightning_arc': True, 'holy_str': False, 'holy_dex': False, 'holy_int': True, 'holy_fai': False, 'holy_arc': True},
    '30000': {'phys_str': False, 'phys_dex': False, 'phys_int': False, 'phys_fai': True, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': False, 'magic_fai': True, 'magic_arc': False, 'fire_str': False, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': False, 'lightning_int': False, 'lightning_fai': True, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': False},
    '30010': {'phys_str': False, 'phys_dex': False, 'phys_int': True, 'phys_fai': True, 'phys_arc': False, 'magic_str': False, 'magic_dex': False, 'magic_int': True, 'magic_fai': True, 'magic_arc': False, 'fire_str': False, 'fire_dex': False, 'fire_int': True, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': False, 'lightning_dex': False, 'lightning_int': True, 'lightning_fai': True, 'lightning_arc': False, 'holy_str': False, 'holy_dex': False, 'holy_int': True, 'holy_fai': True, 'holy_arc': False},
    '30020': {'phys_str': True, 'phys_dex': False, 'phys_int': False, 'phys_fai': True, 'phys_arc': False, 'magic_str': True, 'magic_dex': False, 'magic_int': False, 'magic_fai': True, 'magic_arc': False, 'fire_str': True, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': True, 'lightning_dex': False, 'lightning_int': False, 'lightning_fai': True, 'lightning_arc': False, 'holy_str': True, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': False},
    '30030': {'phys_str': False, 'phys_dex': False, 'phys_int': False, 'phys_fai': True, 'phys_arc': True, 'magic_str': False, 'magic_dex': False, 'magic_int': False, 'magic_fai': True, 'magic_arc': True, 'fire_str': False, 'fire_dex': False, 'fire_int': False, 
              'fire_fai': True, 'fire_arc': True, 'lightning_str': False, 'lightning_dex': False, 'lightning_int': False, 'lightning_fai': True, 'lightning_arc': True, 'holy_str': False, 'holy_dex': False, 'holy_int': False, 'holy_fai': True, 'holy_arc': True},
    '30040': {'phys_str': True, 'phys_dex': True, 'phys_int': True, 'phys_fai': True, 'phys_arc': False, 'magic_str': True, 'magic_dex': True, 'magic_int': True, 'magic_fai': True, 'magic_arc': False, 'fire_str': True, 'fire_dex': True, 'fire_int': True, 
              'fire_fai': True, 'fire_arc': False, 'lightning_str': True, 'lightning_dex': True, 'lightning_int': True, 'lightning_fai': True, 'lightning_arc': False, 'holy_str': True, 'holy_dex': True, 'holy_int': True, 'holy_fai': True, 'holy_arc': False},
}

###

#weapon upgrades component
scaled_phys_weapon = base_phys_weapon * reinforce_param_weapon_phys
scaled_magic_weapon = base_magic_weapon * reinforce_param_weapon_magic
scaled_fire_weapon = base_fire_weapon * reinforce_param_weapon_fire
scaled_lightning_weapon = base_lightning_weapon * reinforce_param_weapon_lightning
scaled_holy_weapon = base_holy_weapon * reinforce_param_weapon_holy

#player stats component
#this is the bulk of the formula, including 25 iterations of damage type-stat values based on AttackElementCorrectParam. All of it is the same formula; only the variables are different.

#phys damage
if AttackElementCorrectParam[attack_element_correct_id]['phys_str'] is False:
    str_output = 0
else:
    if CalcCorrectGraph[calc_correct_id_phys]['stat0'] <= player_str < CalcCorrectGraph[calc_correct_id_phys]['stat1']:
        str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_phys]['stat0']) / (CalcCorrectGraph[calc_correct_id_phys]['stat1'] - CalcCorrectGraph[calc_correct_id_phys]['stat0'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent0'] < 0:
            str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent0']
        else:
            str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent0']))
        str_output = CalcCorrectGraph[calc_correct_id_phys]['grow0'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow1'] - CalcCorrectGraph[calc_correct_id_phys]['grow0']) * str_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat1'] <= player_str < CalcCorrectGraph[calc_correct_id_phys]['stat2']:
        str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_phys]['stat1']) / (CalcCorrectGraph[calc_correct_id_phys]['stat2'] - CalcCorrectGraph[calc_correct_id_phys]['stat1'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent1'] < 0:
            str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent1']
        else:
            str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent1']))
        str_output = CalcCorrectGraph[calc_correct_id_phys]['grow1'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow2'] - CalcCorrectGraph[calc_correct_id_phys]['grow1']) * str_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat2'] <= player_str < CalcCorrectGraph[calc_correct_id_phys]['stat3']:
        str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_phys]['stat2']) / (CalcCorrectGraph[calc_correct_id_phys]['stat3'] - CalcCorrectGraph[calc_correct_id_phys]['stat2'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent2'] < 0:
            str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent2']
        else:
            str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent2']))
        str_output = CalcCorrectGraph[calc_correct_id_phys]['grow2'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow3'] - CalcCorrectGraph[calc_correct_id_phys]['grow2']) * str_growth)
    else:
        str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_phys]['stat3']) / (CalcCorrectGraph[calc_correct_id_phys]['stat4'] - CalcCorrectGraph[calc_correct_id_phys]['stat3'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent3'] < 0:
            str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent3']
        else:
            str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent3']))
        str_output = CalcCorrectGraph[calc_correct_id_phys]['grow3'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow4'] - CalcCorrectGraph[calc_correct_id_phys]['grow3']) * str_growth)
if AttackElementCorrectParam[attack_element_correct_id]['phys_dex'] is False:
    dex_output = 0
else:
    if CalcCorrectGraph[calc_correct_id_phys]['stat0'] <= player_dex < CalcCorrectGraph[calc_correct_id_phys]['stat1']:
        dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_phys]['stat0']) / (CalcCorrectGraph[calc_correct_id_phys]['stat1'] - CalcCorrectGraph[calc_correct_id_phys]['stat0'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent0'] < 0:
            dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent0']
        else:
            dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent0']))
        dex_output = CalcCorrectGraph[calc_correct_id_phys]['grow0'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow1'] - CalcCorrectGraph[calc_correct_id_phys]['grow0']) * dex_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat1'] <= player_dex < CalcCorrectGraph[calc_correct_id_phys]['stat2']:
        dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_phys]['stat1']) / (CalcCorrectGraph[calc_correct_id_phys]['stat2'] - CalcCorrectGraph[calc_correct_id_phys]['stat1'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent1'] < 0:
            dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent1']
        else:
            dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent1']))
        dex_output = CalcCorrectGraph[calc_correct_id_phys]['grow1'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow2'] - CalcCorrectGraph[calc_correct_id_phys]['grow1']) * dex_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat2'] <= player_dex < CalcCorrectGraph[calc_correct_id_phys]['stat3']:
        dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_phys]['stat2']) / (CalcCorrectGraph[calc_correct_id_phys]['stat3'] - CalcCorrectGraph[calc_correct_id_phys]['stat2'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent2'] < 0:
            dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent2']
        else:
            dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent2']))
        dex_output = CalcCorrectGraph[calc_correct_id_phys]['grow2'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow3'] - CalcCorrectGraph[calc_correct_id_phys]['grow2']) * dex_growth)
    else:
        dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_phys]['stat3']) / (CalcCorrectGraph[calc_correct_id_phys]['stat4'] - CalcCorrectGraph[calc_correct_id_phys]['stat3'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent3'] < 0:
            dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent3']
        else:
            dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent3']))
        dex_output = CalcCorrectGraph[calc_correct_id_phys]['grow3'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow4'] - CalcCorrectGraph[calc_correct_id_phys]['grow3']) * dex_growth)
if AttackElementCorrectParam[attack_element_correct_id]['phys_int'] is False:
    int_output = 0
else:
    if CalcCorrectGraph[calc_correct_id_phys]['stat0'] <= player_int < CalcCorrectGraph[calc_correct_id_phys]['stat1']:
        int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_phys]['stat0']) / (CalcCorrectGraph[calc_correct_id_phys]['stat1'] - CalcCorrectGraph[calc_correct_id_phys]['stat0'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent0'] < 0:
            int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent0']
        else:
            int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent0']))
        int_output = CalcCorrectGraph[calc_correct_id_phys]['grow0'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow1'] - CalcCorrectGraph[calc_correct_id_phys]['grow0']) * int_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat1'] <= player_int < CalcCorrectGraph[calc_correct_id_phys]['stat2']:
        int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_phys]['stat1']) / (CalcCorrectGraph[calc_correct_id_phys]['stat2'] - CalcCorrectGraph[calc_correct_id_phys]['stat1'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent1'] < 0:
            int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent1']
        else:
            int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent1']))
        int_output = CalcCorrectGraph[calc_correct_id_phys]['grow1'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow2'] - CalcCorrectGraph[calc_correct_id_phys]['grow1']) * int_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat2'] <= player_int < CalcCorrectGraph[calc_correct_id_phys]['stat3']:
        int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_phys]['stat2']) / (CalcCorrectGraph[calc_correct_id_phys]['stat3'] - CalcCorrectGraph[calc_correct_id_phys]['stat2'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent2'] < 0:
            int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent2']
        else:
            int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent2']))
        int_output = CalcCorrectGraph[calc_correct_id_phys]['grow2'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow3'] - CalcCorrectGraph[calc_correct_id_phys]['grow2']) * int_growth)
    else:
        int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_phys]['stat3']) / (CalcCorrectGraph[calc_correct_id_phys]['stat4'] - CalcCorrectGraph[calc_correct_id_phys]['stat3'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent3'] < 0:
            int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent3']
        else:
            int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent3']))
        int_output = CalcCorrectGraph[calc_correct_id_phys]['grow3'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow4'] - CalcCorrectGraph[calc_correct_id_phys]['grow3']) * int_growth)
if AttackElementCorrectParam[attack_element_correct_id]['phys_fai'] is False:
    fai_output = 0
else:
    if CalcCorrectGraph[calc_correct_id_phys]['stat0'] <= player_fai < CalcCorrectGraph[calc_correct_id_phys]['stat1']:
        fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_phys]['stat0']) / (CalcCorrectGraph[calc_correct_id_phys]['stat1'] - CalcCorrectGraph[calc_correct_id_phys]['stat0'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent0'] < 0:
            fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent0']
        else:
            fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent0']))
        fai_output = CalcCorrectGraph[calc_correct_id_phys]['grow0'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow1'] - CalcCorrectGraph[calc_correct_id_phys]['grow0']) * fai_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat1'] <= player_fai < CalcCorrectGraph[calc_correct_id_phys]['stat2']:
        fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_phys]['stat1']) / (CalcCorrectGraph[calc_correct_id_phys]['stat2'] - CalcCorrectGraph[calc_correct_id_phys]['stat1'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent1'] < 0:
            fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent1']
        else:
            fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent1']))
        fai_output = CalcCorrectGraph[calc_correct_id_phys]['grow1'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow2'] - CalcCorrectGraph[calc_correct_id_phys]['grow1']) * fai_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat2'] <= player_fai < CalcCorrectGraph[calc_correct_id_phys]['stat3']:
        fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_phys]['stat2']) / (CalcCorrectGraph[calc_correct_id_phys]['stat3'] - CalcCorrectGraph[calc_correct_id_phys]['stat2'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent2'] < 0:
            fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent2']
        else:
            fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent2']))
        fai_output = CalcCorrectGraph[calc_correct_id_phys]['grow2'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow3'] - CalcCorrectGraph[calc_correct_id_phys]['grow2']) * fai_growth)
    else:
        fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_phys]['stat3']) / (CalcCorrectGraph[calc_correct_id_phys]['stat4'] - CalcCorrectGraph[calc_correct_id_phys]['stat3'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent3'] < 0:
            fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent3']
        else:
            fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent3']))
        fai_output = CalcCorrectGraph[calc_correct_id_phys]['grow3'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow4'] - CalcCorrectGraph[calc_correct_id_phys]['grow3']) * fai_growth)
if AttackElementCorrectParam[attack_element_correct_id]['phys_arc'] is False:
    arc_output = 0
else:
    if CalcCorrectGraph[calc_correct_id_phys]['stat0'] <= player_arc < CalcCorrectGraph[calc_correct_id_phys]['stat1']:
        arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_phys]['stat0']) / (CalcCorrectGraph[calc_correct_id_phys]['stat1'] - CalcCorrectGraph[calc_correct_id_phys]['stat0'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent0'] < 0:
            arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent0']
        else:
            arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent0']))
        arc_output = CalcCorrectGraph[calc_correct_id_phys]['grow0'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow1'] - CalcCorrectGraph[calc_correct_id_phys]['grow0']) * arc_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat1'] <= player_arc < CalcCorrectGraph[calc_correct_id_phys]['stat2']:
        arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_phys]['stat1']) / (CalcCorrectGraph[calc_correct_id_phys]['stat2'] - CalcCorrectGraph[calc_correct_id_phys]['stat1'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent1'] < 0:
            arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent1']
        else:
            arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent1']))
        arc_output = CalcCorrectGraph[calc_correct_id_phys]['grow1'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow2'] - CalcCorrectGraph[calc_correct_id_phys]['grow1']) * arc_growth)
    elif CalcCorrectGraph[calc_correct_id_phys]['stat2'] <= player_arc < CalcCorrectGraph[calc_correct_id_phys]['stat3']:
        arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_phys]['stat2']) / (CalcCorrectGraph[calc_correct_id_phys]['stat3'] - CalcCorrectGraph[calc_correct_id_phys]['stat2'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent2'] < 0:
            arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent2']
        else:
            arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent2']))
        arc_output = CalcCorrectGraph[calc_correct_id_phys]['grow2'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow3'] - CalcCorrectGraph[calc_correct_id_phys]['grow2']) * arc_growth)
    else:
        arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_phys]['stat3']) / (CalcCorrectGraph[calc_correct_id_phys]['stat4'] - CalcCorrectGraph[calc_correct_id_phys]['stat3'])
        if CalcCorrectGraph[calc_correct_id_phys]['exponent3'] < 0:
            arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_phys]['exponent3']
        else:
            arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_phys]['exponent3']))
        arc_output = CalcCorrectGraph[calc_correct_id_phys]['grow3'] + ((CalcCorrectGraph[calc_correct_id_phys]['grow4'] - CalcCorrectGraph[calc_correct_id_phys]['grow3']) * arc_growth)

#magic damage
if str_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['magic_str'] is False:
        str_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_magic]['stat0'] <= player_str < CalcCorrectGraph[calc_correct_id_magic]['stat1']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_magic]['stat0']) / (CalcCorrectGraph[calc_correct_id_magic]['stat1'] - CalcCorrectGraph[calc_correct_id_magic]['stat0'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent0'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent0']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent0']))
            str_output = CalcCorrectGraph[calc_correct_id_magic]['grow0'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow1'] - CalcCorrectGraph[calc_correct_id_magic]['grow0']) * str_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat1'] <= player_str < CalcCorrectGraph[calc_correct_id_magic]['stat2']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_magic]['stat1']) / (CalcCorrectGraph[calc_correct_id_magic]['stat2'] - CalcCorrectGraph[calc_correct_id_magic]['stat1'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent1'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent1']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent1']))
            str_output = CalcCorrectGraph[calc_correct_id_magic]['grow1'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow2'] - CalcCorrectGraph[calc_correct_id_magic]['grow1']) * str_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat2'] <= player_str < CalcCorrectGraph[calc_correct_id_magic]['stat3']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_magic]['stat2']) / (CalcCorrectGraph[calc_correct_id_magic]['stat3'] - CalcCorrectGraph[calc_correct_id_magic]['stat2'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent2'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent2']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent2']))
            str_output = CalcCorrectGraph[calc_correct_id_magic]['grow2'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow3'] - CalcCorrectGraph[calc_correct_id_magic]['grow2']) * str_growth)
        else:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_magic]['stat3']) / (CalcCorrectGraph[calc_correct_id_magic]['stat4'] - CalcCorrectGraph[calc_correct_id_magic]['stat3'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent3'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent3']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent3']))
            str_output = CalcCorrectGraph[calc_correct_id_magic]['grow3'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow4'] - CalcCorrectGraph[calc_correct_id_magic]['grow3']) * str_growth)
if dex_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['magic_dex'] is False:
        dex_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_magic]['stat0'] <= player_dex < CalcCorrectGraph[calc_correct_id_magic]['stat1']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_magic]['stat0']) / (CalcCorrectGraph[calc_correct_id_magic]['stat1'] - CalcCorrectGraph[calc_correct_id_magic]['stat0'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent0'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent0']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent0']))
            dex_output = CalcCorrectGraph[calc_correct_id_magic]['grow0'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow1'] - CalcCorrectGraph[calc_correct_id_magic]['grow0']) * dex_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat1'] <= player_dex < CalcCorrectGraph[calc_correct_id_magic]['stat2']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_magic]['stat1']) / (CalcCorrectGraph[calc_correct_id_magic]['stat2'] - CalcCorrectGraph[calc_correct_id_magic]['stat1'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent1'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent1']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent1']))
            dex_output = CalcCorrectGraph[calc_correct_id_magic]['grow1'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow2'] - CalcCorrectGraph[calc_correct_id_magic]['grow1']) * dex_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat2'] <= player_dex < CalcCorrectGraph[calc_correct_id_magic]['stat3']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_magic]['stat2']) / (CalcCorrectGraph[calc_correct_id_magic]['stat3'] - CalcCorrectGraph[calc_correct_id_magic]['stat2'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent2'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent2']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent2']))
            dex_output = CalcCorrectGraph[calc_correct_id_magic]['grow2'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow3'] - CalcCorrectGraph[calc_correct_id_magic]['grow2']) * dex_growth)
        else:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_magic]['stat3']) / (CalcCorrectGraph[calc_correct_id_magic]['stat4'] - CalcCorrectGraph[calc_correct_id_magic]['stat3'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent3'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent3']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent3']))
            dex_output = CalcCorrectGraph[calc_correct_id_magic]['grow3'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow4'] - CalcCorrectGraph[calc_correct_id_magic]['grow3']) * dex_growth)
if int_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['magic_int'] is False:
        int_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_magic]['stat0'] <= player_int < CalcCorrectGraph[calc_correct_id_magic]['stat1']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_magic]['stat0']) / (CalcCorrectGraph[calc_correct_id_magic]['stat1'] - CalcCorrectGraph[calc_correct_id_magic]['stat0'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent0'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent0']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent0']))
            int_output = CalcCorrectGraph[calc_correct_id_magic]['grow0'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow1'] - CalcCorrectGraph[calc_correct_id_magic]['grow0']) * int_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat1'] <= player_int < CalcCorrectGraph[calc_correct_id_magic]['stat2']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_magic]['stat1']) / (CalcCorrectGraph[calc_correct_id_magic]['stat2'] - CalcCorrectGraph[calc_correct_id_magic]['stat1'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent1'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent1']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent1']))
            int_output = CalcCorrectGraph[calc_correct_id_magic]['grow1'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow2'] - CalcCorrectGraph[calc_correct_id_magic]['grow1']) * int_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat2'] <= player_int < CalcCorrectGraph[calc_correct_id_magic]['stat3']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_magic]['stat2']) / (CalcCorrectGraph[calc_correct_id_magic]['stat3'] - CalcCorrectGraph[calc_correct_id_magic]['stat2'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent2'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent2']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent2']))
            int_output = CalcCorrectGraph[calc_correct_id_magic]['grow2'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow3'] - CalcCorrectGraph[calc_correct_id_magic]['grow2']) * int_growth)
        else:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_magic]['stat3']) / (CalcCorrectGraph[calc_correct_id_magic]['stat4'] - CalcCorrectGraph[calc_correct_id_magic]['stat3'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent3'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent3']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent3']))
            int_output = CalcCorrectGraph[calc_correct_id_magic]['grow3'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow4'] - CalcCorrectGraph[calc_correct_id_magic]['grow3']) * int_growth)
if fai_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['magic_fai'] is False:
        fai_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_magic]['stat0'] <= player_fai < CalcCorrectGraph[calc_correct_id_magic]['stat1']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_magic]['stat0']) / (CalcCorrectGraph[calc_correct_id_magic]['stat1'] - CalcCorrectGraph[calc_correct_id_magic]['stat0'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent0'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent0']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent0']))
            fai_output = CalcCorrectGraph[calc_correct_id_magic]['grow0'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow1'] - CalcCorrectGraph[calc_correct_id_magic]['grow0']) * fai_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat1'] <= player_fai < CalcCorrectGraph[calc_correct_id_magic]['stat2']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_magic]['stat1']) / (CalcCorrectGraph[calc_correct_id_magic]['stat2'] - CalcCorrectGraph[calc_correct_id_magic]['stat1'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent1'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent1']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent1']))
            fai_output = CalcCorrectGraph[calc_correct_id_magic]['grow1'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow2'] - CalcCorrectGraph[calc_correct_id_magic]['grow1']) * fai_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat2'] <= player_fai < CalcCorrectGraph[calc_correct_id_magic]['stat3']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_magic]['stat2']) / (CalcCorrectGraph[calc_correct_id_magic]['stat3'] - CalcCorrectGraph[calc_correct_id_magic]['stat2'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent2'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent2']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent2']))
            fai_output = CalcCorrectGraph[calc_correct_id_magic]['grow2'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow3'] - CalcCorrectGraph[calc_correct_id_magic]['grow2']) * fai_growth)
        else:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_magic]['stat3']) / (CalcCorrectGraph[calc_correct_id_magic]['stat4'] - CalcCorrectGraph[calc_correct_id_magic]['stat3'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent3'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent3']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent3']))
            fai_output = CalcCorrectGraph[calc_correct_id_magic]['grow3'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow4'] - CalcCorrectGraph[calc_correct_id_magic]['grow3']) * fai_growth)
if arc_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['magic_arc'] is False:
        arc_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_magic]['stat0'] <= player_arc < CalcCorrectGraph[calc_correct_id_magic]['stat1']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_magic]['stat0']) / (CalcCorrectGraph[calc_correct_id_magic]['stat1'] - CalcCorrectGraph[calc_correct_id_magic]['stat0'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent0'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent0']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent0']))
            arc_output = CalcCorrectGraph[calc_correct_id_magic]['grow0'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow1'] - CalcCorrectGraph[calc_correct_id_magic]['grow0']) * arc_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat1'] <= player_arc < CalcCorrectGraph[calc_correct_id_magic]['stat2']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_magic]['stat1']) / (CalcCorrectGraph[calc_correct_id_magic]['stat2'] - CalcCorrectGraph[calc_correct_id_magic]['stat1'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent1'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent1']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent1']))
            arc_output = CalcCorrectGraph[calc_correct_id_magic]['grow1'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow2'] - CalcCorrectGraph[calc_correct_id_magic]['grow1']) * arc_growth)
        elif CalcCorrectGraph[calc_correct_id_magic]['stat2'] <= player_arc < CalcCorrectGraph[calc_correct_id_magic]['stat3']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_magic]['stat2']) / (CalcCorrectGraph[calc_correct_id_magic]['stat3'] - CalcCorrectGraph[calc_correct_id_magic]['stat2'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent2'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent2']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent2']))
            arc_output = CalcCorrectGraph[calc_correct_id_magic]['grow2'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow3'] - CalcCorrectGraph[calc_correct_id_magic]['grow2']) * arc_growth)
        else:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_magic]['stat3']) / (CalcCorrectGraph[calc_correct_id_magic]['stat4'] - CalcCorrectGraph[calc_correct_id_magic]['stat3'])
            if CalcCorrectGraph[calc_correct_id_magic]['exponent3'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_magic]['exponent3']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_magic]['exponent3']))
            arc_output = CalcCorrectGraph[calc_correct_id_magic]['grow3'] + ((CalcCorrectGraph[calc_correct_id_magic]['grow4'] - CalcCorrectGraph[calc_correct_id_magic]['grow3']) * arc_growth)

#fire damage
if str_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['fire_str'] is False:
        str_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_fire]['stat0'] <= player_str < CalcCorrectGraph[calc_correct_id_fire]['stat1']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_fire]['stat0']) / (CalcCorrectGraph[calc_correct_id_fire]['stat1'] - CalcCorrectGraph[calc_correct_id_fire]['stat0'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent0'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent0']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent0']))
            str_output = CalcCorrectGraph[calc_correct_id_fire]['grow0'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow1'] - CalcCorrectGraph[calc_correct_id_fire]['grow0']) * str_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat1'] <= player_str < CalcCorrectGraph[calc_correct_id_fire]['stat2']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_fire]['stat1']) / (CalcCorrectGraph[calc_correct_id_fire]['stat2'] - CalcCorrectGraph[calc_correct_id_fire]['stat1'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent1'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent1']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent1']))
            str_output = CalcCorrectGraph[calc_correct_id_fire]['grow1'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow2'] - CalcCorrectGraph[calc_correct_id_fire]['grow1']) * str_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat2'] <= player_str < CalcCorrectGraph[calc_correct_id_fire]['stat3']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_fire]['stat2']) / (CalcCorrectGraph[calc_correct_id_fire]['stat3'] - CalcCorrectGraph[calc_correct_id_fire]['stat2'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent2'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent2']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent2']))
            str_output = CalcCorrectGraph[calc_correct_id_fire]['grow2'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow3'] - CalcCorrectGraph[calc_correct_id_fire]['grow2']) * str_growth)
        else:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_fire]['stat3']) / (CalcCorrectGraph[calc_correct_id_fire]['stat4'] - CalcCorrectGraph[calc_correct_id_fire]['stat3'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent3'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent3']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent3']))
            str_output = CalcCorrectGraph[calc_correct_id_fire]['grow3'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow4'] - CalcCorrectGraph[calc_correct_id_fire]['grow3']) * str_growth)
if dex_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['fire_dex'] is False:
        dex_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_fire]['stat0'] <= player_dex < CalcCorrectGraph[calc_correct_id_fire]['stat1']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_fire]['stat0']) / (CalcCorrectGraph[calc_correct_id_fire]['stat1'] - CalcCorrectGraph[calc_correct_id_fire]['stat0'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent0'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent0']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent0']))
            dex_output = CalcCorrectGraph[calc_correct_id_fire]['grow0'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow1'] - CalcCorrectGraph[calc_correct_id_fire]['grow0']) * dex_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat1'] <= player_dex < CalcCorrectGraph[calc_correct_id_fire]['stat2']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_fire]['stat1']) / (CalcCorrectGraph[calc_correct_id_fire]['stat2'] - CalcCorrectGraph[calc_correct_id_fire]['stat1'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent1'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent1']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent1']))
            dex_output = CalcCorrectGraph[calc_correct_id_fire]['grow1'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow2'] - CalcCorrectGraph[calc_correct_id_fire]['grow1']) * dex_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat2'] <= player_dex < CalcCorrectGraph[calc_correct_id_fire]['stat3']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_fire]['stat2']) / (CalcCorrectGraph[calc_correct_id_fire]['stat3'] - CalcCorrectGraph[calc_correct_id_fire]['stat2'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent2'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent2']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent2']))
            dex_output = CalcCorrectGraph[calc_correct_id_fire]['grow2'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow3'] - CalcCorrectGraph[calc_correct_id_fire]['grow2']) * dex_growth)
        else:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_fire]['stat3']) / (CalcCorrectGraph[calc_correct_id_fire]['stat4'] - CalcCorrectGraph[calc_correct_id_fire]['stat3'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent3'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent3']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent3']))
            dex_output = CalcCorrectGraph[calc_correct_id_fire]['grow3'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow4'] - CalcCorrectGraph[calc_correct_id_fire]['grow3']) * dex_growth)
if int_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['fire_int'] is False:
        int_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_fire]['stat0'] <= player_int < CalcCorrectGraph[calc_correct_id_fire]['stat1']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_fire]['stat0']) / (CalcCorrectGraph[calc_correct_id_fire]['stat1'] - CalcCorrectGraph[calc_correct_id_fire]['stat0'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent0'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent0']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent0']))
            int_output = CalcCorrectGraph[calc_correct_id_fire]['grow0'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow1'] - CalcCorrectGraph[calc_correct_id_fire]['grow0']) * int_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat1'] <= player_int < CalcCorrectGraph[calc_correct_id_fire]['stat2']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_fire]['stat1']) / (CalcCorrectGraph[calc_correct_id_fire]['stat2'] - CalcCorrectGraph[calc_correct_id_fire]['stat1'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent1'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent1']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent1']))
            int_output = CalcCorrectGraph[calc_correct_id_fire]['grow1'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow2'] - CalcCorrectGraph[calc_correct_id_fire]['grow1']) * int_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat2'] <= player_int < CalcCorrectGraph[calc_correct_id_fire]['stat3']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_fire]['stat2']) / (CalcCorrectGraph[calc_correct_id_fire]['stat3'] - CalcCorrectGraph[calc_correct_id_fire]['stat2'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent2'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent2']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent2']))
            int_output = CalcCorrectGraph[calc_correct_id_fire]['grow2'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow3'] - CalcCorrectGraph[calc_correct_id_fire]['grow2']) * int_growth)
        else:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_fire]['stat3']) / (CalcCorrectGraph[calc_correct_id_fire]['stat4'] - CalcCorrectGraph[calc_correct_id_fire]['stat3'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent3'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent3']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent3']))
            int_output = CalcCorrectGraph[calc_correct_id_fire]['grow3'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow4'] - CalcCorrectGraph[calc_correct_id_fire]['grow3']) * int_growth)
if fai_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['fire_fai'] is False:
        fai_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_fire]['stat0'] <= player_fai < CalcCorrectGraph[calc_correct_id_fire]['stat1']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_fire]['stat0']) / (CalcCorrectGraph[calc_correct_id_fire]['stat1'] - CalcCorrectGraph[calc_correct_id_fire]['stat0'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent0'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent0']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent0']))
            fai_output = CalcCorrectGraph[calc_correct_id_fire]['grow0'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow1'] - CalcCorrectGraph[calc_correct_id_fire]['grow0']) * fai_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat1'] <= player_fai < CalcCorrectGraph[calc_correct_id_fire]['stat2']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_fire]['stat1']) / (CalcCorrectGraph[calc_correct_id_fire]['stat2'] - CalcCorrectGraph[calc_correct_id_fire]['stat1'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent1'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent1']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent1']))
            fai_output = CalcCorrectGraph[calc_correct_id_fire]['grow1'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow2'] - CalcCorrectGraph[calc_correct_id_fire]['grow1']) * fai_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat2'] <= player_fai < CalcCorrectGraph[calc_correct_id_fire]['stat3']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_fire]['stat2']) / (CalcCorrectGraph[calc_correct_id_fire]['stat3'] - CalcCorrectGraph[calc_correct_id_fire]['stat2'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent2'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent2']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent2']))
            fai_output = CalcCorrectGraph[calc_correct_id_fire]['grow2'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow3'] - CalcCorrectGraph[calc_correct_id_fire]['grow2']) * fai_growth)
        else:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_fire]['stat3']) / (CalcCorrectGraph[calc_correct_id_fire]['stat4'] - CalcCorrectGraph[calc_correct_id_fire]['stat3'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent3'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent3']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent3']))
            fai_output = CalcCorrectGraph[calc_correct_id_fire]['grow3'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow4'] - CalcCorrectGraph[calc_correct_id_fire]['grow3']) * fai_growth)
if arc_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['fire_arc'] is False:
        arc_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_fire]['stat0'] <= player_arc < CalcCorrectGraph[calc_correct_id_fire]['stat1']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_fire]['stat0']) / (CalcCorrectGraph[calc_correct_id_fire]['stat1'] - CalcCorrectGraph[calc_correct_id_fire]['stat0'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent0'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent0']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent0']))
            arc_output = CalcCorrectGraph[calc_correct_id_fire]['grow0'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow1'] - CalcCorrectGraph[calc_correct_id_fire]['grow0']) * arc_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat1'] <= player_arc < CalcCorrectGraph[calc_correct_id_fire]['stat2']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_fire]['stat1']) / (CalcCorrectGraph[calc_correct_id_fire]['stat2'] - CalcCorrectGraph[calc_correct_id_fire]['stat1'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent1'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent1']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent1']))
            arc_output = CalcCorrectGraph[calc_correct_id_fire]['grow1'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow2'] - CalcCorrectGraph[calc_correct_id_fire]['grow1']) * arc_growth)
        elif CalcCorrectGraph[calc_correct_id_fire]['stat2'] <= player_arc < CalcCorrectGraph[calc_correct_id_fire]['stat3']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_fire]['stat2']) / (CalcCorrectGraph[calc_correct_id_fire]['stat3'] - CalcCorrectGraph[calc_correct_id_fire]['stat2'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent2'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent2']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent2']))
            arc_output = CalcCorrectGraph[calc_correct_id_fire]['grow2'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow3'] - CalcCorrectGraph[calc_correct_id_fire]['grow2']) * arc_growth)
        else:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_fire]['stat3']) / (CalcCorrectGraph[calc_correct_id_fire]['stat4'] - CalcCorrectGraph[calc_correct_id_fire]['stat3'])
            if CalcCorrectGraph[calc_correct_id_fire]['exponent3'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_fire]['exponent3']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_fire]['exponent3']))
            arc_output = CalcCorrectGraph[calc_correct_id_fire]['grow3'] + ((CalcCorrectGraph[calc_correct_id_fire]['grow4'] - CalcCorrectGraph[calc_correct_id_fire]['grow3']) * arc_growth)

#lightning damage
if str_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['lightning_str'] is False:
        str_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_lightning]['stat0'] <= player_str < CalcCorrectGraph[calc_correct_id_lightning]['stat1']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_lightning]['stat0']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat1'] - CalcCorrectGraph[calc_correct_id_lightning]['stat0'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent0'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent0']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent0']))
            str_output = CalcCorrectGraph[calc_correct_id_lightning]['grow0'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow1'] - CalcCorrectGraph[calc_correct_id_lightning]['grow0']) * str_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat1'] <= player_str < CalcCorrectGraph[calc_correct_id_lightning]['stat2']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_lightning]['stat1']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat2'] - CalcCorrectGraph[calc_correct_id_lightning]['stat1'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent1'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent1']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent1']))
            str_output = CalcCorrectGraph[calc_correct_id_lightning]['grow1'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow2'] - CalcCorrectGraph[calc_correct_id_lightning]['grow1']) * str_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat2'] <= player_str < CalcCorrectGraph[calc_correct_id_lightning]['stat3']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_lightning]['stat2']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat3'] - CalcCorrectGraph[calc_correct_id_lightning]['stat2'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent2'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent2']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent2']))
            str_output = CalcCorrectGraph[calc_correct_id_lightning]['grow2'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow3'] - CalcCorrectGraph[calc_correct_id_lightning]['grow2']) * str_growth)
        else:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_lightning]['stat3']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat4'] - CalcCorrectGraph[calc_correct_id_lightning]['stat3'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent3'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent3']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent3']))
            str_output = CalcCorrectGraph[calc_correct_id_lightning]['grow3'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow4'] - CalcCorrectGraph[calc_correct_id_lightning]['grow3']) * str_growth)
if dex_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['lightning_dex'] is False:
        dex_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_lightning]['stat0'] <= player_dex < CalcCorrectGraph[calc_correct_id_lightning]['stat1']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_lightning]['stat0']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat1'] - CalcCorrectGraph[calc_correct_id_lightning]['stat0'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent0'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent0']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent0']))
            dex_output = CalcCorrectGraph[calc_correct_id_lightning]['grow0'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow1'] - CalcCorrectGraph[calc_correct_id_lightning]['grow0']) * dex_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat1'] <= player_dex < CalcCorrectGraph[calc_correct_id_lightning]['stat2']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_lightning]['stat1']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat2'] - CalcCorrectGraph[calc_correct_id_lightning]['stat1'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent1'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent1']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent1']))
            dex_output = CalcCorrectGraph[calc_correct_id_lightning]['grow1'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow2'] - CalcCorrectGraph[calc_correct_id_lightning]['grow1']) * dex_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat2'] <= player_dex < CalcCorrectGraph[calc_correct_id_lightning]['stat3']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_lightning]['stat2']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat3'] - CalcCorrectGraph[calc_correct_id_lightning]['stat2'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent2'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent2']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent2']))
            dex_output = CalcCorrectGraph[calc_correct_id_lightning]['grow2'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow3'] - CalcCorrectGraph[calc_correct_id_lightning]['grow2']) * dex_growth)
        else:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_lightning]['stat3']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat4'] - CalcCorrectGraph[calc_correct_id_lightning]['stat3'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent3'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent3']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent3']))
            dex_output = CalcCorrectGraph[calc_correct_id_lightning]['grow3'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow4'] - CalcCorrectGraph[calc_correct_id_lightning]['grow3']) * dex_growth)
if int_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['lightning_int'] is False:
        int_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_lightning]['stat0'] <= player_int < CalcCorrectGraph[calc_correct_id_lightning]['stat1']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_lightning]['stat0']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat1'] - CalcCorrectGraph[calc_correct_id_lightning]['stat0'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent0'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent0']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent0']))
            int_output = CalcCorrectGraph[calc_correct_id_lightning]['grow0'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow1'] - CalcCorrectGraph[calc_correct_id_lightning]['grow0']) * int_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat1'] <= player_int < CalcCorrectGraph[calc_correct_id_lightning]['stat2']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_lightning]['stat1']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat2'] - CalcCorrectGraph[calc_correct_id_lightning]['stat1'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent1'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent1']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent1']))
            int_output = CalcCorrectGraph[calc_correct_id_lightning]['grow1'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow2'] - CalcCorrectGraph[calc_correct_id_lightning]['grow1']) * int_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat2'] <= player_int < CalcCorrectGraph[calc_correct_id_lightning]['stat3']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_lightning]['stat2']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat3'] - CalcCorrectGraph[calc_correct_id_lightning]['stat2'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent2'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent2']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent2']))
            int_output = CalcCorrectGraph[calc_correct_id_lightning]['grow2'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow3'] - CalcCorrectGraph[calc_correct_id_lightning]['grow2']) * int_growth)
        else:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_lightning]['stat3']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat4'] - CalcCorrectGraph[calc_correct_id_lightning]['stat3'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent3'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent3']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent3']))
            int_output = CalcCorrectGraph[calc_correct_id_lightning]['grow3'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow4'] - CalcCorrectGraph[calc_correct_id_lightning]['grow3']) * int_growth)
if fai_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['lightning_fai'] is False:
        fai_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_lightning]['stat0'] <= player_fai < CalcCorrectGraph[calc_correct_id_lightning]['stat1']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_lightning]['stat0']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat1'] - CalcCorrectGraph[calc_correct_id_lightning]['stat0'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent0'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent0']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent0']))
            fai_output = CalcCorrectGraph[calc_correct_id_lightning]['grow0'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow1'] - CalcCorrectGraph[calc_correct_id_lightning]['grow0']) * fai_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat1'] <= player_fai < CalcCorrectGraph[calc_correct_id_lightning]['stat2']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_lightning]['stat1']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat2'] - CalcCorrectGraph[calc_correct_id_lightning]['stat1'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent1'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent1']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent1']))
            fai_output = CalcCorrectGraph[calc_correct_id_lightning]['grow1'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow2'] - CalcCorrectGraph[calc_correct_id_lightning]['grow1']) * fai_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat2'] <= player_fai < CalcCorrectGraph[calc_correct_id_lightning]['stat3']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_lightning]['stat2']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat3'] - CalcCorrectGraph[calc_correct_id_lightning]['stat2'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent2'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent2']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent2']))
            fai_output = CalcCorrectGraph[calc_correct_id_lightning]['grow2'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow3'] - CalcCorrectGraph[calc_correct_id_lightning]['grow2']) * fai_growth)
        else:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_lightning]['stat3']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat4'] - CalcCorrectGraph[calc_correct_id_lightning]['stat3'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent3'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent3']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent3']))
            fai_output = CalcCorrectGraph[calc_correct_id_lightning]['grow3'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow4'] - CalcCorrectGraph[calc_correct_id_lightning]['grow3']) * fai_growth)
if arc_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['lightning_arc'] is False:
        arc_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_lightning]['stat0'] <= player_arc < CalcCorrectGraph[calc_correct_id_lightning]['stat1']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_lightning]['stat0']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat1'] - CalcCorrectGraph[calc_correct_id_lightning]['stat0'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent0'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent0']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent0']))
            arc_output = CalcCorrectGraph[calc_correct_id_lightning]['grow0'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow1'] - CalcCorrectGraph[calc_correct_id_lightning]['grow0']) * arc_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat1'] <= player_arc < CalcCorrectGraph[calc_correct_id_lightning]['stat2']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_lightning]['stat1']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat2'] - CalcCorrectGraph[calc_correct_id_lightning]['stat1'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent1'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent1']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent1']))
            arc_output = CalcCorrectGraph[calc_correct_id_lightning]['grow1'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow2'] - CalcCorrectGraph[calc_correct_id_lightning]['grow1']) * arc_growth)
        elif CalcCorrectGraph[calc_correct_id_lightning]['stat2'] <= player_arc < CalcCorrectGraph[calc_correct_id_lightning]['stat3']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_lightning]['stat2']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat3'] - CalcCorrectGraph[calc_correct_id_lightning]['stat2'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent2'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent2']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent2']))
            arc_output = CalcCorrectGraph[calc_correct_id_lightning]['grow2'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow3'] - CalcCorrectGraph[calc_correct_id_lightning]['grow2']) * arc_growth)
        else:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_lightning]['stat3']) / (CalcCorrectGraph[calc_correct_id_lightning]['stat4'] - CalcCorrectGraph[calc_correct_id_lightning]['stat3'])
            if CalcCorrectGraph[calc_correct_id_lightning]['exponent3'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_lightning]['exponent3']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_lightning]['exponent3']))
            arc_output = CalcCorrectGraph[calc_correct_id_lightning]['grow3'] + ((CalcCorrectGraph[calc_correct_id_lightning]['grow4'] - CalcCorrectGraph[calc_correct_id_lightning]['grow3']) * arc_growth)

#holy damage
if str_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['holy_str'] is False:
        str_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_holy]['stat0'] <= player_str < CalcCorrectGraph[calc_correct_id_holy]['stat1']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_holy]['stat0']) / (CalcCorrectGraph[calc_correct_id_holy]['stat1'] - CalcCorrectGraph[calc_correct_id_holy]['stat0'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent0'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent0']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent0']))
            str_output = CalcCorrectGraph[calc_correct_id_holy]['grow0'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow1'] - CalcCorrectGraph[calc_correct_id_holy]['grow0']) * str_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat1'] <= player_str < CalcCorrectGraph[calc_correct_id_holy]['stat2']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_holy]['stat1']) / (CalcCorrectGraph[calc_correct_id_holy]['stat2'] - CalcCorrectGraph[calc_correct_id_holy]['stat1'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent1'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent1']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent1']))
            str_output = CalcCorrectGraph[calc_correct_id_holy]['grow1'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow2'] - CalcCorrectGraph[calc_correct_id_holy]['grow1']) * str_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat2'] <= player_str < CalcCorrectGraph[calc_correct_id_holy]['stat3']:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_holy]['stat2']) / (CalcCorrectGraph[calc_correct_id_holy]['stat3'] - CalcCorrectGraph[calc_correct_id_holy]['stat2'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent2'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent2']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent2']))
            str_output = CalcCorrectGraph[calc_correct_id_holy]['grow2'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow3'] - CalcCorrectGraph[calc_correct_id_holy]['grow2']) * str_growth)
        else:
            str_ratio = (player_str - CalcCorrectGraph[calc_correct_id_holy]['stat3']) / (CalcCorrectGraph[calc_correct_id_holy]['stat4'] - CalcCorrectGraph[calc_correct_id_holy]['stat3'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent3'] < 0:
                str_growth = str_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent3']
            else:
                str_growth = 1 - ((1 - str_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent3']))
            str_output = CalcCorrectGraph[calc_correct_id_holy]['grow3'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow4'] - CalcCorrectGraph[calc_correct_id_holy]['grow3']) * str_growth)
if dex_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['holy_dex'] is False:
        dex_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_holy]['stat0'] <= player_dex < CalcCorrectGraph[calc_correct_id_holy]['stat1']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_holy]['stat0']) / (CalcCorrectGraph[calc_correct_id_holy]['stat1'] - CalcCorrectGraph[calc_correct_id_holy]['stat0'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent0'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent0']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent0']))
            dex_output = CalcCorrectGraph[calc_correct_id_holy]['grow0'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow1'] - CalcCorrectGraph[calc_correct_id_holy]['grow0']) * dex_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat1'] <= player_dex < CalcCorrectGraph[calc_correct_id_holy]['stat2']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_holy]['stat1']) / (CalcCorrectGraph[calc_correct_id_holy]['stat2'] - CalcCorrectGraph[calc_correct_id_holy]['stat1'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent1'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent1']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent1']))
            dex_output = CalcCorrectGraph[calc_correct_id_holy]['grow1'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow2'] - CalcCorrectGraph[calc_correct_id_holy]['grow1']) * dex_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat2'] <= player_dex < CalcCorrectGraph[calc_correct_id_holy]['stat3']:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_holy]['stat2']) / (CalcCorrectGraph[calc_correct_id_holy]['stat3'] - CalcCorrectGraph[calc_correct_id_holy]['stat2'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent2'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent2']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent2']))
            dex_output = CalcCorrectGraph[calc_correct_id_holy]['grow2'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow3'] - CalcCorrectGraph[calc_correct_id_holy]['grow2']) * dex_growth)
        else:
            dex_ratio = (player_dex - CalcCorrectGraph[calc_correct_id_holy]['stat3']) / (CalcCorrectGraph[calc_correct_id_holy]['stat4'] - CalcCorrectGraph[calc_correct_id_holy]['stat3'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent3'] < 0:
                dex_growth = dex_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent3']
            else:
                dex_growth = 1 - ((1 - dex_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent3']))
            dex_output = CalcCorrectGraph[calc_correct_id_holy]['grow3'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow4'] - CalcCorrectGraph[calc_correct_id_holy]['grow3']) * dex_growth)
if int_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['holy_int'] is False:
        int_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_holy]['stat0'] <= player_int < CalcCorrectGraph[calc_correct_id_holy]['stat1']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_holy]['stat0']) / (CalcCorrectGraph[calc_correct_id_holy]['stat1'] - CalcCorrectGraph[calc_correct_id_holy]['stat0'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent0'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent0']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent0']))
            int_output = CalcCorrectGraph[calc_correct_id_holy]['grow0'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow1'] - CalcCorrectGraph[calc_correct_id_holy]['grow0']) * int_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat1'] <= player_int < CalcCorrectGraph[calc_correct_id_holy]['stat2']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_holy]['stat1']) / (CalcCorrectGraph[calc_correct_id_holy]['stat2'] - CalcCorrectGraph[calc_correct_id_holy]['stat1'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent1'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent1']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent1']))
            int_output = CalcCorrectGraph[calc_correct_id_holy]['grow1'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow2'] - CalcCorrectGraph[calc_correct_id_holy]['grow1']) * int_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat2'] <= player_int < CalcCorrectGraph[calc_correct_id_holy]['stat3']:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_holy]['stat2']) / (CalcCorrectGraph[calc_correct_id_holy]['stat3'] - CalcCorrectGraph[calc_correct_id_holy]['stat2'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent2'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent2']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent2']))
            int_output = CalcCorrectGraph[calc_correct_id_holy]['grow2'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow3'] - CalcCorrectGraph[calc_correct_id_holy]['grow2']) * int_growth)
        else:
            int_ratio = (player_int - CalcCorrectGraph[calc_correct_id_holy]['stat3']) / (CalcCorrectGraph[calc_correct_id_holy]['stat4'] - CalcCorrectGraph[calc_correct_id_holy]['stat3'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent3'] < 0:
                int_growth = int_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent3']
            else:
                int_growth = 1 - ((1 - int_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent3']))
            int_output = CalcCorrectGraph[calc_correct_id_holy]['grow3'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow4'] - CalcCorrectGraph[calc_correct_id_holy]['grow3']) * int_growth)
if fai_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['holy_fai'] is False:
        fai_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_holy]['stat0'] <= player_fai < CalcCorrectGraph[calc_correct_id_holy]['stat1']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_holy]['stat0']) / (CalcCorrectGraph[calc_correct_id_holy]['stat1'] - CalcCorrectGraph[calc_correct_id_holy]['stat0'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent0'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent0']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent0']))
            fai_output = CalcCorrectGraph[calc_correct_id_holy]['grow0'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow1'] - CalcCorrectGraph[calc_correct_id_holy]['grow0']) * fai_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat1'] <= player_fai < CalcCorrectGraph[calc_correct_id_holy]['stat2']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_holy]['stat1']) / (CalcCorrectGraph[calc_correct_id_holy]['stat2'] - CalcCorrectGraph[calc_correct_id_holy]['stat1'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent1'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent1']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent1']))
            fai_output = CalcCorrectGraph[calc_correct_id_holy]['grow1'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow2'] - CalcCorrectGraph[calc_correct_id_holy]['grow1']) * fai_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat2'] <= player_fai < CalcCorrectGraph[calc_correct_id_holy]['stat3']:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_holy]['stat2']) / (CalcCorrectGraph[calc_correct_id_holy]['stat3'] - CalcCorrectGraph[calc_correct_id_holy]['stat2'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent2'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent2']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent2']))
            fai_output = CalcCorrectGraph[calc_correct_id_holy]['grow2'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow3'] - CalcCorrectGraph[calc_correct_id_holy]['grow2']) * fai_growth)
        else:
            fai_ratio = (player_fai - CalcCorrectGraph[calc_correct_id_holy]['stat3']) / (CalcCorrectGraph[calc_correct_id_holy]['stat4'] - CalcCorrectGraph[calc_correct_id_holy]['stat3'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent3'] < 0:
                fai_growth = fai_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent3']
            else:
                fai_growth = 1 - ((1 - fai_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent3']))
            fai_output = CalcCorrectGraph[calc_correct_id_holy]['grow3'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow4'] - CalcCorrectGraph[calc_correct_id_holy]['grow3']) * fai_growth)
if arc_output is not 0:
    pass
else:
    if AttackElementCorrectParam[attack_element_correct_id]['holy_arc'] is False:
        arc_output = 0
    else:
        if CalcCorrectGraph[calc_correct_id_holy]['stat0'] <= player_arc < CalcCorrectGraph[calc_correct_id_holy]['stat1']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_holy]['stat0']) / (CalcCorrectGraph[calc_correct_id_holy]['stat1'] - CalcCorrectGraph[calc_correct_id_holy]['stat0'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent0'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent0']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent0']))
            arc_output = CalcCorrectGraph[calc_correct_id_holy]['grow0'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow1'] - CalcCorrectGraph[calc_correct_id_holy]['grow0']) * arc_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat1'] <= player_arc < CalcCorrectGraph[calc_correct_id_holy]['stat2']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_holy]['stat1']) / (CalcCorrectGraph[calc_correct_id_holy]['stat2'] - CalcCorrectGraph[calc_correct_id_holy]['stat1'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent1'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent1']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent1']))
            arc_output = CalcCorrectGraph[calc_correct_id_holy]['grow1'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow2'] - CalcCorrectGraph[calc_correct_id_holy]['grow1']) * arc_growth)
        elif CalcCorrectGraph[calc_correct_id_holy]['stat2'] <= player_arc < CalcCorrectGraph[calc_correct_id_holy]['stat3']:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_holy]['stat2']) / (CalcCorrectGraph[calc_correct_id_holy]['stat3'] - CalcCorrectGraph[calc_correct_id_holy]['stat2'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent2'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent2']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent2']))
            arc_output = CalcCorrectGraph[calc_correct_id_holy]['grow2'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow3'] - CalcCorrectGraph[calc_correct_id_holy]['grow2']) * arc_growth)
        else:
            arc_ratio = (player_arc - CalcCorrectGraph[calc_correct_id_holy]['stat3']) / (CalcCorrectGraph[calc_correct_id_holy]['stat4'] - CalcCorrectGraph[calc_correct_id_holy]['stat3'])
            if CalcCorrectGraph[calc_correct_id_holy]['exponent3'] < 0:
                arc_growth = arc_ratio ** CalcCorrectGraph[calc_correct_id_holy]['exponent3']
            else:
                arc_growth = 1 - ((1 - arc_ratio) ** abs(CalcCorrectGraph[calc_correct_id_holy]['exponent3']))
            arc_output = CalcCorrectGraph[calc_correct_id_holy]['grow3'] + ((CalcCorrectGraph[calc_correct_id_holy]['grow4'] - CalcCorrectGraph[calc_correct_id_holy]['grow3']) * arc_growth)

###

#Putting it together
final_phys_damage = scaled_phys_weapon + str_output + dex_output + int_output + fai_output + arc_output
final_magic_damage = scaled_magic_weapon + str_output + dex_output + int_output + fai_output + arc_output
final_fire_damage = scaled_fire_weapon + str_output + dex_output + int_output + fai_output + arc_output
final_lightning_damage = scaled_lightning_weapon + str_output + dex_output + int_output + fai_output + arc_output
final_holy_damage = scaled_holy_weapon + str_output + dex_output + int_output + fai_output + arc_output

attack_rating = final_phys_damage + final_magic_damage + final_fire_damage + final_lightning_damage + final_holy_damage


