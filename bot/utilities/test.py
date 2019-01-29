import json

author = 'ДОЦ. Д-Р ЮЛИАНА ПЕНЕВА'
theme = 'Databases'


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
    """Въпрос 14: Потребителската представа (view) позволява:
а)дадена база да се използва от много потребители, които работят с различни нейни обекти;
б)всеки потребител да има свое разбиране за структурата и съдържанието на базата;
в)поддържане на виртуални данни, които са извлечени от базата без да се съхраняват явно в нея;
г)всичко, изброено по-горе.
Г
"""
)