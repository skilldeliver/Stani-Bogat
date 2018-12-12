from discord.ext import commands

class Approve:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='approve')
    def approve_question(self, arg):
        pass

def setup(bot):
    bot.add_cog(Approve(bot))