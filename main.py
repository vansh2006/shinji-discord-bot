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
@bot.event
async def on_ready():
    print("Let's get this party started!")


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



# Member joined event
#@bot.event
#async def on_member_join(member):
#    channel = bot.get_channel(809097200923049994)
#    print(f'{member} has joined the server.')
#    await channel.send(f'Welcome to the server {member.mention}!')


# Member left event
#@bot.event
#async def on_member_remove(member):
#    channel = bot.get_channel(809097200923049994)
#    print(f'{member} has left the server.')
#    await channel.send(f'{member.mention} has left the server')


# Spam
# @bot.command()
# @commands.is_owner()
# async def spam(ctx, *, num):
#     try:
#         await ctx.send(f"What do you want to spam?")
#
#         def check(msg):
#             return msg.author == ctx.author and msg.channel == ctx.channel
#
#         msg = await bot.wait_for("message", check=check)
#
#         for i in range(int(num)):
#             await ctx.send(f'{msg.content}')
#     except:
#         pass



# Fun commands honestly I don't even know lmao
# @bot.command()
# async def gucci(ctx):
#     await ctx.send('gang')
#
#
# # Name Game :D
# @bot.command("ngame")
# async def nameGame(ctx, name):
#     nameLength = int(len(name))
#     namewithoutfirst = name[1:nameLength]
#     if name[0] == "a" or "e" or "i" or "o" or "u":
#         namewithoutfirst = name
#     else:
#         namewithoutfirst = name[1:nameLength]
#     await ctx.send(f"{name}, {name}, bo-b{namewithoutfirst}\nbanana-fana fo-f{namewithoutfirst}\n"
#                    f"fee-fi-mo-m{namewithoutfirst}\n{name}!")

#INSERT Discord Provided bot TOKEN in quotations:
bot.run('')
