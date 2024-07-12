import gif_index
import random
import discord
from discord.ext import commands


class Slap(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # slap someone <3
    @commands.command()
    async def slap(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        slap_phrases = [f"{ctx.author.display_name} just slapped {user.display_name}!",
                        f"{user.display_name}, imagine being slapped!",
                        f"AYO {ctx.author.display_name} just slapped {user.display_name}!",
                        f"{user.display_name} just got slapped by {ctx.author.display_name}!"]
        if ctx.author.id == user.id:
            slap_phrases = [f"{user.display_name} is slapping themselves..?"]
        slap_embed = discord.Embed(
            title=random.choice(slap_phrases),
            colour=ctx.author.colour
        )
        url = random.choice(gif_index.slap_gif)
        if str(user) == "Shinji#2956":
            url = "https://media1.tenor.com/images/f7f0d538542373e7e5366b281d3772e7/tenor.gif?itemid=17303228"
        slap_embed.set_image(url=url)
        await ctx.send(embed=slap_embed)


def setup(bot):
    bot.add_cog(Slap(bot))
