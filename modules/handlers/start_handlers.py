from aiogram import types
from main import dp
from aiogram.dispatcher.filters import Text
import logging
from modules import sqLite
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from modules.keyboards import admin_kb_start, noname_start_kb, chat_kb, user_adaptiv_kb
from modules.dispatcher import Admin_Form, NoName, User_Forms, bot
from modules.change_btn_functions import start_q_a


# Start menu
@dp.message_handler(Text(equals='🛠 Админка', ignore_case=True), state='*')
@dp.message_handler(Text(equals='◀️ Назад', ignore_case=True), state=Admin_Form.set_user_type)
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
    if str(admin_data) == 'admin' or str(admin_data) == 'root_admin':
        try:
            admin_confirm = sqLite.read_value_table_name(graph='*', table='admins', telegram_id=telegram_id)[1]
        except:
            admin_confirm = None
        if admin_confirm is not None:
            await message.answer('Телеграм бот конструктор', reply_markup=types.ReplyKeyboardRemove())
            await message.answer(text='Добрый день. Чем могу помочь?', reply_markup=admin_kb_start)
            await Admin_Form.admin_first_menu.set()
        else:
            await message.answer("Введите пароль", reply_markup=chat_kb)
            await User_Forms.first_menu.set()

    elif str(admin_data) == 'success':
        project = sqLite.read_values_by_name(table="project", data=1, id_name='id')
        sqLite.insert_info(table='all_users', name='lust_line_id', data=1, telegram_id=message.from_user.id)



        if (project[3] is None) or (str(project[3]) == '0'):
            # Проверка на наличие клавиатуры inline
            if (project[5] is None) or (str(project[5]) == '0'):

                sqLite.insert_info(table='all_users', name='lust_line_id', data=project[0],
                                   telegram_id=message.from_user.id)
                media_id = str(project[7])[6:]
                if str(project[7]).startswith('photo_'):
                    await bot.send_photo(chat_id=message.from_user.id, photo=media_id, caption=project[2],
                                         reply_markup=user_adaptiv_kb(index=1))

                elif str(project[7]).startswith('video_'):
                    await bot.send_video(chat_id=message.from_user.id, video=media_id, caption=project[2],
                                         reply_markup=user_adaptiv_kb(index=1))

                elif str(project[7]).startswith('anime_'):
                    await bot.send_animation(chat_id=message.from_user.id, animation=media_id, caption=project[2],
                                             reply_markup=user_adaptiv_kb(index=1))
                else:
                    await message.answer(text=f"{project[2]}", reply_markup=user_adaptiv_kb(index=1))

                await User_Forms.main_state.set()

            else:
                url_kb = InlineKeyboardMarkup()
                btns = str(project[6]).split('@@@')
                for btn in btns:
                    if btn.startswith('WIND%'):
                        btn = btn[5:]
                        name = str(btn).split('###')[0]
                        id = str(btn).split('###')[1]
                        i = InlineKeyboardButton(text=name, callback_data=f'WIND{id}')
                        url_kb.add(i)
                    elif btn.startswith('URL%'):
                        btn = btn[4:]
                        name = btn.split('###')[0]
                        url = btn.split('###')[1]
                        i = InlineKeyboardButton(text=name, url=url)
                        url_kb.add(i)
                sqLite.insert_info(table='all_users', name='lust_line_id', data=project[0],
                                   telegram_id=message.from_user.id)
                media_id = str(project[7])[6:]
                if str(project[7]).startswith('photo_'):
                    await bot.send_photo(chat_id=message.from_user.id, photo=media_id, caption=project[2],
                                         reply_markup=url_kb)

                elif str(project[7]).startswith('video_'):
                    await bot.send_video(chat_id=message.from_user.id, video=media_id, caption=project[2],
                                         reply_markup=url_kb)

                elif str(project[7]).startswith('anime_'):
                    await bot.send_animation(chat_id=message.from_user.id, animation=media_id, caption=project[2],
                                             reply_markup=url_kb)
                else:
                    await message.answer(text=f"{project[2]}", reply_markup=url_kb)
                await User_Forms.main_state.set()
        else:
            if (project[5] is None) or (str(project[5]) == '0'):
                start_q_a(str(message.from_user.id))
                sqLite.insert_info(table='all_users', name='lust_line_id', data=1, telegram_id=message.from_user.id)
                sqLite.insert_info(table='all_users', name='post_table', data=project[3],
                                   telegram_id=message.from_user.id)
                media_id = str(project[7])[6:]
                if str(project[7]).startswith('photo_'):
                    await bot.send_photo(chat_id=message.from_user.id, photo=media_id, caption=project[2],
                                         reply_markup=types.ReplyKeyboardRemove())

                elif str(project[7]).startswith('video_'):
                    await bot.send_video(chat_id=message.from_user.id, video=media_id, caption=project[2],
                                         reply_markup=types.ReplyKeyboardRemove())

                elif str(project[7]).startswith('anime_'):
                    await bot.send_animation(chat_id=message.from_user.id, animation=media_id, caption=project[2],
                                             reply_markup=types.ReplyKeyboardRemove())
                else:
                    await message.answer(text=f"{project[2]}", reply_markup=types.ReplyKeyboardRemove())
                await User_Forms.q_a.set()
            else:
                url_kb = InlineKeyboardMarkup()
                btns = str(project[6]).split('@@@')
                for btn in btns:
                    if btn.startswith('WIND%'):
                        btn = btn[5:]
                        name = str(btn).split('###')[0]
                        id = str(btn).split('###')[1]
                        i = InlineKeyboardButton(text=name, callback_data=f'WIND{id}')
                        url_kb.add(i)
                    elif btn.startswith('URL%'):
                        btn = btn[4:]
                        name = btn.split('###')[0]
                        url = btn.split('###')[1]
                        i = InlineKeyboardButton(text=name, url=url)
                        url_kb.add(i)
                start_q_a(str(message.from_user.id))
                sqLite.insert_info(table='all_users', name='lust_line_id', data=1, telegram_id=message.from_user.id)
                sqLite.insert_info(table='all_users', name='post_table', data=project[3],
                                   telegram_id=message.from_user.id)
                media_id = str(project[7])[6:]
                if str(project[7]).startswith('photo_'):
                    await bot.send_photo(chat_id=message.from_user.id, photo=media_id, caption=project[2],
                                         reply_markup=url_kb)

                elif str(project[7]).startswith('video_'):
                    await bot.send_video(chat_id=message.from_user.id, video=media_id, caption=project[2],
                                         reply_markup=url_kb)

                elif str(project[7]).startswith('anime_'):
                    await bot.send_animation(chat_id=message.from_user.id, animation=media_id, caption=project[2],
                                             reply_markup=url_kb)
                else:
                    await message.answer(text=f"{project[2]}", reply_markup=url_kb)
                await User_Forms.q_a.set()

    elif str(admin_data) != ' ':
        if phone_number is None:
            await message.answer(text='Привет. Ты зарегистрировался не до конца.\n'
                                      'Свяжись с администратором.',
                                 reply_markup=noname_start_kb)
            await NoName.first_menu.set()
        else:
            await message.answer("Введите пароль", reply_markup=chat_kb)
            await User_Forms.first_menu.set()

    else:
        sqLite.insert_first_note(table='all_users', telegram_id=message.from_user.id)
        await message.answer(text='Привет. Это закрытый бот. Тебя нет в базе данных. Свяжись с администратором.',
                             reply_markup=noname_start_kb)
        await NoName.first_menu.set()


# Start menu
@dp.callback_query_handler(state=Admin_Form.setings_menu, text='back')
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
