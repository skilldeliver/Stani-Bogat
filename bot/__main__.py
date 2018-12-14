from bot.core.constants import PREFIX as P
from bot.core.model import Bot

def main():
    bot = Bot(prefix=P,
              activity=f"{P}команди")
    bot.load_cogs()
    bot.run('NDU0MjIzNjg1MDEyOTQ2OTQ0.DvVZhA.v6eV1L2rXMlw9e_x7G2TqHPgNQ0')

if __name__ == '__main__':
    main()
