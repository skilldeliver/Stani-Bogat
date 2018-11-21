from discord.ext import commands


class Rules:
    """ Handles this cog - правила"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='правила')
    async def print_rules(self, ctx):
        await ctx.send(f'<@{ctx.author.id}>, отпечатват се правилата.')


def setup(bot):
    bot.add_cog(Rules(bot))
