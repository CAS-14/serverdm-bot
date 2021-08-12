# bot.py
import os
import random
from datetime import datetime

from dotenv import load_dotenv
from discord import *
from discord.ext import commands

# from discord_slash import SlashCommand
# from discord_slash.utils.manage_commands import create_option

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# TOKEN = 'OVERRIDE'

prefix = 'd!'
gameStatus = ""

# activity = Game(name=gameStatus)
# activity = Streaming(name="c!help", url="twitch_url_here")
# activity = Activity(type=ActivityType.listening, name="!help")
# activity = Activity(type=ActivityType.watching, name="!help")

bot = commands.Bot(command_prefix=prefix, status=Status.idle)
client = Client(intents=Intents.all())
# slash = SlashCommand(client, sync_commands=True)

# 738488607261851748 Awesome Realm Official
# 674791516249653277 CAS Testing Server
testServers = [738488607261851748, 
               674791516249653277]

bot_owners  = [642527833410895882]
bot_masters = [642527833410895882]

forward_servers = [674791516249653277]

@bot.command(name='embedtest')
async def embedtest(ctx):
    colorcode = int("0x%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255)), 16)
    testembed = Embed(title="Test Title",description="Test Description",color=colorcode)
    await ctx.send(embed=testembed)

@client.event
async def on_message(message):
    guild = message.guild
    log_channel = utils.get(guild.channels, name="log-test")
    if log_channel is None:
        await client.process_commands(message)
        return
    else:
        embed=Embed(
            color=0xffd700,
            timestamp=datetime.utcnow(),
            description="in {}:\n{}".format(message.channel.mention, message.content)
        )
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        embed.set_footer(text=message.author.id)
        if len(message.attachments) > 0:
            embed.set_image(url = message.attachments[0].url)
        await log_channel.send(embed=embed)
        await client.process_commands(message)

bot.run(TOKEN)
