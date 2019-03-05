import sys

from bot.core.constants import PREFIX as P
from bot.core.model import Bot



def main():
    # os.environ["TOKEN"] = input('Token: ')

    bot = Bot(prefix=P,
              activity=f"{P}команди")
    # bot.run(os.getenv('TOKEN'))
    bot.run(sys.argv[1])

if __name__ == '__main__':
    main()
