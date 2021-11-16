from aiogram import types
from main import dp
from modules import sqLite
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from modules.dispatcher import bot, Admin_Form
from modules.keyboards import user_type_kb, admin_kb_start, confirm_kb, change_data_kb, passwords_kb, back_kb


# Start menu noName Callback
@dp.callback_query_handler(state=Admin_Form.set_user_password_confirm, text='back')
@dp.callback_query_handler(state=Admin_Form.admin_first_menu, text='manual_input')
async def add_person_start(call: types.CallbackQuery):
    await call.message.edit_text(text="Введите телеграм ID или телефонный номер пользователя")
    await Admin_Form.search_user.set()


# Start menu
@dp.message_handler(state=Admin_Form.search_user)
async def start_menu(message: types.Message):
    data = sqLite.read_all()
    bad_deal = True
    for i in data:
        if message.text in str(i):
            sqLite.insert_info(table='admins', name='data', data=str(i[1]), telegram_id=message.from_user.id)
            await message.answer(f"Я нашел пользователя вот его данные:\n<b>"
                                 f"Телеграм ID {i[1]}\n"
                                 f"Номер телефона {i[3]}\n"
                                 f"Пароль {i[5]}</b>", parse_mode='html', reply_markup=user_type_kb)
            bad_deal = False
            await Admin_Form.set_user_type.set()
            break
        else:
            pass
    if bad_deal:
        await message.answer("Такого пользователя нет в базе данных. Пусть с начала пройдет регистрацию. "
                             "Для выхода /start")


# Set type of user
@dp.message_handler(state=Admin_Form.set_user_type)
async def start_menu(message: types.Message):
    data = sqLite.read_values_by_name(table="admins", data=message.from_user.id, name='data')[0]
    if 'Новый администратор' in message.text:
        sqLite.insert_info(table='all_users', name='type_user', data="admin", telegram_id=int(data))
        sqLite.insert_info(table='all_users', name='password', data="admin", telegram_id=int(data))
        sqLite.insert_first_note(table="admins", telegram_id=int(data))
        await message.answer("Данные сохранены")
        await message.answer(text='Добрый день. Чем могу помочь?', reply_markup=admin_kb_start)
        await Admin_Form.admin_first_menu.set()
    elif 'Пользователь' in message.text:
        await message.answer("Задайте пароль для входа в бот")
        await Admin_Form.set_user_password.set()
    elif '❌ Удалаить пользователя' in message.text:
        await message.answer("Вы уверены что хотите удалить этот аккаунт из базы данных?", reply_markup=confirm_kb)
        await Admin_Form.delete_user_confirm.set()
    else:
        await message.answer("Нажмите одну из кнопок")


# Set password for user
@dp.message_handler(state=Admin_Form.set_user_password)
async def start_menu(message: types.Message):
    if len(message.text) >= 6:
        data = sqLite.read_value_table_name(graph="*", table="admins", telegram_id=message.from_user.id)[2]
        sqLite.insert_info(table='admins', name='data_2', data=message.text, telegram_id=message.from_user.id)
        await message.answer(f'Вы уверенны что хотите задать пароль <b>{message.text}</b>\n'
                             f'Пользоватею с телеграм ID <b>{data}</b>', parse_mode='html', reply_markup=confirm_kb)
        await Admin_Form.set_user_password_confirm.set()
    else:
        await message.answer("Длинна пароля должна быть больше 6 символов")


# Set password for user confirm changes
@dp.callback_query_handler(state=Admin_Form.set_user_password_confirm, text='yes_all_good')
async def add_person_start(call: types.CallbackQuery):
    data = sqLite.read_value_table_name(graph="*", table="admins", telegram_id=call.from_user.id)
    sqLite.insert_info(table='all_users', name='password', data=data[3], telegram_id=int(data[2]))
    try:
        await bot.send_message(chat_id=int(data[2]), text=f"Вы были успешно добавлены в базу данных.\n"
                                                          f"Вот ваш пароль")
        await bot.send_message(chat_id=int(data[2]), text=f"{data[3]}")
        await call.message.answer(text="Данные сохранены. Новый пароль отправлен пользователю")
    except:
        await call.message.answer(text="Ошибка отправки запроса пользователю. \n"
                                       "Возможно такой аккаунт не существует, либо пользователь не подписан на бот")
    await call.message.answer(text='Добрый день. Чем могу помочь?', reply_markup=admin_kb_start)
    await Admin_Form.admin_first_menu.set()


# Delete user
@dp.callback_query_handler(state=Admin_Form.delete_user_confirm, text='yes_all_good')
async def start_menu(call: types.CallbackQuery):
    user_id = sqLite.read_value_table_name(graph="*", table="admins", telegram_id=call.from_user.id)[2]
    admin_data = sqLite.read_value_table_name(graph='*', table='all_users', telegram_id=user_id)[5]
    if str(admin_data) == 'root_admin':
        await call.message.answer("Этого пользователя нельзя удалить")
        await call.message.answer(text='Добрый день. Чем могу помочь?', reply_markup=admin_kb_start)
        await Admin_Form.admin_first_menu.set()
    else:
        sqLite.delete_str(table="all_users", data=user_id)
        try:
            sqLite.delete_str(table="admins", data=user_id)
        except:
            pass
        await call.message.answer("Данные удалены.")
        await call.message.answer(text='Добрый день. Чем могу помочь?', reply_markup=admin_kb_start)
        await Admin_Form.admin_first_menu.set()


