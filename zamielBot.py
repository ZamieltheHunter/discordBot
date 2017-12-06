import discord
import mongoengine
from discord.ext import commands

class userMention(mongoengine.Document):
#    mentionFrom = discord.User(Required=True)
#   mentionFrom = discord.User(Required=True)
    mentionTo = mongoengine.StringField(Required=True)
    mentionFrom = mongoengine.StringField(Required=True)

def __init__():
    mongoengine.connect('discordMentions')

mentions = {}
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
    
@bot.event
async def on_message(message):
    if(len(message.mentions) < 1):
        pass
    else:
        for sender in message.mentions:
            if(message.author.id + "To" + sender.id in mentions):
                mentions[message.author.id + "To" + sender.id] += 1
            else:
                mentions[message.author.id + "To" + sender.id] = 1

    await bot.process_commands(message)

__init__()
test = userMention(mentionTo = "Zamiel", mentionFrom = "Ziv")
test.save()
for mention in userMention.objects():
    print("From:" + mention.mentionFrom)
    print("To:" + mention.mentionTo)
with open(".token", 'r') as tokenFile:
    token = tokenFile.read()
    bot.run(token.strip())
