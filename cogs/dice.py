import random
from discord.ext import commands


class Dice(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Roll a dice
    @commands.command()
    async def dice(self, ctx, limit=6):
        rolled_num = random.randint(1, int(limit))
        await ctx.send(f"You rolled `{rolled_num}`")


def setup(bot):
    bot.add_cog(Dice(bot))
