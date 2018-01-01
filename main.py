import json
from bot_data import *
from addon_overwatch import OWInfo

import bot_dnd

@my_bot.event
async def on_ready():
    print("Started up")

@my_bot.command()
async def overwatch_get_hero(left : str):
    if ow.checkInHero(left) != 'OK':
        await my_bot.say(ow.checkInHero(left))
    elif ow.checkInHero(left) == 'OK':
        dummy = ow.getHeroData(left)
        msg = '**Name ** : ' + dummy['name'] + '\n\n'
        msg += '**Description : **' + '```' + dummy['description'] + '```' + '\n\n'
        msg += '**Health : **' + str(dummy['health']) + '\n\n'
        msg += str('**Armour : **' + str(dummy['armour'])) + '\n\n'
        msg += '**Real Name : **' + dummy['real_name'] + '\n\n'
        msg += '**Age : **' + str(dummy['age']) + '\n\n'
        msg += '**Affiliation : **' + str(dummy['affiliation']) + '\n\n'
        msg += '**Base Of Operations : **' + str(dummy['base_of_operations'] + '\n\n')
        msg += '**Difficulty : **' + str(dummy['difficulty']) + '\n\n\n'
        msg += '**Abilities : ** \n '
        ability_msg = '\n'
        for x in dummy['abilities']:
            if(x['is_ultimate']):
                ability_msg += '-- This ability is an ultimate --' + '\n'
            ability_msg += '**Name : **' + str(x['name']) + '\n'
            ability_msg += '**Description : **' + str(x['description'] + '\n\n')
        ability_msg += ''
        msg += ability_msg

        await my_bot.say(msg)


my_bot.run('MzAyMjY4MzY5MzM0NDM1ODUz.DSwnqA.BGliBkpHOG_JtwiJOtyv6nAIACk')