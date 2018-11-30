from discord.ext import commands

from bot.core.embeds import InfoEmbed


class Info:
    """ Handles this cog - инфо"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='инфо')
    async def print_info(self, ctx):
        connected_servers = int()
        total_members = int()

        for guild in self.bot.guilds:
            connected_servers += 1
            total_members += guild.member_count

        embed = InfoEmbed(connected_servers=len(self.bot.guilds),
                          total_members=total_members)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
