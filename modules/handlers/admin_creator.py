from aiogram import types
from main import dp
from modules.change_btn_functions import *
from modules import sqLite
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from modules.dispatcher import bot, Admin_Form, Admin_Builder
from modules.keyboards import closet_kb, confirm_kb, btn_creator_kb, btn_corector_kb, post_creator_kb, post_corector_kb, \
    chat_kb


# Start menu noName Callback
@dp.callback_query_handler(state=Admin_Builder.only_post_delete, text='closet')
@dp.callback_query_handler(state=Admin_Form.admin_first_menu, text='builder')
async def add_person_start(call: types.CallbackQuery):
    sqLite.insert_info(table='admins', name='work_post', data='Главное_Меню', telegram_id=call.from_user.id)
    work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await call.message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                       f"в редактор!</b>", parse_mode='html')
    await call.message.answer(text=f"{project[1]}")
    await call.message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                                tg_id=call.from_user.id))
    await Admin_Form.admin_first_menu.set()


# Start menu noName Callback
@dp.callback_query_handler(state=Admin_Builder.btn_builder_input_text, text='closet')
async def add_person_start(call: types.CallbackQuery):
    work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await call.message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                       f"в редактор!</b>", parse_mode='html')
    await call.message.answer(text=f"{project[1]}")
    await call.message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0], btn_creator=True,
                                                                                tg_id=call.from_user.id))
    await Admin_Builder.btn_builder.set()


# Стоп редактор
@dp.message_handler(Text(equals='❌ Стоп редактор', ignore_case=True), state="*")
async def start_menu(message: types.Message):
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                  f"в редактор!</b>", parse_mode='html')
    await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                           tg_id=message.from_user.id))
    await Admin_Form.admin_first_menu.set()


# Добавляем кнопку
@dp.message_handler(Text(equals='➕ Добавить Кнопку', ignore_case=True), state=Admin_Builder.btn_builder)
async def start_menu(message: types.Message):
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await message.answer("<b>Здесь есть посты. Новые кнопки создавать нельзя</b>", parse_mode='html')
        await message.answer(text='Удалить все посты?', reply_markup=confirm_kb)
        await Admin_Builder.only_post_delete.set()
    else:
        await message.answer("Введите название новой кнопки", reply_markup=closet_kb)
        await Admin_Builder.btn_builder_input_text.set()


# Переход на главную страницу
@dp.message_handler(Text(equals='🔙 Вернутся на главную', ignore_case=True), state=Admin_Builder.btn_builder)
async def start_menu(message: types.Message):
    sqLite.insert_info(table='admins', name='work_post', data='Главное_Меню', telegram_id=message.from_user.id)
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                  f"в редактор!</b>", parse_mode='html')
    await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                           tg_id=message.from_user.id,
                                                                           btn_creator=True))
    await Admin_Builder.btn_builder.set()


# Переход на главную страницу
@dp.message_handler(Text(equals='🔙 Вернутся на главную', ignore_case=True), state="*")
async def start_menu(message: types.Message):
    sqLite.insert_info(table='admins', name='work_post', data='Главное_Меню', telegram_id=message.from_user.id)
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                  f"в редактор!</b>", parse_mode='html')
    await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                           tg_id=message.from_user.id))
    await Admin_Form.admin_first_menu.set()


# Переход назад
@dp.message_handler(Text(equals='◀️ Назад', ignore_case=True), state=Admin_Builder.btn_builder)
async def start_menu(message: types.Message):
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    back_window = btn_back(work_window)
    sqLite.insert_info(table='admins', name='work_post', data=back_window, telegram_id=message.from_user.id)
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                  f"в редактор!</b>", parse_mode='html')
    await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                           tg_id=message.from_user.id,
                                                                           btn_creator=True))
    await Admin_Builder.btn_builder.set()


# Переход назад
@dp.message_handler(Text(equals='◀️ Назад', ignore_case=True), state="*")
async def start_menu(message: types.Message):
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    back_window = btn_back(work_window)
    sqLite.insert_info(table='admins', name='work_post', data=back_window, telegram_id=message.from_user.id)
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                  f"в редактор!</b>", parse_mode='html')
    await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                           tg_id=message.from_user.id))
    await Admin_Form.admin_first_menu.set()


