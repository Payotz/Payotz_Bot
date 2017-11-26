import discord
from discord.ext.commands import Bot
import json
from overwatch import OWInfo
from dnd import DNDGame

my_bot = Bot(command_prefix="$")
ow = OWInfo()
ow.create()

dnd = DNDGame()

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


@my_bot.command()
async def dnd_dm_rules():
    await my_bot.say('https://dnd.wizards.com/products/tabletop/dm-basic-rules')

@my_bot.command()
async def dnd_player_rules():
    await my_bot.say('https://dnd.wizards.com/articles/features/basicrules')

@my_bot.command()
async def dnd_rolld20():
    await my_bot.say(dnd.rollD20())

@my_bot.command()
async def dnd_rolld6():
    await my_bot.say(dnd.rollD6())

@my_bot.command()
async def dnd_rolldice(min : int,max : int):
    await my_bot.say(str(dnd.rollDice(min,max)))

@my_bot.command()
async def dnd_eli5_general():
    msg = str()
    msg += '```'
    msg += 'Roll d20 for most stuff. i.e: disarm a trap, convince a lord, climb a cliff \n\n'
    msg += 'Once you roll. Add modifiers to it. i.e: convince a lord = persuasion, climb a cliff = acrobatics \n\n'
    msg += 'DM will decide if the value is a fail, success or very successful \n\n'
    msg += 'Example : \n\n'
    msg += 'Player: I would like to climb a cliff \n\n'
    msg += 'Player rolls 15 from d20 \n\n'
    msg += 'Player adds +2 modifier from his acrobatics to 15, resulting in 17 \n\n'
    msg += 'Player: Ok I got 17. \n\n'
    msg += 'DM: You Jumped up the cliff without a sweat \n\n'
    msg += '```'
    msg += '\n** Relevant Bot Commands: **\n'
    msg += 'dnd_rolld20 : Rolls a d20 dice \n'
    msg += 'dnd_rolld6 : Rolls a d6 dice \n'
    msg += 'dnd_rolldice <minimum> <maximum> : Rolls a number between minimum and maximum.\n'
    msg += 'dnd_get <attribute> <name> : Gets the <attribute> modifier of <name>\n'
    await my_bot.say(msg)

@my_bot.command()
async def dnd_eli5_battle():
    msg = str()
    msg += 'Roll d20 then add the initiative modifier to it. \n'
    msg += 'Fight order is determined highest to lowest \n'
    msg += 'Relevant Bot Commands : \n'
    msg += '**dnd_get_init <name>** : Gets the initiative of <name>'
    await my_bot.say(msg)

@my_bot.command()
async def dnd_eli5_character_creation():
    msg = str()
    msg += '``` \n'
    msg += 'Add a character.\n'
    msg += 'Roll d6 4 times.\n'
    msg += 'Take the 3 highest numbers.\n'
    msg += 'Set them as one of your attributes. i.e: Strength\n'
    msg += 'Do the same to the initiative.\n'
    msg += '`dnd_eli5_character_creation_example` for an example \n'
    msg += '```'
    msg += 'Relevant Bot Commands:\n'
    msg += '\n'
    msg += '**dnd_add <name>** : Adds a new Character. Owner is <name>\n\n'
    msg += '**dnd_delete_character <name>**: Deletes a Character. Owner is <name>\n\n'
    msg += '**dnd_set <attribute> <name> <value1> <value2> <value3>** : Sets <attribute> of Character <name> depending on value1, value2 and value3 \n\n'
    msg += '**dnd_set_init <name> <value1> <value2> <value3>** : Sets Initiative of Character <name> depending on value1, value2 and value3 \n\n'
    msg += '**dnd_calculate_skills <name>** : Calculates the skills of the Character according to the 5 attributes\n\n'
    await my_bot.say(msg)

@my_bot.command()
async def dnd_eli5_character_creation_example():
    msg = str()
    msg += '$dnd_add Payotz \n'
    msg += '$dnd_rolld6 `bot says 4`\n'
    msg += '$dnd_rolld6 `bot says 5`\n'
    msg += '$dnd_rolld6 `bot says 6`\n'
    msg += '$dnd_set_init Payotz 4 5 6\n'
    msg += '$dnd_rolld6 `bot says 9`\n'
    msg += '$dnd_rolld6 `bot says 5`\n'
    msg += '$dnd_rolld6 `bot says 2`\n'
    msg += '$dnd_set strength Payotz 9 5 2 \n'
    msg += '`Do this for all attributes`\n'
    msg += '$dnd_calculate_skills Payotz'

    await my_bot.say(msg)

@my_bot.command()
async def dnd_add(name : str):
    dnd.addCharacter(name)
    await my_bot.say("Character Added. Owner is : " + name)

@my_bot.command()
async def dnd_delete_character(name : str):
    dnd.deleteCharacter(name)
    await my_bot.say("Character Deleted. Owner is : " + name)

@my_bot.command()
async def dnd_set(attribute,name,value1,value2,value3):
    dnd.getCharacter(name).setSavingThrow(attribute.lower(),value1,value2,value3)
    await my_bot.say(str(attribute + " for " + name + " is now set to: " + str(int(value1) + int(value2) + int(value3))))

