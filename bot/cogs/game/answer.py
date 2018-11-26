import asyncio

from discord.ext import commands

from bot.core.embeds import QuestionEmbed, RightAnswerEmbed, WrongAnswerEmbed


class Answer:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='А', aliases=list("БВГабвг"))
    async def take_answer(self, ctx):
        user_id = str(ctx.author.id)  # id of the player or helper

        for game in self.bot.games.values():
            if game.waiting_audience_help:
                if user_id != str(game.user.id):  # should be different
                    letter = ctx.message.content[1:].upper()
                    game.audience_votes[f'{letter})'].add(user_id)
                    return

        print(self.bot.helping_friends)

        if user_id in self.bot.helping_friends.keys():  # this is the second case when the helper is invoked
            letter = ctx.message.content[1:].upper()
            helper = self.bot.get_user(ctx.author.id) # the discord.User object of the helper
            help_for = self.bot.helping_friends[str(helper.id)]

            game = self.bot.games[help_for]

            val = game.last_question['answers'][letter + ')']
            del game.last_question['answers'][letter + ')']
            game.last_question['answers'][f'{letter})     {helper.name}'] = val

            print(game.last_question)
            game = QuestionEmbed(**game.last_question)
            await game.last_embed.edit(embed=embed)

            return

        if user_id not in self.bot.games.keys():
            await ctx.send(f'<@{user_id}>, не си в игра.')
        else:
            game = self.bot.games[user_id]  # the game of the player
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
