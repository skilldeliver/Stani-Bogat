import asyncio
import re

from discord.ext import commands


class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='помощ')
    async def get_help(self, ctx, arg):  # arg - приятел[tag] or публика
        user_id = ctx.author.id
        game = self.bot.games[str(user_id)]

        if arg == 'публика':
            await ctx.send('Нека публиката се включи сега!')
            game.audience = False
        else:
            help_user_id = self._extract_id_from_tag(arg)
            if help_user_id and game.friend:
                help_user = self.bot.get_user(help_user_id)
                if help_user.bot and help_user_id != user_id:
                    msg = await ctx.send(f'{help_user.name}, имаш 30 секунди да помогнеш на своят приятел.')
                    game.friend = False
                    for i in range(29, -1, -1):
                        await asyncio.sleep(1)
                        await msg.edit(content=f'{help_user.name}, имаш {i} секунди да помогнеш на своят приятел.')
                await msg.add_reaction('\u23f0')

    @staticmethod
    def _extract_id_from_tag(tag):
        try:
            user_id = re.search(r'<@(\d*)>', tag).group(1)
            return int(user_id)
        except Exception:
            return None


def setup(bot):
    bot.add_cog(Help(bot))
