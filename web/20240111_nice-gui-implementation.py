from nicegui import app, ui
import json

@ui.page('/')
def index():
    strength = ui.number(label='Strength (STR)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(app.storage_browser, 'strength')
    base_player_str = ui.number().bind_value(strength, 'value')

    dexterity = ui.number(label='Dexterity (DEX)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(app.storage.browser, 'dexterity')
    player_stats['dex'] = ui.number().bind_value(dexterity, 'value')

    intelligence = ui.number(label='Intelligence (INT)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(app.storage.browser, 'intelligence')
    player_stats['int'] = ui.number().bind_value(intelligence, 'value')

    faith = ui.number(label='Faith (FAI)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(app.storage.browser, 'faith')
    player_stats['fai'] = ui.number().bind_value(faith, 'value')

    arcane = ui.number(label='Arcane (ARC)', value=10, min=1, max=99, precision=0).props('clearable').bind_value(app.storage_browser, 'arcane')
    player_stats['arc'] = ui.number().bind_value(arcane, 'value')

    weight = ui.number(label='Maximum weight you want to spend on this weapon', value=0, min=1, max=50, precision=1).props('clearable').bind_value(app.storage_browser, 'weight')
    player_stats['wgt'] = ui.number().bind_value(weight, 'value')

    two_handed = ui.switch(text='Do you want to use this weapon two-handed? (This will multiply your STR value for the calculation by 1.5x).')
        if ui.switch.value == True:
            player_stats['str'] = base_player_str * 1.5
        else:
            player_stats['str'] = base_player_str * 1



with ui.row():
    ui.button('Find your weapon!', color=red)
    ui.button('Save as JSON')