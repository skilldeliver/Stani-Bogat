from platform import python_version, uname

import github
import discord
from discord import Embed

g = github.Github('ноне', 'ноне')


class QuestionEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 question: str,
                 question_leva: int,
                 question_level: int,
                 answers: dict,
                 color: int,
                 author: str,
                 author_thumbnail: str,
                 ):
        super().__init__(
                         title=question,
                         color=color)

        self.set_author(name=f'{question_level}. Играта на {player}. Въпрос за {question_leva} лева.',
                        icon_url=player_thumbnail)

        for key in answers:
            self.add_field(name=key,
                           value=answers[key],
                           inline=False)

        self.set_footer(text=f"Въпрос добавен от {author}.",
                        icon_url=author_thumbnail)


class InfoEmbed(Embed):
    def __init__(self, connected_servers: int, total_members: int):
        pc = uname()
        super().__init__(color=0x000000)

        repo = g.get_repo("skilldeliver/Stani-Bogat")
        stars = repo.stargazers_count
        issues = repo.open_issues_count
        forks = repo.forks_count

        owner = repo.owner

        self.set_author(name=f'ГитХъб репо. {stars} \u2b50 {forks} 🍴 {issues} \u2757',
                        url='https://github.com/skilldeliver/Stani-Bogat',
                        icon_url='https://avatars0.githubusercontent.com/u/9919?s=280&v=4')
        self.add_field(name=f'🏴 Дискорд сървъри:',
                       value=f'{connected_servers}',
                       inline=True)
        self.add_field(name=f':busts_in_silhouette: Потребители:',
                       value=f'{total_members}',
                       inline=True)
        self.add_field(name=f'💻 Хост:',
                       value=f'{pc.node}\n{pc.system} {pc.release}',
                       inline=False)
        self.add_field(name='🛠️ Използвани технологии:',
                       value=f'''Python {python_version()} :snake:
discord.py rewrite branch {discord.__version__},
PyGithub
Pipenv''',
                       inline=False)
        self.add_field(name='📝 Автор:',
                       value='Владислав Михов',
                       inline=False)
        self.add_field(name='👷 Топ сътрудници(contributors):',
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


class AudienceEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 question_level: int,
                 count_votes: int,
                 votes: dict,
                 color: int,
                 ):
        super().__init__(color=color)

        self.set_author(name=f'Играта на {player}. Гласoве на публиката за въпрос {question_level}.',
                        icon_url=player_thumbnail)
        for vote in votes:
            lines = votes[vote] * '|'
            if not lines:
                lines = u"\u2063"

            self.add_field(name=f'{vote} {votes[vote]} %',
                           value=f'{lines}',
                           inline=False)

        self.set_footer(text=f"Общо гласoве: {count_votes}.")


class FriendEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 helper: str,
                 helper_thumbnail: str,
                 question_level: int,
                 vote: dict,
                 color: int,
                 ):
        super().__init__(color=color)

        self.set_author(name=f'Играта на {player}. Предложението на {helper} за въпрос {question_level}.',
                        icon_url=player_thumbnail)

        self.add_field(name=f'{list(vote.keys())[0]}',
                       value=f'{list(vote.values())[0]}',
                       inline=False)

        self.set_thumbnail(url=helper_thumbnail)


class CommandsEmbed(Embed):
    pass


class StatsEmbed(Embed):
    pass


class Top10Embed(Embed):
    pass
