import discord
from discord.ext import commands

TITLE = "Shinji Help"
DESCRIPTION = "User `.help <command>` for extended information on a command."

FUN_COMMANDS = "```roast, dog, 8ball, rps, mohit, explode```"
MISCELLANEOUS_COMMANDS = "```profile, pfp, ping, dice, art, snipe, time, speech```"
INTERACTIVE_COMMANDS = "```yeet, hug, slap, kill, wave```"


class Help(commands.Cog):

    def __init__(self, bot):
        self.client = bot

    # Custom Help Command
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(
            title=TITLE,
            description=DESCRIPTION,
            colour=ctx.author.colour
        )
        em.add_field(name=":japanese_goblin: Fun", value=FUN_COMMANDS, inline=False)
        em.add_field(name=":reminder_ribbon: Miscellaneous", value=MISCELLANEOUS_COMMANDS, inline=False)
        em.add_field(name=":open_hands: Interaction", value=INTERACTIVE_COMMANDS, inline=False)
        em.set_footer(text="The bot prefix is set to '.'")
        await ctx.send(embed=em)

    # Help command submenu for DICE command
    @help.command()
    async def dice(self, ctx):
        em = discord.Embed(
            title="Dice",
            description="Command to roll a dice with any amount of sides",
            colour=ctx.author.colour
        )
        em.add_field(name="**Fun Fact**", value="You can input a number to choose how many sides the dice has")
        em.add_field(name="**Syntax**", value="To use this command, do: *.dice <number>*", inline=False)
        await ctx.send(embed=em)

    # Help command submenu for ROAST command
    @help.command()
    async def roast(self, ctx):
        em = discord.Embed(
            title="Roast",
            description="Absolutely **ROAST** the living sh8t out of someone lol",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.roast <username>*")
        await ctx.send(embed=em)

    # Help command submenu for PROFILE PICTURE command (pfp)
    @help.command()
    async def pfp(self, ctx):
        em = discord.Embed(
            title="Profile Picture",
            description="You can use this command to show someone's profile picture!",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.pfp <username>*")
        await ctx.send(embed=em)

    # Help command submenu for USER PROFILE command
    @help.command()
    async def profile(self, ctx):
        em = discord.Embed(
            title="Profile",
            description="This command will show a user's guild profile!",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.profile <username>*")
        await ctx.send(embed=em)

    # Help command submenu for PING/LATENCY command
    @help.command()
    async def ping(self, ctx):
        em = discord.Embed(
            title="Ping (Latency)",
            description="Show's the bot response latency speed.",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.ping*")
        await ctx.send(embed=em)

    # Help command submenu for CLEAR/PURGE command
    @help.command()
    async def clear(self, ctx):
        em = discord.Embed(
            title="Clear",
            description="The command to *purge* messages in a text channel >:)\n"
                        "'<number>' is the number of messages you wish to delete",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.clear <number>*")
        await ctx.send(embed=em)

    # Help command submenu for 8BALL command
    @help.command(aliases=["8ball"])
    async def _8ball(self, ctx):
        em = discord.Embed(
            title="8 Ball",
            description="This command will answer any *yes or no* question!",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.8ball <question>*")
        await ctx.send(embed=em)

    # Help command submenu for DOG command
    @help.command()
    async def dog(self, ctx):
        em = discord.Embed(
            title="Dog",
            description="The greatest showcase of all the dogs",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.dog*")
        await ctx.send(embed=em)

    # Help command submenu for EXPLODE command
    @help.command()
    async def explode(self, ctx):
        em = discord.Embed(
            title="Explode",
            description="The command to start a countdown to an explosion!",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.explode*")
        await ctx.send(embed=em)

    # Help command submenu for Rock Paper Scissors command
    @help.command()
    async def rps(self, ctx):
        em = discord.Embed(
            title="RPS: Rock Paper Scissors",
            description="This command let's you play the game: rock paper scissors.",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.rps <option>*\n"
                                              "Options are: 'rock' 'paper' 'scissors'\n"
                                              "These are the only options available.")
        await ctx.send(embed=em)

    # Help command submenu for TEXT ART command
    @help.command()
    async def art(self, ctx):
        em = discord.Embed(
            title="Text Art",
            description="This command create text art.",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value='For one word art: *.art <text>*\n'
                                              'For multi word art: *.art <"text">*\n'
                                              'To create text art of multiple words, you must use double quotes.')
        await ctx.send(embed=em)

    # Help command submenu for YEET command
    @help.command()
    async def yeet(self, ctx):
        em = discord.Embed(
            title="Yeet",
            description="This command is used to YEET people lol!",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.yeet <username>*")
        await ctx.send(embed=em)

    # Help command submenu for HUG command
    @help.command()
    async def hug(self, ctx):
        em = discord.Embed(
            title="Hug",
            description="You can hug people with this command <3",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.hug <username>*")
        await ctx.send(embed=em)

    # Help command submenu for HUG command
    @help.command()
    async def slap(self, ctx):
        em = discord.Embed(
            title="Slap",
            description="You can slap people with this command LOL!",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.slap <username>*")
        await ctx.send(embed=em)

    # Help command submenu for KILL command
    @help.command()
    async def kill(self, ctx):
        em = discord.Embed(
            title="Kill",
            description="The command to kill members...",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.kill <username>*")
        await ctx.send(embed=em)

    # Help command submenu for MOHIT command
    @help.command()
    async def mohit(self, ctx):
        em = discord.Embed(
            title="Mohit",
            description="Nicknames more mohit >:)",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.mohit*")
        await ctx.send(embed=em)

    # Help command submenu for SNIPE command
    @help.command()
    async def snipe(self, ctx):
        em = discord.Embed(
            title="Snipe",
            description="This command can dig up any messages deleted 60 seconds ago :)",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.snipe*")
        await ctx.send(embed=em)

    # Help command submenu for SNIPE command
    @help.command()
    async def wave(self, ctx):
        em = discord.Embed(
            title="Wave",
            description="You can wave at people using this command!)",
            colour=ctx.author.colour
        )
        em.add_field(name="**Syntax**", value="*.wave <username>*")
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Help(bot))
