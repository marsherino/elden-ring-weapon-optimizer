import re
import json

def get_saved_player_stats():
    save_json_flag = True
    while save_json_flag:
      input_save_json = input("Do you want to load an existing stat block file? (.eldenringplayerstats.json) (Y/N): ").strip()
      if not (input_save_json.upper() == 'Y' or input_save_json.upper() == 'N'):
          print("Please enter a valid response.")
      elif input_save_json.upper() == 'Y':
          try:
              with open('.eldenringplayerstats.json', 'r', encoding='utf-8') as f:
                result = json.loads(f.read())
                return result
          except FileNotFoundError:
              print("Couldn't find .eldenringplayerstats.json in the directory you're running this in! Maybe enter those details again if you don't mind...")
              return False
      else:
          save_json_flag = False
          return False

def get_player_stats():
    player_stats = {
    'str': None,
    'dex': None,
    'int': None,
    'fai': None,
    'arc': None,
    'wgt': None,
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

    flag_wgt = True
    while flag_wgt:
        input_wgt = input("Please enter the maximum weight you want to invest in your weapon. To check all weapons without restriction, please enter 100: ").strip()
        match_val = re.match("[-+]?\\d+$", input_wgt)
        if match_val is None:
            print("Please enter a valid integer.")
        else:
            flag_wgt = False
    player_stats['wgt'] = int(input_wgt)

    save_json_flag = True
    while save_json_flag:
      input_save_json = input("Do you want to save these player stats to a local file that can be loaded next time? (.eldenringplayerstats.json) (Y/N): ").strip()
      if not (input_save_json.upper() == 'Y' or input_save_json.upper() == 'N'):
          print("Please enter a valid response.")
      elif input_save_json.upper() == 'Y':
          with open('.eldenringplayerstats.json', 'w', encoding='utf-8') as f:
              json.dump(player_stats, f, ensure_ascii=False, indent=4)
          save_json_flag = False
      else:
          save_json_flag = False
    

    return player_stats