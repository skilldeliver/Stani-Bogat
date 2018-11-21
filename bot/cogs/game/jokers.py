from discord.ext import commands

from bot.core.embeds import JokersEmbed


class Jokers:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='жокери', aliases=['жокер'])
    async def jokers(self, ctx):
        user_id = str(ctx.author.id)
        game = self.bot.games[user_id]

        embed = JokersEmbed(game.user.name,
                            game.user.avatar_url,
                            game.jokers_left())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jokers(bot))
