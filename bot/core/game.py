import random

import discord


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

        self.question_amount_map = [50,
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
        from bot.json_util import load_question

        self.question_level += 1
        questions = load_question(str(self.question_level).zfill(2),
                                  'general')

        amount = self.question_amount_map[self.question_level - 1]
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

    def correct_answer(self, ans):
        print(self.answers[f'{ans})'], self.right_answer)
        return self.answers[f'{ans})'] == self.right_answer

    @staticmethod
    def _get_rand_color():
        r = lambda: random.randint(0, 255)
        hex_num = f'0x{r():02X}{r():02X}{r():02X}'
        return int(hex_num, 16)
