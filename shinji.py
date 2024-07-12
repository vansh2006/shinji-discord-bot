import discord
import os
# from prsaw import RandomStuff
from discord.ext import commands, tasks
from itertools import cycle

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
bot = commands.Bot(command_prefix='.', intents=intents)
status = cycle(['Code Mania', 'Shinji Dynasty'])
bot.remove_command("help")


# Change the bots status/presence
@tasks.loop(seconds=30)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.command()
async def load_cog(cog):
    bot.load_extension(f"cogs.{cog}")


@bot.command()
async def unload_cog(cog):
    bot.unload_extension(f"cogs.{cog}")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


@bot.event
async def on_ready():
    print("Let's get this party started!")



# rs = RandomStuff(async_mode=True)
#
#
# @bot.event
# async def on_message(message):
#     # chat_bot_on = True
#     # while chat_bot_on:
#     if bot.user == message.author:
#         return
#     if message.channel.id == 825114726932807700 :
#         response = await rs.get_ai_response(message.content)
#         await message.reply(response)
#     await bot.process_commands(message)

#INSERT Discord Provided bot TOKEN in quotations:
bot.run('')
