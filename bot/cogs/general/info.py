import shutil
from platform import python_version, uname


import discord
from discord.ext import commands
import github
import psutil

from bot.core.constants import Cogs
from bot.core.embeds import InfoEmbed


class Info:
    """ Handles this cog - инфо"""
    def __init__(self, bot):
        self.bot = bot
        self.g = github.Github('boneredcoder', 'stanibogatbot1')

    @commands.command(name=Cogs.General.info)
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
        ram = dict(psutil.virtual_memory()._asdict())['used'] / 2 ** 30
        ram = round(ram, 2)
        ram_tot = dict(psutil.virtual_memory()._asdict())['total'] / 2 ** 30
        ram_tot = round(ram_tot, 2)
        cpu = psutil.cpu_percent()

        total, used, free = shutil.disk_usage('/')
        hdd_tot = round(total // (2**30), 2)
        hdd = round(used // (2**30), 2)

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
                          ram=ram,
                          ram_tot=ram_tot,
                          hdd=hdd,
                          hdd_tot=hdd_tot)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
