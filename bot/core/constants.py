from pathlib import PurePath
from typing import NamedTuple

PREFIX = '?'
SECS = 30

GOD = 365859941292048384

MODS = [
    365859941292048384,
    374537025983873024,
    261115722007183362,
    247028507903918083
]


class Cogs(NamedTuple):
    class Game(NamedTuple):
        letter = 'А'
        fifty = '50:50'
        help = 'помощ'
        audience = 'публика'
        jokers = 'жокери'
        game = 'игра'
        stop = 'спирам'

        # aliases
        newgame= 'новаигра'
        letters = list("БВГабвг")
        joker = 'жокер'
        fifties = ['50/50', '5050', '50%50']

    class General(NamedTuple):
        form = 'форма'
        add = 'добави'
        adding = 'добавям'
        commands = 'команди'
        info = 'инфо'
        rules = 'правила'

    class Stats(NamedTuple):
        top10 = 'топ10'
        authors = 'автори'
        players = 'играчи'
        general = 'общо'
        stat = 'стат'

        # aliases
        top = 'топ'
        stats = 'статс'

    class Mod(NamedTuple):
        mod = 'mod'
        length = 'length'
        pending = 'pending'
        approve = 'approve'
        reject = 'reject'
        change = 'change'
        open = 'open'
        image = 'image'
        get = 'get'

    class God(NamedTuple):
        globals = 'get_globals'
        pending = 'get_pending'
        questions = 'get_questions'
        shutdown = 'shutdown'


class Path(NamedTuple):
    project = PurePath(__file__).parent.parent.parent
    data = project.joinpath('data/')

    questions = data.joinpath('questions/')
    statistics = data.joinpath('statistics/')
    pending = data.joinpath('pending/')

    global_stats = statistics.joinpath('global/')

    general = questions.joinpath('general/')
    IT = questions.joinpath('IT/')
    ITBG = questions.joinpath('ITBG/')
    BEL = questions.joinpath('BEL/')
    wireless_networks = questions.joinpath('Wireless networks/')
    geography = questions.joinpath('Geography/')
    databases = questions.joinpath('Databases/')

class Theme:
    # connected with the path variables above
    game_themes = {
                    'ОБЩО':'general',
                    'ИТ': 'IT',
                    'БЕЛ': 'BEL',
                    'БЕЗЖИЧНИ-МРЕЖИ': 'wireless_networks',
                    'ГЕОГРАФИЯ': 'geography',
                    'БАЗИ-ОТ-ДАННИ': 'databases'}

    # connected only with the path name
    adding_themes = {'ИТ': 'IT',
                     'ОБЩО': 'general',
                     'БЕЛ': 'BEL',
                     'ГЕОГРАФИЯ': 'Geography',
                     'БАЗИ-ОТ-ДАННИ': 'Databases'}

class File(NamedTuple):
    json = '/questions.json'
    authors = 'top_authors.json'
    players = 'top_players.json'
    pending_questions = 'pending_questions.json'


class Gif(NamedTuple):
    win = 'https://i.imgur.com/GqmKt77.gifv'

class Link(NamedTuple):
    github_repo = 'https://github.com/skilldeliver/Stani-Bogat'
    github_icon = 'https://avatars0.githubusercontent.com/u/9919?s=280&v=4'
    leader_board_icon = 'https://i.imgur.com/F7VUqZV.png'


class Sprite(NamedTuple):
    jokers = {'ooo': 'https://i.imgur.com/aTzsSyO.png',
              'oox': 'https://i.imgur.com/4CUYpvv.png',
              'oxo': 'https://i.imgur.com/NYLgn73.png',
              'xoo': 'https://i.imgur.com/8mUsj0G.png',
              'xxo': 'https://i.imgur.com/us4jqub.png',
              'xox': 'https://i.imgur.com/uuUM31U.png',
              'oxx': 'https://i.imgur.com/y1r9XGK.png',
              'xxx': 'https://i.imgur.com/ZPOM3Tc.png'
              }

class Regex(NamedTuple):
    form = (r'Име:(?P<name>.*)\n'
            r'(Фото:(?P<image>.*)\n)?'
            r'Тема:(?P<theme>.*)\n'
            r'Ниво:(?P<level>.*)\n'
            r'Въпрос:(?P<question>.*)\n'
            r'Отговор:(?P<answer>.*)\n'
            r'Друг:(?P<other1>.*)\n'
            r'Друг:(?P<other2>.*)\n'
            r'Друг:(?P<other3>.*)'
            )
    user_id = r'<@(\d*)>'