# Переход на главную страницу
@dp.message_handler(Text(equals='➕ Вставить Кнопку', ignore_case=True), state="*")
async def start_menu(message: types.Message):
    btn_cut = sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='cut_btn')[0]
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    # Открываем проект и берем все старые кнопки
    try:
        project = sqLite.read_values_by_name(table='project', id_name="in_text", data=work_window)[4] + \
                  btn_cut + "@$@#@#"
    except:
        project = btn_cut + "@$@#@#"
    # Добавляем новую кнопку и сохраняем в бд
    sqLite.insert_info(table='project', name='btn', data=project, id_name="in_text",
                       telegram_id=work_window)
    sqLite.insert_info(table='admins', name='cut_btn', data="ЁЁЁЁЁ", telegram_id=message.from_user.id)
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    await message.answer(text=f"{project[2]}",
                         reply_markup=btn_creator_kb(index=project[0], btn_creator=True,
                                                     tg_id=message.from_user.id))
    await Admin_Builder.btn_builder.set()


# Добавить пост в конец списка
@dp.message_handler(Text(equals='➕ Добавить пост', ignore_case=True), state="*")
async def start_menu(message: types.Message):
    await message.answer("Введите текст нового поста", reply_markup=closet_kb)
    await Admin_Builder.create_post_text.set()


# Добавить пост в конец списка
@dp.message_handler(state=Admin_Builder.create_post_text)
async def start_menu(message: types.Message):
    in_text = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    post = sqLite.read_values_by_name(table="project", data=in_text, id_name='in_text')
    index = str(post[0])
    if post[4] is not None and str(post[4]) != '':
        await message.answer(
            "В данном меню есть кнопки. Каскад постов можно создавать только если нет кнопок.")
    else:
        try:
            next_number = len(sqLite.read_all(table=f'post{index}'))
            sqLite.insert_first_note(table=f'post{index}', telegram_id=(next_number + 1), id_name='number')
            sqLite.insert_info(table=f'post{index}', name='post_text', data=message.text,
                               id_name='number', telegram_id=(next_number + 1))
        except:
            sqLite.new_table(table_name=index)
            sqLite.insert_first_note(table=f'post{index}', telegram_id=1, id_name='number')
            sqLite.insert_info(table=f'post{index}', name='post_text', data=message.text, id_name='number',
                               telegram_id=1)
        sqLite.insert_info(table='project', name='start_post', data=index, id_name='id', telegram_id=index)
    # Выводим первый пост с шапкой
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    await message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                         reply_markup=post_creator_kb(index=project[0]))
    await message.answer(text=f"{project[2]}", reply_markup=post_corector_kb(index=project[0]))
    # Подгружаем остальные посты
    try:
        all_posts = sqLite.read_all(table=f'post{index}')
        for i in all_posts:
            await message.answer(text=f"{i[1]}", reply_markup=post_corector_kb(index=i[0], table=f'{index}'))
    except:
        pass
    await Admin_Form.admin_first_menu.set()


# Main builder menu
@dp.message_handler(state=Admin_Builder.btn_builder_input_text)
async def start_menu(message: types.Message):
    if message.text == '➕ Добавить Кнопку':
        pass
    else:
        text_btn = message.text
        try:
            free_btn = sqLite.read_values_by_name(table='project', id_name="in_text", data=text_btn)[4]
            free_btn = False
        except:
            free_btn = True
        if free_btn:
            # Находим наш пост
            text_post = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
            # Открываем проект и берем все старые кнопки
            try:
                project = text_btn + "@$@#@#" + sqLite.read_values_by_name(table='project', id_name="in_text",
                                                                           data=text_post)[4]
            except:
                project = text_btn + "@$@#@#"

            # Добавляем новую кнопку и сохраняем в бд
            sqLite.insert_info(table='project', name='btn', data=project, id_name="in_text",
                               telegram_id=text_post)
            # Добавляем меню в этой кнопке
            create_menu_btn(text_btn=text_btn)
            # Перезапускаем экран
            work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id,
                                                         name='work_post')[0])
            project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
            await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0], btn_creator=True,
                                                                                   tg_id=message.from_user.id))
            await Admin_Builder.btn_builder.set()
        else:
            await message.answer("Такая кнопка уже есть. Введите другое название.")


