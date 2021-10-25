from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


sex_btn_M = KeyboardButton(f'Первая кнопка')
sex_btn_W = KeyboardButton(f'Вторая кнопка')

sex_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(sex_btn_M, sex_btn_W)
