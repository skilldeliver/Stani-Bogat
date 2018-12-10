
class Reply:
    @staticmethod
    def not_in_game(user):
        return f'<@{user}>, не си в игра.'

    @staticmethod
    def used_50(player):
        return f'<@{player}>, използвал си 50:50.'

    @staticmethod
    def used_friend(player):
        return f'<@{player}>, използвал си помощ от приятел.'

    @staticmethod
    def used_audience(player):
        return f'<@{player}>, използвал си помощ от публиката.'

    @staticmethod
    def end_game(player, m):
        return f'<@{player}>, твоята игра приключи. Тръгваш си с - {m} лева.'

    @staticmethod
    def unknown_2_arg(player):
        return f'<@{player}>, не разпознат втори аргумент.'

    @staticmethod
    def no_yourself(player):
        return f'<@{player}>, не може да искаш помощ от себе си.'

    @staticmethod
    def no_player(player):
        return f'<@{player}>, не може да искаш помощ от потребител в игра.'

    @staticmethod
    def no_bot(player):
        return f'<@{player}>, не може да искаш помощ от бот.'

    @staticmethod
    def friend_help(helper, sec):
        return f'{helper}, имаш {sec} секунди да помогнеш на своят приятел.'

    @staticmethod
    def audience_help(sec):
        return f'Нека публиката се включи сега! Оставящи {sec} секунди.'

    @staticmethod
    def not_finished(player):
        return f'<@{player}>, все още не си приключил играта си.'

    @staticmethod
    def start_game(player):
        return f'<@{player}>, твоята игра започва сега!'

    @staticmethod
    def game_title(question_level, player, question_leva):
        return f'{question_level}. Играта на {player}. Въпрос за {question_leva} лева.'

    @staticmethod
    def question_added_by(author):
        return f"Въпрос добавен от {author}."

    @staticmethod
    def github_repo(stars, forks, issues):
        return f'ГитХъб репо. {stars} \u2b50 {forks} 🍴 {issues} \u2757'

    @staticmethod
    def used_tech(python_version, discord_version):
        return f'''
Python {python_version} :snake:
discord.py rewrite branch {discord_version}
PyGithub
Pipenv
'''