from aiogram import types
from main import dp
from modules import sqLite
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from modules.dispatcher import bot, NoName
from modules.keyboards import send_contact_kb, repl_pass_users_kb, chat_kb


# Start menu noName Callback
@dp.callback_query_handler(state=NoName.first_menu, text='send_invoice')
async def add_person_start(call: types.CallbackQuery):
    await call.message.edit_text(text="Введите ваше Имя.")
    await NoName.noname_send_name.set()


# Start menu noName name
@dp.message_handler(state=NoName.noname_send_name)
async def add_person_start(message: types.Message):
    # sqLite.insert_first_note(table='all_users', telegram_id=message.from_user.id)
    sqLite.insert_info(table='all_users', name='type_user', data=f"{message.text}",
                       telegram_id=message.from_user.id)
    await message.answer(text="Если хотите зарегистрироваться отправьте свои данные администратору.",
                         reply_markup=send_contact_kb)
    await NoName.noname_contact.set()


# Keep contact
@dp.message_handler(state=NoName.noname_contact, content_types=['contact'])
async def contact(message: types.Message, state: FSMContext):
    if message.contact is not None:
        phone_number = str(message.contact.phone_number)
        if '+' in phone_number:
            pass
        else:
            phone_number = '+' + phone_number
        user_id = message.contact.user_id
        data = sqLite.read_value_table_name(graph='*', table='all_users', telegram_id=user_id)
        sqLite.insert_info(table='all_users', name='phone', data=f"{phone_number}", telegram_id=user_id)

        await bot.send_message(message.chat.id, 'Ваша заявка сформирована ждите сообщение от администратора.\n'
                                                'Если у вас будут вопросы, то мы ответим на них в нашем чате тех. '
                                                'поддержки.\n'
                                                'Для перехода на стартовую страницу нажмите /start',
                               reply_markup=chat_kb)
        admins = sqLite.read_all()
        for i in admins:
            if 'admin' in str(i[5]):
                try:
                    await bot.send_message(chat_id=int(i[1]), text=f'У вас новая заявка от <b>{data[2]}</b>\n'
                                                                   f'Вот его телефон и телеграм ID', parse_mode='html')
                    await bot.send_message(chat_id=int(i[1]), text=f'<b>{phone_number}</b>', parse_mode='html')
                    await bot.send_message(chat_id=int(i[1]), text=f'<b>{user_id}</b>', parse_mode='html')
                    await bot.send_message(chat_id=int(i[1]), text=f'Вы можите сразу отправить пароль. '
                                                                   f'Для этого нажмите кнопку ниже.', parse_mode='html',
                                           reply_markup=repl_pass_users_kb(message.from_user.id))
                except:
                    print(int(i[0]), 'Ошибка новой заявки')
            else:
                pass
        await state.finish()
    else:
        pass


# Keep contact
@dp.message_handler(state=NoName.noname_contact)
async def contact(message: types.Message):
    await message.answer(text="Поделится контактом нужно нажав кнопку",
                         reply_markup=send_contact_kb)
    await NoName.noname_contact.set()