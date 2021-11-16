from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from modules import sqLite

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

back_kb = InlineKeyboardMarkup()
back_kb.add(back_btn)

# ДАть заявку на вступление
send_invoice = InlineKeyboardButton(text='Связаться с администратором', callback_data='send_invoice')
input_password = InlineKeyboardButton(text='Ввести пароль', callback_data='input_password')

noname_start_kb = InlineKeyboardMarkup().add(input_password)
noname_start_kb.add(send_invoice)

# Задать тип аккаунта
admin_btn = KeyboardButton(f'Новый администратор')
delete_btn = KeyboardButton(f'❌ Удалаить пользователя')
back_messege_btn = KeyboardButton(f'◀️ Назад')
user_type_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_type_kb.add(admin_btn)
user_type_kb.add(delete_btn)
user_type_kb.add(back_messege_btn)

# Клавиатуро подтверждения действия
closet = InlineKeyboardButton(text='🚫 Отмена', callback_data='closet')
closet_kb = InlineKeyboardMarkup().add(closet)


# Клавиатуро подтверждения действия
yes_all_good = InlineKeyboardButton(text='Да. Все верно!', callback_data='yes_all_good')

confirm_kb = InlineKeyboardMarkup().add(yes_all_good)
confirm_kb.add(closet)


# Клавиатуро настроек админа
spam_limit = InlineKeyboardButton(text='Лимит по спаму', callback_data='spam_limit')
password_work = InlineKeyboardButton(text='Пароли', callback_data='password_work')
change_data_kb = InlineKeyboardMarkup().add(spam_limit)
change_data_kb.add(password_work)
change_data_kb.add(back_btn)

# ДАть заявку на вступление
left = InlineKeyboardButton(text='⬅️', callback_data='left')
right = InlineKeyboardButton(text='➡️', callback_data='right')
upper = InlineKeyboardButton(text='⬆️', callback_data='upper')
down = InlineKeyboardButton(text='⬇️', callback_data='down')
change_btn = InlineKeyboardButton(text='Изменить', callback_data='change_btn')
delete_btn = InlineKeyboardButton(text='Удалить', callback_data='delete_btn')
cut_btn = InlineKeyboardButton(text='Вырезать', callback_data='cut_btn')
create_menu_btn = InlineKeyboardButton(text='Создать меню', callback_data='create_menu_btn')

btn_corector_kb = InlineKeyboardMarkup().row(left, upper, down, right)
btn_corector_kb.add(change_btn, delete_btn, cut_btn)


type_post = InlineKeyboardButton(text='Изменить тип поста', callback_data='type_post')
inline_url_kb = InlineKeyboardButton(text='Инлайн кнопка с url', callback_data='inline_url_kb')
inline_window_kb = InlineKeyboardButton(text='Инлайн кнопка с вспл. окном', callback_data='inline_window_kb')
post_type_kb = InlineKeyboardMarkup().add(type_post)
post_type_kb.add(inline_url_kb)
post_type_kb.add(inline_window_kb)
post_type_kb.add(closet)


# Главные кнопки в редакторе
def btn_creator_kb(tg_id: int, index: int = 0, btn_creator: bool = False, active_btn: str = None):
    # Проверка на вырезанную кнопку
    btn_cut = sqLite.read_values_by_name(table="admins", data=tg_id, name='cut_btn')[0]
    project = sqLite.read_values_by_name(table='project', id_name='id', data=index)
    builder_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
    btn_builder = KeyboardButton(f'🎛 Редактор кнопок')
    post_builder = KeyboardButton(f'📝 Редактор постов')
    btn_builder_stop = KeyboardButton(f'❌ Стоп редактор')
    admin_page_btn = KeyboardButton(f'🛠 Админка')
    add_btn = KeyboardButton(f'➕ Добавить Кнопку')
    past_btn = KeyboardButton(f'➕ Вставить Кнопку')
    main_post_btn = KeyboardButton(f'🔙 Вернутся на главную')
    if project[4] is None:
        pass
    else:
        rows = str(project[4]).split('#@#')
        for i in rows:
            if str(i) != '':
                btn_s = str(i).split('@$@')
                number_btns = len(btn_s)
                for k in range(0, number_btns):
                    if str(btn_s[k]) != '':
                        if active_btn is not None:
                            if active_btn == str(btn_s[k]):
                                n = KeyboardButton(f'[{str(btn_s[k])}]')
                                if k == 0:
                                    builder_kb.add(n)
                                else:
                                    builder_kb.insert(n)
                            else:
                                n = KeyboardButton(str(btn_s[k]))
                                if k == 0:
                                    builder_kb.add(n)
                                else:
                                    builder_kb.insert(n)
                        else:
                            n = KeyboardButton(str(btn_s[k]))
                            if k == 0:
                                builder_kb.add(n)
                            else:
                                builder_kb.insert(n)
                    else:
                        pass
            else:
                pass
    if str(btn_cut) == "ЁЁЁЁЁ":
        pass
    else:
        builder_kb.add(past_btn)

    if btn_creator:
        builder_kb.add(add_btn)
        builder_kb.add(main_post_btn, back_messege_btn)
        builder_kb.add(btn_builder_stop, post_builder)
    else:
        builder_kb.add(main_post_btn, back_messege_btn)
        builder_kb.add(btn_builder, admin_page_btn, post_builder)
    return builder_kb


