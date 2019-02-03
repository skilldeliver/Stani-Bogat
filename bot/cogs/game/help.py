import re

from discord.ext import commands

from bot.core.embeds import JokersEmbed, AudienceEmbed
from bot.core.replies import Reply
from bot.core.constants import Cogs, Emoji, Regex


class Help:
    def __init__(self, bot):
        self.bot = bot
        self.user_id = str()
        self.ctx = None

    @commands.guild_only()
    @commands.command(name=Cogs.Game.help)
    async def get_help(self, ctx, arg):  # arg - приятел[tag] or публика
        self.ctx = ctx
        self.arg = arg

        self.user_id = str(ctx.author.id)

        if await self._request_help_from_audience():
            return

        await self._request_help_from_friend()

    async def _request_help_from_audience(self):
        if self.arg != Cogs.Game.audience:
            return

        if self.user_id not in self.bot.games.keys():
            await self.ctx.send(Reply.not_in_game(self.user_id))
            return True

        player_game = self.bot.games[self.user_id]
        if not player_game.audience:
            await self.ctx.send(Reply.used_audience(self.user_id))

            embed = JokersEmbed(player_game.user.name,
                                player_game.user.avatar_url,
                                player_game.jokers_left())
            await self.ctx.send(embed=embed)
            return True

        player_game.audience_msg = await self.ctx.send(Reply.audience_help(10))
        player_game.audience = False
        player_game.audience_channel = self.ctx.channel
        player_game.start_audience_help = self.bot.time

        player_game.waiting_audience_help = True


    async def _request_help_from_friend(self):
        if self.user_id not in self.bot.games.keys():
            await self.ctx.send(Reply.not_in_game(self.user_id))
            return

        player_game = self.bot.games[self.user_id]
        helper_id = self._extract_id_from_tag(self.arg)

        if not helper_id:
            await self.ctx.send(Reply.unknown_2_arg(self.user_id))
            return

        if not player_game.friend:
            await self.ctx.send(Reply.used_friend(self.user_id))

            embed = JokersEmbed(player_game.user.name,
                                player_game.user.avatar_url,
                                player_game.jokers_left())
            await self.ctx.send(embed=embed)
            return

        if str(helper_id) == self.user_id:
            await self.ctx.send(Reply.no_yourself(self.user_id))
            return

        if str(helper_id) in self.bot.games.keys():
            await self.ctx.send(Reply.no_player(self.user_id))
            return

        helper = self.bot.get_user(helper_id)
        # get discord.User object of the helper

        if helper.bot:
            await self.ctx.send(Reply.no_bot(self.user_id))
            return

        # Asserts that the helper is not a bot or the player itself
        player_game.friend_msg = await self.ctx.send(Reply.friend_help(helper.name, 10))
        player_game.helper_id = str(helper_id)
        player_game.friend = False
        # the joker is gone

        self.bot.helping_friends[str(helper_id)] = self.user_id
        # add the helper to the queue and bind the player id
        player_game.waiting_friend_help = True
        player_game.start_friend_help = self.bot.time

        # await self._count_seconds_down_friend(player_game,
        #                                       helper.name,
        #                                       msg)
        # remove the helper from the queue

    @staticmethod
    def _extract_id_from_tag(tag):
        if tag == Cogs.Game.audience:
            return True

        try:
            user_id = re.search(Regex.user_id, tag).group(1)
            return int(user_id)
        except Exception:
            return None

def setup(bot):
    bot.add_cog(Help(bot))
