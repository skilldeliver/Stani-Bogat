from discord.ext import commands

from bot.core.embeds import InfoEmbed


class Info:
    """ Handles this cog - инфо"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='инфо')
    async def print_info(self, ctx):
        embed = InfoEmbed(connected_servers=len(self.bot.guilds))
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Info(bot))
