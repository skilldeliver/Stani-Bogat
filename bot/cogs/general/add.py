from discord.ext import commands

from bot.core.embeds import HowToAddEmbed


class Add:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='добави')
    async def print_how_to_add(self, ctx):
        await ctx.send(embed=HowToAddEmbed())

    @commands.command(name='добавям')
    async def print_rules(self, ctx):
        await ctx.send()


def setup(bot):
    bot.add_cog(Add(bot))
