from time import strftime, gmtime
from discord import Embed

from bot.core.constants import PREFIX as P, Link, Text, LargeText, Color, Theme
from bot.core.replies import Reply


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

        self.set_author(name=Reply.game_title(question_level, player, question_leva),
                        icon_url=player_thumbnail)

        for key in answers:
            self.add_field(name=Reply.choice(key, answers[key]),
                           value=Text.invisible,
                           inline=False)

        if author_thumbnail:
            self.set_footer(text=Reply.question_added_by(author),
                            icon_url=author_thumbnail)
        else:
            self.set_footer(text=Reply.question_added_by(author))


class InfoEmbed(Embed):
    def __init__(self,
                 uptime,
                 python_version,
                 discord_version,
                 stars,
                 forks,
                 issues,
                 connected_servers,
                 total_members,
                 pc,
                 cpu_use,
                 ram,
                 ram_tot,
                 hdd,
                 hdd_tot):
        super().__init__(color=Color.info)


        uptime = strftime('%H hours %M mins %S secs', gmtime(uptime))

        self.set_author(name=Reply.github_repo(stars, forks, issues),
                        url=Link.github_repo,
                        icon_url=Link.github_icon)
        self.add_field(name='🤖 Бот:',
                       value=f'**Uptime**: {uptime}\n**Сървъри**: {connected_servers}\n**Потребители**: {total_members}')
        self.add_field(name=Text.host,
                       value=Reply.system_info(
                                               pc.node,
                                               pc.system,
                                               pc.release,
                                               cpu_use,
                                               ram,
                                               ram_tot,
                                               hdd,
                                               hdd_tot),
                       inline=False)
        self.add_field(name=Text.used_technologies,
                       value=Reply.used_tech(python_version,
                                             discord_version),
                       inline=False)
        # self.add_field(name=Text.author,
        #                value=Text.me,
        #                inline=False)
        self.add_field(name=Text.top_contributors,
                       value=Text.contributors,
                       inline=False)


class RightAnswerEmbed(Embed):
    def __init__(self):
        super().__init__(title=Text.right,
                         color=Color.right)


class WrongAnswerEmbed(Embed):
    def __init__(self):
        super().__init__(title=Text.wrong,
                         color=Color.wrong)


class JokersEmbed(Embed):
    def __init__(self,
                 player: str,
                 player_thumbnail: str,
                 image_url: str,):
        color = 0x1b87e7
        super().__init__(color=color)

        self.set_author(name=Reply.game_of(player),
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

        self.set_author(name=Reply.help_from_audience(player, question_level),
                        icon_url=player_thumbnail)
        for vote in votes:
            lines = votes[vote] * '|'
            if not lines:
                lines = Text.invisible

            self.add_field(name=Reply.letter_percent(vote, votes[vote]),
                           value=lines,
                           inline=False)

        self.set_footer(text=Reply.total_votes(count_votes))


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

        self.set_author(name=Reply.help_from_friend(player, helper, question_level),
                        icon_url=player_thumbnail)

        self.add_field(name=str(list(vote.keys())[0]),
                       value=str(list(vote.values())[0]),
                       inline=False)

        self.set_thumbnail(url=helper_thumbnail)


class CommandsEmbed(Embed):

    def __init__(self):
        super().__init__(color=Color.commands)
        self.add_field(name=Text.main_commands,
                       value=Reply.list_general_commands(P))
        self.add_field(name=Text.statistics,
                       value=Reply.list_stat_commands(P))

        self.add_field(name=Text.game_commands,
                       value=Reply.list_game_commands(P))


class RulesEmbed(Embed):
    def __init__(self):
        super().__init__(color=Color.rules)

        self.add_field(name=Text.rules,
value=LargeText.list_rules)

class ThemesEmbed(Embed):
    def __init__(self):
        super().__init__(color=Color.rules)

        themes = [t.lower() for t in Theme.game_themes]
        self.add_field(name=Text.themes,
value='\n'.join(themes))

class Top10Embed(Embed):
    def __init__(self, target, authors_n):
        super().__init__(color=Color.top)
        title = what = str()

        if target == 'authors':
            title = Text.top_authors
            what = Text.added_questions
        elif target == 'players':
            what = Text.points
            title = Text.top_players

        self.set_author(name=title,
                        icon_url=Link.leader_board_icon)

        for i in range(len(authors_n)):
            item = authors_n[i]
            if i == 0:
                self.add_field(name=Reply.first_place(i+1, item[0], item[1], what),
                               value=Text.invisible,
                               inline=False)
            elif i == 1:
                self.add_field(name=Reply.sec_place(i+1, item[0], item[1], what),
                               value=Text.invisible,
                               inline=False)    
            elif i == 2:
                self.add_field(name=Reply.third_place(i+1, item[0], item[1], what),
                               value=Text.invisible,
                               inline=False)
            else:
                self.add_field(name=Reply.other_place(i+1, item[0], item[1], what),
                               value=Text.invisible,
                               inline=False)


class HowToAddEmbed(Embed):
    def __init__(self):
        super().__init__(color=Color.how_add)
        self.add_field(name=Text.question_add,
                       value=LargeText.instructions)


class FormEmbed(Embed):
    def __init__(self):
        super().__init__(color=Color.form)
        self.add_field(name=Text.form,
                       value=LargeText.form
                       )

class StatsEmbed(Embed):
    def __init__(self,
                 name,
                 img_url,
                 games,
                 time,
                 money):
        super().__init__(color=Color.top)
        self.set_author(name=f'📊 Статистика на {name}')
        self.set_thumbnail(url=img_url)
        self.add_field(name=f'🎲 **Всички изиграни игри**: {games}',
                       value=Text.invisible,
                       inline=False)
        self.add_field(name=f'🕒 **Време в игри**: {time}',
                       value=Text.invisible,
                       inline=False)
        self.add_field(name=f'💰 **Спечелени пари**: {money} лева.',
                       value=Text.invisible,
                       inline=False)


class Total(Embed):
    def __init__(self,
                 games,
                 money,
                 time,
                 questions):
        secs = time
        mins = secs // 60
        hours = mins // 60

        time = f'{hours} hours {mins % 60} mins {secs % 60} secs'

        super().__init__(color=Color.top)
        self.set_author(name='ℹ     Сумирана информация:')
        self.add_field(name=f'🎮 **Всички изиграни игри**: {games}',
                       value=Text.invisible,
                       inline=False
                       )
        self.add_field(name=f'🤑 **Генерирани пари**: {money} лева.',
                       value=Text.invisible,
                       inline=False
                       )
        self.add_field(name=f'⏲ **Време в игри**: {time}',
                       value=Text.invisible,
                       inline=False
                       )
        self.add_field(name=f'🙋 **Въпроси**: {questions}',
                       value=Text.invisible,
                       inline=False
                       )
