import random
from discord.ext import commands


class eight_ball(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # 8ball to predict/answer yes or no questions
    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, question):
        try:
            yes_responses = random.choice(["Yes!", "It is decidedly so", "Without a doubt", "Yup, for sure",
                                           "The answer is yes!", "As I see it, yep", "Signs point to yes", "Of course",
                                           "Indeed", "Certainly"])
            no_responses = random.choice(["No...", "Nope.", "My sources say no",
                                          "Not a chance", "Nope", "Not a chance", "I'd say no", "Very doubtful"])
            maybe_responses = random.choice(["Maybe", "Perhaps"])
            dont_know_responses = random.choice(["Ask again."])
            punctuation = random.choice(["!", "."])
            responses = [yes_responses, no_responses, maybe_responses, dont_know_responses]
            final_response = f"{random.choice(responses)}{punctuation}"
            await ctx.reply(final_response)
        except:
            await ctx.reply("Well at least ask the 8ball a *question* ya big oaf!")


def setup(bot):
    bot.add_cog(eight_ball(bot))
