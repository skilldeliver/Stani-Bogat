from discord.ext import commands


class Stop:
    def __init__(self, bot):
        self.bot = bot
        self.player_id = str()

    @commands.command(name='спирам')
    async def terminate(self, ctx):
        self.player_id = str(ctx.author.id)
        game = self.bot.games[self.player_id]
        del self.bot.games[self.player_id]

        await ctx.send(f'<@{self.player_id}>, твоята игра приключи.\
Тръгваш си с {game.return_money(wrong_answer=False)} лева.')


def setup(bot):
    bot.add_cog(Stop(bot))
