from discord.ext import commands

from bot.json_util import get_pending

class Approve:
    def __init__(self, bot):
        self.bot = bot
        self.ctx = None
        self.question = None


    @commands.command(name='pending')
    async def get_question(self, ctx):
        self.ctx = ctx
        if self.question:
            await ctx.send('Незатворен въпрос!')
            await self._send_question()
            return

        self.question = get_pending()
        await self._send_question()

    @commands.command(name='approve')
    async def approve_question(self, ctx, arg):
        pass

    async def _send_question(self):
        string = str()
        for k, v in self.question.items():
            string += f'{k}:{v}\n'

        await self.ctx.send(f'```{string}```')

    @commands.command(name='change')
    async def approve_question(self, ctx, key, value):
        self.ctx = ctx

        self.question[key] = value
        await self._send_question()


def setup(bot):
    bot.add_cog(Approve(bot))