@my_bot.command()
async def dnd_set_init(name,value1 : int,value2 : int,value3 : int):
    dnd.getCharacter(name).setInitiative(value1,value2,value3)
    await my_bot.say(str("Initiative for " + name + " is now set to: " + str(int(value1) + int(value2) + int(value3))))

@my_bot.command()
async def dnd_get(name,attribute):
    await my_bot.say(name + " " + attribute + "Modifier is : " + str(dnd.getCharacter(name).getSavingThrow(attribute.lower())))

@my_bot.command()
async def dnd_get_init(name):
    await my_bot.say(name + " Initiative is : " + str(dnd.getCharacter(name).getInitiative()))

@my_bot.command()
async def dnd_addHP(name,value):
    dnd.getCharacter(name).setHP(dnd.getCharacter(name).getHP() - value)
    await my_bot.say(name + " Added " + str(value) + " to the current HP")

@my_bot.command()
async def dnd_setHP(name,value):
    dnd.getCharacter(name).setHP(value)
    await my_bot.say(name + " HP set to " + str(value))

@my_bot.command()
async def dnd_getHP(name,value):
    current_hp = dnd.getCharacter(name).getHP()
    max_hp = dnd.getCharacter(name).getMaxHP()
    await my_bot.say(name + " HP : " + str(current_hp) + "/" + max_hp)

@my_bot.command()
async def dnd_setMaxHP(name,value):
    dnd.getCharacter(name).setMaxHP(value)
    await my_bot.say(name + " MaxHP set to + " + str(value))

@my_bot.command()
async def dnd_addMaxHP(name,value):
    dnd.getCharacter(name).addMaxHP(value)
    await my_bot.say(name + " Added " + str(value) + " to the Max HP")

@my_bot.command()
async def dnd_calculate_skills(name):
    dnd.getCharacter(name).calculateSkills()
    await my_bot.say(name + "\'s skills are all good!")

@my_bot.command()
async def dnd_get_character_stats(name):
    msg = str()
    msg +="**" + name + " Stats ** \n"
    msg +="** Character Name : **" + dnd.getCharacter(name).getDescription("name")
    msg +="\n** Character Background : **" + dnd.getCharacter(name).getDescription("background")
    msg +="\n** HP: **" + str(dnd.getCharacter(name).getDescription("current_hp")) + "/" + str(dnd.getCharacter(name).getDescription("max_hp"))
    msg +="\n** Strength Modifier: **" + str(dnd.getCharacter(name).getSavingThrow("strength"))
    msg +="\n** Dexterity Modifier: **" + str(dnd.getCharacter(name).getSavingThrow("dexterity"))
    msg +="\n** Constitution Modifier: **" + str(dnd.getCharacter(name).getSavingThrow("constitution"))
    msg +="\n** Intelligence Modifier: **" + str(dnd.getCharacter(name).getSavingThrow("intelligence"))
    msg +="\n** Charisma Modifier: **" + str(dnd.getCharacter(name).getSavingThrow("charisma"))
    msg +="\n** Initiative is : **" + str(dnd.getCharacter(name).getDescription("initiative"))
    msg +="\n\n ** Skills ** "
    msg +="\n\n **Acrobatics** : " + str(dnd.getCharacter(name).getSkill("athletics"))
    msg +="\n **Animal Handling** : " + str(dnd.getCharacter(name).getSkill("animal_handling"))
    msg +="\n **Arcana** : " + str(dnd.getCharacter(name).getSkill("arcana"))
    msg +="\n **Athletics** : " + str(dnd.getCharacter(name).getSkill("athletics"))
    msg +="\n **Deception** : " + str(dnd.getCharacter(name).getSkill("deception"))
    msg +="\n **History** : " + str(dnd.getCharacter(name).getSkill("history"))
    msg +="\n **Insight** : " + str(dnd.getCharacter(name).getSkill("insight"))
    msg +="\n **Intimidation** : " + str(dnd.getCharacter(name).getSkill("intimidation"))
    msg +="\n **Investigation** : " + str(dnd.getCharacter(name).getSkill("investigation"))
    msg +="\n **Medicine** : " + str(dnd.getCharacter(name).getSkill("medicine"))
    msg +="\n **Nature** : " + str(dnd.getCharacter(name).getSkill("nature"))
    msg +="\n **Perception** : " + str(dnd.getCharacter(name).getSkill("perception"))
    msg +="\n **Performance** : " + str(dnd.getCharacter(name).getSkill("performance"))
    msg +="\n **Persuasion** : " + str(dnd.getCharacter(name).getSkill("persuasion"))
    msg +="\n **Religion** : " + str(dnd.getCharacter(name).getSkill("religion"))
    msg +="\n **Sleight of Hand** : " + str(dnd.getCharacter(name).getSkill("sleight_of_hand"))
    msg +="\n **Stealth** : " + str(dnd.getCharacter(name).getSkill("stealth"))
    msg +="\n **Survival** : " + str(dnd.getCharacter(name).getSkill("survival"))
    await my_bot.say(msg)



my_bot.run('token')