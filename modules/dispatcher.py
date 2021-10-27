from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import logging

with open('modules/telegram_token.txt', 'r') as file:
    telegram_token = file.read()
    file.close()


storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(telegram_token)
dp = Dispatcher(bot, storage=storage)


# Welcome form admin
class start_Form(StatesGroup):
    admin_first_menu = State()


# Welcome form admin
class Admin_Form(StatesGroup):
    admin_first_menu = State()
    search_user = State()
    set_user_type = State()
    set_user_password = State()
    set_user_password_confirm = State()

    delete_user_confirm = State()

    change_data = State()
    change_data_confirm = State()


# Welcome form noName
class NoName(StatesGroup):
    first_menu = State()
    noname_send_name = State()
    noname_contact = State()


# Welcome form user
class User_Forms(StatesGroup):
    first_menu = State()


