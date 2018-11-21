from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self,
                 prefix: str,
                 ):
        commands.Bot.__init__(self,
                              command_prefix=prefix)

        self.games = dict()
