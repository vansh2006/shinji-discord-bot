import pyfiglet
from discord.ext import commands


class Art(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Text Art Command
    @commands.command("art")
    async def text_art(self, ctx, message):
        result = pyfiglet.figlet_format(message)
        art = f"```{result}```"
        await ctx.send(art)


def setup(bot):
    bot.add_cog(Art(bot))
