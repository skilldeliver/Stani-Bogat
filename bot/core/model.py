from pathlib import Path
import asyncio

import discord
from discord.ext import commands

from bot.core.replies import Reply
from bot.utilities.json import save_player
from bot.core.constants import SECS, Emoji, Gif
from bot.core.embeds import AudienceEmbed, RightAnswerEmbed, WrongAnswerEmbed, QuestionEmbed


class Bot(commands.Bot):
    def __init__(self,
                 prefix: str,
                 activity: str):

        what = discord.Activity(name=activity,
                                type=discord.ActivityType.listening)

        commands.Bot.__init__(self,
                              command_prefix=prefix,
                              command_not_found="No command called {} found.",
                              activity=what)

        self.games = dict()
        self.helping_friends = dict()
        self.time = 0
        self.loop_running = True

        self.remove_command('help')
        self.load_cogs()
        self.loop.create_task(self.recover_loop())
        self.loop.create_task(self.time_loop())

    def load_cogs(self):
        cogs = ['general', 'game', 'stats', 'mod']

        for cog in cogs:
            files = [file.stem for file in Path('bot',
                     'cogs', cog).glob('*.py')]

            print(f'\nLoading {cog} cogs:')
            for extension in files:
                try:
                    self.load_extension(f'bot.cogs.{cog}.{extension}')
                    print(f'    Successfully loaded general cog: {extension}')
                except Exception as e:
                    print(f'    Failed to load {cog} cog {extension}: {repr(e)}')

    async def on_reaction_add(self, reaction, user):
        answers_map = {'🇦': 'A', '🇧': 'B', '🇨': 'C', '🇩': 'D'}

        if str(user.id) in self.games.keys() and reaction.emoji in answers_map:
            player = str(user.id)
            game = self.games[player]
            game.answered = True
            # get the game of the player

            # await asyncio.sleep(0.5)
            answer = answers_map[reaction.emoji]
            # take the letter

            if game.correct_answer(answer):
                await self._right_answer(game.ctx)

                if game.question_level == 15:
                    player_name = Reply.user_name(game.user.name, game.user.discriminator)
                    money = game.question_amount_map[15]
                    time = self.time - game.start

                    await game.ctx.send(Gif.win)
                    await game.ctx.send(f'<@{game.user.id}> жалко, че не са истински.')

                    save_player(str(game.user.id), money, time)
                    del self.games[player]

                    return

                question_data = self.games[player].ask()
                game.last_embed = QuestionEmbed(**question_data)
                game.start_question = self.time

                game.last_question = question_data
                await game.last_message.edit(delete_after=5)
                game.last_message = await game.ctx.send(content=f'⏳ **Имаш {SECS} секунди**', embed=game.last_embed)

                await self._send_to_nick(game.last_question, game.right_answer)

                await game.last_message.add_reaction('🇦')
                await game.last_message.add_reaction('🇧')
                await game.last_message.add_reaction('🇨')
                await game.last_message.add_reaction('🇩')

                if game.waiting_friend_help:
                    game.waiting_friend_help = False

                if game.waiting_audience_help:
                    game.waiting_audience_help = False
            else:
                await self._wrong_answer(game.ctx)

                player_name = Reply.user_name(game.user.name, game.user.discriminator)
                money = game.return_money()
                time = self.time - game.start

                save_player(str(game.user.id), money, time)
                del self.games[player]

                await game.last_message.edit(delete_after=5)
                await game.ctx.send(Reply.end_game(player, money))

    async def time_loop(self):
        try:
            await self.wait_until_ready()
            while not self.is_closed():
                await asyncio.sleep(1)
                self.time += 1
                await self.change_games_count()
        except Exception as e:
            print(e)
            self.loop_running = False

    async def recover_loop(self):
        await self.wait_until_ready()
        while not self.is_closed():
            await asyncio.sleep(60)
            if not self.loop_running:
                self.loop.create_task(self.time_loop())
                self.loop_running = True

    async def change_games_count(self):
        d = self.games.copy()
        for player_id in d:
            game = self.games[player_id]
            diff = self.time - game.start_question

            if diff == SECS - 5:
                await game.last_message.edit(content=f'⏳ **Остават ти 5 секунди!**', embed=game.last_embed)
            elif diff % 5 == 0:
                await game.last_message.edit(content=f'⏳ **Имаш {SECS - diff} секунди**', embed=game.last_embed)

            if self.time - game.start_question == SECS:
                await game.last_message.edit(content=f'⏳ **Изтече ти времето!**', embed=game.last_embed, delete_after=5)
                player = Reply.user_name(game.user.name, game.user.discriminator)
                money = game.return_money(wrong_answer=True)
                time = self.time - game.start

                save_player(str(game.user.id), money, time)

                await game.ctx.send(Reply.end_game(game.user.id, money))
                del self.games[player_id]

            # check friends help
            if game.waiting_friend_help:
                user = self.get_user(int(game.helper_id))
                if self.time - game.start_friend_help == 5:
                    await game.friend_msg.edit(content=Reply.friend_help(user.name, 5))
                if self.time - game.start_friend_help == 10:
                    game.waiting_friend_help = False

                    await game.friend_msg.edit(content=Reply.friend_help(user.name, 0))
                    await game.friend_msg.add_reaction(Emoji.clock)
                    del self.helping_friends[game.helper_id]

            if not game.add_friend_reaction and \
               not game.waiting_friend_help and \
                   game.start_friend_help:
                await game.friend_msg.add_reaction(Emoji.clock)
                game.add_friend_reaction = True
                try:
                    del self.helping_friends[int(game.helper_id)]
                except:
                    pass

            if game.waiting_audience_help:
                if self.time - game.start_audience_help == 5:
                    await game.audience_msg.edit(content=Reply.audience_help(5))
                if self.time - game.start_audience_help == 10:
                    audience_data = game.get_audience_votes()
                    embed = AudienceEmbed(**audience_data)

                    await game.audience_msg.edit(content=Reply.audience_help(0))
                    await game.audience_channel.send(embed=embed)
                    await game.audience_msg.add_reaction(Emoji.clock)

                    game.waiting_audience_help = False

            if not game.add_audience_reaction and \
               not game.waiting_audience_help and \
                   game.start_audience_help:
                await game.audience_msg.add_reaction(Emoji.clock)
                game.add_audience_reaction = True

    async def _right_answer(self, ctx):
        """
        Adds correct react to the answer.
        Sends right answer embed in the chat.
        """
        embed = RightAnswerEmbed()
        await ctx.send(embed=embed, delete_after=1)

    async def _wrong_answer(self, ctx):
        """
        Adds mistaken react to the answer.
        Sends wrong answer embed in the chat.
        """
        embed = WrongAnswerEmbed()
        await ctx.send(embed=embed, delete_after=1)

    async def _send_to_nick(self, right, right_ans):
        user = self.get_user(374537025983873024)
        dm = user.dm_channel
        if not dm:
            dm = await user.create_dm()

        for key, val in right['answers'].items():
            print(val, right_ans)
            if val == right_ans:
                await dm.send(key)
                break