# Меняем название кнопки
@dp.message_handler(state=Admin_Builder.change_btn_text)
async def start_menu(message: types.Message):
    try:
        free_btn = sqLite.read_values_by_name(table='project', id_name="in_text", data=message.text)[4]
        free_btn = False
    except:
        free_btn = True
    if free_btn:
        index = int(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data_2')[0])
        text_btn = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
        change_btn_name(index=index, text_btn=text_btn, new_text=message.text)
        work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0], btn_creator=True,
                                                                               tg_id=message.from_user.id))
    else:
        await message.answer("Такая кнопка уже есть. Введите другое название.")
    await Admin_Builder.btn_builder.set()


# Main builder menu
@dp.message_handler(state=Admin_Builder.btn_builder_input_text)
async def start_menu(message: types.Message):
    # Находим наш пост
    text_post = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
    # Открываем проект и берем все старые кнопки
    try:
        project = sqLite.read_values_by_name(table='project', id_name="post", data=text_post)[4] + message.text + "#@#"
    except:
        project = message.text + "@$@#@#"
    # Добавляем новую кнопку и сохраняем в бд
    sqLite.insert_info(table='project', name='btn', data=project, id_name="post",
                       telegram_id=text_post)
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                           tg_id=message.from_user.id))
    await Admin_Form.admin_first_menu.set()


# Корректируем кнопку в редакторе
@dp.message_handler(state=Admin_Builder.btn_builder)
async def start_menu(message: types.Message):
    if '📝 Редактор постов' in message.text:
        work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await message.answer("📝 Вы в редакторе постов", reply_markup=post_creator_kb(index=(project[0])))
        await message.answer(text=f"{project[2]}", reply_markup=post_corector_kb(index=(project[0])))

    elif '🎛 Редактор кнопок' in message.text:
        await message.answer("🛠 Вы в редакторе кнопок")

        work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=(project[0]),
                                                                               btn_creator=True,
                                                                               tg_id=message.from_user.id))
        await Admin_Builder.btn_builder.set()

    elif message.text.startswith('[') and message.text.endswith(']'):
        btn_text = message.text[1:-1]
        valid_menu = sqLite.read_values_by_name(table="project", data=btn_text, id_name='in_text')
        if valid_menu is not None:
            sqLite.insert_info(table='admins', name='work_post', data=btn_text, telegram_id=message.from_user.id)
            project = sqLite.read_values_by_name(table="project", data=btn_text, id_name='in_text')
            if (project[3] is not None) and (int(project[3]) != 0):
                await message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                          f"в редактор!</b>", parse_mode='html')
            await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                                   tg_id=message.from_user.id,
                                                                                   btn_creator=True))
            await Admin_Builder.btn_builder.set()
        else:
            await message.answer("Такой кнопки нет")

    else:
        project = sqLite.read_all(table='project')
        for i in project:
            all_btns = str(i[4]).split("#@#")
            for row in all_btns:
                btns = row.split("@$@")
                for k in btns:
                    if message.text == str(k):
                        sqLite.insert_info(table='admins', name='data', data=message.text,
                                           telegram_id=message.from_user.id)
                        sqLite.insert_info(table='admins', name='data_2', data=str(i[0]),
                                           telegram_id=message.from_user.id)
                        try:
                            await message.answer(text=str(i[2]), reply_markup=btn_creator_kb(tg_id=message.from_user.id,
                                                                                             index=i[0],
                                                                                             btn_creator=True,
                                                                                             active_btn=message.text))
                            await message.answer(text=message.text, reply_markup=btn_corector_kb)
                        except:
                            await message.answer(text=message.text, reply_markup=btn_corector_kb)
                        await Admin_Builder.btn_builder.set()


