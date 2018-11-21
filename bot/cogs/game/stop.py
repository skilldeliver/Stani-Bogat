from discord.ext import commands


class Stop:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='спирам')
    async def terminate(self, ctx):
        user_id = str(ctx.author.id)
        game = self.bot.games[user_id]
        del self.bot.games[user_id]

        await ctx.send(f'<@{user_id}>, твоята игра приключи.\
Тръгваш си с {game.return_money(wrong_answer=False)} лева.')


def setup(bot):
    bot.add_cog(Stop(bot))
