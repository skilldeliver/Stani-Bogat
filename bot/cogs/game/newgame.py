import asyncio

import discord
from discord.ext import commands

from bot.core.game import Game
from bot.core.embeds import QuestionEmbed


class NewGame:
    def __init__(self, bot):
        self.bot = bot
        self.ctx = None

        self.player = None
        self.player_id = str()

    @commands.command(name='игра', aliases=['новаигра'])
    async def new_game(self, ctx):
        '''
        Creates new Game.
        Add it to the bot games (dictionary).
        Key - string of the user ID
        Value - instance of the bot.core.game.Game class
        '''
        self.ctx = ctx
        self._get_player()

        if self.player_id in self.bot.games.keys():
            await ctx.send(f'<@{self.player_id}>, все още не си\
 приключил играта ти.')
            return

        await self._create_new_game()
        await self._send_first_question()

    def _get_player(self):
        # get a User object of the author
        self.player = self.bot.get_user(self.ctx.author.id)
        self.player_id = str(self.player.id)

    async def _create_new_game(self):
        # Create new Game and bind it to the user_id in the queue
        self.bot.games[self.player_id] = Game(self.player)
        await self.ctx.send(f'<@{self.player_id}>, твоята игра започва сега!')
        await asyncio.sleep(1)

    async def _send_first_question(self):
        # ask the first question
        question_data = self.bot.games[self.player_id].ask()
        embed = QuestionEmbed(**question_data)

        self.bot.games[self.player_id].last_question = question_data
        self.bot.games[self.player_id].last_embed = \
            await self.ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(NewGame(bot))
