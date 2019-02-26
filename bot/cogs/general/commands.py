from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.embeds import CommandsEmbed


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name=Cogs.General.commands)
    async def print_info(self, ctx):
        await ctx.send(embed=CommandsEmbed())


def setup(bot):
    bot.add_cog(Commands(bot))
