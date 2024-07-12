import gif_index
import random
import discord
from discord.ext import commands


class Wave(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Wave at someone :D
    @commands.command()
    async def wave(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        wave_phrases = [f"{ctx.author.display_name} is waving to {user.display_name}!",
                       f"{ctx.author.display_name} waved to {user.display_name}!",
                       f"{ctx.author.display_name} is waving at {user.display_name}!",
                       f"{user.display_name} is being waved to by {ctx.author.display_name}!"]
        if ctx.author.id == user.id:
            wave_phrases = [f"{user.display_name} is waving at themselves..?"]
        wave_embed = discord.Embed(
            title=random.choice(wave_phrases),
            colour=ctx.author.colour
        )
        url = random.choice(gif_index.wave_gif)
        wave_embed.set_image(url=url)
        await ctx.send(embed=wave_embed)


def setup(bot):
    bot.add_cog(Wave(bot))
