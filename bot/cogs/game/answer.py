import asyncio

from discord.ext import commands

from bot.core.embeds import QuestionEmbed, RightAnswerEmbed, WrongAnswerEmbed


class Answer:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='А', aliases=list("БВГабвг"))
    async def take_answer(self, ctx):
        user_id = str(ctx.author.id)
        game = self.bot.games[user_id]

        if user_id not in self.bot.games.keys():
            await ctx.send(f'<@{user_id}>, не си в игра.')
        else:
            await asyncio.sleep(0.5)
            answer = ctx.message.content[1:].upper()

            if self.bot.games[user_id].correct_answer(answer):
                await ctx.message.add_reaction('\u2705')
                embed = RightAnswerEmbed()
                await ctx.send(embed=embed)

                await asyncio.sleep(1.5)
                question_data = self.bot.games[user_id].ask()
                embed = QuestionEmbed(**question_data)

                game.last_question = question_data
                game.last_embed = await ctx.send(embed=embed)
            else:
                await ctx.message.add_reaction('\u274C')
                embed = WrongAnswerEmbed()
                await ctx.send(embed=embed)
                del self.bot.games[user_id]

                await asyncio.sleep(1.5)
                await ctx.send(f'<@{user_id}>, твоята игра приключи. \
Тръгваш си с - {game.return_money()} лева.')


def setup(bot):
    bot.add_cog(Answer(bot))
