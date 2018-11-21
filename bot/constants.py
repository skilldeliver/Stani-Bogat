from pathlib import PurePath


class Path:
    project = PurePath(__file__).parent.parent
    data = project.joinpath('data/')

    questions = data.joinpath('questions/')
    general = questions.joinpath('general/')

class Files:
    pass
    # general_questions = [questifor i in range(1, 16)]

class Image:
    jokers = {'ooo': 'https://i.imgur.com/aTzsSyO.png',
              'oox': 'https://i.imgur.com/4CUYpvv.png',
              'oxo': 'https://i.imgur.com/NYLgn73.png',
              'xoo': 'https://i.imgur.com/8mUsj0G.png',
              'xxo': 'https://i.imgur.com/us4jqub.png',
              'xox': 'https://i.imgur.com/uuUM31U.png',
              'oxx': 'https://i.imgur.com/y1r9XGK.png',
              'xxx': 'https://i.imgur.com/ZPOM3Tc.png'}