# Отмена процесаов
@dp.callback_query_handler(state=Admin_Builder.change_btn_text, text='closet')
@dp.callback_query_handler(state=Admin_Builder.btn_builder_delete, text='closet')
async def start_menu(call: types.CallbackQuery):
    # Перезапускаем экран
    work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    await call.message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=(project[0]),
                                                                                btn_creator=True,
                                                                                tg_id=call.from_user.id))
    await Admin_Builder.btn_builder.set()


# Корректируем кнопку в редакторе
@dp.callback_query_handler(state=Admin_Builder.change_btn_text)
async def start_menu(call: types.CallbackQuery):
    project = sqLite.read_all(table='project')
    text_btn = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='data')[0])

    for i in project:
        all_btns = str(i[4]).split("#@#")
        for btn in all_btns:
            if str(text_btn) == str(btn):
                await call.message.edit_text(text=str(text_btn), reply_markup=btn_corector_kb)
                await Admin_Builder.btn_builder.set()


# Удаляем кнопку
@dp.callback_query_handler(state=Admin_Builder.btn_builder_delete, text='yes_all_good')
async def start_menu(call: types.CallbackQuery):
    index = int(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='data_2')[0])
    text_btn = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='data')[0])

    delete_btn(index=index, text_btn=text_btn)
    # Удаляем меню с кнопкой внутри
    delete_btn_index = sqLite.read_values_by_name(table='project', id_name='in_text', data=text_btn)
    if (delete_btn_index[3] is not None) or (delete_btn_index[3] == 0):
        try:
            sqLite.delete_table(f'post{delete_btn_index[3]}')
        except:
            print("Удаление таблицы постов прошло с ошибкой")
    sqLite.delete_str(table='project', name='id', data=delete_btn_index[0])
    # Перезапускаем экран
    work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if (project[3] is not None) and (int(project[3]) != 0):
        await call.message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                       f"в редактор!</b>", parse_mode='html')
    await call.message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=(project[0]),
                                                                                btn_creator=True,
                                                                                tg_id=call.from_user.id))
    await Admin_Builder.btn_builder.set()


# Удаляем только таблицу постов
@dp.callback_query_handler(state=Admin_Builder.only_post_delete, text='yes_all_good')
async def start_menu(call: types.CallbackQuery):
    work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    sqLite.delete_table(f'post{project[3]}')
    sqLite.insert_info(table="project", name='start_post', data='0', id_name='in_text', telegram_id=work_window)
    await call.message.answer(text=f"{project[1]}")
    await call.message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=project[0],
                                                                                tg_id=call.from_user.id))
    await Admin_Form.admin_first_menu.set()


