import random
from discord.ext import commands


class Rps(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Rock Paper Scissor (Jan Ken Po)
    @commands.command()
    async def rps(self, ctx, user_choice):
        options = ["rock", "paper", "scissors"]
        bot_choice = random.choice(options)

        if user_choice == "rock":
            if bot_choice == "rock":
                await ctx.reply(f"Argh, we tied.\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
            elif bot_choice == "paper":
                await ctx.reply(
                    f"Nice try bud, I won!\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
            elif bot_choice == "scissors":
                await ctx.reply(
                    f"Wow, you won.\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")

        elif user_choice == "paper":
            if bot_choice == "rock":
                await ctx.reply(f"The paper beats the rock!\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
            elif bot_choice == "paper":
                await ctx.reply(f"Oof, we tied.\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
            elif bot_choice == "scissors":
                await ctx.reply(f"Damn, you won.\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")

        elif user_choice == "scissors":
            if bot_choice == "rock":
                await ctx.reply(f"HAHA! I just CRUSHED you!\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
            elif bot_choice == "paper":
                await ctx.reply(f"Bruh, you won.\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
            elif bot_choice == "scissors":
                await ctx.reply(f"Oh well, we tied.\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
        elif user_choice == "scissor":
            if bot_choice == "rock":
                await ctx.reply(f"HAHA! I just CRUSHED you!\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
            elif bot_choice == "paper":
                await ctx.reply(f"Bruh, you won.\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
            elif bot_choice == "scissors":
                await ctx.reply(f"Oh well, we tied.\nYour choice: `{user_choice}`\nMy choice: `{bot_choice}`")
        else:
            await ctx.reply("Heyyy you used an option that doesn't exist! \n"
                            "Try using: [a] `rock`, [b] `paper`, or [c] `scissor(s)`")


def setup(bot):
    bot.add_cog(Rps(bot))
