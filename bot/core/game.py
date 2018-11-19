import random
from bot.questions import questions


class Game:
    def __init__(self, user_id: int):
        self.user = user_id
        self.question_level = 0

    def ask(self):
        self.question_level += 1
        unpack = questions[str(self.question_level)]
        question = unpack.keys()[0]
        answers = unpack.values()[0]

    def format_question(self, q, r, a):
        string = f"""{question}
                    """