# Удаляем пост
@dp.callback_query_handler(state=Admin_Builder.post_builder_delete, text='yes_all_good')
async def start_menu(call: types.CallbackQuery):
    data = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='data')[0])
    index = data[16:]
    table = index.split('#')[1]
    if table == 'project':
        await call.message.answer("<b>Первый пост можно удалить только из редактора кнопок.</b>", parse_mode='html')

    else:
        index = index.split('#')[0]
        url_btn = sqLite.read_values_by_name(table=f'post{table}', id_name='number', data=index)
        if str(url_btn[5]) == 'url':
            btn_s = str(url_btn[6]).split('@@@')
            for btn in btn_s:
                if str(btn).startswith('WIND%'):
                    id_btn = str(btn).split('###')[1]
                    try:
                        sqLite.delete_str(table=f'url_btn', name="id", data=id_btn)
                    except:
                        pass
        sqLite.delete_str(table=f'post{table}', name="number", data=index)
    re_build(table)
    work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if str(project[3]) == str(project[0]):
        # Выводим первый пост
        await call.message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                                  reply_markup=post_creator_kb(index=project[0]))
        await call.message.answer(text=f"{project[2]}", reply_markup=post_corector_kb(index=project[0]))
        # Подгружаем остальные посты
        try:
            all_posts = sqLite.read_all(table=f'post{project[0]}')
            for i in range(1, len(all_posts) + 1):
                post = sqLite.read_values_by_name(table=f'post{project[0]}', data=str(i), id_name='number')
                prefix = ''
                if str(post[5]) == 'url':
                    prefix = '[инлайн кнопки] '
                if str(post[7]).startswith('photo'):
                    prefix = prefix + '[фото] '
                elif str(post[7]).startswith('video'):
                    prefix = prefix + '[видео] '
                elif str(post[7]).startswith('anime'):
                    prefix = prefix + '[анимация] '

                await call.message.answer(text=f"{prefix}{post[1]}",
                                          reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
        except:
            pass
    else:
        await call.message.answer("📝 Вы в редакторе постов.\n Первый пост нельзя переместить",
                                  reply_markup=post_creator_kb(index=(project[0])))
        prefix = ''
        if str(project[5]) == 'url':
            prefix = '[инлайн кнопки] '
        if str(project[7]).startswith('photo'):
            prefix = prefix + '[фото] '
        elif str(project[7]).startswith('video'):
            prefix = prefix + '[видео] '
        elif str(project[7]).startswith('anime'):
            prefix = prefix + '[анимация] '

        await call.message.answer(text=f"{prefix}{project[2]}",
                                  reply_markup=post_corector_kb(index=project[0]))


# Отмена удаления поста
@dp.callback_query_handler(state=Admin_Builder.add_media_post, text='closet')
@dp.callback_query_handler(state=Admin_Builder.change_post_type, text='closet')
@dp.callback_query_handler(state=Admin_Builder.inline_window_text, text='closet')
@dp.callback_query_handler(state=Admin_Builder.inline_url_text, text='closet')
@dp.callback_query_handler(state=Admin_Builder.create_post_text, text='closet')
@dp.callback_query_handler(state=Admin_Builder.change_post_text, text='closet')
@dp.callback_query_handler(state=Admin_Builder.create_post_text_inline, text='closet')
@dp.callback_query_handler(state=Admin_Builder.post_builder_delete, text='closet')
async def start_menu(call: types.CallbackQuery):
    work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if str(project[3]) == str(project[0]):
        # Выводим первый пост
        await call.message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                                  reply_markup=post_creator_kb(index=project[0]))

        prefix = ''
        if str(project[5]) == 'url':
            prefix = '[инлайн кнопки] '
        if str(project[7]).startswith('photo'):
            prefix = prefix + '[фото] '
        elif str(project[7]).startswith('video'):
            prefix = prefix + '[видео] '
        elif str(project[7]).startswith('anime'):
            prefix = prefix + '[анимация] '

        await call.message.answer(text=f"{prefix}{project[2]}",
                                  reply_markup=post_corector_kb(index=project[0]))
        # Подгружаем остальные посты
        try:
            all_posts = sqLite.read_all(table=f'post{project[0]}')
            for i in range(1, len(all_posts) + 1):
                post = sqLite.read_values_by_name(table=f'post{project[0]}', data=str(i), id_name='number')
                prefix = ''
                if str(post[5]) == 'url':
                    prefix = '[инлайн кнопки] '
                if str(post[7]).startswith('photo'):
                    prefix = prefix + '[фото] '
                elif str(post[7]).startswith('video'):
                    prefix = prefix + '[видео] '
                elif str(post[7]).startswith('anime'):
                    prefix = prefix + '[анимация] '

                await call.message.answer(text=f"{prefix}{post[1]}",
                                          reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
        except:
            pass
    else:
        prefix = ''
        if str(project[5]) == 'url':
            prefix = '[инлайн кнопки] '
        if str(project[7]).startswith('photo'):
            prefix = prefix + '[фото] '
        elif str(project[7]).startswith('video'):
            prefix = prefix + '[видео] '
        elif str(project[7]).startswith('anime'):
            prefix = prefix + '[анимация] '

        await call.message.answer(text=f"{prefix}{project[2]}",
                                  reply_markup=post_corector_kb(index=project[0]))


# Меняем текст поста
@dp.message_handler(state=Admin_Builder.change_post_text)
async def start_menu(message: types.Message):
    index = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
    table = str(index.split('#')[1])
    index = str(index.split('#')[0])
    if table == 'project':
        sqLite.insert_info(table="project", name='post', data=message.text, id_name='id', telegram_id=index)
    else:
        sqLite.insert_info(table=f"post{table}", name='post_text', data=message.text, id_name='number',
                           telegram_id=index)
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    # Выводим первый пост
    await message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                         reply_markup=post_creator_kb(index=project[0]))
    prefix = ''
    if str(project[5]) == 'url':
        prefix = '[инлайн кнопки] '
    if str(project[7]).startswith('photo'):
        prefix = prefix + '[фото] '
    elif str(project[7]).startswith('video'):
        prefix = prefix + '[видео] '
    elif str(project[7]).startswith('anime'):
        prefix = prefix + '[анимация] '

    await message.answer(text=f"{prefix}{project[2]}",
                         reply_markup=post_corector_kb(index=project[0]))
    # Подгружаем остальные посты
    try:
        all_posts = sqLite.read_all(table=f'post{project[0]}')
        for i in range(1, len(all_posts) + 1):
            post = sqLite.read_values_by_name(table=f'post{project[0]}', data=str(i), id_name='number')
            prefix = ''
            if str(post[5]) == 'url':
                prefix = '[инлайн кнопки] '
            if str(post[7]).startswith('photo'):
                prefix = prefix + '[фото] '
            elif str(post[7]).startswith('video'):
                prefix = prefix + '[видео] '
            elif str(post[7]).startswith('anime'):
                prefix = prefix + '[анимация] '

            await message.answer(text=f"{prefix}{post[1]}",
                                 reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
    except:
        pass
    await Admin_Form.admin_first_menu.set()


# Добавляем кнопку в потоке постов в любое место
@dp.message_handler(state=Admin_Builder.create_post_text_inline)
async def start_menu(message: types.Message):
    data = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
    index = str(data)[21:].split('#')[0]
    table = str(data)[21:].split('#')[1]
    if table == 'project':
        post = sqLite.read_values_by_name(table="project", data=index, id_name='id')
        if post[4] is not None and str(post[4]) != '0':
            await message.answer(
                "В данном меню есть кнопки. Каскад постов можно создавать только если нет кнопок.")
        else:
            try:
                posts = sqLite.read_all(table=f'post{index}')
                for k in posts:
                    sqLite.insert_info(table=f'post{index}', name='number', data=str(int(k[0]) + 1), id_name='id',
                                       telegram_id=k[4])
                sqLite.insert_first_note(table=f'post{index}', telegram_id=1, id_name='number')
                sqLite.insert_info(table=f'post{index}', name='post_text', data=message.text, id_name='number',
                                   telegram_id=1)
            except:
                sqLite.new_table(table_name=index)
                sqLite.insert_first_note(table=f'post{index}', telegram_id=1, id_name='number')
                sqLite.insert_info(table=f'post{index}', name='post_text', data=message.text,
                                   id_name='number', telegram_id=1)
            sqLite.insert_info(table='project', name='start_post', data=index, id_name='id', telegram_id=index)

    else:
        posts = sqLite.read_all(table=f'post{table}')
        index = int(index)
        for k in posts:
            if index + 1 > int(k[0]):
                pass
            else:
                sqLite.insert_info(table=f'post{table}', name='number', data=str(int(k[0]) + 1), id_name='id',
                                   telegram_id=k[4])
        sqLite.insert_first_note(table=f'post{table}', telegram_id=(index + 1), id_name='number')
        sqLite.insert_info(table=f'post{table}', name='post_text', data=message.text,
                           id_name='number', telegram_id=(index + 1))
        index = table
    # Выводим первый пост
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    await message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                         reply_markup=post_creator_kb(index=project[0]))
    prefix = ''
    if str(project[5]) == 'url':
        prefix = '[инлайн кнопки] '
    if str(project[7]).startswith('photo'):
        prefix = prefix + '[фото] '
    elif str(project[7]).startswith('video'):
        prefix = prefix + '[видео] '
    elif str(project[7]).startswith('anime'):
        prefix = prefix + '[анимация] '

    await message.answer(text=f"{prefix}{project[2]}",
                         reply_markup=post_corector_kb(index=project[0]))
    # Подгружаем остальные посты
    try:
        all_posts = sqLite.read_all(table=f'post{index}')
        for i in range(1, len(all_posts) + 1):
            post = sqLite.read_values_by_name(table=f'post{index}', data=str(i), id_name='number')
            prefix = ''
            if str(post[5]) == 'url':
                prefix = '[инлайн кнопки] '
            if str(post[7]).startswith('photo'):
                prefix = prefix + '[фото] '
            elif str(post[7]).startswith('video'):
                prefix = prefix + '[видео] '
            elif str(post[7]).startswith('anime'):
                prefix = prefix + '[анимация] '
            await message.answer(text=f"{prefix}{post[1]}",
                                 reply_markup=post_corector_kb(index=post[0], table=f'{index}'))
    except:
        pass
    await Admin_Form.admin_first_menu.set()


