from aiogram import types
import asyncio
from main import dp
from modules import sqLite
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from modules.dispatcher import bot, User_Forms, NoName
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from modules.keyboards import user_type_kb, admin_kb_start, confirm_kb, user_adaptiv_kb
from modules.change_btn_functions import save_q_a, start_q_a


# Set new constant confirm
@dp.callback_query_handler(state=NoName.first_menu, text='input_password')
async def start_menu(call: types.CallbackQuery):
    await call.message.answer("Введите пароль")
    await User_Forms.first_menu.set()


# Start menu noName Callback
@dp.message_handler(state=User_Forms.first_menu)
async def add_person_start(message: types.Message):
    password = sqLite.read_value_table_name(graph="password", table="constant", telegram_id=1, id_name='id')[0]
    user_data = sqLite.read_value_table_name(graph="*", table="all_users", telegram_id=message.from_user.id)
    const = sqLite.read_all(table="constant")[0][1]
    password = str(password).split('#№#')
    status = False
    for i in password:
        if str(i) == message.text:
            status = True
    if int(user_data[4]) >= int(const):
        await message.answer(f"Ваш аккаунт заблакирован вы ввели неверный пароль слишком много раз")
    elif status:
        sqLite.insert_info(table='all_users', name='ddos', data=0, telegram_id=message.from_user.id)
        sqLite.insert_info(table='all_users', name='password', data='success', telegram_id=message.from_user.id)
        sqLite.insert_info(table='all_users', name='lust_line_id', data=1, telegram_id=message.from_user.id)
        await message.answer("Ваш пароль верный")
        project = sqLite.read_values_by_name(table="project", data=1, id_name='id')
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

    else:
        sqLite.insert_info(table='all_users', name='ddos', data=(int(user_data[4]) + 1),
                           telegram_id=message.from_user.id)
        await message.answer(f"Ваш пароль неверный! Вы ввели неверный пароль <b>{int(user_data[4]) + 1}</b> раз.\n"
                             f"Если вы введете неверный пароль <b>{const}</b> раз, вы будете заблокированы!",
                             parse_mode='html')


# Переход на главную страницу
@dp.message_handler(Text(equals='🔙 Вернутся на главную', ignore_case=True), state=User_Forms.main_state)
async def start_menu(message: types.Message):
    sqLite.insert_info(table='all_users', name='lust_line_id', data=1, telegram_id=message.from_user.id)
    project = sqLite.read_values_by_name(table="project", data=1, id_name='id')
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


# Переход на главную страницу
@dp.message_handler(Text(equals='◀️ Назад', ignore_case=True), state=User_Forms.main_state)
async def start_menu(message: types.Message):
    post = sqLite.read_values_by_name(table="all_users", data=message.from_user.id)[6]
    lust_in_text = sqLite.read_values_by_name(table="project", data=post, id_name='id')[1]
    project = sqLite.read_all(table='project')
    id = None
    for line in project:
        btns = str(line[4]).split('#@#')
        for b in btns:
            btn = str(b).split('@$@')
            for k in btn:
                # print(k, lust_in_text)
                if str(k) == lust_in_text:
                    id = line[0]
                    break
                else:
                    pass
    if post == 1:
        id = 1
    if id is None:
        await message.answer("Ошибка. Пост не найден.")
    else:
        sqLite.insert_info(table='all_users', name='lust_line_id', data=id, telegram_id=message.from_user.id)
        project = sqLite.read_values_by_name(table="project", data=id, id_name='id')
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


# Start menu noName Callback
@dp.message_handler(state=User_Forms.main_state)
async def add_person_start(message: types.Message):
    project = sqLite.read_all(table='project')
    find = 0
    for post in project:
        if str(post[1]) == message.text:
            find = post[0]
        else:
            pass
    if find == 0:
        await message.answer('Команда не найдена. Нажмите кнопку ниже')
    else:
        project = sqLite.read_values_by_name(table="project", data=find, id_name='id')

        if (project[3] is None) or (str(project[3]) == '0'):
            # Проверка на наличие клавиатуры inline
            if (project[5] is None) or (str(project[5]) == '0'):

                sqLite.insert_info(table='all_users', name='lust_line_id', data=project[0],
                                   telegram_id=message.from_user.id)
                media_id = str(project[7])[6:]
                if str(project[7]).startswith('photo_'):
                    await bot.send_photo(chat_id=message.from_user.id, photo=media_id, caption=project[2],
                                         reply_markup=user_adaptiv_kb(index=find))

                elif str(project[7]).startswith('video_'):
                    await bot.send_video(chat_id=message.from_user.id, video=media_id, caption=project[2],
                                         reply_markup=user_adaptiv_kb(index=find))

                elif str(project[7]).startswith('anime_'):
                    await bot.send_animation(chat_id=message.from_user.id, animation=media_id, caption=project[2],
                                             reply_markup=user_adaptiv_kb(index=find))
                else:
                    await message.answer(text=f"{project[2]}", reply_markup=user_adaptiv_kb(index=find))

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


