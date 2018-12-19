from discord.ext import commands
from discord import Embed

from bot.core.constants import MODS, Cogs, LargeText
from bot.utilities.json import get_pending, add_question


def is_mod():
    def predicate(ctx):
        return ctx.message.author.id in MODS
    return commands.check(predicate)

class Approve:
    def __init__(self, bot):
        self.bot = bot
        self.ctx = None
        self.question = None

    @is_mod()
    @commands.command(name=Cogs.Mod.mod)
    async def get_info(self, ctx):
        await ctx.send(LargeText.mod_cogs)

    @is_mod()
    @commands.command(name=Cogs.Mod.pending)
    async def get_question(self, ctx):
        self.ctx = ctx
        if self.question:
            await ctx.send('Има незатворен въпрос!')
            await self._send_question()
            return

        self.question = get_pending()
        if not self.question:
            await ctx.send('Няма висящи въпроси...')
            return
        await self._send_question()

    @is_mod()
    @commands.command(name=Cogs.Mod.approve)
    async def approve_question(self, ctx, arg):
        theme_map = {'ИТ': 'IT', 'общо': 'general', 'ИТБГ': 'ITBG'}
        image = None

        if arg == Cogs.Mod.image:
            image = self.question['image']
        q = self.question
        choices = [q['answer'], q['other1'], q['other2'], q['other3']]
        add_question(author=q['name'],
                     theme=theme_map[q['theme'].lower()],
                     question_level=q['level'],
                     question=q['question'],
                     choices=choices,
                     author_thumbnail=image
                     )
        await self._notify_user(int(q['user_id']), q['question'], True)
        self.question = None
        await ctx.send('Въпросът е добавен!')

    @is_mod()
    @commands.command(name=Cogs.Mod.reject)
    async def reject(self, ctx, *args):
        # TODO send explanation to the user for the rejecting reason
        text = " ".join(args)
        q = self.question
        await self._notify_user(int(q['user_id']), q['question'], False, text)
        self.question = None
        await ctx.send('Въпросът е отхвърлен!')

    @is_mod()
    @commands.command(name=Cogs.Mod.change)
    async def change_value(self, ctx, key, *args):
        self.ctx = ctx

        value = ' '.join(args)
        self.question[key] = value
        await self._send_question()

    @is_mod()
    @commands.command(name=Cogs.Mod.open)
    async def open_image(self, ctx, arg):
        self.ctx = ctx

        if arg == 'image':
            embed = Embed()
            embed.set_image(url=self.question['image'])
            await self.ctx.send(embed=embed)

    @is_mod()
    @commands.command(name=Cogs.Mod.get)
    async def get_key(self, ctx, arg):
        await ctx.send(self.question[arg])

    async def _send_question(self):
        string = str()
        for k, v in self.question.items():
            string += f'{k}:{v}\n'
            if k == 'other3':
                string += '\n\nExta data:\n'

        await self.ctx.send(f'''
            ```css
{string}```''')

    async def _notify_user(self, user_id, question, approved, text=''):
        user = self.bot.get_user(user_id)
        dm = user.dm_channel
        if not dm:
            dm = await user.create_dm()

        if approved:
            await dm.send(f'Въпросът `{question}`... е одобрен. Благодарим за съдействието.')
        else:
            await dm.send(f'Въпросът `{question}`... е отхвърлен. {text}')


def setup(bot):
    bot.add_cog(Approve(bot))