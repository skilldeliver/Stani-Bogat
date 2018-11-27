import asyncio

from discord.ext import commands

from bot.core.embeds import QuestionEmbed, RightAnswerEmbed, WrongAnswerEmbed,
FriendEmbed


class Answer:
    def __init__(self, bot):
        self.bot = bot
        self.player_id = str()
        self.ctx = str()

    @commands.command(name='А', aliases=list("БВГабвг"))
    async def take_answer(self, ctx):
        self.player_id = str(ctx.author.id)  # id of the player or helper
        self.ctx = ctx

        # first of all take the vote from the audience
        if self._take_vote_from_audience():
            # the audience voter vote is taken so the method 'breaks'
            return

        # then try to get help from of friend
        if await self._take_help_from_friend():
            # vote from friend is taken so the method 'breaks'
            return

        # assert that the user is in game
        if await self._user_not_in_game():
            # break if the user is not in game
            return

        # finnaly try to take the player answer
        await self._take_player_answer()

    def _take_vote_from_audience(self)->bool:
        """
        Asserts key conditions to be valid audience vote.
        Returns True if the audience voter vote is taken.
        """
        voter = self.player_id

        # iterate all current games.
        for game in self.bot.games.values():
            if game.waiting_audience_help:
                # Asserts that any of the players is waiting for help.
                if voter != str(game.user.id) and \
                   self.ctx.channel != game.audience_channel:
                    # Asserts that the audience voter it's not the player.
                    # Asserts that the audience voter is in the same channel.

                    letter = self.ctx.message.content[1:].upper() + ')'
                    # takes the letter suggested from the audience voter
                    game.audience_votes[f'{letter}'].add(voter)
                    # add the audience voter vote
                    return True

    async def _take_help_from_friend(self)->bool:
        """
        Asserts key conditions to be valid friend help (vote).
        Returns True if the friend vote is taken.
        """
        friend_id = self.player_id

        if friend_id in self.bot.helping_friends.keys():
            # Asserts that the friend id  tagged by another player
            #   ^ helping_friends stores friends who are tagged for help
            letter = self.ctx.message.content[1:].upper() + ')'
            # get the letter suggested from the friend

            friend = self.bot.get_user(int(friend_id))
            # get the discord.User object of the friend
            help_for = self.bot.helping_friends[friend_id]
            # get the player id who the help is for

            game = self.bot.games[help_for]
            # get his(player) Game

            if game.waiting_friend_help:
                # Asserts that this player is still waiting for friend help
                val = game.last_question['answers'][letter]
                vote = {letter: val}
                # get the letter and option of the friend suggestion

                embed = FriendEmbed(player=game.user.name,
                                    player_thumbnail=game.user.avatar_url,
                                    helper=helper.name,
                                    helper_thumbnail=helper.avatar_url,
                                    question_level=game.question_level,
                                    vote=vote,
                                    color=game.color)
                # make Friend embed and send it in the chat
                await self.ctx.send(embed=embed)
                return True

    async def _user_not_in_game(self)->bool:
        if self.player_id not in self.bot.games.keys():
            await self.ctx.send(f'<@{self.player_id}>, не си в игра.')
            return True

    async def _take_player_answer(self):
            game = self.bot.games[self.player_id]  # the game of the player
            await asyncio.sleep(0.5)
            answer = self.ctx.message.content[1:].upper()

            if self.bot.games[self.player_id].correct_answer(answer):
                await self.ctx.message.add_reaction('\u2705')
                embed = RightAnswerEmbed()
                await self.ctx.send(embed=embed)

                await asyncio.sleep(1.5)
                question_data = self.bot.games[self.player_id].ask()
                embed = QuestionEmbed(**question_data)

                game.waiting_audience_help = False
                game.waiting_friend_help = False

                game.last_question = question_data
                game.last_embed = await self.ctx.send(embed=embed)
            else:
                await self.ctx.message.add_reaction('\u274C')
                embed = WrongAnswerEmbed()
                await self.ctx.send(embed=embed)

                del self.bot.games[self.player_id]

                await asyncio.sleep(1.5)
                await self.ctx.send(f'<@{self.player_id}>, твоята игра приключи. \
Тръгваш си с - {game.return_money()} лева.')


def setup(bot):
    bot.add_cog(Answer(bot))
