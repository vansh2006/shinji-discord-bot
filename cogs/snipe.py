import asyncio
from discord.ext import commands
import discord


class Snipe(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        global snipe_message_content
        global snipe_message_author
        global created_at
        global channel_name
        global snipe_avatar
        # Variables outside a function have to be declared as global in order to be changed

        snipe_message_content = message.content
        snipe_message_author = message.author
        created_at = message.created_at
        channel_name = message.channel.name
        snipe_avatar = message.author.avatar_url
        if snipe_message_author.id == 622874167020093461 or snipe_message_author.id == 807388836983734282:
            snipe_message_author = None
            snipe_message_content = None
        else:
            print(
                f"Message: {snipe_message_content} Author: {snipe_message_author} Timestamp: {created_at} Channel: {channel_name}")

        # elif snipe_message_author.id == 538189508370235413:
        #     embed = discord.Embed(
        #         description=f'"{snipe_message_content}"',
        #         timestamp=created_at
        #     )
        #     embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}\n"
        #                           f"in #{channel_name}",
        #                      icon_url=message.author.avatar_url)
        #     embed.set_author(name=f"{snipe_message_author} said:", icon_url=snipe_avatar)
        #     await message.channel.send(embed=embed)
        # autosnipe for ravdeep :)
        await asyncio.sleep(60)
        snipe_message_author = None
        snipe_message_content = None
        created_at = None
        channel_name = None
        snipe_avatar = None

    @commands.command()
    async def snipe(self, message):
        if snipe_message_content == None:
            await message.channel.send("There's nothing to snipe.")
        elif snipe_message_author.id == 622874167020093461:
            await message.channel.send("There's nothing to snipe.")
        else:
            embed = discord.Embed(
                description=f'"{snipe_message_content}"',
                timestamp=created_at
            )
            embed.set_footer(text=f"Asked by {message.author.name}#{message.author.discriminator}\n"
                                  f"in #{channel_name}",
                             icon_url=message.author.avatar_url)
            embed.set_author(name=f"{snipe_message_author} said:", icon_url=snipe_avatar)
            await message.channel.send(embed=embed)
            return


# snipe_message_content = None
# snipe_message_author = None
# snipe_message_id = None
#
# # Event to log deleted messages
# @commands.Cog.listener()
# async def on_message_delete(self, message):
#     global snipe_message_content
#     global snipe_message_author
#     global snipe_message_id
#     # Variables outside a function have to be declared as global in order to be changed
#
#     snipe_message_content = message.content
#     snipe_message_author = message.author.name
#     await asyncio.sleep(60)
#
#     # This if statement is to check if a new message has been deleted, and if it has then it will wait
#     # another 60 seconds before deleting, or else it will use the same countdown as the message deleted earlier
#     # and delete the record of a deleted message within a few seconds only
#     if message.id == snipe_message_id:
#         snipe_message_content = None
#     snipe_message_author = None
#     snipe_message_id = None
#
# # A Snipe command to find deleted messages
# @commands.command()
# async def snipe(self, message):
#     if snipe_message_content == None:
#         await message.channel.send("There's nothing to snipe!")
#     else:
#         em = discord.Embed(
#             description=f"{snipe_message_content}",
#             colour=random.randint(0, 255))
#         em.set_author(name=str(snipe_message_author), icon_url=message.author.avatar_url)
#         await message.channel.send(embed=em)
#         return


def setup(bot):
    bot.add_cog(Snipe(bot))
