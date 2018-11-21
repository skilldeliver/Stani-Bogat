import asyncio

from discord.ext import commands

from bot.core.game import Game
from bot.core.embeds import QuestionEmbed


class NewGame:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='игра', aliases=['новаигра'])
    async def new_game(self, ctx):
        '''
        Creates new Game.
        Add it to the game queue (dictionary).
        Key - string of the user ID
        Value - instance of the bot.core.game.Game class
        '''

        # get a User object of the author
        user = self.bot.get_user(ctx.author.id)
        user_id = str(user.id)

        if user_id in self.bot.games:
            await ctx.send(f'<@{user_id}>, все още не си приключил играта ти.')
            return

        # Create new Game and bind it to the user_id in the queue
        self.bot.games[user_id] = Game(user)
        await ctx.send(f'<@{user_id}>, твоята игра започва сега!')
        await asyncio.sleep(1)

        # ask the first question
        question_data = self.bot.games[user_id].ask()
        embed = QuestionEmbed(**question_data)

        self.bot.games[user_id].last_question = question_data
        self.bot.games[user_id].last_embed = await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(NewGame(bot))
