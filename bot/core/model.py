from pathlib import Path
import asyncio

import discord
from discord.ext import commands

from bot.core.replies import Reply
from bot.utilities.json import save_player
from bot.core.constants import Emoji
from bot.core.embeds import AudienceEmbed


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
        general_cogs = [file.stem for file in Path('bot',
                        'cogs', 'general').glob('*.py')]

        game_cogs = [file.stem for file in Path('bot',
                     'cogs', 'game').glob('*.py')]

        stats_cogs = [file.stem for file in Path('bot',
                      'cogs', 'stats').glob('*.py')]

        mod_cogs = [file.stem for file in Path('bot',
                      'cogs', 'mod').glob('*.py')]

        print('Loading general cogs:')
        for extension in general_cogs:
            try:
                self.load_extension(f'bot.cogs.general.{extension}')
                print(f'    Successfully loaded general cog: {extension}')
            except Exception as e:
                print(f'    Failed to load general cog {extension}: {repr(e)}')

        print('\nLoading gaming cogs:')
        for extension in game_cogs:
            try:
                self.load_extension(f'bot.cogs.game.{extension}')
                print(f'    Successfully loaded game cog: {extension}')
            except Exception as e:
                print(f'    Failed to load game cog {extension}: {repr(e)}')

        print('\nLoading stats cogs:')
        for extension in stats_cogs:
            try:
                self.load_extension(f'bot.cogs.stats.{extension}')
                print(f'    Successfully loaded game cog: {extension}')
            except Exception as e:
                print(f'    Failed to load game cog {extension}: {repr(e)}')

        print('\nLoading mod cogs:')
        for extension in mod_cogs:
            try:
                self.load_extension(f'bot.cogs.mod.{extension}')
                print(f'    Successfully loaded game cog: {extension}')
            except Exception as e:
                print(f'    Failed to load game cog {extension}: {repr(e)}')

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

            if self.time - game.start_question == 15:
                await game.last_message.edit(content=f'⏳ **Остават ти 5 секунди!**', embed=game.last_embed)
            if self.time - game.start_question == 20:
                player = Reply.user_name(game.user.name, game.user.discriminator)
                money = game.return_money(wrong_answer=True)
                time = self.time - game.start

                save_player(player, money, time)

                await game.ctx.send(Reply.end_game(game.user.id, money))

                try:
                    await game.last_message.delete()
                except:
                    pass

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