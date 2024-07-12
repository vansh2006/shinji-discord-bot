from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Bot Ping Checker
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Shinji is running at `{round(self.client.latency * 1000)}` milliseconds of delay!")


def setup(bot):
    bot.add_cog(Ping(bot))
