from bot.model import Bot


def main():
    bot = Bot(prefix='$',
              activity="$команди")
    bot.load_cogs()
    bot.run('none')


if __name__ == '__main__':
    main()
