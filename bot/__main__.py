from bot.core.constants import PREFIX as P
from bot.core.model import Bot
from bot.utilities.loader import load_input

def main():
    bot = Bot(prefix=P,
              activity=f"{P}команди")
    bot.load_cogs()
    bot.run(load_input(as_string=True))

if __name__ == '__main__':
    main()
