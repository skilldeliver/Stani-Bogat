import json
import random

from bot.constants import Path, File


def load_question(question_level, theme):
    path = eval(f'Path.{theme}')

    with open(path.joinpath(f'{question_level}{File.json}'),
              encoding="utf-8") as f:
        data = json.load(f)

        author = random.choice(list(data.keys()))

        try:
            author_thumbnail = data[author]['author_img']
        except KeyError:
            author_thumbnail = None

        random_quest = random.choice(data[author]['questions'])
        question = random_quest['question']
        choices = random_quest['choices']

        return dict(author=author,
                    author_thumbnail=author_thumbnail,
                    question=question,
                    choices=choices,
                    )


def save_player_money(player, money):
    file = Path.global_stats.joinpath(File.players)

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if player not in data.keys():
        data[player] = int()

    data[player] += money

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def append_to_authors(author):
    file = Path.global_stats.joinpath(File.authors)

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if author not in data.keys():
        data[author] = int()

    data[author] += 1

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def add_question(author,
                 theme,
                 question_level,
                 question,
                 choices,
                 author_thumbnail=None):

    file = f'data/questions/{theme}/{str(question_level).zfill(2)}{File.json}'

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if author not in data.keys():
        print('IN')
        data[author] = {
                    "questions": list()
                    }

    if author_thumbnail:
        data[author]['author_img'] = author_thumbnail

    data[author]['questions'].append(dict(question=question,
                                          choices=choices))

    append_to_authors(author)

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def return_top(target, how):
    file = str()
    if target == 'authors':
        file = Path.global_stats.joinpath(File.authors)
    elif target == 'players':
        file = Path.global_stats.joinpath(File.players)

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    authors_n = sorted(data.items(), key=lambda kv: kv[1], reverse=True)

    if len(authors_n) > how:
        return authors_n[:how]
    return authors_n


def append_to_pending(alist):
    file = Path.pending.joinpath(File.pending_questions)

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in alist:
        data['queue'].append(item)

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

def get_pending():

    file = Path.pending.joinpath(File.pending_questions)

    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not data['queue']:
        return None

    question = data['queue'][-1]
    del data['queue'][-1]

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

    return question



def how_many_questions(author,
                       theme,
                       question_level):
    file = f'data/questions/{theme}/{str(question_level).zfill(2)}{File.json}'

    with open(file, 'r',
              encoding="utf8") as f:
        data = json.load(f)
        questions = data[author]['questions']

        for question in questions:
            print(question)
        print(len(questions))


def refactor():
    for theme in ('general', 'IT'):
        for i in range(1, 16):
            path = eval(f'Path.{theme}')
            path = path.joinpath(str(i).zfill(2))
            file = path.joinpath('questions.json')

            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            with open(file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
