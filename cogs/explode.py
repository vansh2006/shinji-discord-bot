import time
from discord.ext import commands


class Explode(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Start a countdown and send an explosion gif
    @commands.command()
    async def explode(self, ctx):
        time_left = 5
        while time_left > 0:
            await ctx.send(time_left)
            time.sleep(1)
            time_left = time_left - 1
        await ctx.send("*Boom!*")
        await ctx.send("https://media1.tenor.com/images/2eb91897ed939dcfed0a0f1705cdd9c7/tenor.gif?itemid=16089684")
        time.sleep(50)


def setup(bot):
    bot.add_cog(Explode(bot))
