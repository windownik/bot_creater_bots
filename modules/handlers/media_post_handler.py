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


# Начинаем менять пост
@dp.callback_query_handler(state=Admin_Builder.change_post_type, text='type_post')
async def start_menu(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Для добавления медиа данных в выбранный пост. \nОтправьте мне фото, видео или анимацию',
        reply_markup=closet_kb)
    await Admin_Builder.add_media_post.set()


# Добавляем видео
@dp.message_handler(content_types=types.ContentType.VIDEO, state=Admin_Builder.add_media_post)
async def start_menu(message: types.Message):
    data = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
    index = str(data).split('#')[0]
    table = str(data).split('#')[1]

    video_id = message.video.file_id
    # Сахраняем данные в нужную нам таблицу
    if str(table) == 'project':
        sqLite.insert_info(table="project", name='post_type', data=f"video_{video_id}", id_name='id', telegram_id=index)
    else:
        sqLite.insert_info(table=f"post{table}", name='post_type', data=f"video_{video_id}", id_name='number',
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


# Добавляем фото
@dp.message_handler(content_types=types.ContentType.PHOTO, state=Admin_Builder.add_media_post)
async def start_menu(message: types.Message):
    data = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
    index = str(data).split('#')[0]
    table = str(data).split('#')[1]

    photo_id = message.photo[-1].file_id
    # Сахраняем данные в нужную нам таблицу
    if str(table) == 'project':
        sqLite.insert_info(table="project", name='post_type', data=f"photo_{photo_id}", id_name='id', telegram_id=index)
    else:
        sqLite.insert_info(table=f"post{table}", name='post_type', data=f"photo_{photo_id}", id_name='number',
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


# Добавляем анимацию
@dp.message_handler(content_types=types.ContentType.ANIMATION, state=Admin_Builder.add_media_post)
async def start_menu(message: types.Message):
    data = str(sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0])
    index = str(data).split('#')[0]
    table = str(data).split('#')[1]
    anime_id = message.animation.file_id
    # Сахраняем данные в нужную нам таблицу
    if str(table) == 'project':
        sqLite.insert_info(table="project", name='post_type', data=f"anime_{anime_id}", id_name='id', telegram_id=index)
    else:
        sqLite.insert_info(table=f"post{table}", name='post_type', data=f"anime_{anime_id}", id_name='number',
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

