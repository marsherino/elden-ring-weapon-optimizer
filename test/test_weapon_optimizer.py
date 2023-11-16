import pytest
from weapon_optimizer_v2 import base_damage_reinforcement, base_scaling_reinforcement, player_scaling_multiplier, combined_calc

def test_base_damage_reinforcement():
    weapon_id = '16030200'
    reinforce_type_id = '225'

    result = base_damage_reinforcement(weapon_id, reinforce_type_id)

    assert int(result['phys']) == 223
    assert int(result['magic']) == 119
    assert result['fire'] == 0
    assert result['lightning'] == 0
    assert result['holy'] == 0

def test_base_scaling_reinforcement():
    weapon_id = '16030200'
    reinforce_type_id = '225'

    result = base_scaling_reinforcement(weapon_id, reinforce_type_id)

    assert round(result['str'], 3) == 0.247
    assert round(result['dex'], 2) == 1.26
    assert round(result['int'], 3) == 0.342
    assert result['fai'] == 0
    assert result['arc'] == 0

# FIXME: This doesn't test anything sensible (or anything at all at this point actually)
def test_player_scaling_multiplier():
    player = {'str': 12,
              'dex': 50,
              'int': 50,
              'fai': 10,
              'arc': 10,}

    attack_element_correct_id = '10000'
    weapon_id = '16030200'

    base_phys_weapon = 95
    base_magic_weapon = 51
    base_fire_weapon = 0
    base_lightning_weapon = 0
    base_holy_weapon = 0

    base_weapon_dmg = {
        'phys': 95,
        'magic': 51,
        'fire': 0,
        'lightning': 0,
        'holy': 0,
    }

    result = player_scaling_multiplier(weapon_id, player)
    print(result)

    #assert result['phys'] == 114.09621961766977
    #assert result['magic'] == 80.0
    #assert result['fire'] == 14.881659562559502
    #assert result['lightning'] == 94.29297041297163
    #assert result['holy'] == 14.881659562559502

def test_combined_calc():
    player = {'str': 12,
              'dex': 50,
              'int': 50,
              'fai': 10,
              'arc': 10,}
    attack_element_correct_id = '10000'
    weapon_id = '16030200'
    reinforce_type_id = '225'

    psm = player_scaling_multiplier(attack_element_correct_id, weapon_id, player)
    bdr = base_damage_reinforcement(weapon_id, reinforce_type_id)
    bsr = base_scaling_reinforcement(weapon_id, reinforce_type_id)

    print(f"psm = {psm}")
    print(f"bdr = {bdr}")
    print(f"bsr = {bsr}")
    result = combined_calc(bdr, bsr, psm)

    assert result == 575