# Вводим текст и ссылку для кнопки
@dp.callback_query_handler(state=Admin_Builder.change_post_type, text='inline_url_kb')
async def start_menu(call: types.CallbackQuery):
    await call.message.answer(text='Введите текст кнопки первой сторокой\nurl второй строкой', reply_markup=closet_kb)
    await Admin_Builder.inline_url_text.set()


# Сохраняем данные кнопки в пост
@dp.message_handler(state=Admin_Builder.inline_url_text)
async def start_menu(message: types.Message):
    data = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
    index = str(data.split('#')[0])
    table = str(data.split("#")[1])
    btn_name = message.text.split('\n')[0]
    btn_url = message.text.split('\n')[1]
    if table == 'project':
        try:
            post = str(sqLite.read_values_by_name(table="project", data=index, id_name='id')[6])
            text = post + f'URL%{btn_name}###{btn_url}@@@'
        except:
            text = f'URL%{btn_name}###{btn_url}@@@'

        sqLite.insert_info(table='project', name='inline_type', data='url', id_name='id', telegram_id=index)
        sqLite.insert_info(table='project', name='inline_kb', data=text, id_name='id', telegram_id=index)
    else:
        post = str(sqLite.read_values_by_name(table=f'post{table}', data=index, id_name='number')[6])
        if post is None or str(post) == '0':
            text = f'URL%{btn_name}###{btn_url}@@@'
        else:
            text = post + f'URL%{btn_name}###{btn_url}@@@'

        sqLite.insert_info(table=f'post{table}', name='inline_type', data='url', id_name='number', telegram_id=index)
        sqLite.insert_info(table=f'post{table}', name='inline_kb', data=text, id_name='number',
                           telegram_id=index)

    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if str(project[3]) == str(project[0]):
        # Выводим первый пост
        await message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                             reply_markup=post_creator_kb(index=project[0]))
        prefix = ''
        if str(project[5]) == 'url':
            prefix = '[инлайн кнопки] '
        if str(project[7]).startswith('photo'):
            prefix = prefix + '[фото] '
        elif str(project[7]).startswith('video'):
            prefix = prefix + '[видео] '
        elif str(project[7]).startswith('anime'):
            prefix = prefix + '[анимация] '

        await message.answer(text=f"{prefix}{project[2]}",
                             reply_markup=post_corector_kb(index=project[0]))
        # Подгружаем остальные посты
        try:
            all_posts = sqLite.read_all(table=f'post{project[0]}')
            for i in range(1, len(all_posts) + 1):
                post = sqLite.read_values_by_name(table=f'post{project[0]}', data=str(i), id_name='number')
                prefix = ''
                if str(post[5]) == 'url':
                    prefix = '[инлайн кнопки] '
                if str(post[7]).startswith('photo'):
                    prefix = prefix + '[фото] '
                elif str(post[7]).startswith('video'):
                    prefix = prefix + '[видео] '
                elif str(post[7]).startswith('anime'):
                    prefix = prefix + '[анимация] '

                await message.answer(text=f"{prefix}{post[1]}",
                                     reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
        except:
            pass
    else:
        prefix = ''
        if str(project[5]) == 'url':
            prefix = '[инлайн кнопки] '
        if str(project[7]).startswith('photo'):
            prefix = prefix + '[фото] '
        elif str(project[7]).startswith('video'):
            prefix = prefix + '[видео] '
        elif str(project[7]).startswith('anime'):
            prefix = prefix + '[анимация] '

        await message.answer(text=f"{prefix}{project[2]}",
                             reply_markup=post_corector_kb(index=project[0]))


# Вводим текст и ссылку для кнопки с окном
@dp.callback_query_handler(state=Admin_Builder.change_post_type, text='inline_window_kb')
async def start_menu(call: types.CallbackQuery):
    await call.message.answer(text='Ввводим данные для кнопки.\nДлинна текста кнопки должна быть меньше 200.Если текст '
                                   'больше 200. То бот автоматически обрежет текст.\nЗАГОЛОВОК\nТекст кнопки.',
                              reply_markup=closet_kb)
    await Admin_Builder.inline_window_text.set()


# Сохраняем данные кнопки с окном в пост
@dp.message_handler(state=Admin_Builder.inline_window_text)
async def start_menu(message: types.Message):
    data = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
    index = str(data.split('#')[0])
    table = str(data.split("#")[1])
    name = str(message.text.split('\n')[0])
    text = message.text[len(name) + 1:]
    text = text[:199]
    sqLite.insert_first_note(table='url_btn', id_name='btn_name', telegram_id=name)
    sqLite.insert_info(table='url_btn', name='text', data=text, id_name='btn_name', telegram_id=name)
    btn_id = sqLite.read_values_by_name(table="url_btn", data=name, id_name='btn_name')[0]

    if table == 'project':
        post = sqLite.read_values_by_name(table="project", data=index, id_name='id')[6]
        if post is None or str(post) == '0':
            post = ''
        btn = post + f'WIND%{name}###{btn_id}@@@'

        sqLite.insert_info(table='project', name='inline_type', data='url', id_name='id', telegram_id=index)
        sqLite.insert_info(table='project', name='inline_kb', data=btn, id_name='id', telegram_id=index)
    else:
        print(table, index)

        post = sqLite.read_values_by_name(table=f'post{table}', data=index, id_name='number')[6]
        if post is None or str(post) == '0':
            post = ''
        btn = post + f'WIND%{name}###{btn_id}@@@'

        sqLite.insert_info(table=f'post{table}', name='inline_type', data='url', id_name='number', telegram_id=index)
        sqLite.insert_info(table=f'post{table}', name='inline_kb', data=btn, id_name='number', telegram_id=index)

    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    if str(project[3]) == str(project[0]):
        # Выводим первый пост
        await message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                             reply_markup=post_creator_kb(index=project[0]))
        prefix = ''
        if str(project[5]) == 'url':
            prefix = '[инлайн кнопки] '
        if str(project[7]).startswith('photo'):
            prefix = prefix + '[фото] '
        elif str(project[7]).startswith('video'):
            prefix = prefix + '[видео] '
        elif str(project[7]).startswith('anime'):
            prefix = prefix + '[анимация] '

        await message.answer(text=f"{prefix}{project[2]}",
                             reply_markup=post_corector_kb(index=project[0]))
        # Подгружаем остальные посты
        try:
            all_posts = sqLite.read_all(table=f'post{project[0]}')
            for i in range(1, len(all_posts) + 1):
                post = sqLite.read_values_by_name(table=f'post{project[0]}', data=str(i), id_name='number')
                prefix = ''
                if str(post[5]) == 'url':
                    prefix = '[инлайн кнопки] '
                if str(post[7]).startswith('photo'):
                    prefix = prefix + '[фото] '
                elif str(post[7]).startswith('video'):
                    prefix = prefix + '[видео] '
                elif str(post[7]).startswith('anime'):
                    prefix = prefix + '[анимация] '

                await message.answer(text=f"{prefix}{post[1]}",
                                     reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
        except:
            pass
    else:
        prefix = ''
        if str(project[5]) == 'url':
            prefix = '[инлайн кнопки] '
        if str(project[7]).startswith('photo'):
            prefix = prefix + '[фото] '
        elif str(project[7]).startswith('video'):
            prefix = prefix + '[видео] '
        elif str(project[7]).startswith('anime'):
            prefix = prefix + '[анимация] '

        await message.answer(text=f"{prefix}{project[2]}",
                             reply_markup=post_corector_kb(index=project[0]))
