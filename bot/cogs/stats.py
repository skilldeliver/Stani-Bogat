from discord.ext import commands


class Stats:
    """ Handles these cogs - топ10, статс"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='топ10', aliases=['топ'])
    async def print_top10(self, ctx):
        await ctx.send(f'<@{ctx.author.id}>, отпечатва се класацията.')

    @commands.command(name='статс', aliases=['стат'])
    async def stats(self, ctx):
        await ctx.send(f'<@{ctx.author.id}>, отпечатва се статистиката на юзъра.')


def setup(bot):
    bot.add_cog(Stats(bot))
