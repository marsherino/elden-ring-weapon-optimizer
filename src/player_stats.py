

def get_player_stats():
    flag_str = True
    input_value_str = None
    while flag_str:
        input_str = input("Please enter your STR. This should be a value between 1 and 99.")
        match_val = re.match("[-+]?\\d+$", input_value_str)
    if match_val is None:
        print("Please enter a valid integer.")
    elif match_val > 99:
        print("Please enter a value between 1 and 99.")
    elif match_val < 0:
        print("Please enter a value between 1 and 99.")
    else:
        flag = False
    base_player_str = int(input_value_str)
    two_handed = None
    while two_handed is None:
      input_two_handed = input("Do you intend to two-hand this weapon? Please enter Y or N. (This will multiply your STR by 1.5.)")
      if input_two_handed is not 'Y' or 'N':
          print("Please enter a valid response.")
      elif input_two_handed is 'Y':
          player_stats['str'] = base_player_str * 1.5
      else:
          player_stats['str'] = base_player_str * 1
    flag_dex = True
    input_value_dex = None
    while flag_dex:
        input_dex = input("Please enter your DEX. This should be a value between 1 and 99.")
        match_val = re.match("[-+]?\\d+$", input_value_dex)
    if match_val is None:
        print("Please enter a valid integer.")
    elif match_val > 99:
        print("Please enter a value between 1 and 99.")
    elif match_val < 0:
        print("Please enter a value between 1 and 99.")
    else:
        flag = False
    player_stats['dex'] = int(input_value_dex)
    flag_int = True
    input_value_int = None
    while flag_int:
        input_int = input("Please enter your INT. This should be a value between 1 and 99.")
        match_val = re.match("[-+]?\\d+$", input_value_int)
    if match_val is None:
        print("Please enter a valid integer.")
    elif match_val > 99:
        print("Please enter a value between 1 and 99.")
    elif match_val < 0:
        print("Please enter a value between 1 and 99.")
    else:
        flag = False
    player_stats['int'] = int(input_value_int)
    flag_fai = True
    input_value_fai = None
    while flag_fai:
        input_fai = input("Please enter your FAI. This should be a value between 1 and 99.")
        match_val = re.match("[-+]?\\d+$", input_value_fai)
    if match_val is None:
        print("Please enter a valid integer.")
    elif match_val > 99:
        print("Please enter a value between 1 and 99.")
    elif match_val < 0:
        print("Please enter a value between 1 and 99.")
    else:
        flag = False
    player_stats['fai'] = int(input_value_fai)
    flag_arc = True
    input_value_arc = None
    while flag_arc:
        input_dex = input("Please enter your ARC. This should be a value between 1 and 99.")
        match_val = re.match("[-+]?\\d+$", input_value_arc)
    if match_val is None:
        print("Please enter a valid integer.")
    elif match_val > 99:
        print("Please enter a value between 1 and 99.")
    elif match_val < 0:
        print("Please enter a value between 1 and 99.")
    else:
        flag = False
    player_stats['arc'] = int(input_value_arc)