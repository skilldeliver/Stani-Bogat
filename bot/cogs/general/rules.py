from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.embeds import RulesEmbed


class Rules:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name=Cogs.General.rules)
    async def print_rules(self, ctx):
        await ctx.send(embed=RulesEmbed())


def setup(bot):
    bot.add_cog(Rules(bot))
