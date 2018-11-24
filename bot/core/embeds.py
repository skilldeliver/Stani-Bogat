from platform import python_version, uname

import discord
from discord import Embed


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
        super().__init__()
        self.set_author(name=f'ГитХъб репо',
                        url='https://github.com/skilldeliver/Stani-Bogat',
                        icon_url='https://avatars2.githubusercontent.com/u/37806520?s=400&u=581fd4ac6786e8d1e4880f51922592d1945aaaeb&v=4')
        self.add_field(name=f'Дискорд сървъри:',
                       value=f'{connected_servers}',
                       inline=False)
        self.add_field(name=f'Хост:',
                       value=f'{pc.node}\n{pc.system} {pc.release}',
                       inline=False)
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
