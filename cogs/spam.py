from discord.ext import commands
import discord


class Dice(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Roll a dice
    @commands.has_any_role("Owner")
    @commands.command()
    async def spam(self, ctx, num, message):
        for i in range(int(num)):
            await ctx.send(f'{message}')


def setup(bot):
    bot.add_cog(Dice(bot))
