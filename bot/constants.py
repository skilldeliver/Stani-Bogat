from pathlib import PurePath
from typing import NamedTuple


class Path(NamedTuple):
    project = PurePath(__file__).parent.parent
    data = project.joinpath('data/')

    questions = data.joinpath('questions/')
    general = questions.joinpath('general/')
    IT = questions.joinpath('IT/')


class File(NamedTuple):
    json = '/questions.json'


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
