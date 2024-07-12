import gif_index
import random
import discord
from discord.ext import commands


class Yeet(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Yeet someone out the sky xD
    @commands.command()
    async def yeet(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        yeet_phrases = [f"Bruh, {user.display_name} was yeeted out the sky",
                        f"Imagine being yeeted, {user.display_name}!",
                        f"Hey {user.display_name}, are ya 'havin fun up there?",
                        f"YOO {user.display_name} just got YEETED!",
                        f"{user.display_name} just went flying..."]
        if ctx.author.id == user.id:
            yeet_phrases = [f"{user.display_name} is yeeting themselves..?"]
        yeet_embed = discord.Embed(
            title=random.choice(yeet_phrases),
            colour=ctx.author.colour
        )
        url = random.choice(gif_index.yeet_gif)
        if str(user) == "Shinji#2956":
            url = "https://media1.tenor.com/images/738829fcb07c26490e4e76d3833644be/tenor.gif?itemid=5857525"
        yeet_embed.set_image(url=url)
        await ctx.send(embed=yeet_embed)


def setup(bot):
    bot.add_cog(Yeet(bot))
