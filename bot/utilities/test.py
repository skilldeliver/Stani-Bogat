import json

author = 'ДОЦ. Д-Р ЮЛИАНА ПЕНЕВА'
theme = 'SQL'


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


fill("""Въпрос 6: В SQL командата ALTER:
а)променя данните в указаната таблица;
б)изтрива редове от указаната таблица;
в)променя структурата на схемата;
г)друго.
В
Въпрос 7: В SQL данни се извличат чрез командата:
а)UPDATE DATABASE;
б)USE TABLE;
в)SELECT;
г)и трите са верни.
В
Въпрос 17: Какъв е резултатът от изпълнението на следната SQL заявка: Select E.Fname, E.Lname, S.Fname.S.Lname From Employee Е S  Where E.Manager=S.Egn
а)грешен синтаксис;
б)извежда имената на служителите и съответните им ръководители;
в)извежда съименниците;
г)комбинира по случаен начин име и фамилия.
Б
Въпрос 2: За езика SQL е вярно:
а)интегриран език;
б)може да се вгражда в език за програмиране;
в)стандартизиран;
г)и трите са верни.
Г
Въпрос 4: В SQL обекти се унищожават чрез командата:
а)DELETE;
б)DROP;
в)ALTER;
г)друго.
Б
Въпрос 10: В SQL командата DELETE:
а)променя структурата на указаната таблица;
б)изтрива редове от указаната таблица;
в)премахва схемата от каталога;
г)друго.
Б
Въпрос 18: Какъв е резултатът от изпълнението на следната SQL заявка: Select count(*) From Employee, Department Where Dno=Dnumber and Dname ='Изследователски'
а)извежда броя на редовете в получената таблица;
б)извежда броя на служителите в посочения отдел ;
в)заявката няма смисъл;
г)извежда число.
Б
Въпрос 20: Какъв е резултатът от изпълнението на следната SQL заявка: Delete From Employee
а)изтрива всички данни за служителите;
б)изтрива таблицата Employee;
в)изтрива описанието на таблицата от каталога;
г)изтрива базата.
А
Въпрос 1: Разликата между релационната алгебра и SQL е:
а)те са несравними;
б)SQL допуска идентични кортежи в релацията;
в)релационната алгебра е подмножество на SQL;
г)няма разлика.
Б
Въпрос 16: Какъв е резултатът от изпълнението на следната SQL заявка: Select Pnumber, Pname, count (*) From Project, Works_on  Where Pnumber=Pno Group by Pnumber, Pname
а)извежда номерата и имената на проектите;
б)извежда за всеки проект номер, име и брой на работещите по него служители;
в)извежда броя на проектите;
г)грешен синтаксис.
Б
Въпрос 11: Какъв е резултатът от изпълнението на следната SQL заявка: Select Fname, Lname  From EMPLOYEE  Where Egn LIKE '75%’
а)извежда имената и ЕГН на всички служители;
б)извежда имената на служителите, родени през 1975 година;
в)извежда имената на служителите;
г)извежда ЕГН на служителите.
Б
Въпрос 12: Какъв е резултатът от изпълнението на следната SQL заявка: Select Fname, Lname  From Employee  Where Manager is null
а)извежда имената на всички служители и техните ръководители;
б)извежда имената на служителите;
в)извежда имената на служителите, които са ръководители;
г)друго.
А
Въпрос 15: Какъв е резултатът от изпълнението на следната SQL заявка: Select Dno, count (*), avg (salary) From Employee Group by Dno
а)извежда средната заплата по отдели;
б)извежда за всеки отдел номер, брой служители и средна заплата;
в)извежда средната заплата;
г)извежда броя на редовете на указаната таблица.
Б
Въпрос 2: За езика SQL е вярно:
а)интегриран език;
б)може да се вгражда в език за програмиране;
в)стандартизиран;
г)и трите са верни.
Г
Въпрос 9: В SQL условието за групиране се задава чрез:
а)WHERE;
б)GROUP BY;
в)HAVING;
г)ORDER BY.
Б""")