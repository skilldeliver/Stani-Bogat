import discord
from discord.ext import commands

from bot.core.constants import GOD, Path, File


def is_god():
    def predicate(ctx):
        return ctx.message.author.id == GOD
    return commands.check(predicate)


class God:
    def __init__(self, bot):
        self.bot = bot
        self.ctx = None
        self.question = None

    @is_god()
    @commands.command(name='get_globals')
    async def get_globals(self, ctx):
        f1 = str(Path.global_stats.joinpath(File.players))
        f2 = str(Path.global_stats.joinpath(File.authors))

        file1 = discord.File(f1)
        file2 = discord.File(f2)

        await ctx.send(files=[file1, file2])

    @is_god()
    @commands.command(name='get_pending')
    async def get_pending(self, ctx):
        f = str(Path.pending.joinpath(File.pending_questions))
        file = discord.File(f)

        await ctx.send(file=file)

    @is_god()
    @commands.command(name='get_questions')
    async def get_questions(self, ctx, arg):
        for i in range(1, 16):
            f = str(Path.questions.joinpath(f'{arg}/' + str(i).zfill(2) + '/' + File.json))
            await ctx.send(file=discord.File(f, filename=str(i)))

    @is_god()
    @commands.command(name='shutdown')
    async def shutdown(self, ctx):
        await self.bot.logout()

def setup(bot):
    bot.add_cog(God(bot))