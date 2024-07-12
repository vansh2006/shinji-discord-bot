import discord
from discord.ext import commands


class Profile(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Show a user's guild profile/data
    @commands.command()
    async def profile(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        em = discord.Embed(
            title=f"{user.name}'s Profile:",
            colour=user.colour
        )
        em.add_field(name=":busts_in_silhouette: Nickname", value=f"{user.display_name}", inline=False)
        em.add_field(name=":bow_and_arrow: Status", value=f"{user.activity}")
        em.add_field(name=":alarm_clock: Date Joined", value=f"{user.joined_at}", inline=False)
        em.add_field(name=":tools: Highest Role", value=f"User's Highest Role: `{user.top_role}`", inline=False)
        em.set_footer(text=f"{ctx.guild.name} | {user}")
        user_avatar = user.avatar_url
        em.set_thumbnail(url=user_avatar)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Profile(bot))
