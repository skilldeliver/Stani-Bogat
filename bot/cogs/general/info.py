from platform import python_version, uname


import discord
from discord.ext import commands
import github
import psutil

from bot.core.embeds import InfoEmbed


class Info:
    """ Handles this cog - инфо"""
    def __init__(self, bot):
        self.bot = bot
        self.g = github.Github('none', 'none')

    @commands.command(name='инфо')
    async def print_info(self, ctx):
        # versions stuff
        python_v = python_version()
        discord_v = discord.__version__

        # repo stuff
        repo = self.g.get_repo("skilldeliver/Stani-Bogat")
        stars = repo.stargazers_count
        issues = repo.open_issues_count
        forks = repo.forks_count

        # servers stuff
        connected_servers = int()
        total_members = int()
        for guild in self.bot.guilds:
            connected_servers += 1
            total_members += guild.member_count

        # pc stuff
        pc = uname()
        ram = dict(psutil.virtual_memory()._asdict())['used'] / 2 ** 20
        ram = round(ram, 2)
        cpu = psutil.cpu_percent()

        embed = InfoEmbed(
                          python_version=python_v,
                          discord_version=discord_v,
                          stars=stars,
                          forks=forks,
                          issues=issues,
                          connected_servers=connected_servers,
                          total_members=total_members,
                          pc=pc,
                          cpu_use=cpu,
                          ram=ram)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
