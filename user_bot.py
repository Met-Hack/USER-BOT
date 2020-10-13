import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix="_")
channels = [765346710435266581, 755769922289664060, 754869146453278856, 761914882635202640, 758379429964546080, 764561567143559178, 765273000995848282, 760409070829174794]


@bot.event
async def on_message(message):
    if message.channel.id in channels:
        if "j4j" in message.content:
            await message.author.send("https://discord.gg/mNpdkW")
            army_town_channel = bot.get_channel(765229524349747231)
            await army_town_channel.send(f"Invite Sent to {message.author.name}")
            time.sleep(600)
            

@bot.event
async def on_ready():
    while True:
        await bot.change_presence(status=discord.Status.invisible)

@bot.command(pass_context=True)
async def myname(ctx):
    await ctx.send("My name is " + bot.user.name)
    

bot.run("NzU0MTYyMjA3MzYwNTQ4OTk0.X4XMxQ.jVzz9XR99ZRvp5IRaJjNDl_OoNU", bot=False)