# Start menu noName Callback
@dp.message_handler(state=User_Forms.q_a)
async def add_person_start(message: types.Message):
    data = sqLite.read_values_by_name(table="all_users", data=message.from_user.id)
    next_line = data[6]
    post_table = data[7]
    save_q_a(name=str(message.from_user.id), data=f'{message.text}\n')
    try:
        q_a = sqLite.read_values_by_name(table=f'post{post_table}', id_name='number', data=next_line)
        if (q_a[5] is None) or str(q_a[5]) == '0':

            media_id = str(q_a[7])[6:]
            if str(q_a[7]).startswith('photo_'):
                await bot.send_photo(chat_id=message.from_user.id, photo=media_id, caption=q_a[1])

            elif str(q_a[7]).startswith('video_'):
                await bot.send_video(chat_id=message.from_user.id, video=media_id, caption=q_a[1])

            elif str(q_a[7]).startswith('anime_'):
                await bot.send_animation(chat_id=message.from_user.id, animation=media_id, caption=q_a[1])
            else:
                await message.answer(text=q_a[1])
            sqLite.insert_info(table='all_users', name='lust_line_id', data=(int(next_line) + 1),
                               telegram_id=message.from_user.id)
        else:
            url_kb = InlineKeyboardMarkup()
            btns = str(q_a[6]).split('@@@')
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
            sqLite.insert_info(table='all_users', name='lust_line_id', data=(int(next_line) + 1),
                               telegram_id=message.from_user.id)

            media_id = str(q_a[7])[6:]
            if str(q_a[7]).startswith('photo_'):
                await bot.send_photo(chat_id=message.from_user.id, photo=media_id, caption=q_a[1],
                                     reply_markup=url_kb)

            elif str(q_a[7]).startswith('video_'):
                await bot.send_video(chat_id=message.from_user.id, video=media_id, caption=q_a[1],
                                     reply_markup=url_kb)

            elif str(q_a[7]).startswith('anime_'):
                await bot.send_animation(chat_id=message.from_user.id, animation=media_id, caption=q_a[1],
                                         reply_markup=url_kb)
            else:
                await message.answer(text=q_a[1], reply_markup=url_kb)

    except:
        await message.answer(text='Опрос окончен. Спасибо за ваши ответы')
        sqLite.insert_info(table='all_users', name='lust_line_id', data=0, telegram_id=message.from_user.id)
        sqLite.insert_info(table='all_users', name='post_table', data=0, telegram_id=message.from_user.id)
        user_data = sqLite.read_values_by_name(data=message.from_user.id, table='all_users')

        #         Выводим стартовый пост
        project = sqLite.read_values_by_name(table="project", data=1, id_name='id')
        sqLite.insert_info(table='all_users', name='lust_line_id', data=1, telegram_id=message.from_user.id)
        if (project[3] is None) or (str(project[3]) == 0):

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
            start_q_a(str(message.from_user.id))
            sqLite.insert_info(table='all_users', name='post_table', data=project[3], telegram_id=message.from_user.id)

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

        admins = sqLite.read_all(table='admins')
        for line in admins:
            await asyncio.sleep(0.5)
            with open(f'modules/answers/{str(message.from_user.id)}.txt', 'rb') as file:
                await bot.send_document(chat_id=line[1], document=file,
                                        caption=f"Пользователь с ником <b>{user_data[2]}</b> прошел опрос\ntg id="
                                                f"<b>{message.from_user.id}</b>,\nтелефонный номер <b>{user_data[3]}</b>",
                                        parse_mode='html')
