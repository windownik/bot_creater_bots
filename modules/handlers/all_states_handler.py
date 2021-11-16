from aiogram import types
from main import dp
from modules.change_btn_functions import *
from modules import sqLite
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from modules.dispatcher import bot, Admin_Form, Admin_Builder
from modules.keyboards import closet_kb, confirm_kb, btn_creator_kb, post_creator_kb, post_corector_kb, \
    post_type_kb


# Корректируем кнопку в редакторе применяем команду c инлайн клавиатур в любом месте
@dp.callback_query_handler(state="*")
async def add_person_start(call: types.CallbackQuery):
    try:
        index = int(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='data_2')[0])
        text_btn = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='data')[0])
    except:
        pass
    if str(call.data) == "left":
        left_btn(index=index, text_btn=text_btn)
        work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await call.message.answer(text=f"{project[2]}",
                                  reply_markup=btn_creator_kb(index=(project[0]), active_btn=text_btn,
                                                              btn_creator=True,
                                                              tg_id=call.from_user.id))
        await Admin_Builder.btn_builder.set()

    elif str(call.data) == "right":
        right_btn(index=index, text_btn=text_btn)
        work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await call.message.answer(text=f"{project[2]}",
                                  reply_markup=btn_creator_kb(index=(project[0]), active_btn=text_btn,
                                                              btn_creator=True,
                                                              tg_id=call.from_user.id))
        await Admin_Builder.btn_builder.set()

    elif str(call.data) == "upper":
        upp_btn(index=index, text_btn=text_btn)
        work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await call.message.answer(text=f"{project[2]}",
                                  reply_markup=btn_creator_kb(index=(project[0]), active_btn=text_btn,
                                                              btn_creator=True,
                                                              tg_id=call.from_user.id))
        await Admin_Builder.btn_builder.set()

    elif str(call.data) == "down":
        down_btn(index=index, text_btn=text_btn)
        work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await call.message.answer(text=f"{project[2]}",
                                  reply_markup=btn_creator_kb(index=(project[0]), active_btn=text_btn,
                                                              btn_creator=True,
                                                              tg_id=call.from_user.id))
        await Admin_Builder.btn_builder.set()

    elif str(call.data) == "change_btn":
        await call.message.edit_text("Введите новое название кнопки", reply_markup=closet_kb)
        await Admin_Builder.change_btn_text.set()

    elif str(call.data) == "delete_btn":
        await call.message.answer(text='Вы точно хотите удалить кнопку?', reply_markup=confirm_kb)
        await Admin_Builder.btn_builder_delete.set()

    elif str(call.data) == "cut_btn":
        cut_btn(index=index, text_btn=text_btn)
        sqLite.insert_info(table='admins', name='cut_btn', data=text_btn, telegram_id=call.from_user.id)
        work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await call.message.answer(text=f"{project[2]}",
                                  reply_markup=btn_creator_kb(index=(project[0]), btn_creator=True,
                                                              tg_id=call.from_user.id))
        await Admin_Builder.btn_builder.set()

    elif str(call.data).startswith('change_btn_post'):
        index = str(call.data)[16:]
        sqLite.insert_info(table='admins', name='data', data=index, telegram_id=call.from_user.id)
        await call.message.answer("Введите новый текст поста", reply_markup=closet_kb)
        await Admin_Builder.change_post_text.set()

    elif str(call.data).startswith('delete_btn_post_'):
        sqLite.insert_info(table='admins', name='data', data=str(call.data), telegram_id=call.from_user.id)
        await call.message.answer(text='Вы точно хотите удалить пост?', reply_markup=confirm_kb)
        await Admin_Builder.post_builder_delete.set()

    elif str(call.data).startswith('create_menu_btn_post_'):
        await call.message.answer("Введите текст нового поста", reply_markup=closet_kb)
        sqLite.insert_info(table='admins', name='data', data=str(call.data), telegram_id=call.from_user.id)
        await Admin_Builder.create_post_text_inline.set()

    elif str(call.data).startswith('upper_post_'):
        table = str(call.data)[11:]
        table = str(table.split('#')[1])
        index = str(table.split('#')[0])
        if table == 'project' or (index == '1'):
            pass
        else:
            post_upp(str(call.data)[11:])
        work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        if str(project[3]) == str(project[0]):
            # Выводим первый пост
            await call.message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                                      reply_markup=post_creator_kb(index=project[0]))
            if str(project[5]) == 'url':
                await call.message.answer(text=f"[инлайн кнопки] {project[2]}",
                                          reply_markup=post_corector_kb(index=project[0]))
            else:
                await call.message.answer(text=f"{project[2]}", reply_markup=post_corector_kb(index=project[0]))
            # Подгружаем остальные посты
            try:
                all_posts = sqLite.read_all(table=f'post{project[0]}')
                for i in range(1, len(all_posts) + 1):
                    post = sqLite.read_values_by_name(table=f'post{project[0]}', data=str(i), id_name='number')
                    if str(post[5]) == 'url':
                        await call.message.answer(text=f"[инлайн кнопки] {post[1]}",
                                                  reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
                    else:
                        await call.message.answer(text=f"{post[1]}",
                                                  reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
            except:
                pass
        else:
            await call.message.answer("📝 Вы в редакторе постов.\n Первый пост нельзя переместить",
                                      reply_markup=post_creator_kb(index=(project[0])))
            if str(project[5]) == 'url':
                await call.message.answer(text=f"[инлайн кнопки] {project[2]}",
                                          reply_markup=post_corector_kb(index=project[0]))
            else:
                await call.message.answer(text=f"{project[2]}", reply_markup=post_corector_kb(index=project[0]))

    elif str(call.data).startswith('down_post_'):
        table = str(call.data)[10:]
        table = str(table.split('#')[1])
        index = str(table.split('#')[0])
        if table == 'project' or (index == '1'):
            pass
        else:
            post_down(str(call.data)[10:])
        work_window = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        if str(project[3]) == str(project[0]):
            # Выводим первый пост
            await call.message.answer(text='📝 Вы в редакторе постов.\n Первый пост нельзя переместить',
                                      reply_markup=post_creator_kb(index=project[0]))
            if str(project[5]) == 'url':
                await call.message.answer(text=f"[инлайн кнопки] {project[2]}",
                                          reply_markup=post_corector_kb(index=project[0]))
            else:
                await call.message.answer(text=f"{project[2]}", reply_markup=post_corector_kb(index=project[0]))
            # Подгружаем остальные посты
            try:
                all_posts = sqLite.read_all(table=f'post{project[0]}')
                for i in range(1, len(all_posts) + 1):
                    post = sqLite.read_values_by_name(table=f'post{project[0]}', data=str(i), id_name='number')
                    if str(post[5]) == 'url':
                        await call.message.answer(text=f"[инлайн кнопки] {post[1]}",
                                                  reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
                    else:
                        await call.message.answer(text=f"{post[1]}",
                                                  reply_markup=post_corector_kb(index=post[0], table=f'{project[0]}'))
            except:
                pass
        else:
            await call.message.answer("📝 Вы в редакторе постов.\n Первый пост нельзя переместить",
                                      reply_markup=post_creator_kb(index=(project[0])))
            if str(project[5]) == 'url':
                await call.message.answer(text=f"[инлайн кнопки] {project[2]}",
                                          reply_markup=post_corector_kb(index=project[0]))
            else:
                await call.message.answer(text=f"{project[2]}", reply_markup=post_corector_kb(index=project[0]))

    elif str(call.data).startswith('creat_btn_post_'):
        table = str(call.data)[15:]
        line = str(table.split('#')[0])
        table = str(table.split('#')[1])
        if table == 'project':
            project = sqLite.read_values_by_name(table="project", data=line, id_name='id')
        else:
            project = sqLite.read_values_by_name(table=f"post{table}", data=line, id_name='number')
        if (project[5] is None) or (str(project[5]) == '0'):
            pass
        else:
            # собираем инлайн клавиатуру
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
                               telegram_id=call.message.from_user.id)
            await call.message.answer(text=f"{project[1]}", reply_markup=url_kb)
        #     Выводим редактор кнопок
        table = str(call.data)[15:]
        sqLite.insert_info(table='admins', name='data', data=table, telegram_id=call.from_user.id)
        await call.message.answer('Для редактирования нажмите кнопку ниже', reply_markup=post_type_kb)
        await Admin_Builder.change_post_type.set()

    elif str(call.data).startswith('pass-'):
        tg_id = str(call.data).split('%%%')[1]
        password = str(call.data).split('%%%')[0]
        password = password[5:]
        await bot.send_message(chat_id=int(tg_id), text="Вот ваш пароль для входа в бот")
        await bot.send_message(chat_id=int(tg_id), text=f"<b>{password}</b>", parse_mode='html')

    elif str(call.data).startswith('WIND'):
        btn_id = str(call.data).split('WIND')[1]
        text = sqLite.read_values_by_name(table="url_btn", data=btn_id, id_name='id')[2]
        await call.answer(text, show_alert=True)


# Выбираем редактор
@dp.message_handler(state='*')
async def start_menu(message: types.Message):
    # Открываем проект
    work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
    work_post = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
    valid_menu = sqLite.read_values_by_name(table="project", data=message.text, id_name='in_text')
    new_work_window = valid_menu
    if valid_menu is not None:
        valid_menu = True
    else:
        valid_menu = False
    # Собираем кнопки меню
    if '🎛 Редактор кнопок' in message.text:
        await message.answer("🛠 Вы в редакторе кнопок")

        work_window = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='work_post')[0])
        project = sqLite.read_values_by_name(table="project", data=work_window, id_name='in_text')
        await message.answer(text=f"{project[2]}", reply_markup=btn_creator_kb(index=(project[0]),
                                                                               btn_creator=True,
                                                                               tg_id=message.from_user.id))
        await Admin_Builder.btn_builder.set()

    elif '📝 Редактор постов' in message.text:
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
            await message.answer("📝 Вы в редакторе постов.\n Первый пост нельзя переместить",
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

            await message.answer(text=f"{prefix}{project[2]}",
                                 reply_markup=post_corector_kb(index=project[0]))

    elif not valid_menu:
        await message.answer("Команда не определена")

    elif message.text == str(new_work_window[1]):
        sqLite.insert_info(table='admins', name='work_post', data=message.text, telegram_id=message.from_user.id)
        project = sqLite.read_values_by_name(table="project", data=message.text, id_name='in_text')
        if (project[3] is not None) and (int(project[3]) != 0):
            await message.answer(text=f"<b>В этом меню есть посты. Для просмотра и редактирования постов перейдите "
                                      f"в редактор!</b>", parse_mode='html')
        else:
            # Проверка на наличие клавиатуры inline
            if (project[5] is None) or (str(project[5]) == '0'):

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
                                     reply_markup=btn_creator_kb(index=project[0], tg_id=message.from_user.id))

                await Admin_Form.admin_first_menu.set()

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
                prefix = ''
                if str(project[5]) == 'url':
                    prefix = '[инлайн кнопки] '
                if str(project[7]).startswith('photo'):
                    prefix = prefix + '[фото] '
                elif str(project[7]).startswith('video'):
                    prefix = prefix + '[видео] '
                elif str(project[7]).startswith('anime'):
                    prefix = prefix + '[анимация] '

                await message.answer(text=f"{prefix}{project[2]}", reply_markup=url_kb)

                await Admin_Form.admin_first_menu.set()
