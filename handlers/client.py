from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from data_base import sqlite_db
from keyboards.all_kb import keyboard1, keyboard2, keyboard3, keyboard4, keyboard5


photo = open('img/vid.png', 'rb')


TEXT = '''🌟 Добро пожаловать в официальный телеграм-канал магазина Maili! 🌟

Мы — ваш надежный проводник в мир моды из Китая! 🚀 Наша команда с любовью отбирает самые стильные и актуальные вещи, чтобы вы всегда были на пике трендов. 

✨ Что мы предлагаем:

• 📦 Быстрая доставка модных товаров прямо к вашей двери!

• 👗 Широкий ассортимент: от одежды до аксессуаров!

• 💰 Конкурентные цены и регулярные акции!

Подписывайтесь на наш канал, чтобы первыми узнавать о новинках, эксклюзивах и специальных предложениях! Ваш стиль — наша забота! 💖

#Maili #МодаИзКитая #БыстраяДоставка #СтильКаждыйДень

Контакты для заказа:
@wxhzx
@qwerty_txx
'''


################################################# START #################################################
async def start(message: types.Message):
    await message.reply(TEXT, reply_markup=keyboard1)


################################################# CALLBACK #################################################
async def process_callback_button_tovar(callback_query: types.CallbackQuery):
    await bot.send_photo(callback_query.from_user.id, photo, 'Выберите вид товара:', reply_markup=keyboard2)


async def process_callback_button_support(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.from_user.id, 'Поддержка')


################################################# ПОИСК ОДЕЖДЫ #################################################
class FSMAdmin(StatesGroup):
    clot_message = State()
    acses_message = State()
    obyv_message = State()

async def process_callback_clot(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, "Введи название для поиска одежды:")
    await FSMAdmin.clot_message.set()


async def input_clot(message: types.Message, state):
    async with state.proxy() as data:
        data['clot_message'] = message.text

    await state.finish()

    text = data['clot_message']

    sqlite_db.cur.execute('SELECT img, name, size, ids, quantity FROM clot WHERE name = ?', (text,))
    result = sqlite_db.cur.fetchmany(6)

    if result:
        for value in result:
            global ids1
            ids1 = value[3]
            await bot.send_photo(message.from_user.id, value[0],
                                 f'Название: {value[1]}\nРазмер: {value[2]}\nАйди: {value[3]}\nКоличество пар: {value[4]}', reply_markup=keyboard3)
    else:
        response = f'Нет информации по запросу в базе данных.'
        await message.answer(response)


################################################# ПОИСК АКСЕССУАРА #################################################
async def process_callback_acses(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, "Введи название для поиска аксессуара:")
    await FSMAdmin.acses_message.set()


async def input_acses(message: types.Message, state):
    async with state.proxy() as data:
        data['acses_message'] = message.text

    await state.finish()

    text = data['acses_message']

    sqlite_db.cur.execute('SELECT img, name, size, ids, quantity FROM acses WHERE name = ?', (text,))
    result = sqlite_db.cur.fetchmany(6)

    if result:
        for value in result:
            global ids2
            ids2 = value[3]
            await bot.send_photo(message.from_user.id, value[0],
                                 f'Название: {value[1]}\nРазмер: {value[2]}\nАйди: {value[3]}\nКоличество пар: {value[4]}', reply_markup=keyboard4)
    else:
        response = f'Нет информации по запросу в базе данных.'
        await message.answer(response)


################################################# ПОИСК ОБУВИ #################################################
async def process_callback_obyv(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, "Введи название для поиска обуви:")
    await FSMAdmin.obyv_message.set()


async def input_obyv(message: types.Message, state):
    async with state.proxy() as data:
        data['obyv_message'] = message.text

    await state.finish()

    text = data['obyv_message']

    sqlite_db.cur.execute('SELECT img, name, size, ids, quantity FROM obyv WHERE name = ?', (text,))
    result = sqlite_db.cur.fetchmany(6)

    if result:
        for value in result:
            global ids3
            ids3 = value[3]
            await bot.send_photo(message.from_user.id, value[0],
                                 f'Название: {value[1]}\nРазмер: {value[2]}\nАйди: {value[3]}\nКоличество пар: {value[4]}', reply_markup=keyboard5)
    else:
        response = f'Нет информации по запросу в базе данных.'
        await message.answer(response)

################################################# ЗАКАЗЫ #################################################
TEXT_ZAKAZA = '''
Оплатите ваш заказа **** **** **** ****

Статус заказа: "ОЖИДАНИЕ ОПЛАТЫ ЗАКАЗА"!
'''

