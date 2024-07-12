import discord
import requests
import random
from discord.ext import commands


class Dog(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Send cute dog images
    @commands.command()
    async def dog(self, ctx):
        images = requests.get('https://dog.ceo/api/breeds/image/random')
        dog_titles = ['Look at dis doggo', 'If you are a cat person ur bad :dog2:',
                      'Now tell me whos a good boyy', 'Where that puppy at??', ':dog: Fetch doggo FETCH!',
                      'I wonder what breed this one is...', 'Look, its a wild dog!',
                      'Is that supposed to be a dog or a T-Rex?', 'Reject doggo, return to  **m o n k e!**']
        value = random.randint(0, 0xffffff)
        em = discord.Embed(
            title=random.choice(dog_titles),
            colour=value
        )
        em.set_image(url=images.json()['message'])

        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Dog(bot))
