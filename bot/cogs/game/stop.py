from discord.ext import commands

from bot.core.constants import Cogs
from bot.core.replies import Reply
from bot.utilities.json import save_player_money


class Stop:
    def __init__(self, bot):
        self.bot = bot
        self.user_id = str()

    @commands.guild_only()
    @commands.command(name=Cogs.Game.stop)
    async def terminate(self, ctx):
        self.user_id = str(ctx.author.id)

        if self.user_id not in self.bot.games.keys():
            await ctx.send(Reply.not_in_game(self.user_id))
            return

        game = self.bot.games[self.user_id]
        player = Reply.user_name(game.user.name, game.user.discriminator)
        money = game.return_money(wrong_answer=False)

        await game.last_embed.delete()
        if money:
            save_player_money(player, money)

        del self.bot.games[self.user_id]
        await ctx.send(Reply.end_game(self.user_id, money))


def setup(bot):
    bot.add_cog(Stop(bot))
