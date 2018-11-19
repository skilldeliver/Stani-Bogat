from discord.ext import commands

from bot.core.embeds import InfoEmbed


class Info:
    """ Handles this cog - инфо"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='инфо')
    async def print_info(self, ctx):
        alist = list()
        for guild in self.bot.guilds:
            for member in guild.members:
                alist.append(member.name)

        embed = InfoEmbed(connected_servers=len(self.bot.guilds))
        await ctx.send(embed=embed)
        # await ctx.send(f'<@ctx.author.id>, {alist} отпечатват се информация.')


def setup(bot):
    bot.add_cog(Info(bot))
