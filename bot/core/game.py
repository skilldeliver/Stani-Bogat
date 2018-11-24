import random
import discord

from bot.constants import Image
from bot.json_util import load_question

from bot.core.embeds import QuestionEmbed


class Game:
    def __init__(self, user: discord.User):
        self.user = user
        self.question_level = 0
        self.letters = ['А)', 'Б)', 'В)', 'Г)']
        self.color = self._get_rand_color()
        self.right_answer = None

        # the jokers
        self.fifty = True
        self.friend = True
        self.audience = True

        self.last_question = None
        self.last_embed = None

        self.waiting_friend_help = False
        self.waiting_audience_help = False

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
        questions = load_question(str(self.question_level).zfill(2),
                                  'general')

        amount = self.question_amount_map[self.question_level]
        unpack = questions['1']

        question = f'{self.question_level}. {list(unpack.keys())[0]}'
        choices = list(unpack.values())[0]
        self.right_answer = choices[0]

        author = 'Skilldeliver'
        author_url = 'https://github.com/skilldeliver'
        author_thumbnail = 'https://i.imgur.com/GXTzOA0.png'

        random.shuffle(choices)
        self.answers = dict(zip(self.letters, choices))

        return dict(player=self.user.name,
                    player_thumbnail=self.user.avatar_url,
                    question=question,
                    question_leva=amount,
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
        return Image.jokers[key]

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
