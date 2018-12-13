from bot.constants import PREFIX as P
from bot.model import Bot

def main():
    bot = Bot(prefix=P,
              activity=f"{P}команди")
    bot.load_cogs()
    bot.run('NDU0MjIzNjg1MDEyOTQ2OTQ0.DvK6qQ.pznDOEeJLk1RiMfcSpnGbazNnBY')


if __name__ == '__main__':
    main()
