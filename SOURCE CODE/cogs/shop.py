"""
Магазин.
Помните, что это всего лишь шаблон, вы можете его дополнять чем-то новым или изменять "во-все".
"""

import disnake
from disnake.ext import commands

from utils import database


class Shop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="добавить-роль",
        aliases=["add", "add-shop", "добавить"],
        brief="Добавить новую роль в магазин",
        usage="add <@role> <cost>"
    )
    async def add_role_to_shop(self, ctx, role: disnake.Role, cost: int=0):
        pass

    @commands.command(
        name="удалить-роль",
        aliases=["remove", "rm-role", "remove-role", "удалить"],
        brief="Удалить роль из магазина",
        usage="remove <@role>"
    )
    async def remove_role(self, ctx, role: disnake.Role):
        pass

    @commands.command(
        name="купить-роль",
        aliases=["buy", "buy-role", "купить"],
        brief="Купить роль",
        usage="buy <@role>"
    )
    async def buy_role(self, ctx, role: disnake.Role):
        pass

    @commands.command(
        name="магазин-ролей",
        aliases=["shop", "roles-shop", "магазин"],
        brief="Магазин ролей"
    )
    async def view_shop(self, ctx):
        pass


def setup(bot):
    bot.add_cog(Shop(bot))
