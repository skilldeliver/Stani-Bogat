from platform import python_version

import discord
from discord import Embed


class QuestionEmded(Embed):
    def __init__(self,
                 question: str,
                 question_leva: int,
                 answers: str,
                 color: int,
                 author: str,
                 author_url=Embed.Empty,
                 author_thumbnail=Embed.Empty
                 ):
        Embed.__init__(self,
                       title=question,
                       color=color)

        self.set_author(name=f'Добавен от: {author}',
                        url=author_url,
                        icon_url=author_thumbnail)

        for key in answers:
            self.add_field(name=key,
                           value=answers[key],
                           inline=False)

        self.set_footer(text=f"Въпрос за {question_leva} лева.")


class InfoEmbed(Embed):
    def __init__(self):
        Embed.__init__(self)
        self.set_author(name=f'ГитХъб репо',
                        url='https://github.com/skilldeliver',
                        icon_url='https://avatars2.githubusercontent.com/u/37806520?s=400&u=581fd4ac6786e8d1e4880f51922592d1945aaaeb&v=4')
        self.add_field(name='Използвани технологии:',
                       value=f'discord.py rewrite branch {discord.__version__},\n Python {python_version()} :snake:',
                       inline=False)
        self.add_field(name='Автор:',
                       value='Владислав Михов',
                       inline=False)
        self.add_field(name='Топ сътрудници(contributors):',
                       value=':one:Някакво име\n:two:Друго име',
                       inline=False)


class WrongAnswerEmbed(Embed):
    def __init__(self):
        text = f'Грешен отговор!'
        color = 0xdd2e44

        Embed.__init__(self,
                       title=text,
                       color=color)


class RightAnswerEmbed(Embed):
    def __init__(self):
        text = f'Верен отговор!'
        color = 0x77b255

        Embed.__init__(self,
                       title=text,
                       color=color)


class CommandsEmbed(Embed):
    pass


class StatsEmbed(Embed):
    pass


class Top10Embed(Embed):
    pass
