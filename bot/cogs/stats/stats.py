from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.embeds import Top10Embed, Total
from bot.utilities.json import return_top_authors, return_top_players, total

class Stats:
    """ Handles these cogs - топ10, статс"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name=Cogs.Stats.top10, aliases=[Cogs.Stats.top])
    async def print_top10(self, ctx, arg): # автори or играчи
        if arg == Cogs.Stats.authors:
            authors = return_top_authors(10)
            await ctx.send(embed=Top10Embed('authors', authors))
        elif arg == Cogs.Stats.players:
            players = return_top_players(10)
            await ctx.send(embed=Top10Embed('players', players))

    @commands.command(name='общо')
    async def total(self, ctx):
        await ctx.send(embed=Total(**total()))

# автори or играчи
    # @commands.command(name='статс', aliases=['стат'])
    # async def stats(self, ctx):
    #     await ctx.send(f'<@{ctx.author.id}>, отпечатва се статистиката на юзъра.')


def setup(bot):
    bot.add_cog(Stats(bot))
