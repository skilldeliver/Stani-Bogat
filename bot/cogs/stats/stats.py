from time import strftime, gmtime

from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.replies import Reply
from bot.core.embeds import Top10Embed, Total, StatsEmbed
from bot.utilities.jsoner import return_top_authors, return_top_players, total, get_player_stats

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
            raw_players = return_top_players(1000)
            players = list()

            for p in raw_players:
                u = self.bot.get_user(int(p[0]))
                players.append((u, p[1]))
            await ctx.send(embed=Top10Embed('players', players))

    @commands.command(name=Cogs.Stats.general)
    async def total(self, ctx):
        await ctx.send(embed=Total(**total()))

    @commands.command(name=Cogs.Stats.stat, aliases=[Cogs.Stats.stats])
    async def stats(self, ctx):
        user_id = str(ctx.author.id)
        user = self.bot.get_user(ctx.author.id)
        stats = get_player_stats(user_id)

        if not stats:
            await ctx.send(f'<@{user_id}> няма Ви в дата базата. Ако мислите, че има проблем свържете се с модераторите.')
            return

        time = strftime('%H hours %M mins %S secs', gmtime(stats['time']))
        embed = StatsEmbed(name=user.name,
                           img_url=user.avatar_url,
                           games=stats['games'],
                           time=time,
                           money=stats['money'])
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Stats(bot))
