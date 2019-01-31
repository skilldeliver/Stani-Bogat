import json

author = 'ДОЦ. Д-Р ЮЛИАНА ПЕНЕВА'
theme = 'Databases1'


lets = ['А', 'Б', 'В', 'Г']

def add_question(author,
                 theme,
                 question_level,
                 question,
                 choices,
                 author_thumbnail=None):

    file = f'C:/ABC/CODING/#CRAFTING/Stani-Bogat/data/questions/{theme}/{str(question_level).zfill(2)}/questions.json'

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

    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def fill(text):
    level = 1
    count = 0
    question = str()
    choices = list()

    print(text.split('\n'))
    for line in text.split('\n'):
        if count == 0:
            question = ' '.join(line.split()[2:])
        elif count in [1, 2, 3, 4]:
            print(line)
            choices.append(line.split(')')[1])
        elif line:
            index = lets.index(line[0])
            if index != 0:
                choices[0], choices[index] = choices[index], choices[0]

            add_question(author,
                         theme,
                         level,
                         question,
                         choices)
            level += 1
            count = -1
            choices = list()
        count += 1


fill(
    """Въпрос 20: Езикът за обработване на данните позволява:
а)само достъп данните в базата;
б)промяна на физическата организация на базата;
в)промяна на схемата на базата;
г)извличане на данни и обновяване на базата.
Г
Въпрос 11: При дефиниране на нова база 
а)се задава нейната схема, която се включва в каталога на СУБД;
б)се задава ново състояние на базата, което се отразява в каталога на СУБД;
в)се дефинират права за достъп до данните;
г)нито едно от изброените по-горе.
А
Въпрос 1: При дефиниране на нова база се задава:
а)съдържанието на един запис от нея;
б)състоянието на данните;
в)схемата на базата;
г)изграждащите я файлове.
В
Въпрос 14: Схемата на базата съдържа:
а)обекти, атрибути и връзки между тях на дадено приложение;
б)съвкупността от всички заявки, свързани с дадено приложение;
в)графично описание на данните от дадена предметна област;
г)нито едно от изброените.
А
Въпрос 23 Описанието на базата от данни се нарича:
а)схема на базата;
б)състояние на базата;
в)модел на данни от ниско ниво;
г)физически модел на данни.
А"""
)