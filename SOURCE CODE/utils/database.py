"""
База данных.

Этот файл вы можете модифицировать как угодно,
главное загружайте релизы в FunnySQUAD (GitHub) во время,
что бы остальные участники понимали с чем им работать.
Желательно оставлять комментарии с объяснением и примером работы
"""

import aiosqlite


class DataBase:

    def __init__(self):
        self.db_name = "test-database.db"

    async def get_data(self):
        pass

    async def create_table(self):
        pass

    async def insert_new_member(self):
        pass

    async def update_member(self):
        pass

    """METHODS FOR SHOP"""

    async def insert_new_role(self):
        pass

    async def delete_role_from_shop(self):
        pass

    async def get_shop_data(self):
        pass
