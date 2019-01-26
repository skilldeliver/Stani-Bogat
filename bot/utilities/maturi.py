


class Work:
    """
    Represents bulgarian literature work
    """
    questions = [
        'Кой е автора на',
        'Какъв е жанра на',
        'Кои са основните мотиви в'
    ]

    def __init__(self,
                 name: str,
                 genre: str,
                 author: str,
                 main_theme: str,
                 main_motives: list
                 ):
        self.name = name
        self.genre = genre
        self.author = author

        self.main_theme = main_theme
        self.man_motives = main_motives

    def ask_question(self):
        pass