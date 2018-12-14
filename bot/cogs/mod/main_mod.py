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
            await ctx.send()
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
        theme_map = {'ИТ': 'IT', 'общо': 'general'}
        image = None

        if arg == Cogs.Mod.image:
            image = self.question['image']
        q = self.question
        choices = [q['answer'], q['other1'], q['other2'], q['other3']]
        add_question(author=q['name'],
                     theme=theme_map[q['theme']],
                     question_level=q['level'],
                     question=q['question'],
                     choices=choices,
                     author_thumbnail=image
                     )
        self.question = None
        await ctx.send('Въпросът е добавен!')

    @is_mod()
    @commands.command(name=Cogs.Mod.reject)
    async def reject(self, ctx):
        # TODO send explanation to the user for the rejecting reason
        self.question = None
        await ctx.send('Въпросът е отхвърлен!')

    @is_mod()
    @commands.command(name=Cogs.Mod.change)
    async def change_value(self, ctx, key, value):
        self.ctx = ctx

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

    async def _notify_user(self, user_id, approved,):
        #TODO finish notifiying user
        user = self.bot.get_user(user_id)
        dm = self.user.dm_channel
        if not dm:
            dm = await self.user.create_dm()

        dm.send()


def setup(bot):
    bot.add_cog(Approve(bot))