async def process_callback_button_zakaz_clot(callback_query: types.CallbackQuery):
    global user
    user = callback_query.from_user.username
    # global ids1
    sqlite_db.cur.execute('SELECT img, name, size, quantity, ids FROM clot WHERE ids = ?', (ids1,))
    result = sqlite_db.cur.fetchmany(5)
    status_check = "Ожидание оплаты заказа"
    group_id = -1002210462273
    for values in result:
        sqlite_db.cur.execute('INSERT INTO zakazy (user, img, name, size, ids, quantity, check_status) VALUES (?, ?, ?, ?, ?, ?, ?)',
                              (user, values[0], values[1], values[2], values[3], values[4], status_check))
        sqlite_db.base.commit()
        await bot.send_photo(group_id, values[0], f'ПОЛЬЗОВАТЕЛЬ ХОЧЕТ КУПИТЬ У ВАС ТОВАР: @{user}\nНазвание: {values[1]}\nРазмер: {values[2]}\nАйди: {values[3]}\nКоличество пар: {values[4]}\nСтатус: {status_check.upper()}')
    await bot.send_message(callback_query.from_user.id, TEXT_ZAKAZA)

async def process_callback_button_zakaz_acses(callback_query: types.CallbackQuery):
    global user
    user = callback_query.from_user.username
    global ids2
    sqlite_db.cur.execute('SELECT img, name, size, quantity, ids FROM acses WHERE ids = ?', (ids2,))
    result = sqlite_db.cur.fetchmany(5)
    status_check = "Ожидание оплаты заказа"
    group_id = -1002210462273
    for values in result:
        sqlite_db.cur.execute('INSERT INTO zakazy (user, img, name, size, ids, quantity, check_status) VALUES (?, ?, ?, ?, ?, ?, ?)',
                              (user, values[0], values[1], values[2], values[3], values[4], status_check))
        sqlite_db.base.commit()
        await bot.send_photo(group_id, values[0], f'ПОЛЬЗОВАТЕЛЬ ХОЧЕТ КУПИТЬ У ВАС ТОВАР: @{user}\nНазвание: {values[1]}\nРазмер: {values[2]}\nАйди: {values[3]}\nКоличество пар: {values[4]}\nСтатус: {status_check.upper()}')
    await bot.send_message(callback_query.from_user.id, TEXT_ZAKAZA)

async def process_callback_button_zakaz_obyv(callback_query: types.CallbackQuery):
    global user
    user = callback_query.from_user.username
    global ids3
    sqlite_db.cur.execute('SELECT img, name, size, ids, quantity FROM obyv WHERE ids = ?', (ids3,))
    result = sqlite_db.cur.fetchmany(7)
    status_check = "Ожидание оплаты заказа"
    group_id = -1002210462273
    for values in result:
        sqlite_db.cur.execute('INSERT INTO zakazy (user, img, name, size, ids, quantity, check_status) VALUES (?, ?, ?, ?, ?, ?, ?)',
                              (user, values[0], values[1], values[2], values[3], values[4], status_check))
        sqlite_db.base.commit()
        await bot.send_photo(group_id, values[0], f'ПОЛЬЗОВАТЕЛЬ ХОЧЕТ КУПИТЬ У ВАС ТОВАР: @{user}\nНазвание: {values[1]}\nРазмер: {values[2]}\nАйди: {values[3]}\nКоличество пар: {values[4]}\nСтатус: {status_check.upper()}')
    await bot.send_message(callback_query.from_user.id, TEXT_ZAKAZA)

async def my_zakazy(message: types.Message):
    user = message.from_user.username
    for value in sqlite_db.cur.execute('SELECT img, name, size, ids, quantity, check_status FROM zakazy WHERE user = ?', (user,)).fetchmany(7):
        await bot.send_photo(message.from_user.id, value[0], f'Название: {value[1]}\nРазмер: {value[2]}\nАйди: {value[3]}\nКоличество пар: {value[4]}\nСтатус: {value[5].upper()}')


############################################################# ALL FUCTION #############################################################
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

    dp.register_callback_query_handler(process_callback_button_tovar, lambda query: query.data == 'tovar')
    dp.register_callback_query_handler(process_callback_button_support, lambda query: query.data == 'support')

    dp.register_callback_query_handler(process_callback_clot, lambda query: query.data == 'clot')
    dp.register_message_handler(input_clot, state=FSMAdmin.clot_message)

    dp.register_callback_query_handler(process_callback_acses, lambda query: query.data == 'acses')
    dp.register_message_handler(input_acses, state=FSMAdmin.acses_message)

    dp.register_callback_query_handler(process_callback_obyv, lambda query: query.data == 'obyv')
    dp.register_message_handler(input_obyv, state=FSMAdmin.obyv_message)

    dp.register_callback_query_handler(process_callback_button_zakaz_clot, lambda query: query.data == 'zakaz_clot')
    dp.register_callback_query_handler(process_callback_button_zakaz_acses, lambda query: query.data == 'zakaz_acses')
    dp.register_callback_query_handler(process_callback_button_zakaz_obyv, lambda query: query.data == 'zakaz_obyv')

    dp.register_message_handler(my_zakazy, commands=['МоиЗаказы'])

