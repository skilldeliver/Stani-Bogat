import re
import datetime
from discord.ext import commands

from bot.utilities.json import append_to_pending
from bot.core.constants import Cogs, Emoji, Regex, Text, GOD
from bot.core.embeds import HowToAddEmbed, FormEmbed
from bot.core.replies import Reply


class Add:
    def __init__(self, bot):
        self.bot = bot
        self.user = str()

    @commands.command(name=Cogs.General.form)
    async def print_form(self, ctx):
        embed = FormEmbed()
        await ctx.send(embed=embed)

    @commands.command(name=Cogs.General.add)
    async def print_how_to_add(self, ctx):
        self.user = self.bot.get_user(ctx.author.id)
        dm = self.user.dm_channel
        if not dm:
            dm = await self.user.create_dm()

        embed = HowToAddEmbed()
        await dm.send(embed=embed)
        embed = FormEmbed()
        await dm.send(embed=embed)

    @commands.command(name=Cogs.General.adding)
    async def add_it(self, ctx):
        self.user = self.bot.get_user(ctx.author.id)
        self.god = self.bot.get_user(GOD)

        dm = self.user.dm_channel
        if not dm:
            dm = await self.user.create_dm()
        pins = await dm.pins()

        if not len(pins):
            await dm.send(Text.no_pins)
            return

        pattern = Regex.form

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

                adict['user'] = Reply.user_name(self.user.name, self.user.discriminator)
                adict['user_id'] = ctx.author.id
                adict['date'] = str(datetime.datetime.now())
                questions.append(adict)
            else:
                await pin.add_reaction(Emoji.thumb_down)
                await pin.unpin()

        if questions:
            append_to_pending(questions)

        if len(pins) == 1 and success == 0:
            await dm.send(Text.pin_not_inform)
        elif len(pins) == 1:
            await dm.send(Text.success_send)
            await self.god.dm_channel.send('Има добавен въпрос!')
        elif success == 0:
            await dm.send(Text.pins_not_inform)
        else:
            await dm.send(Reply.successfully_send(success, len(pins)))
            await self.god.dm_channel.send('Има добавени въпроси!')

def setup(bot):
    bot.add_cog(Add(bot))
