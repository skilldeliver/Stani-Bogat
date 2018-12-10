from discord import Embed

from bot.core.replies import Reply


class QuestionEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 question: str,
                 question_leva: int,
                 question_level: int,
                 answers: dict,
                 color: int,
                 author: str,
                 author_thumbnail: str,
                 ):
        super().__init__(
                         title=question,
                         color=color)

        self.set_author(name=Reply.game_title(question_level, player, question_leva),
                        icon_url=player_thumbnail)

        for key in answers:
            self.add_field(name=key,
                           value=answers[key],
                           inline=False)

        if author_thumbnail:
            self.set_footer(text=Reply.question_added_by(author),
                            icon_url=author_thumbnail)
        else:
            self.set_footer(text=Reply.question_added_by(author))


class InfoEmbed(Embed):
    def __init__(self,
                 python_version,
                 discord_version,
                 stars,
                 forks,
                 issues,
                 connected_servers: int,
                 total_members: int,
                 pc,
                 cpu_use,
                 ram):
        super().__init__(color=0x000000)

        self.set_author(name=Reply.github_repo(stars, forks, issues),
                        url='https://github.com/skilldeliver/Stani-Bogat',
                        icon_url='https://avatars0.githubusercontent.com/u/9919?s=280&v=4')
        self.add_field(name=f'🏴 Дискорд сървъри:',
                       value=f'{connected_servers}',
                       inline=True)
        self.add_field(name=f':busts_in_silhouette: Потребители:',
                       value=f'{total_members}',
                       inline=True)
        self.add_field(name=f'💻 Хост:',
                       value=f'{pc.node}\n{pc.system} {pc.release}\n\
CPU usage: {cpu_use} % \n\
RAM usage: {ram} MiB',
                       inline=False)
        self.add_field(name='🛠️ Използвани технологии:',
                       value=Reply.used_tech(python_version,
                                             discord_version),
                       inline=False)
        self.add_field(name='📝 Автор:',
                       value='Владислав Михов (skilldeliver)',
                       inline=False)
        self.add_field(name='👷 Топ сътрудници(contributors):',
                       value=':one: skilldeliver \n:two: surister',
                       inline=False)


class WrongAnswerEmbed(Embed):
    def __init__(self):
        text = f'Грешен отговор!'
        color = 0xdd2e44

        super().__init__(title=text,
                         color=color)


class RightAnswerEmbed(Embed):
    def __init__(self):
        text = f'Верен отговор!'
        color = 0x77b255

        super().__init__(title=text,
                         color=color)


class JokersEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 image_url: str,):
        color = 0x1b87e7
        super().__init__(color=color)

        self.set_author(name=f'Играта на {player}.',
                        icon_url=player_thumbnail)
        self.set_image(url=image_url)


class AudienceEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 question_level: int,
                 count_votes: int,
                 votes: dict,
                 color: int,
                 ):
        super().__init__(color=color)

        self.set_author(name=f'Играта на {player}. Гласoве на публиката за въпрос {question_level}.',
                        icon_url=player_thumbnail)
        for vote in votes:
            lines = votes[vote] * '|'
            if not lines:
                lines = u"\u2063"

            self.add_field(name=f'{vote} {votes[vote]} %',
                           value=f'{lines}',
                           inline=False)

        self.set_footer(text=f"Общо гласoве: {count_votes}.")


class FriendEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 helper: str,
                 helper_thumbnail: str,
                 question_level: int,
                 vote: dict,
                 color: int,
                 ):
        super().__init__(color=color)

        self.set_author(name=f'Играта на {player}. Предложението на {helper} за въпрос {question_level}.',
                        icon_url=player_thumbnail)

        self.add_field(name=f'{list(vote.keys())[0]}',
                       value=f'{list(vote.values())[0]}',
                       inline=False)

        self.set_thumbnail(url=helper_thumbnail)


