from discord.ext import commands
import discord


class Ban(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Command to ban members
    @commands.command()
    @commands.has_any_role("Admin", "Owner", "Co-Owner")
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')


def setup(bot):
    bot.add_cog(Ban(bot))
