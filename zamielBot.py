import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='&', description='''Zamiel's Place home bot''')
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("----------")

async def _bot():
    await bot.say("I'm here bitches")

with open(".token", 'r') as tokenFile:
    token = tokenFile.read()
    print(token)
    bot.run(token)
