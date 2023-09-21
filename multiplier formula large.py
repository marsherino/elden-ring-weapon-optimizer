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