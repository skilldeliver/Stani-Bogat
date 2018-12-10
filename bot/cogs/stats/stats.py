from discord.ext import commands

from bot.core.embeds import Top10Embed
from bot.json_util import return_top

class Stats:
    """ Handles these cogs - топ10, статс"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='топ10', aliases=['топ'])
    async def print_top10(self, ctx, arg): # автори or играчи
        if arg == 'автори':
            authors = return_top(target='authors', how=10)
            await ctx.send(embed=Top10Embed('authors', authors))
        elif arg == 'играчи':
            players = return_top(target='players', how=10)
            await ctx.send(embed=Top10Embed('players', players))

    @commands.command(name='статс', aliases=['стат'])
    async def stats(self, ctx):
        await ctx.send(f'<@{ctx.author.id}>, отпечатва се статистиката на юзъра.')


def setup(bot):
    bot.add_cog(Stats(bot))
