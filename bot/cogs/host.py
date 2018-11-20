import asyncio
import re

import discord
from discord.ext import commands
from discord import Embed
from discord.ext.commands.context import Context

from bot.core.game import Game
from bot.core.users import Users
from bot.core.embeds import QuestionEmbed, WrongAnswerEmbed, RightAnswerEmbed,\
    JokersEmbed


class Host:
    """
    Handles these cogs:
        игра,
        [A, Б, В, Г, а, б, в, г](answer),
        помощ публика,
        помощ [tag],
        50:50,
        жокери,
        спирам
    """
    letters = list("BCDabcdАВСас")

    def __init__(self, bot):
        self.bot = bot
        self.games_queue = dict()

    @commands.command(name='игра', aliases=['новаигра'])
    async def new_game(self, ctx):
        '''
        Creates new Game.
        Add it to the game queue (dictionary).
        Key - string of the user ID
        Value - instance of the bot.core.game.Game class
        '''

        # get a User object of the author
        user = self.bot.get_user(ctx.author.id)
        user_id = str(user.id)

        if user_id in self.games_queue:
            await ctx.send(f'<@{user_id}>, все още не си приключил играта ти.')
            return

        # Create new Game and bind it to the user_id in the queue
        self.games_queue[user_id] = Game(user)
        await ctx.send(f'<@{user_id}>, твоята игра започва сега!')
        await asyncio.sleep(1)

        # ask the first question
        question_data = self.games_queue[user_id].ask()
        embed = QuestionEmbed(**question_data)

        self.games_queue[user_id].last_question = question_data
        self.games_queue[user_id].last_embed = await ctx.send(embed=embed)

    @commands.command(name='А', aliases=list("БВГабвг"))
    async def take_answer(self, ctx):
        user_id = str(ctx.author.id)
        game = self.games_queue[user_id]

        if user_id not in self.games_queue.keys():
            await ctx.send(f'<@{user_id}>, не си в игра.')
        else:
            await asyncio.sleep(0.5)
            answer = ctx.message.content[1:].upper()

            if self.games_queue[user_id].correct_answer(answer):
                await ctx.message.add_reaction('\u2705')
                embed = RightAnswerEmbed()
                await ctx.send(embed=embed)

                await asyncio.sleep(1.5)
                question_data = self.games_queue[user_id].ask()
                embed = QuestionEmbed(**question_data)

                game.last_question = question_data
                game.last_embed = await ctx.send(embed=embed)
            else:
                await ctx.message.add_reaction('\u274C')
                embed = WrongAnswerEmbed()
                await ctx.send(embed=embed)
                del self.games_queue[user_id]

                await asyncio.sleep(1.5)
                await ctx.send(f'<@{user_id}>, твоята игра приключи. Тръгваш си с - {0} лева.')

    @commands.command(name='помощ')
    async def get_help(self, ctx, arg):  # arg - приятел[tag] or публика
        user_id = ctx.author.id
        game = self.games_queue[str(user_id)]

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

    @commands.command(name='50:50', aliases=['50/50', '5050', '50%50'])
    async def cut_2_answers(self, ctx):
        game = self.games_queue[str(ctx.author.id)]

        if game.fifty:
            game.remove_2_choices()
            embed = QuestionEmbed(**game.last_question)

            await game.last_embed.edit(embed=embed)
            game.fifty = False
        else:
            await ctx.send(f'<@{ctx.author.id}>, използвал си 50:50.')
            embed = JokersEmbed(game.user.name,
                                game.user.avatar_url,
                                game.jokers_left())
            await ctx.send(embed=embed)

    @commands.command(name='жокери', aliases=['жокер'])
    async def jokers(self, ctx):
        user_id = str(ctx.author.id)
        game = self.games_queue[user_id]

        embed = JokersEmbed(game.user.name,
                            game.user.avatar_url,
                            game.jokers_left())
        await ctx.send(embed=embed)

    @commands.command(name='спирам')
    async def terminate(self, ctx):
        await ctx.send(f'<@{ctx.author.id}>, игра ти приключва и си взимаш парите.')

    @staticmethod
    def _extract_id_from_tag(tag):
        try:
            user_id = re.search(r'<@(\d*)>', tag).group(1)
            return int(user_id)
        except Exception:
            return None


def setup(bot):
    bot.add_cog(Host(bot))
