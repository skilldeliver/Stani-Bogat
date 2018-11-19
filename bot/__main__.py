from discord.ext import commands
from pathlib import Path


def main():
    bot = commands.Bot(command_prefix='*')
    cogs = [file.stem for file in Path('bot', 'cogs').glob('*.py')]
    # Scan for files in the /cogs/ directory and make a list of the file names.
    for extension in cogs:
        try:
            bot.load_extension(f'bot.cogs.{extension}')
            print(f'Successfully loaded extension: {extension}')
        except Exception as e:
            print(f'Failed to load extension {extension}: {repr(e)}')

    bot.run('NTEzNDMzMjcxMDUzNDUxMjY1.DtH7uA.de9Iw6nw2dtqhkspui3e63L2lgI')


if __name__ == '__main__':
    main()
