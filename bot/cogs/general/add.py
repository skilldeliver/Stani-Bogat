import re
import datetime
from discord.ext import commands

from bot.json_util import  append_to_pending
from bot.constants import Emoji
from bot.core.embeds import HowToAddEmbed, FormEmbed


class Add:
    def __init__(self, bot):
        self.bot = bot
        self.user = str()

    @commands.command(name='форма')
    async def print_form(self, ctx):
        embed = FormEmbed()
        await ctx.send(embed=embed)

    @commands.command(name='добави')
    async def print_how_to_add(self, ctx):
        self.user = self.bot.get_user(ctx.author.id)
        dm = self.user.dm_channel
        if not dm:
            dm = await self.user.create_dm()

        embed = HowToAddEmbed()
        await dm.send(embed=embed)
        embed = FormEmbed()
        await dm.send(embed=embed)

    @commands.command(name='добавям')
    async def add_it(self, ctx):
        self.user = self.bot.get_user(ctx.author.id)

        dm = self.user.dm_channel
        if not dm:
            dm = await self.user.create_dm()
        pins = await dm.pins()

        if not len(pins):
            await dm.send('Няма pin-нати съобщения в този чат.')
            return

        pattern = r'Име:(?P<name>.*)\n(Фото:(?P<image>.*)\n)?Тема:(?P<theme>.*)\nНиво:(?P<level>.*)\nВъпрос:(?P<question>.*)\nОтговор:(?P<answer>.*)\nДруг:(?P<other1>.*)\nДруг:(?P<other2>.*)\nДруг:(?P<other3>.*)'

        success = int()
        questions = list()

        for pin in pins:
            content = pin.content
            print(content)
            match = re.search(pattern, content)
            print(match)

            if match:
                success += 1
                await pin.add_reaction(Emoji.thumb_up)
                await pin.unpin()

                adict = match.groupdict()

                for k in adict:
                    if adict[k]:
                        new_item = adict[k].strip()
                    else:
                        new_item = None

                    if new_item:
                        adict[k] = new_item
                    else:
                        adict[k] = None

                adict['user'] = f'{self.user.name}#{self.user.discriminator}'
                adict['user_id'] = str(ctx.author.id)
                adict['date'] = str(datetime.datetime.now())
                questions.append(adict)
            else:
                await pin.add_reaction(Emoji.thumb_down)
                await pin.unpin()

        if questions:
            append_to_pending(questions)

        if len(pins) == 1 and success == 0:
            await dm.send('Pin-натото съобщение не отговаря на формата.')
        elif len(pins) == 1:
            await dm.send('Успешно изпратен въпрос. Очаква се преглед от модератор. Ще Ви известим ако въпроса Ви е в игра.')
        elif success == 0:
            await dm.send('Pin-натите съобщения не отговарят на формата.')
        else:
            await dm.send(f'{success} от {len(pins)} успешно изпратени въпроса. Очаква се преглед от модератор. Ще Ви известим ако въпросите Ви са в игра.')

def setup(bot):
    bot.add_cog(Add(bot))
