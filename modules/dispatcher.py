
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from modules.states import AllStates
import json


import logging

with open("telegram.json", 'r') as file:
    telegram_token = str(json.load(file)["telegram_token"])
    file.close()

storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(telegram_token)
dp = Dispatcher(bot, storage=storage)

        