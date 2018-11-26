from discord.ext import commands

from bot.core.embeds import JokersEmbed


class Jokers:
    def __init__(self, bot):
        self.bot = bot
        self.player_id = str()

    @commands.command(name='жокери', aliases=['жокер'])
    async def jokers(self, ctx):
        self.player_id = str(ctx.author.id)

        if self.player_id not in self.bot.games.keys():
            await ctx.send(f'<@{self.player_id}>, не си в игра.')
            return

        game = self.bot.games[self.player_id]
        embed = JokersEmbed(game.user.name,
                            game.user.avatar_url,
                            game.jokers_left())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jokers(bot))
