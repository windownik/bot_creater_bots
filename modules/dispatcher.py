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

    setings_menu = State()
    change_data = State()
    change_data_confirm = State()

    setings_pass = State()
    delete_pass = State()

    new_pass = State()
    new_pass_confirm = State()


# Welcome form noName
class NoName(StatesGroup):
    first_menu = State()
    noname_send_name = State()
    noname_contact = State()


# Welcome form user
class User_Forms(StatesGroup):
    first_menu = State()
    main_state = State()
    q_a = State()


# Welcome form admin
class Admin_Builder (StatesGroup):
    btn_builder = State()
    btn_builder_input_text = State()
    change_btn_text = State()

    post_builder = State()
    change_post_text = State()
    post_builder_delete = State()
    only_post_delete = State()

    create_post_text = State()
    create_post_text_inline = State()

    change_post_type = State()
    inline_url_text = State()
    inline_window_text = State()

    btn_builder_delete = State()

    add_media_post = State()


