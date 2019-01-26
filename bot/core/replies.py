
class Reply:
    @staticmethod
    def not_in_game(user):
        return f'<@{user}>, не сте в игра. 🙄'

    @staticmethod
    def used_50(player):
        return f'<@{player}>, използвали сте 50:50. 😯'

    @staticmethod
    def used_friend(player):
        return f'<@{player}>, използвали сте помощ от приятел. 😯'

    @staticmethod
    def used_audience(player):
        return f'<@{player}>, използвали сте помощ от публиката. 😯'

    @staticmethod
    def end_game(player, m):
        return f'<@{player}>, Вашата игра приключи. Тръгвате си с - {m} лева. 😭'

    @staticmethod
    def unknown_2_arg(player):
        return f'<@{player}>, не разпознат втори аргумент. 🤔'

    @staticmethod
    def no_yourself(player):
        return f'<@{player}>, не може да искате помощ от себе си. 😀'

    @staticmethod
    def no_player(player):
        return f'<@{player}>, не може да искате помощ от потребител в игра. 😉'

    @staticmethod
    def no_bot(player):
        return f'<@{player}>, не може да искате помощ от бот. 😀'

    @staticmethod
    def friend_help(helper, sec):
        return f'{helper}, имате {sec} секунди да помогнете на своят приятел. 🤩'

    @staticmethod
    def audience_help(sec):
        return f'Нека публиката се включи сега! Оставящи {sec} секунди. 🤩'

    @staticmethod
    def not_finished(player):
        return f'<@{player}>, все още не сте приключили играта си. 😏'

    @staticmethod
    def another_game_in_channel(player):
        return f'<@{player}>, само по една игра в канал. 😏'

    @staticmethod
    def start_game(player):
        return f'<@{player}>, Вашата игра започва сега! 🎉'

    @staticmethod
    def user_name(user, tag):
        return f'{user}#{tag}'

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
    def first_place(place, name, count, what):
        return f'{place}. **{name}**🥇: {count} {what}'

    @staticmethod
    def sec_place(place, name, count, what):
        return f'{place}. **{name}**🥈: {count} {what}'

    @staticmethod
    def third_place(place, name, count, what):
        return f'{place}. **{name}**🥉: {count} {what}'

    @staticmethod
    def other_place(place, name, count, what):
        return f'{place}. **{name}**: {count} {what}'

    @staticmethod
    def system_info(node, sys, rel, cpu, ram, ram_tot, hdd, hdd_tot):
        return f'Name: {node}\nOS: {sys} {rel}\n\
CPU usage: {cpu} % \n\
RAM total: {ram_tot} GB\n\
RAM usage: {ram} GB\n\
HDD total: {hdd_tot} MB\n\
HDD usage: {hdd} MB'

    @staticmethod
    def choice(key, answer):
        return f'**{key}** `{answer}`'

    @staticmethod
    def total_votes(votes):
        return f"Общо гласoве: {votes}."

    @staticmethod
    def letter_percent(vote, percent):
        return f'{vote} {percent} %'

    @staticmethod
    def used_tech(python_version, discord_version):
        return f'''
Python {python_version} :snake:
discord.py rewrite branch {discord_version}
Dropbox API
PyGithub
Pipenv
'''

    @staticmethod
    def game_of(player):
        return f'Играта на {player}.'

    @staticmethod
    def help_from_friend(player, helper, level):
        return f'Играта на {player}. Предложението на {helper} за въпрос {level}.'

    @staticmethod
    def help_from_audience(player, level):
        return f'Играта на {player}. Гласoве на публиката за въпрос {level}.'

    @staticmethod
    def successfully_send(success, pins):
        return f'{success} от {pins} успешно изпратени въпроса. Очаква се преглед от модератор. Ще Ви известим ако въпросите Ви са в игра.'

    @staticmethod
    def list_general_commands(P):
        return (f'**{P}инфо** - изпраща информация за бота.\n'
                f'**{P}правила** - изпраща правилата на играта.\n'
                f'**{P}команди** - изпраща всички команди с пояснение.\n'          
                f'**{P}добави** - изпраща информация как да добавиш въпрос.\n'
                f'**{P}добавям** - ботът събира твоите въпроси (pin-нати съобщения в личния чат)\n'
                f'**{P}форма** - ботът изпраща формата за въпроса.\n')

    @staticmethod
    def list_stat_commands(P):
        return (f'**{P}топ10 автори** - изпраща класацията на потребителите с най-много добавени въпроси.\n'
                f'**{P}топ10 играчи** - изпраща класацията на потребителите с най-много спечелени пари от игрите.\n'
                f'**{P}общо** - изпраща сумираната информация за няколко статистики\n'
                f'**{P}статс** - изпраща статистиките на потребителя')

    @staticmethod
    def list_game_commands(P):
        return (f'**{P}игра** [общо, ИТ, ИТБГ, БЕЛ, безжични_мрежи, география] - стартира се нова игра за потребителя\n'
                f'**{P}50:50** - жокер, два грешни отговора се премахват.\n'
                f'**{P}помощ [таг]** - жокер, 30 секунди се изчаква помощ от тагнатият.\n'
                f'**{P}помощ публика** - жокери, 30 секунди се изчакват отговори в същият канал.\n'
                f'**{P}жокери** - изпраща се илюстрация на наличните жокери.\n'
                f'**{P}спирам** - играча се отказва от играта и се запазват парите от последният отговорен въпрос.\n')