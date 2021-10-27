from aiogram import types
from main import dp
from aiogram.dispatcher.filters import Text
import logging
from modules import sqLite
from aiogram.dispatcher import FSMContext
from modules.keyboards import admin_kb_start, noname_start_kb
from modules.dispatcher import Admin_Form, NoName, User_Forms


# Start menu
@dp.message_handler(commands=['start'], state='*')
async def start_menu(message: types.Message):
    telegram_id = message.from_user.id
    try:
        admin_data = sqLite.read_value_table_name(graph='*', table='all_users', telegram_id=telegram_id)[5]
    except:
        admin_data = ' '
    try:
        phone_number = sqLite.read_value_table_name(graph='*', table='all_users', telegram_id=telegram_id)[3]
    except:
        phone_number = None
    if str(admin_data) == 'admin':
        try:
            admin_confirm = sqLite.read_value_table_name(graph='*', table='admins', telegram_id=telegram_id)[2]
        except:
            admin_confirm = None
        if admin_confirm is not None:
            await message.answer(text='Добрый день. Чем могу помочь?', reply_markup=admin_kb_start)
            await Admin_Form.admin_first_menu.set()
        else:
            await message.answer("Введите пароль")
            await User_Forms.first_menu.set()
    elif str(admin_data) != ' ':
        if phone_number is None:
            await message.answer(text='Привет. Ты зарегистрировался не до конца.\n'
                                      'Свяжись с администратором.',
                                 reply_markup=noname_start_kb)
            await NoName.first_menu.set()
        else:
            await message.answer("Введите пароль")
            await User_Forms.first_menu.set()
    else:
        await message.answer(text='Привет. Это закрытый бот. Тебя нет в базе данных. Свяжись с администратором.',
                             reply_markup=noname_start_kb)
        await NoName.first_menu.set()


# Start menu
@dp.callback_query_handler(state=Admin_Form.change_data_confirm, text='back')
async def start_menu(call: types.CallbackQuery):
    await call.message.edit_text(text='Добрый день. Чем могу помочь?', reply_markup=admin_kb_start)
    await Admin_Form.admin_first_menu.set()


# Help menu
@dp.message_handler(commands=['help'], state='*')
async def start_menu(message: types.Message):
    await message.answer(text='Привет! Ты попал в Телеграм бот.\n'
                              'Для отмены всех действий в любой момент нажмите /cancel')


# Cancel all process
@dp.message_handler(state='*', commands=['cancel'])
@dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    await message.reply('Процес отменен. Все данные стерты. Что бы начать все с начала нажми /start',
                        reply_markup=types.ReplyKeyboardRemove())
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
