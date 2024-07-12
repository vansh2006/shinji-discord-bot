import discord
from discord.ext import commands


class Pfp(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Show a user's profile picture
    @commands.command()
    async def pfp(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        await ctx.send(member.avatar_url)


def setup(bot):
    bot.add_cog(Pfp(bot))
