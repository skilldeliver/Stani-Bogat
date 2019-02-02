import json

author = 'Д.Енчев'
theme = 'Javascript'


lets = ['a', 'b', 'c', 'd']

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
            question = line
        elif count in [1, 2, 3, 4]:
            # print(line)
            choices.append(line[3:])
        elif line:
            index = lets.index(line[0])
            if index != 0:
                choices[0], choices[index] = choices[index], choices[0]


            print(level, question, choices)
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
    """С коя функция дефинираме AMD модул?
a. declare
b. require
c. declaration
d. define
d
С кой метод се хвърлят/dispatch-ват събития в NodeJS?
a. fire
b. emit
c. throw
d. dispatch
b
Към какво сочи прототипа на последното звено от прототипната верига?
a. undefined
b. object
c. {}
d. null
d
Какъв вид модули използва NodeJS?
a. ES6 Harmony
b. SDK
c. CommonJS
d. AMD
c
В общия случай с коя команда изпълняваме NodeJS код?
a. execute
b. nodejs
c. npm
d. node
d"""
)