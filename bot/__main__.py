from bot.model import Bot
from pathlib import Path


def main():
    bot = Bot(prefix='*')

    general_cogs = [file.stem for file in Path('bot',
                    'cogs', 'general').glob('*.py')]

    game_cogs = [file.stem for file in Path('bot',
                 'cogs', 'game').glob('*.py')]

    stats_cogs = [file.stem for file in Path('bot',
                  'cogs', 'stats').glob('*.py')]

    print('Loading general cogs:')
    for extension in general_cogs:
        try:
            bot.load_extension(f'bot.cogs.general.{extension}')
            print(f'    Successfully loaded general cog: {extension}')
        except Exception as e:
            print(f'    Failed to load general cog {extension}: {repr(e)}')

    print('\nLoading gaming cogs:')
    for extension in game_cogs:
        try:
            bot.load_extension(f'bot.cogs.game.{extension}')
            print(f'    Successfully loaded game cog: {extension}')
        except Exception as e:
            print(f'    Failed to load game cog {extension}: {repr(e)}')

    print('\nLoading stats cogs:')
    for extension in stats_cogs:
        try:
            bot.load_extension(f'bot.cogs.stats.{extension}')
            print(f'    Successfully loaded game cog: {extension}')
        except Exception as e:
            print(f'    Failed to load game cog {extension}: {repr(e)}')

    bot.run('none')


if __name__ == '__main__':
    main()
