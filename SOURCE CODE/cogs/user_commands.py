"""
Команды для обычных пользователей.
Помните, что это всего лишь шаблон, вы можете его дополнять чем-то новым или изменять "во-все".
"""

import disnake
from disnake.ext import commands

from utils import database


class UserCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="баланс",
        aliases=["cash", "balance", "деньги"],
        brief="Баланс пользователя",
        usage="balance <@user=None>"
    )
    async def user_balance(self, ctx, member: disnake.Member=None):
        pass

    @commands.command(
        name="наградить",
        aliases=["award"],
        brief="Наградить пользователя суммой денег",
        usage="award <@user> <amount>"
    )
    async def award_user(self, ctx, member: disnake.Member, amount: int):
        pass

    @commands.command(
        name="забрать",
        aliases=["take", "отнять"],
        brief="Забрать сумму денег у пользователя",
        usage="take <@user> <amount (int or all)>"
    )
    async def take_cash(self, ctx, member: disnake.Member, amount):
        pass

    @commands.command(
        name="перевести",
        aliases=["pay", "transfer", "перевод"],
        brief="Перевести деньги пользователю",
        usage="pay <@user> <amount>"
    )
    async def pay_cash(self, ctx, member: disnake.Member, amount: int):
        pass

    @commands.command(
        name="+репутация",
        aliases=["rep", "+rep", "реп", "репутация"],
        brief="Респект пользователю",
        usage="rep <@user>"
    )
    async def reputation(self, ctx, member: disnake.Member):
        pass

    @commands.command(
        name="лидеры",
        aliases=["leaders", "leadersboard", "лидер", "top"],
        brief="Таблица лидеров"
    )
    async def server_leadersboard(self, ctx):
        pass

def setup(bot):
    bot.add_cog(UserCommands(bot))
