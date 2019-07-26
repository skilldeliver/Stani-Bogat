import re
from discord.ext import commands

from bot.core.constants import Cogs, Regex
from bot.core.replies import Reply
from bot.core.embeds import Top10Embed, Total, StatsEmbed
from bot.utilities.jsoner import return_top_authors, return_top_players, total, get_player_stats

class Stats(commands.Cog):
    """ Handles these cogs - топ10, статс"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name=Cogs.Stats.top10, aliases=[Cogs.Stats.top])
    async def print_top10(self, ctx, arg): # автори or играчи
        if arg == Cogs.Stats.authors:
            authors = return_top_authors(10)
            await ctx.send(embed=Top10Embed('authors', authors))
        elif arg == Cogs.Stats.players:
            raw_players = return_top_players(10)
            players = list()

            for p in raw_players:
                u = self.bot.get_user(int(p[0]))
                players.append((u, p[1]))
            await ctx.send(embed=Top10Embed('players', players))

    @commands.command(name=Cogs.Stats.general)
    async def total(self, ctx):
        await ctx.send(embed=Total(**total()))

    @commands.command(name=Cogs.Stats.stat, aliases=[Cogs.Stats.stats])
    async def stats(self, ctx, *args):
        if not args:
            user_id = ctx.author.id
        else:
            user_id = self._extract_id_from_tag(args[0])

        print(user_id)
        user = self.bot.get_user(user_id)
        stats = get_player_stats(str(user_id))

        if not stats:
            await ctx.send(f'<@{user_id}> няма Ви в дата базата. Ако мислите, че има проблем свържете се с модераторите.')
            return

        secs = stats['time']
        mins = secs // 60
        hours = mins // 60

        time = f'{hours} hours {mins % 60} mins {secs % 60} secs'
        embed = StatsEmbed(name=user.name,
                           img_url=user.avatar_url,
                           games=stats['games'],
                           time=time,
                           money=stats['money'])
        await ctx.send(embed=embed)


    @staticmethod
    def _extract_id_from_tag(tag):
        try:
            user_id = re.search(Regex.user_id, tag).group(1)
            return int(user_id)
        except Exception:
            return None

def setup(bot):
    bot.add_cog(Stats(bot))