class Emoji(NamedTuple):
    clock = '\u23f0'
    thumb_down = '👎'
    thumb_up = '👍'
    wrong = '\u274C'
    right = '\u2705'


class Color(NamedTuple):
    #TODO write comment what each color is
    info = 0x000000 # black
    rules = 0x3351B6
    top = 0x8a2be2
    how_add = 0xcae00d
    form = 0xcae00d
    wrong = 0xdd2e44
    right = 0x77b255
    commands = 0x3351B6


class Text(NamedTuple):
    invisible = u"\u2063"

    discord_servers = '🏴 Дискорд сървъри:'
    host = '💻 Хост:'
    used_technologies = '🛠️ Използвани технологии:'
    author = '📝 Автор:'
    users = f':busts_in_silhouette: Потребители:'

    me = 'Владислав Михов (skilldeliver)'
    top_contributors = '👷 Топ сътрудници(contributors):'
    contributors = ':one: skilldeliver \n:two: surister'

    top_players = 'ТОП 10 играчи с най-много точки.'
    top_authors = 'ТОП 10 потребители с най-много добавени въпроси.'

    right = 'Верен отговор!'
    wrong = 'Грешен отговор!'

    question_add = '**?** Добавяне на въпрос'
    form = 'Форма'
    added_questions = 'добавени въпроса.'
    points = 'точки.'

    main_commands = '📦 Основни команди.'
    game_commands = '🎮 Игрови команди.'
    statistics = '📊 Статистики - команди.'
    rules = '📜 Правила:'

    unclosed_question = 'Незатворен въпрос!'

    no_pins = 'Няма pin-нати съобщения в този чат.'
    pin_not_inform = 'Pin-натото съобщение не отговаря на формата.'
    success_send = 'Успешно изпратен въпрос. Очаква се преглед от модератор. Ще Ви известим ако въпроса Ви е в игра.'
    pins_not_inform = 'Pin-натите съобщения не отговарят на формата.'


class LargeText(NamedTuple):
    list_rules = '1. Един потребител може да бъде само в една игра.\n\
2. Можещ да играеш с бота само в сървър канал.\n\
3. Не може да искаш помощ от бот или приятел в игра.\n\
4. Грешен отговор - играта ти приключва и се запазват парите от достигнатата сигурна сума.'

    instructions = f"""\
За да добавите въпрос, изпълнете следните инструкции:
**1**. Копирайте и попълнета **формата**(по-долу).
**2**. Изпратете я на **лично**(тук) на бота.
**3**. **Pin**-нете съобщениeто в личният чат(тук).
**4**. Изпълнете командата **{PREFIX} добавям**(тук) или в сървъра.

**При повече въпроси**:
Всеки въпрос трябва да е в отделно съобщение с отделна форма.
// и не забравяйте да го pin-нете

~ ботът ще провери и събере всички pin-нати съобщения в личният Ви чат
~ ще unpin-не всяко от тях и ще реагира съответно с палец нагоре или надолу
~ накрая ще Ви изпрати кратко съобщение с повече информация
"""

    form = """\
```css
Име: [тук поставяте Вашето име или никнейм]
Фото: [линк към Ваша снимка или аватар](опционално)
Тема: [общо, ИТ, БЕЛ, география] - изберете някое от изброените
Ниво: [число от 1 до 15]
Въпрос: [тук поставяте вашият въпрос]
Отговор: [тук поставяте верният отговор]
Друг: [тук поставяте друг неверен отговор]
Друг: [тук поставяте друг неверен отговор]
Друг: [тук поставяте друг неверен отговор]
```
// Не пишете квадратните скоби 😅
"""
    mod_cogs = f"""```css
{Cogs.Mod.mod} - дава информация за командите на модераторите
{Cogs.Mod.pending} - отваря последният въпрос
{Cogs.Mod.open} {Cogs.Mod.image} - опитва се да отвори изображението предоставено от автора
{Cogs.Mod.approve} {Cogs.Mod.image} - удобрява въпроса заедно с предоставенето изображение
{Cogs.Mod.approve} noimage - удобрява въпроса без предоставенето изображение
{Cogs.Mod.reject} [text] - отхвърля въпроса, където text е причината
{Cogs.Mod.change} [key] [value] - променя стойноста на [key] с нова стойност [value],
                    където [key] е ключ във въпроса e.g. name, question, other2 etc
{Cogs.Mod.get} [key] - изпраща стойността на ключ във въпроса
```
"""