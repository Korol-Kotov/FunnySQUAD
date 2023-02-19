"""
Это основной файл, желательно создать команды для взаимодействия с когами.

:test_guilds: - вставить ID вашего тестового сервера
"""

import os

import disnake
from disnake.ext import commands

import config

bot = commands.Bot(command_prefix=".", intents=disnake.Intents.all(), test_guilds=[1])


"""
Реализовать следующие команды, желательно использовать слеш-команды.

bot.load_extension()
bot.unload_extension()
bot.reload_extension()

bot.load_extensions()
"""


bot.run(config.TOKEN)