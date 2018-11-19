from discord.ext import commands
from discord import Embed

from bot.core.game import Game
from bot.core.users import Users
from bot.core.embeds import QuestionEmded, WrongAnswerEmbed, RightAnswerEmbed


class Host:
    """
    Handles these cogs
    игра, [A, B, C, D](отговор), помощ публика,
    помощ приятел, 50/50, жокери, спирам
    """
    letters = list("BCDabcdАВСас")

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='игра', aliases=['новаигра'])
    async def new_game(self, ctx):
        embed = QuestionEmded(
            question='3. Как се нарича човек, който не вярва в Бог?',
            answers={'А)': 'нихилист', 'Б)': 'атеист',
                     'В)': 'екзистенциалист', 'Г)': 'пацифист'},
            color=0xb6f7c2,
            question_leva=2000,
            # thumbnail_url='https://i.imgur.com/pLTtYwk.png',
            author='Skilldeliver',
            author_url='https://github.com/skilldeliver',
            author_thumbnail='https://i.imgur.com/GXTzOA0.png'
        )
        embed = RightAnswerEmbed()
        alist = list()
        # await ctx.send(embed=embed)
        user = self.bot.get_user(ctx.author.id)
        await ctx.send(f'{user.name} {user.discriminator}')
        # await ctx.send(f'<@{ctx.author.id}>, твоята игра започва сега!')

    @commands.command(name='A', aliases=list("BCDabcdАВСас"))
    async def take_answer(self, ctx):
        await ctx.send(f'<@{ctx.author.id}>, вземаме отговора и проверяваме верността му.')

    @commands.command(name='помощ')
    async def get_help(self, ctx, arg):  # arg - приятел or публика
        if arg == 'приятел':
            await ctx.send(f'<@{ctx.author.id}>, получаваш помощ от приятел.')
        elif arg == 'публика':
            await ctx.send(f'<@{ctx.author.id}>, получаваш помощ от публика.')

    @commands.command(name='50:50', aliases=['50/50', '5050', '50%50'])
    async def cut_2_answers(self, ctx):
        await ctx.send(f'<@{ctx.author.id}>, махат се два отговора.')

    @commands.command(name='жокери', aliases=['жокер'])
    async def jokers(self, ctx):
        embed = Embed(title="Твоите ж", color=0x2365b4)
        embed.set_image(url='https://vignette.wikia.nocookie.net/millionaire/images/c/c6/ClassicATA.png/revision/latest?cb=20160407180412')
        await ctx.send(embed=embed)
        # await ctx.send(f'<@{ctx.author.id}>, изписват се оставащите ти жокери')

    @commands.command(name='спирам')
    async def terminate(self, ctx):
        await ctx.send(f'<@{ctx.author.id}>, игра ти приключва и си взимаш парите.')


def setup(bot):
    bot.add_cog(Host(bot))
