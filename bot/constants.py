from pathlib import PurePath
from typing import NamedTuple


class Path(NamedTuple):
    project = PurePath(__file__).parent.parent
    data = project.joinpath('data/')

    questions = data.joinpath('questions/')
    statistics = data.joinpath('statistics/')
    pending = data.joinpath('pending/')

    global_stats = statistics.joinpath('global/')

    general = questions.joinpath('general/')
    IT = questions.joinpath('IT/')


class File(NamedTuple):
    json = '/questions.json'
    players = 'top_players.json'
    authors = 'top_authors.json'
    pending_questions = 'pending_questions.json'


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


class Emoji(NamedTuple):
    clock = '\u23f0'
    thumb_down = '👎'
    thumb_up = '👍'