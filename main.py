import discord
from discord.ext.commands import Bot
import json
from overwatch import OWInfo

my_bot = Bot(command_prefix="$")
ow = OWInfo()
ow.create()
@my_bot.event
async def on_read():
    print("Client logged in")
    

@my_bot.command()
async def hello(*args):
    return await my_bot.say("Hello, world!")

@my_bot.command()
async def goodbye():
    await my_bot.say("Bye")

@my_bot.command()
async def add(left : int, right : int):
    await my_bot.say(left + right)

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


my_bot.run('token')