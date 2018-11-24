from pathlib import Path

from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self,
                 prefix: str,
                 ):
        commands.Bot.__init__(self,
                              command_prefix=prefix)

        self.games = dict()
        self.helping_friends = dict()

    def load_cogs(self):
        general_cogs = [file.stem for file in Path('bot',
                        'cogs', 'general').glob('*.py')]

        game_cogs = [file.stem for file in Path('bot',
                     'cogs', 'game').glob('*.py')]

        stats_cogs = [file.stem for file in Path('bot',
                      'cogs', 'stats').glob('*.py')]

        print(general_cogs, game_cogs, stats_cogs)

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
