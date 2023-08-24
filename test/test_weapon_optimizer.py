import pytest
from weapon_optimizer import walk_weapons

def test_walk_weapons():
    example_player = {'str': 12,
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

    result = walk_weapons(attack_element_correct_id, weapon_id, example_player)
    print(result)

    assert result['phys'] == 114.09621961766977
    assert result['magic'] == 80.0
    assert result['fire'] == 14.881659562559502
    assert result['lightning'] == 94.29297041297163
    assert result['holy'] == 14.881659562559502


def test_outputs_to_final_values():
    # TODO: Make me line up with the function that does the final value assembly in the main program
    assert True
