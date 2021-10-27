from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Отправить котакт при регистрации
send_contact = KeyboardButton(f'Отправить контакт', request_contact=True)

send_contact_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(send_contact)

# Стартовое меню администратора
builder = InlineKeyboardButton(text='Перейти в конструктор', callback_data='builder')
hand_data = InlineKeyboardButton(text='Работа с пользователями', callback_data='manual_input')
change_data = InlineKeyboardButton(text='Изменить параметры', callback_data='change_data')
back_btn = InlineKeyboardButton(text='Назад', callback_data='back')

admin_kb_start = InlineKeyboardMarkup()
admin_kb_start.add(builder)
admin_kb_start.add(change_data)
admin_kb_start.add(hand_data)

# ДАть заявку на вступление
send_invoice = InlineKeyboardButton(text='Связаться с администратором', callback_data='send_invoice')

noname_start_kb = InlineKeyboardMarkup()
noname_start_kb.add(send_invoice)

# Задать тип аккаунта
admin_btn = KeyboardButton(f'Новый администратор')
user_btn = KeyboardButton(f'Пользователь')
delete_btn = KeyboardButton(f'❌ Удалаить пользователя')

user_type_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(user_btn)
user_type_kb.add(admin_btn)
user_type_kb.add(delete_btn)


# Клавиатуро подтверждения действия
yes_all_good = InlineKeyboardButton(text='Да. Все верно!', callback_data='yes_all_good')

confirm_kb = InlineKeyboardMarkup().add(yes_all_good)
confirm_kb.add(back_btn)
