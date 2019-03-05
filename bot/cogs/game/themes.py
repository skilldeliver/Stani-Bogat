from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.embeds import ThemesEmbed
from bot.core.replies import Reply
from bot.utilities.jsoner import save_player


class Themes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_id = str()

    @commands.guild_only()
    @commands.command(name=Cogs.Game.themes)
    async def print_themes(self, ctx):
        await ctx.send(embed=ThemesEmbed())


def setup(bot):
    bot.add_cog(Themes(bot))