# Главные кнопки в редакторе
def passwords_kb():
    all_pass = str(sqLite.read_all(table='constant')[0][2])
    all_pass = all_pass.split('#№#')
    pass_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    add_btn = KeyboardButton(f'➕ Добавить новый пароль')
    for i in all_pass:
        if str(i) == '':
            pass
        else:
            i = KeyboardButton(f'{i}')
            pass_kb.insert(i)
    pass_kb.add(add_btn)
    pass_kb.add(back_messege_btn)
    return pass_kb


# Главные кнопки в редакторе
def repl_pass_users_kb(id: int):
    all_pass = str(sqLite.read_all(table='constant')[0][2])
    all_pass = all_pass.split('#№#')
    pass_kb = InlineKeyboardMarkup()
    for i in all_pass:
        if str(i) == '':
            pass
        else:
            i = InlineKeyboardButton(text=f'{i}', callback_data=f'pass-{i}%%%{id}')
            pass_kb.insert(i)
    return pass_kb


chat_btn = InlineKeyboardButton(text='Перейти в чат', url='https://t.me/joinchat/HFdNLqQ664UyNWIy')

chat_kb = InlineKeyboardMarkup().add(chat_btn)


# Редактор постов
def post_corector_kb(index: int, table: str = 'project'):
    upper_post = InlineKeyboardButton(text='⬆️', callback_data=f'upper_post_{index}#{table}')
    creat_btn_post = InlineKeyboardButton(text='*️⃣', callback_data=f'creat_btn_post_{index}#{table}')
    down_post = InlineKeyboardButton(text='⬇️', callback_data=f'down_post_{index}#{table}')
    change_btn_post = InlineKeyboardButton(text='Изменить текст', callback_data=f'change_btn_post_{index}#{table}')
    delete_btn_post = InlineKeyboardButton(text='Удалить', callback_data=f'delete_btn_post_{index}#{table}')
    create_menu_btn_post = InlineKeyboardButton(text='Добавить', callback_data=f'create_menu_btn_post_{index}#{table}')

    post_corector_kb = InlineKeyboardMarkup().row(upper_post, creat_btn_post, down_post)
    post_corector_kb.add(change_btn_post, delete_btn_post, create_menu_btn_post)
    return post_corector_kb


# Главные кнопки в редакторе
def post_creator_kb(index: int = 0):
    # Проверка на вырезанную кнопку
    project = sqLite.read_values_by_name(table='project', id_name='id', data=index)
    builder_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)

    post_builder = KeyboardButton(f'📝 Редактор постов')
    add_btn = KeyboardButton(f'➕ Добавить пост')
    btn_builder = KeyboardButton(f'🎛 Редактор кнопок')
    btn_builder_stop = KeyboardButton(f'❌ Стоп редактор')
    if project[4] is None:
        pass
    else:
        rows = str(project[4]).split('#@#')
        for i in rows:
            if str(i) != '':
                btn_s = str(i).split('@$@')
                number_btns = len(btn_s)
                for k in range(0, number_btns):
                    if str(btn_s[k]) != '':
                        n = KeyboardButton(str(btn_s[k]))
                        if k == 0:
                            builder_kb.add(n)
                        else:
                            builder_kb.insert(n)
                    else:
                        pass
            else:
                pass

    builder_kb.add(add_btn)
    builder_kb.add(btn_builder, btn_builder_stop)
    return builder_kb


# Клавиатура Пользователя в сложном меню
def user_adaptiv_kb(index: int = 0):
    # Проверка на вырезанную кнопку
    project = sqLite.read_values_by_name(table='project', id_name='id', data=index)
    builder_kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=10)
    main_post_btn = KeyboardButton(f'🔙 Вернутся на главную')
    if project[4] is None:
        pass
    else:
        rows = str(project[4]).split('#@#')
        for i in rows:
            if str(i) != '':
                btn_s = str(i).split('@$@')
                number_btns = len(btn_s)
                for k in range(0, number_btns):
                    if str(btn_s[k]) != '':
                        n = KeyboardButton(f'{str(btn_s[k])}')
                        if k == 0:
                            builder_kb.add(n)
                        else:
                            builder_kb.insert(n)
                    else:
                        pass
            else:
                pass
    builder_kb.add(main_post_btn, back_messege_btn)

    return builder_kb
