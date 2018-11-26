from platform import python_version, uname

import github
import discord
from discord import Embed

g = github.Github('none', 'none')


class QuestionEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 question: str,
                 question_leva: int,
                 answers: dict,
                 color: int,
                 author: str,
                 author_thumbnail: str,
                 ):
        super().__init__(
                         title=question,
                         color=color)

        self.set_author(name=f'Играта на {player}. Въпрос за {question_leva} лева.',
                        icon_url=player_thumbnail)

        for key in answers:
            self.add_field(name=key,
                           value=answers[key],
                           inline=False)

        self.set_footer(text=f"Въпрос добавен от {author}.",
                        icon_url=author_thumbnail)


class InfoEmbed(Embed):
    def __init__(self, connected_servers: int):
        pc = uname()
        super().__init__(color=0x000000)

        repo = g.get_repo("skilldeliver/Stani-Bogat")
        stars = repo.stargazers_count
        issues = repo.open_issues_count
        forks = repo.forks_count

        owner = repo.owner

        self.set_author(name=f'ГитХъб репо. {stars} \u2b50 {forks} 🍴 {issues} \u2757',
                        url='https://github.com/skilldeliver/Stani-Bogat',
                        icon_url='https://camo.githubusercontent.com/7710b43d0476b6f6d4b4b2865e35c108f69991f3/68747470733a2f2f7777772e69636f6e66696e6465722e636f6d2f646174612f69636f6e732f6f637469636f6e732f313032342f6d61726b2d6769746875622d3235362e706e67')
        self.add_field(name=f'Дискорд сървъри:',
                       value=f'{connected_servers}',
                       inline=False)
        self.add_field(name=f'Хост:',
                       value=f'{pc.node}\n{pc.system} {pc.release}',
                       inline=False)
        self.add_field(name='Използвани технологии:',
                       value=f'''Python {python_version()} :snake:
discord.py rewrite branch {discord.__version__},
PyGithub
Pipenv''',
                       inline=False)
        self.add_field(name='Автор:',
                       value='Владислав Михов',
                       inline=False)
        self.add_field(name='Топ сътрудници(contributors):',
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


class CommandsEmbed(Embed):
    pass


class StatsEmbed(Embed):
    pass


class Top10Embed(Embed):
    pass
