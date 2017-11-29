import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='&', description='''Zamiel's Place home bot''')
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("----------")

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

async def _bot():
    await bot.say("I'm here bitches")

with open(".token", 'r') as tokenFile:
    token = tokenFile.read()
    bot.run(token.strip())
