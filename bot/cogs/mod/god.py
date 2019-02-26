import discord
from discord.ext import commands

from bot.core.constants import GOD, Path, File, Gif, Cogs


def is_god():
    def predicate(ctx):
        return ctx.message.author.id == GOD
    return commands.check(predicate)


class God(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ctx = None
        self.question = None

    @is_god()
    @commands.command(name='get_servers')
    async def return_servers(self, ctx):
        for guild in self.bot.guilds:
            owner = self.bot.get_user(guild.owner_id)
            s = f'''
Guild name: {guild.name}
Guild icon: {guild.icon_url}
Guild owner: {owner}
------------------------'''
            await ctx.send(s + '\n\n')

    @commands.command(name='help')
    async def help(self, ctx):
        await ctx.send('Тази команда е илюзия на твоето съзнание.')

    @is_god()
    @commands.command(name='test')
    async def test(self, ctx):
        await ctx.send(Gif.win)

    @is_god()
    @commands.command(name=Cogs.God.globals)
    async def get_globals(self, ctx):
        f1 = str(Path.global_stats.joinpath(File.players))
        f2 = str(Path.global_stats.joinpath(File.authors))

        file1 = discord.File(f1)
        file2 = discord.File(f2)

        await ctx.send(files=[file1, file2])

    @is_god()
    @commands.command(name=Cogs.God.pending)
    async def get_pending(self, ctx):
        f = str(Path.pending.joinpath(File.pending_questions))
        file = discord.File(f)

        await ctx.send(file=file)

    @is_god()
    @commands.command(name=Cogs.God.questions)
    async def get_questions(self, ctx, arg):
        for i in range(1, 16):
            f = str(Path.questions.joinpath(f'{arg}/' + str(i).zfill(2) + '/' + File.json))
            await ctx.send(file=discord.File(f, filename=str(i).zfill(2) + '.json'))

    @is_god()
    @commands.command(name=Cogs.God.shutdown)
    async def shutdown(self, ctx):
        quit()

def setup(bot):
    bot.add_cog(God(bot))