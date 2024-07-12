import discord
import random
import roast_index
from discord.ext import commands


class Roast(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Absolutely ROAST the living sh8t out of someone lol
    @commands.command()
    async def roast(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        random_roast = random.choice(roast_index.roast_list)
        value = user.colour
        em = discord.Embed(
            description=f"{user.mention}, {random_roast}",
            colour=value
        )
        await ctx.channel.send(embed=em)


def setup(bot):
    bot.add_cog(Roast(bot))