class CommandsEmbed(Embed):

    def __init__(self):
        super().__init__(color=0x3351B6)
        self.add_field(name='📦 Основни команди.',
                       value='**$инфо** - изпраща информация за бота.\n\
**$правила** - изпраща правилата на играта.\n\
**$команди** - изпраща всички команди с пояснение.')

        self.add_field(name='📊 Статистики - команди.',
                       value='**$топ10 автори** - изпраща класацията на потребителите с най-много добавени въпроси.\n\
**$топ10 играчи** - изпраща класацията на потребителите с най-много спечелени пари от игрите.')

        self.add_field(name='🎮 Игрови команди.',
                       value='**$игра** - стартира се нова игра за потребителя.\n\
**$[А, Б, В, Г]** - отговор на въпроса.\n\
**$50:50** - жокер, два грешни отговора се премахват.\n\
**$помощ [таг]** - жокер, 30 секунди се изчаква помощ от тагнатият.\n\
**$помощ публика** - жокери, 30 секунди се изчакват отговори в същият канал.\n\
**$жокери** - изпраща се илюстрация на наличните жокери.\n\
**$спирам** - играча се отказва от играта и се запазват парите от последният отговорен въпрос.')


class RulesEmbed(Embed):
    def __init__(self):
        super().__init__(color=0x3351B6)

        self.add_field(name='📜 Правила:',
value='1. Един потребител може да бъде само в една игра.\n\
2. Не може да искаш помощ от бот или приятел в игра.\n\
3. Грешен отговор - играта ти приключва и се запазват парите от достигнатата сигурна сума.')  


class StatsEmbed(Embed):
    pass


class Top10Embed(Embed):
    def __init__(self, target, authors_n):
        super().__init__(color=0x8a2be2)
        title = what = str()

        if target == 'authors':
            title = 'ТОП 10 потребители с най-много добавени въпроси.'
            what = 'добавени въпроса.'
        elif target == 'players':
            what = 'лева.'
            title = 'ТОП 10 играчи с най-много спечелени пари.'

        self.set_author(name=title,
                        icon_url='https://i.imgur.com/F7VUqZV.png')

        for i in range(len(authors_n)):
            item = authors_n[i]
            if i == 0:
                self.add_field(name=f'{i+1}. **{item[0]}**🥇: {item[1]} {what}',
                               value=u"\u2063",
                               inline=False)
            elif i == 1:
                self.add_field(name=f'{i+1}. **{item[0]}**🥈: {item[1]} {what}',
                               value=u"\u2063",
                               inline=False)    
            elif i == 2:
                self.add_field(name=f'{i+1}. **{item[0]}**🥉: {item[1]} {what}',
                               value=u"\u2063",
                               inline=False)
            else:
                self.add_field(name=f'{i+1}. **{item[0]}**: {item[1]} {what}',
                               value=u"\u2063",
                               inline=False)


class HowToAddEmbed(Embed):
    def __init__(self):
        super().__init__(color=0xcae00d)

        self.add_field(name='❓ Добавяне на въпрос',
                       value="""\
За да добавите въпрос, изпълнете следните инструкции.
**1**. Копирайте и попълнета **формата**(по-долу).
**2**. Изпратете я на **лично** на бота.
**3**. **Pin**-нете съобщениeто/съобщенията в личният чата.
**4**. Изпълнете командата **$добавям** в **сървъра**.

~ ботът ще провери и събере всички pin-нати съобщения в личният Ви чат
~ след като получите потвърждение, че са успешно събрани,
махнете въпроса/въпросите от пиновете.

 **Форма**
```css
Име: [тук поставяте Вашето име или никнейм]
Фото: [линк към Ваша снимка или аватар](опционално)
Тема: [общо, ИТ] - изберете някое от изброените
Ниво: [число от 1 до 15]
Въпрос: [тук поставяте вашият въпрос]
Отговор: [тук поставяте верният отговор]
Друг: [тук поставяте друг неверен отговор]
Друг: [тук поставяте друг неверен отговор]
Друг: [тук поставяте друг неверен отговор]
```
// Не пишете квадратните скоби 😅
""")