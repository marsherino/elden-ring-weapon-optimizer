from weapon_optimizer_v2 import *
from data_puller import *
from AttackElementCorrectParam import AttackElementCorrectParam
from CalcCorrectGraph import CalcCorrectGraph
from dataclasses import dataclass
from nicegui import ui, run

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
    async def run_weapon_optimizer(player_stats):
        ReinforceParamWeaponDamage, ReinforceParamWeaponScaling, weapon_id_to_reinforce_type_id = get_reinforce_data()
        WeaponDamage, weapon_names_map, WeaponScaling, attack_element_correct_id_dict, weapon_weight, weapon_minimums = get_raw_data()
        CALC_CORRECT_DICT = get_weapon_calc_correct_id()

        result = await run.cpu_bound(optimizer, player_stats)
        output.clear()
        with output:
            ui.label(result).style('font-size: 200%; font-weight: 300')
    
    ui.label('Elden Ring Weapon Optimizer').classes('text-h1')

    ui.label("Welcome to the Elden Ring Weapon Optimizer! This tool will figure out which weapon and infusion in Elden Ring will give you the highest AR for your character's stats by checking them against every weapon in the game. Use this as a starting point to figure out what weapon might fit your build best.")

    ui.label("Note that this app is not a damage calculator - it can't figure out how much damage you'll do to a given enemy with a given attack. Also, due to how the game balances elemental infusions, this app will tend to recommend those. Check out the corresponding physical infusion(s) for the recommended weapon if you don't want the split damage.")
    
    with ui.row():
        ui.label("Many thanks to u/TarnishedSpreadsheet on Reddit (Phil#5171 on Discord) for creating the data sheet this calculator uses and for his excellent walkthough of how to calculate AR in Elden Ring.")
        ui.link('You can find his post with links to his data here.', 'https://www.reddit.com/r/Eldenring/comments/tbco46/elden_ring_weapon_calculator/')

    with ui.row():
        ui.label("Thanks also to Scott Beru, who mentored me through this project.")
        ui.link('You can find his Github profile here.', 'https://github.com/scooberu')

    ui.link("This project's repo, including a CLI version of this app and documentation, is available here.", 'https://github.com/marsherino/elden-ring-weapon-optimizer')

    ui.number.default_style('min-width: 300px')

    ui.number(label='Strength (STR)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'strength')

    ui.number(label='Dexterity (DEX)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'dexterity')

    ui.number(label='Intelligence (INT)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'intelligence')

    ui.number(label='Faith (FAI)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'faith')

    ui.number(label='Arcane (ARC)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(player, 'arcane')

    ui.number(label='Maximum weight for this weapon', value=0, min=1, max=50, precision=1).props('clearable').bind_value(player, 'max_weight')

    two_handed = ui.switch(text='Do you want to use this weapon two-handed? (This will multiply your STR value for the calculation by 1.5x).')
    if two_handed:
        player.strength = int(float(player.strength) * 1.5)

    ui.button('Find your weapon!', on_click=lambda: run_weapon_optimizer({'str': player.strength, 'dex': player.dexterity, 'int': player.intelligence, 'fai': player.faith, 'arc': player.arcane, 'wgt': player.max_weight}))

    output = ui.column()

player = Player()

ui.run(reload=False)
