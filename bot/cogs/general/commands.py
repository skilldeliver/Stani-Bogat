from discord.ext import commands


class Commands:
    """ Handles this cog - команди"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='команди')
    async def print_info(self, ctx):
        await ctx.send(f"""
        <@{ctx.author.id}>, *игра, *[A, B, C, D], *помощ [приятел(tag)], *помощ публика,
        *50/50, *правила, *жокери, *спирам, *топ10, *статс, *инфо, *команди, *команда [команда]
        """)


def setup(bot):
    bot.add_cog(Commands(bot))
