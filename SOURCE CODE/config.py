"""
Подгрузка токена и остальных переменных из файла .env

> переименовать файл .env.example в .env
"""

from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
