import discord
from discord.ext.commands import Bot
from addon_overwatch import OWInfo
from addon_dnd import DNDGame

my_bot = Bot(command_prefix="$")
ow = OWInfo()
ow.create()

dndclass = DNDGame()