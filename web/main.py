from nicegui import app, ui
from weapon_optimizer_v2 import optimizer

player_stats = {}

@ui.page('/')
def index():
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

with ui.row():
    ui.button('Find your weapon!', color='red')
    # optimizer(player_stats)
    # --> we should call the weapon_optimizer_v2 functions here to do some calculatio

if __name__ in {"__main__", "__mp_main__"}:
    ui.run()
