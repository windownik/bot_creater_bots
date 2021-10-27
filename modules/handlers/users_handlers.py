from aiogram import types
from main import dp
from modules import sqLite
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from modules.dispatcher import bot, User_Forms
from modules.keyboards import user_type_kb, admin_kb_start, confirm_kb


# Start menu noName Callback
@dp.message_handler(state=User_Forms.first_menu)
async def add_person_start(message: types.Message):
    user_data = sqLite.read_value_table_name(graph="*", table="all_users", telegram_id=message.from_user.id)
    const = sqLite.read_all(table="constant")[0][1]
    if str(message.text) == str(user_data[5]):
        sqLite.insert_info(table='all_users', name='ddos', data=0, telegram_id=message.from_user.id)
        await message.answer("Ваш пароль верный")
    elif int(user_data[4]) >= int(const):
        await message.answer(f"Ваш аккаунт заблакирован вы ввели неверный пароль слишком много раз")
    else:
        sqLite.insert_info(table='all_users', name='ddos', data=(int(user_data[4])+1), telegram_id=message.from_user.id)
        await message.answer(f"Ваш пароль неверный! Вы ввели неверный пароль <b>{int(user_data[4])+1}</b> раз.\n"
                             f"Если вы введете неверный пароль <b>{const}</b> раз, вы будете заблокированы!",
                             parse_mode='html')



