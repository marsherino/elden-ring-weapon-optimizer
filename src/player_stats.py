import re

def get_player_stats():
    player_stats = {
    'str': None,
    'dex': None,
    'int': None,
    'fai': None,
    'arc': None,
}
    flag_str = True
    while flag_str:
        input_str = input("Please enter your STR. This should be a value between 1 and 99: ").strip()
        match_val = re.match("[-+]?\\d+$", input_str)
        if match_val is None:
            print("Please enter a valid integer.")
        elif 0 > int(match_val.group(0)) or int(match_val.group(0)) > 99:
            print("Please enter a value between 1 and 99.")
        else:
            flag_str = False
    base_player_str = int(input_str)
    
    two_handed_flag = True
    while two_handed_flag:
      input_two_handed = input("Do you intend to two-hand this weapon? (This will multiply your STR by 1.5.) (Y/N): ").strip()
      if not (input_two_handed.upper() == 'Y' or input_two_handed.upper() == 'N'):
          print("Please enter a valid response.")
      elif input_two_handed.upper() == 'Y':
          player_stats['str'] = int(base_player_str * 1.5)
          two_handed_flag = False
      else:
          player_stats['str'] = base_player_str * 1
          two_handed_flag = False

    flag_dex = True
    while flag_dex:
        input_dex = input("Please enter your DEX. This should be a value between 1 and 99: ").strip()
        match_val = re.match("[-+]?\\d+$", input_dex)
        if match_val is None:
            print("Please enter a valid integer.")
        elif 0 > int(match_val.group(0)) or int(match_val.group(0)) > 99:
            print("Please enter a value between 1 and 99.")
        else:
            flag_dex = False
    player_stats['dex'] = int(input_dex)
    
    flag_int = True
    while flag_int:
        input_int = input("Please enter your INT. This should be a value between 1 and 99: ").strip()
        match_val = re.match("[-+]?\\d+$", input_int)
        if match_val is None:
            print("Please enter a valid integer.")
        elif 0 > int(match_val.group(0)) or int(match_val.group(0)) > 99:
            print("Please enter a value between 1 and 99.")
        else:
            flag_int = False
    player_stats['int'] = int(input_int)
    
    flag_fai = True
    while flag_fai:
        input_fai = input("Please enter your FAI. This should be a value between 1 and 99: ").strip()
        match_val = re.match("[-+]?\\d+$", input_fai)
        if match_val is None:
            print("Please enter a valid integer.")
        elif 0 > int(match_val.group(0)) or int(match_val.group(0)) > 99:
            print("Please enter a value between 1 and 99.")
        else:
            flag_fai = False
    player_stats['fai'] = int(input_fai)
    
    flag_arc = True
    while flag_arc:
        input_arc = input("Please enter your ARC. This should be a value between 1 and 99: ").strip()
        match_val = re.match("[-+]?\\d+$", input_arc)
        if match_val is None:
            print("Please enter a valid integer.")
        elif 0 > int(match_val.group(0)) or int(match_val.group(0)) > 99:
            print("Please enter a value between 1 and 99.")
        else:
            flag_arc = False
    player_stats['arc'] = int(input_arc)

    return player_stats