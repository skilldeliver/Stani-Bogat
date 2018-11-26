import json
import random

from bot.constants import Path


def load_question(question_level, theme):
    with open(eval(f'Path.{theme}').joinpath(f'{question_level}/questions.json'), encoding="utf8") as f:
        return json.load(f)
