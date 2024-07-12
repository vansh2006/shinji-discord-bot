import gif_index
import random
import discord
from discord.ext import commands


class Hug(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Hug someone <3
    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        hug_phrases = [f"{ctx.author.display_name} is giving {user.display_name} a hug!",
                       f"{ctx.author.display_name} hugged {user.display_name}!",
                       f"{ctx.author.display_name} is hugging {user.display_name}!",
                       f"{user.display_name} is being hugged by {ctx.author.display_name}!"]
        if ctx.author.id == user.id:
            hug_phrases = [f"{user.display_name} is hugging themselves..?"]
        hug_embed = discord.Embed(
            title=random.choice(hug_phrases),
            colour=ctx.author.colour
        )
        url = random.choice(gif_index.hug_gif)
        if str(user) == "Shinji#2956":
            url = "https://media1.tenor.com/images/4d08ef0489b3e7fadeba192e33338916/tenor.gif?itemid=19552747"
        hug_embed.set_image(url=url)
        await ctx.send(embed=hug_embed)


def setup(bot):
    bot.add_cog(Hug(bot))
