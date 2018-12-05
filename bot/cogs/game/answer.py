import asyncio

from discord.ext import commands

from bot.core.embeds import QuestionEmbed, RightAnswerEmbed, WrongAnswerEmbed,\
    FriendEmbed
from bot.core.replies import Reply


class Answer:
    def __init__(self, bot):
        self.bot = bot
        self.user_id = str()
        self.ctx = None

    @commands.command(name='А', aliases=list("БВГабвг"))
    async def take_answer(self, ctx):
        self.ctx = ctx
        self.user_id = str(ctx.author.id)
        # player, just user, audience voter or friend

        print(self.bot.helping_friends.keys())
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
        voter = self.user_id  # appropriate variable name

        # iterate all current games.
        for player_game in self.bot.games.values():
            if player_game.waiting_audience_help:
                # Asserts that any of the players is waiting for help.
                if voter != str(player_game.user.id) and \
                   self.ctx.channel == player_game.audience_channel:
                    # Asserts that the audience voter it's not the player.
                    # Asserts that the audience voter is in the same channel.

                    letter = self.ctx.message.content[1:].upper() + ')'
                    # takes the letter suggested from the audience voter
                    player_game.audience_votes[f'{letter}'].add(voter)
                    # add the audience voter vote
                    return True

    async def _take_help_from_friend(self)->bool:
        """
        Asserts key conditions to be valid friend help (vote).
        Returns True if the friend vote is taken.
        """
        friend_id = self.user_id

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
                                    helper=friend.name,
                                    helper_thumbnail=friend.avatar_url,
                                    question_level=game.question_level,
                                    vote=vote,
                                    color=game.color)
                # make Friend embed and send it in the chat
                await self.ctx.send(embed=embed)
                game.waiting_friend_help = False

                return True

    async def _user_not_in_game(self)->bool:
        """
        Returns True if the user is not playing game yet.
        """
        if self.user_id not in self.bot.games.keys():
            await self.ctx.send(Reply.not_in_game(self.user_id))
            return True

    async def _take_player_answer(self):
        """
        Takes player answer.
        Asks new question - if the answer is correct.
        Terminates the game - if the answer is wrong.
        """
        player = self.user_id
        game = self.bot.games[self.user_id]
        # get the game of the player

        await asyncio.sleep(0.5)
        answer = self.ctx.message.content[1:].upper()
        # take the letter

        if game.correct_answer(answer):
            await self._right_answer()

            await asyncio.sleep(1.5)
            question_data = self.bot.games[player].ask()
            embed = QuestionEmbed(**question_data)

            game.last_question = question_data
            game.last_embed = await self.ctx.send(embed=embed)

            if game.waiting_friend_help:
                game.waiting_friend_help = False

            if game.waiting_audience_help:
                game.waiting_audience_help = False

        else:
            await self._wrong_answer()

            del self.bot.games[player]

            await asyncio.sleep(1.5)
            await self.ctx.send(Reply.end_game(player, game.return_money()))

    async def _right_answer(self):
        """
        Adds correct react to the answer.
        Sends right answer embed in the chat.
        """
        await self.ctx.message.add_reaction('\u2705')
        embed = RightAnswerEmbed()
        await self.ctx.send(embed=embed)

    async def _wrong_answer(self):
        """
        Adds mistaken react to the answer.
        Sends wrong answer embed in the chat.
        """
        await self.ctx.message.add_reaction('\u274C')
        embed = WrongAnswerEmbed()
        await self.ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Answer(bot))
