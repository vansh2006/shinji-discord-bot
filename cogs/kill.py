import gif_index
import random
import discord
from discord.ext import commands


class Kill(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # kill someone out the sky xD
    @commands.command()
    async def kill(self, ctx, user: discord.Member = None):
        if not user:
            user = ctx.author
        kill_phrases = [f"{user.display_name} was killed...",
                        f"{ctx.author.display_name} just killed {user.display_name}",
                        f"OMG {ctx.author.display_name} killed {user.display_name}!",
                        f"YOO {user.display_name} just died!",
                        f"{user.display_name} was killed by {ctx.author.display_name}..."]
        if ctx.author.id == user.id:
            kill_phrases = [f"{user.display_name} is killing themselves..?"]
        kill_embed = discord.Embed(
            title=random.choice(kill_phrases),
            colour=ctx.author.colour
        )
        url = random.choice(gif_index.kill_gif)
        if str(user) == "Shinji#2956":
            url = "https://media1.tenor.com/images/9dfd073104b43994dd66b216855ad371/tenor.gif?itemid=5881539"
        kill_embed.set_image(url=url)
        await ctx.send(embed=kill_embed)


def setup(bot):
    bot.add_cog(Kill(bot))
