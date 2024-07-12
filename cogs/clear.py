from discord.ext import commands


class Clear(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Message Deleter/Purger
    @commands.command()
    @commands.has_any_role("Admin", "Owner", "Co-Owner")
    async def clear(self, ctx, amount):
        await ctx.channel.purge(limit=int(amount) + 1)


def setup(bot):
    bot.add_cog(Clear(bot))
