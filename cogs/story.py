import random
from discord.ext import commands


class Story(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Create a fun short story!
    @commands.command()
    async def story(self, ctx):
        name = ctx.author.name
        when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']
        what = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a horse']
        residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']
        went = ['cinema', 'university', 'seminar', 'school', 'laundry']
        happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book']

        message = f"{random.choice(when)}, {name} lived in {random.choice(residence)}, went to the {random.choice(went)} with " \
                  f"{random.choice(what)} and {random.choice(happened)}"

        await ctx.reply(message)


def setup(bot):
    bot.add_cog(Story(bot))
