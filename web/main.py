from weapon_optimizer_v2 import *
from data_puller import *
from AttackElementCorrectParam import AttackElementCorrectParam
from CalcCorrectGraph import CalcCorrectGraph
from nicegui import ui, run

player_stats = {}
PLAYER_STATS = ['str', 'dex', 'int', 'fai', 'arc']
DMG_TYPES = ['phys', 'magic', 'fire', 'lightning', 'holy']

@ui.page('/')
def index():
    async def run_weapon_optimizer():
        ReinforceParamWeaponDamage, ReinforceParamWeaponScaling, weapon_id_to_reinforce_type_id = get_reinforce_data()
        WeaponDamage, weapon_names_map, WeaponScaling, attack_element_correct_id_dict, weapon_weight, weapon_minimums = get_raw_data()
        CALC_CORRECT_DICT = get_weapon_calc_correct_id()
    
        result = await run.cpu_bound(optimizer, player_stats)
        ui.label(result)

    strength = ui.number(label='Strength (STR)', value=10, min=1, max=99, precision=0).props('clearable')

    dexterity = ui.number(label='Dexterity (DEX)', value=10, min=1, max=99, precision=0).props('clearable')
    player_stats['dex'] = dexterity

    intelligence = ui.number(label='Intelligence (INT)', value=10, min=1, max=99, precision=0).props('clearable')
    player_stats['int'] = intelligence

    faith = ui.number(label='Faith (FAI)', value=10, min=1, max=99, precision=0).props('clearable')
    player_stats['fai'] = faith

    arcane = ui.number(label='Arcane (ARC)', value=10, min=1, max=99, precision=0).props('clearable')
    player_stats['arc'] = arcane

    weight = ui.number(label='Maximum weight you want to spend on this weapon', value=0, min=1, max=50, precision=1).props('clearable')
    player_stats['wgt'] = weight

    two_handed = ui.switch(text='Do you want to use this weapon two-handed? (This will multiply your STR value for the calculation by 1.5x).')
    if ui.switch.value:
        player_stats['str'] = strength * 1.5

    ui.button('Find your weapon!', on_click=run_weapon_optimizer)

ui.run(reload=False)
