"""
События на сервере.
Помните, что это всего лишь шаблон, вы можете его дополнять чем-то новым или изменять "во-все".
"""

import disnake
from disnake.ext import commands

from utils import database


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.Cog.listener()
    async def on_member_join(self, member):
        pass

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        pass

    @commands.Cog.listener()
    async def on_message(self, message):
        pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(error)


def setup(bot):
    bot.add_cog(Events(bot))
