from bot_data import *

@my_bot.group(pass_context = True)
async def dnd(ctx):
    if ctx.invoked_subcommand is None:
        await my_bot.say("Invalid Command : " + str(ctx.message.content))

@dnd.command()
async def dm_rules():
    await my_bot.say('https://dnd.wizards.com/products/tabletop/dm-basic-rules')

@dnd.command()
async def player_rules():
    await my_bot.say('https://dnd.wizards.com/articles/features/basicrules')

@dnd.command()
async def rolld20(count : int):
    msg = '('
    if count is None:
        await my_bot.say("rolld20 Usage = $dnd rolld20 <dice count>")
        return
    for x in range (count):
        msg += ' ' + str(dndclass.rollD20())
    msg += ')'

@dnd.command()
async def rolld6(count : int):
    msg = '('
    if count is None:
        await my_bot.say("rolld6 Usage = $dnd rolld6 <dice count>")
        return
    for x in range (count):
        msg += ' ' + str(dndclass.rollD6())
    msg += ')'
    await my_bot.say(msg)

@dnd.command()
async def rolldice(min : int,max : int, count : int):
    msg = '('
    if count is None:
        await my_bot.say("rolld6 Usage = $dnd rolldice <dice count>")
        return
    for x in range (count):
        msg += ' ' + str(dndclass.rollDice(min,max))
    msg += ')'
    await my_bot.say(msg)

@dnd.command()
async def add(name : str, method : str):
    if(method.lower() == "manual"):
        dndclass.addCharacter(name)
    elif(method.lower() == "automatic"):
        dndclass.addCharacter(name)
        dndclass.getCharacter(name).setAttribute("strength",15)
        dndclass.getCharacter(name).setAttribute("dexterity",14)
        dndclass.getCharacter(name).setAttribute("constitution",13)
        dndclass.getCharacter(name).setAttribute("intelligence",12)
        dndclass.getCharacter(name).setAttribute("wisdom",10)
        dndclass.getCharacter(name).setAttribute("charisma",8)
    else:
        await my_bot.say("Must choose between automatic or manual. i.e: $dnd add <name> automatic")

@dnd.command()
async def delete(name : str):
    dndclass.deleteCharacter(name)

@dnd.command()
async def set(name,attribute,value):
    dndclass.getCharacter(name).setAttribute(attribute.lower(),value)

@dnd.command()
async def get(name,attribute : str):
    await my_bot.say(name + " " + attribute + ": " + str(dndclass.getCharacter(name).getAttribute(attribute)))

@dnd.command()
async def get_modified(value):
    await my_bot.say(dndclass.getModified(value))

@dnd.command()
async def get_stats(name):
    msg = str()
    msg +="**" + name + " Stats ** \n"
    msg +="** Character Name : **" + dndclass.getCharacter(name).getAttribute("name")
    msg +="\n** Character Background : **" + dndclass.getCharacter(name).getAttribute("background")
    msg +="\n** HP: **" + str(dndclass.getCharacter(name).getAttribute("current_hp")) + "/" + str(dndclass.getCharacter(name).getAttribute("max_hp"))
    msg +="\n** Strength Modifier: **" + str(dndclass.getCharacter(name).getAttribute("strength"))
    msg +="\n** Dexterity Modifier: **" + str(dndclass.getCharacter(name).getAttribute("dexterity"))
    msg +="\n** Constitution Modifier: **" + str(dndclass.getCharacter(name).getAttribute("constitution"))
    msg +="\n** Intelligence Modifier: **" + str(dndclass.getCharacter(name).getAttribute("intelligence"))
    msg +="\n** Charisma Modifier: **" + str(dndclass.getCharacter(name).getAttribute("charisma"))
    msg +="\n** Wisdom Modifer: **" + str(dndclass.getCharacter(name).getAttribute("wisdom"))
    msg +="\n** Initiative is : **" + str(dndclass.getCharacter(name).getAttribute("initiative"))
    msg +="\n\n ** Skills ** "
    msg +="\n\n **Acrobatics** : " + str(dndclass.getCharacter(name).getAttribute("athletics"))
    msg +="\n **Animal Handling** : " + str(dndclass.getCharacter(name).getAttribute("animal_handling"))
    msg +="\n **Arcana** : " + str(dndclass.getCharacter(name).getAttribute("arcana"))
    msg +="\n **Athletics** : " + str(dndclass.getCharacter(name).getAttribute("athletics"))
    msg +="\n **Deception** : " + str(dndclass.getCharacter(name).getAttribute("deception"))
    msg +="\n **History** : " + str(dndclass.getCharacter(name).getAttribute("history"))
    msg +="\n **Insight** : " + str(dndclass.getCharacter(name).getAttribute("insight"))
    msg +="\n **Intimidation** : " + str(dndclass.getCharacter(name).getAttribute("intimidation"))
    msg +="\n **Investigation** : " + str(dndclass.getCharacter(name).getAttribute("investigation"))
    msg +="\n **Medicine** : " + str(dndclass.getCharacter(name).getAttribute("medicine"))
    msg +="\n **Nature** : " + str(dndclass.getCharacter(name).getAttribute("nature"))
    msg +="\n **Perception** : " + str(dndclass.getCharacter(name).getAttribute("perception"))
    msg +="\n **Performance** : " + str(dndclass.getCharacter(name).getAttribute("performance"))
    msg +="\n **Persuasion** : " + str(dndclass.getCharacter(name).getAttribute("persuasion"))
    msg +="\n **Religion** : " + str(dndclass.getCharacter(name).getAttribute("religion"))
    msg +="\n **Sleight of Hand** : " + str(dndclass.getCharacter(name).getAttribute("sleight_of_hand"))
    msg +="\n **Stealth** : " + str(dndclass.getCharacter(name).getAttribute("stealth"))
    msg +="\n **Survival** : " + str(dndclass.getCharacter(name).getAttribute("survival"))
    await my_bot.say(msg)


@dnd.command()
async def eli5_general():
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
    await my_bot.say(msg)

@dnd.command()
async def eli5_battle():
    msg = str()
    msg += 'Roll d20 then add the initiative modifier to it. \n'
    msg += 'Fight order is determined highest to lowest \n'
    await my_bot.say(msg)

@dnd.command()
async def eli5_character_creation():
    msg = str()
    msg += '``` \n'
    msg += 'Add a character.\n'
    msg += 'Roll d6 4 times.\n'
    msg += 'Take the 3 highest numbers.\n'
    msg += 'Set them as one of your attributes. i.e: Strength\n'
    msg += 'Do the same to the initiative.\n'
    msg += '`dnd_eli5_character_creation_example` for an example \n'
    msg += '```'
    await my_bot.say(msg)
