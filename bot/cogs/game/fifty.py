from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.embeds import QuestionEmbed, JokersEmbed
from bot.core.replies import Reply


class Fifty(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_id = str()

    @commands.guild_only()
    @commands.command(name=Cogs.Game.fifty, aliases=Cogs.Game.fifties)
    async def cut_2_answers(self, ctx):
        self.user_id = str(ctx.author.id)

        if self.user_id not in self.bot.games.keys():
            await ctx.send(Reply.not_in_game(self.user_id))
            return

        game = self.bot.games[self.user_id]

        if game.fifty:
            game.remove_2_choices()
            game.last_embed = QuestionEmbed(**game.last_question)

            await game.last_message.edit(embed=game.last_embed)
            game.fifty = False
        else:
            await ctx.send(Reply.used_50(self.user_id))
            embed = JokersEmbed(game.user.name,
                                game.user.avatar_url,
                                game.jokers_left())
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fifty(bot))