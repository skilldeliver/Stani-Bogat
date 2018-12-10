from discord.ext import commands

from bot.core.embeds import RulesEmbed


class Rules:
    """ Handles this cog - правила"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='правила')
    async def print_rules(self, ctx):
        await ctx.send(embed=RulesEmbed())


def setup(bot):
    bot.add_cog(Rules(bot))
