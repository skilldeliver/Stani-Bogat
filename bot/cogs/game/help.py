import asyncio
import re

from discord.ext import commands

from bot.core.embeds import JokersEmbed, AudienceEmbed


class Help:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ембед')
    async def test(self, ctx, arg):
        letters = ['А)', 'Б)', 'В)', 'Г)']
        pers = arg.replace(',', ' ').split()

        adict = dict(zip(letters, map(int, pers)))
        embed = AudienceEmbed(adict, color=0x77b255)
        await ctx.send(embed=embed)

    @commands.command(name='помощ')
    async def get_help(self, ctx, arg):  # arg - приятел[tag] or публика
        user_id = ctx.author.id
        game = self.bot.games[str(user_id)]

        if arg == 'публика':
            if game.audience:
                msg = await ctx.send('Нека публиката се включи сега! Оставящи 30 секунди.')
                game.audience = False

                game.waiting_audience_help = True
                game.audience_channel = ctx.channel

                for i in range(29, -1, -1): # count seconds 
                    await asyncio.sleep(1)
                    await msg.edit(content=f'Нека публиката се включи сега! Оставящи {i} секунди.')
                game.waiting_audience_help = False
                await ctx.send(game.audience_votes)
            else:
                await ctx.send(f'<@{user_id}>, използвал си помощ от публиката.')
                embed = JokersEmbed(game.user.name,
                                    game.user.avatar_url,
                                    game.jokers_left())
                await ctx.send(embed=embed)

        # TODO pack this shit into methods >>>>
        else:  # helper is invoked
            help_user_id = self._extract_id_from_tag(arg)  # get his id with regex
            if help_user_id and game.friend:  # assert that is a thing and the player still has a friend joker
                if str(help_user_id) not in self.bot.games.keys():  # assert that the helper is not in a game
                    help_user = self.bot.get_user(help_user_id)   #  get discord.User object

                    if not help_user.bot and help_user_id != user_id: # the helper is not a bot or the player itself
                        msg = await ctx.send(f'{help_user.name}, имаш 30 секунди да помогнеш на своят приятел.')
                        game.friend = False # the joker is gone
                        self.bot.helping_friends[str(help_user_id)] = str(user_id) # add the helper to the queue and bind the player id
                        game.waiting_friend_help = True
                        print(self.bot.helping_friends)
                        for i in range(29, -1, -1): # count seconds
                            if not game.waiting_friend_help:
                                break
                            await asyncio.sleep(1)
                            await msg.edit(content=f'{help_user.name}, имаш {i} секунди да помогнеш на своят приятел.')
                        game.waiting_friend_help = False
                    await msg.add_reaction('\u23f0')
                    del self.bot.helping_friends[str(help_user_id)] # remove the helper from the queue
                else:
                    await ctx.send(f'{user_id}, не може да искаш помощ от потребител в игра.')

    @staticmethod
    def _extract_id_from_tag(tag):
        try:
            user_id = re.search(r'<@(\d*)>', tag).group(1)
            return int(user_id)
        except Exception:
            return None


def setup(bot):
    bot.add_cog(Help(bot))
