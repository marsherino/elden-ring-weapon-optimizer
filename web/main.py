from weapon_optimizer_v2 import *
from data_puller import *
from AttackElementCorrectParam import AttackElementCorrectParam
from CalcCorrectGraph import CalcCorrectGraph
from dataclasses import dataclass
from nicegui import ui, run

player_stats = {}
PLAYER_STATS = ['str', 'dex', 'int', 'fai', 'arc']
DMG_TYPES = ['phys', 'magic', 'fire', 'lightning', 'holy']

@dataclass
class Player:
    strength: int = 0
    dexterity: int = 0
    intelligence: int = 0
    faith: int = 0
    arcane: int = 0
    max_weight: float = 0

@ui.page('/')
def index():
    async def run_weapon_optimizer():
        ReinforceParamWeaponDamage, ReinforceParamWeaponScaling, weapon_id_to_reinforce_type_id = get_reinforce_data()
        WeaponDamage, weapon_names_map, WeaponScaling, attack_element_correct_id_dict, weapon_weight, weapon_minimums = get_raw_data()
        CALC_CORRECT_DICT = get_weapon_calc_correct_id()
    
        result = await run.cpu_bound(optimizer, player_stats)
        ui.label(result)

    ui.number(label='Strength (STR)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'strength')

    ui.number(label='Dexterity (DEX)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'dexterity')

    ui.number(label='Intelligence (INT)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'intelligence')

    ui.number(label='Faith (FAI)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'faith')

    ui.number(label='Arcane (ARC)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'arcane')

    ui.number(label='Maximum weight you want to spend on this weapon', value=0, min=1, max=50, precision=1).props('clearable').bind_value(player, 'max_weight')

    two_handed = ui.switch(text='Do you want to use this weapon two-handed? (This will multiply your STR value for the calculation by 1.5x).')
    if two_handed:
        player.strength = int(float(player.strength) * 1.5)

    player_stats = {
                    'str': player.strength,
                    'dex': player.dexterity,
                    'int': player.intelligence,
                    'fai': player.faith,
                    'arc': player.arcane,
                    'wgt': player.max_weight
                   }
    ui.button('Find your weapon!', on_click=lambda: run_weapon_optimizer(player_stats))

player = Player()

ui.run(reload=False)
