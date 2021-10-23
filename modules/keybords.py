
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                   
btn_2_E = KeyboardButton('Привет')                   
btn_3_E = KeyboardButton('Привет')                   
btn_3_F = KeyboardButton('спасибо')                   
btn_4_E = KeyboardButton('Привет')                   
btn_4_F = KeyboardButton('спасибо')                   
btn_4_G = KeyboardButton('кнопка 3')
    
keyboard_2.add(btn_2_E)    
keyboard_3.add(btn_3_E)    
keyboard_3.add(btn_3_F)    
keyboard_4.add(btn_4_E)    
keyboard_4.add(btn_4_F)    
keyboard_4.add(btn_4_G)