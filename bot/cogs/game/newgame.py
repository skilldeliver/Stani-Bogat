from discord.ext import commands

from bot.core.constants import SECS, Cogs
from bot.core.game import Game
from bot.core.embeds import QuestionEmbed
from bot.core.replies import Reply


class NewGame:
    def __init__(self, bot):
        self.bot = bot
        self.ctx = None
        self.arg = None

        self.player = None
        self.player_id = str()
        self.embed = None

    @commands.guild_only()
    @commands.command(name=Cogs.Game.game, aliases=[Cogs.Game.newgame])
    async def new_game(self, ctx, *args):
        '''
        Creates new Game.
        Add it to the bot games (dictionary).
        Key - string of the user ID
        Value - instance of the bot.core.game.Game class
        '''
        if not args:
            self.arg = 'ИТБГ'
        else:
            self.arg = args[0].upper()

        self.ctx = ctx
        self._get_player()

        if self.player_id in self.bot.games.keys():
            await ctx.send(Reply.not_finished(self.player_id))
            return


        await self._create_new_game()
        await self._send_first_question()

    def _get_player(self):
        # get a User object of the author
        self.player = self.bot.get_user(self.ctx.author.id)
        self.player_id = str(self.player.id)

    async def _create_new_game(self):
        # Create new Game and bind it to the user_id in the queue
        self.bot.games[self.player_id] = Game(self.player,
                                              self.arg,
                                              self.bot.time)
        self.bot.games[self.player_id].ctx = self.ctx

        await self.ctx.send(Reply.start_game(self.player_id))

    async def _send_first_question(self):
        # ask the first question
        question_data = self.bot.games[self.player_id].ask()
        game = self.bot.games[self.player_id]
        game.last_embed = QuestionEmbed(**question_data)

        game.last_question = question_data
        game.last_message= \
            await self.ctx.send(content=f'⏳ **Имаш {SECS} секунди**', embed=game.last_embed)
        game.start_question = self.bot.time


def setup(bot):
    bot.add_cog(NewGame(bot))
