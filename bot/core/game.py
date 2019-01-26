import random
import discord

from bot.core.constants import Sprite
from bot.utilities.json import load_question


class Game:
    def __init__(self,
                 user: discord.User,
                 channel,
                 theme: str,
                 start: int):
        # the user - discord.User instance
        self.user = user
        self.channel = channel
        self.map_themes = {'ОБЩО':'general',
                           'ИТБГ': 'ITBG',
                           'ИТ': 'IT',
                           'БЕЛ': 'BEL',
                           'БЕЗЖИЧНИ_МРЕЖИ': 'wireless_networks',
                           'ГЕОГРАФИЯ': 'geography'}

        self.theme = self.map_themes[theme]
        self.start = start

        self.question_level = 0
        self.ctx = None

        self.letters = ['A)', 'B)', 'C)', 'D)']
        self.color = self._get_rand_color()  # color of the question embed
        self.right_answer = None  # save the right answer

        # the jokers
        self.fifty = True
        self.friend = True
        self.audience = True

        self.start_question = int()
        # save the last question dict and embed to change them later
        self.last_question = None
        self.last_embed = None
        self.last_message =  None

        self.helper_id = None

        self.start_friend_help = int()
        self.start_audience_help = int()

        self.add_friend_reaction = False
        self.add_audience_reaction = False

        self.friend_msg = None
        self.audience_msg = None

        # boolean values to check if the joker is running
        # similar with the previous ones - but those expire after 30 secs
        self.waiting_friend_help = False
        self.waiting_audience_help = False

        # store the audience votes in a dictionary
        self.audience_votes = dict(zip(self.letters, [set(),
                                                      set(),
                                                      set(),
                                                      set()]))

        # audience help should be only from one channel
        # that's why we keep it - should take votes only from
        # the same channel
        self.audience_channel = str()

        # price of every question
        self.question_amount_map = [0,
                                    50,
                                    100,
                                    200,
                                    300,
                                    500,
                                    700,
                                    1_000,
                                    1_500,
                                    2_000,
                                    2_500,
                                    5_000,
                                    10_000,
                                    15_000,
                                    20_000,
                                    100_000]

    def ask(self)->dict:
        self.question_level += 1
        amount = self.question_amount_map[self.question_level]

        data = load_question(str(self.question_level).zfill(2),
                             self.theme)

        author = data["author"]
        author_thumbnail = data["author_thumbnail"]

        question = data["question"]
        choices = data["choices"]
        self.right_answer = choices[0]

        print(self.right_answer)
        random.shuffle(choices)
        self.answers = dict(zip(self.letters, choices))

        return dict(player=self.user.name,
                    player_thumbnail=self.user.avatar_url,
                    question=question,
                    question_leva=amount,
                    question_level=self.question_level,
                    answers=self.answers,
                    color=self.color,
                    author=author,
                    author_thumbnail=author_thumbnail,
                    )

    def remove_2_choices(self)->None:
        removed = 0
        loop = 0

        while removed < 2:
            try:
                choice = self.letters[random.randint(0, 3-removed)]
                to_remove = self.last_question['answers'][choice]
            except KeyError:
                continue

            if to_remove != self.right_answer:
                del self.last_question['answers'][choice]
                removed += 1

            loop += 1
            if loop > 200:
                print('''
                \n\n\nInfinity while loop error!
                bot.core.game.py line - 88!\n\n\n
                ''')
                break

    def correct_answer(self, ans: str)->bool:
        return self.answers[f'{ans})'] == self.right_answer

    def jokers_left(self)->str:
        lrs = 'xo'
        n1 = int(self.fifty)
        n2 = int(self.friend)
        n3 = int(self.audience)

        key = f'{lrs[n1]}{lrs[n2]}{lrs[n3]}'
        return Sprite.jokers[key]

    def get_audience_votes(self)->dict:
        votes = dict()
        count_votes = int()

        for letter in self.audience_votes:
            votes[letter] = len(self.audience_votes[letter])
            count_votes += len(self.audience_votes[letter])

        try:
            coef = 100 / count_votes
        except ZeroDivisionError:
            coef = 0

        for letter in votes:
            votes[letter] = int(round(votes[letter] * coef, 0))

        return dict(player=self.user.name,
                    player_thumbnail=self.user.avatar_url,
                    question_level=self.question_level,
                    count_votes=count_votes,
                    votes=votes,
                    color=self.color)


    def return_money(self, wrong_answer=True)->int:
        if wrong_answer:
            secure_prices = [2500, 500]
            if self.question_level > \
               self.question_amount_map.index(secure_prices[0]):
                return secure_prices[0]
            if self.question_level > \
               self.question_amount_map.index(secure_prices[1]):
                return secure_prices[1]
            return 0
        else:
            if self.question_level == 0:
                return 0
            else:
                return self.question_amount_map[self.question_level - 1]

    @staticmethod
    def _get_rand_color():
        r = lambda: random.randint(0, 255)
        hex_num = f'0x{r():02X}{r():02X}{r():02X}'
        return int(hex_num, 16)
