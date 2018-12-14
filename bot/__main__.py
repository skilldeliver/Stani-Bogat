import os

from bot.core.constants import PREFIX as P
from bot.core.model import Bot

def main():
    bot = Bot(prefix=P,
              activity=f"{P}команди")
    bot.load_cogs(os.getenv('TOKEN'))
    bot.run()

if __name__ == '__main__':
    main()