# Change menu
@dp.callback_query_handler(state=Admin_Form.admin_first_menu, text='change_data')
async def start_menu(call: types.CallbackQuery):
    await call.message.edit_text(text=f'Вы в настройках.', reply_markup=change_data_kb)
    await Admin_Form.setings_menu.set()


# Change passwords
@dp.callback_query_handler(state=Admin_Form.new_pass_confirm, text='back')
@dp.callback_query_handler(state=Admin_Form.new_pass, text='back')
@dp.callback_query_handler(state=Admin_Form.delete_pass, text='back')
@dp.callback_query_handler(state=Admin_Form.setings_menu, text='password_work')
async def start_menu(call: types.CallbackQuery):
    await call.message.answer("Вот все ваши пароли", reply_markup=passwords_kb())
    await Admin_Form.setings_pass.set()


# Change passwords
@dp.message_handler(state=Admin_Form.setings_pass)
async def start_menu(message: types.Message):
    all_pass = str(sqLite.read_all(table='constant')[0][2])
    all_pass = all_pass.split('#№#')
    find = False
    for i in all_pass:
        if str(i) == message.text:
            find = True
            break
    if find:
        sqLite.insert_info(table='admins', name='data_2', data=message.text, telegram_id=message.from_user.id)
        await message.answer(f"Удалить пароль {message.text}?", reply_markup=confirm_kb)
        await Admin_Form.delete_pass.set()
    elif message.text == '◀️ Назад':
        await message.answer("Перешел назад", reply_markup=types.ReplyKeyboardRemove())
        await message.answer(text=f'Вы в нвстройках.', reply_markup=change_data_kb)
        await Admin_Form.setings_menu.set()
    elif message.text == '➕ Добавить новый пароль':
        await message.answer('Введите новый пароль', reply_markup=back_kb)
        await Admin_Form.new_pass.set()
    else:
        await message.answer('Нажмите кнопку ниже', reply_markup=passwords_kb())


# Add new passwords
@dp.message_handler(state=Admin_Form.new_pass)
async def start_menu(message: types.Message):
    await message.answer(f"Вы хотите добавить этот пароль {message.text}", reply_markup=confirm_kb)
    sqLite.insert_info(table='admins', name='data_2', data=message.text, telegram_id=message.from_user.id)
    await Admin_Form.new_pass_confirm.set()


# Add new passwords
@dp.callback_query_handler(state=Admin_Form.new_pass_confirm, text='yes_all_good')
async def start_menu(call: types.CallbackQuery):
    add_pass = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='data_2')[0])
    all_pass = str(sqLite.read_all(table='constant')[0][2])
    new_all_pass = all_pass + add_pass + '#№#'
    sqLite.insert_info(table='constant', name='password', data=new_all_pass, id_name='id', telegram_id=1)
    await call.message.answer("Пароль успешно добавлен", reply_markup=types.ReplyKeyboardRemove())
    await call.message.answer("Вот все ваши пароли", reply_markup=passwords_kb())
    await Admin_Form.setings_pass.set()


# Change data
@dp.callback_query_handler(state=Admin_Form.delete_pass, text='yes_all_good')
async def start_menu(call: types.CallbackQuery):
    delete_pass = str(sqLite.read_values_by_name(table="admins", data=call.from_user.id, name='data_2')[0])
    all_pass = str(sqLite.read_all(table='constant')[0][2])
    all_pass = all_pass.split('#№#')
    new_kb = ''
    for i in all_pass:
        if str(i) == delete_pass or str(i) == '':
            pass
        else:
            new_kb = new_kb + str(i) + '#№#'
    sqLite.insert_info(table='constant', name='password', data=new_kb, id_name='id', telegram_id=1)
    await call.message.answer("Пароль удален", reply_markup=types.ReplyKeyboardRemove())
    await call.message.answer("Вот все ваши пароли", reply_markup=passwords_kb())
    await Admin_Form.setings_pass.set()


# Change data
@dp.callback_query_handler(state=Admin_Form.setings_menu, text='spam_limit')
async def start_menu(call: types.CallbackQuery):
    const = sqLite.read_all(table="constant")[0][1]
    await call.message.edit_text(text=f'Текужее значение лимита по спаму равно {const}\n\n'
                                      f'Введите новое значение (только цифры)\n'
                                      f'Для выхода нажмите /start')
    await Admin_Form.change_data.set()


# Set new constant
@dp.message_handler(state=Admin_Form.change_data)
async def start_menu(message: types.Message):
    if message.text.isdigit():
        await message.answer(f"Новое число попыток ввести пароль равно {message.text}", reply_markup=confirm_kb)
        sqLite.insert_info(table='admins', name='data', data=message.text, telegram_id=message.from_user.id)
        await Admin_Form.change_data_confirm.set()
    else:
        await message.answer("Введите только цифры")


# Set new constant confirm
@dp.callback_query_handler(state=Admin_Form.change_data_confirm, text='yes_all_good')
async def start_menu(call: types.CallbackQuery):
    const = sqLite.read_value_table_name(graph="*", table="admins", telegram_id=call.from_user.id)[2]
    sqLite.insert_info(table='constant', name='ddos', data=const, id_name='id', telegram_id=1)
    await call.message.answer("Данные изменены.")
    await call.message.answer(text='Добрый день. Чем могу помочь?', reply_markup=admin_kb_start)
    await Admin_Form.admin_first_menu.set()
