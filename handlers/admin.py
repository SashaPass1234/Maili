from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot
from data_base import sqlite_db
from keyboards.all_kb import kb_admin

ID3 = False
product_id = 0


############################################################# ADMIN #############################################################

# @dp.message_handler(commands=['admin'])
async def autor_admin(message: types.Message):
    user = message.from_user
    admin_teg = user.username
    try:
        for ret4 in sqlite_db.cur.execute('SELECT admin_id FROM admins').fetchall():
            if ret4[0] == admin_teg:
                global ID3
                ID3 = True
                await message.answer('Вы успешно авторизовались как админ!', reply_markup=kb_admin)
    except:
        await message.answer('Ошибка базы данных!!!')

class FSMAdmin1(StatesGroup):
    admin_id = State()

# @dp.message_handler(commands='add_admin', State=None)
async def cm_start4(message: types.Message):
    # if ID3 == True:
        await FSMAdmin1.admin_id.set()
        await message.reply('Загрузи ид админа')

# @dp.message_handler(state=FSMAdmin1.admin_id)
async def load_admin_id(message: types.Message, state: FSMContext):
    # if ID3 == True:
        async with state.proxy() as data:
            data['admin_id'] = message.text

        await message.reply("Вы успешно добавили админа!")
        await state.finish()

        admins = data['admin_id']
        try:
            sqlite_db.cur.execute('INSERT INTO admins (admin_id) VALUES (?)', (admins, ))
            sqlite_db.base.commit()
        except:
            await message.answer('Ошибка базы данных!!!')

# @dp.message_handler(commands=['all_admin'])
async def sql_read(message):
    try:
        for ret3 in sqlite_db.cur.execute('SELECT admin_id FROM admins').fetchall():
            await bot.send_message(message.from_user.id, f'Админ: {ret3[0]}')
    except:
        await message.answer('Ошибка базы данных!!!')

################################################# Add CLOT #################################################

class FSMAdmin(StatesGroup):
    photo1 = State()
    name = State()
    quantity = State()
    size = State()
    ids = State()


# @dp.message_handler(commands=['add_clot'], state=None)
async def cm_start1(message: types.Message):
    if ID3 == True:
        await FSMAdmin.photo1.set()
        await message.reply('Загрузи фото одежды:')

# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo1)
async def load_photo1(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['photo1'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply("Теперь введи название:")

# @dp.message_handler(state=FSMAdmin.name)
async def load_name1(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply("Теперь введи количество:")

# @dp.message_handler(state=FSMAdmin.quantity)
async def load_quantity1(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['quantity'] = message.text
        await FSMAdmin.next()
        await message.reply("Теперь введи размер:")

# @dp.message_handler(state=FSMAdmin.size)
async def load_size1(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['size'] = message.text

        await state.finish()

        global product_id
        product_id += 1

        photo1 = data['photo1']
        name = data['name']
        size = data['size']
        quantity = data['quantity']

        try:
            sqlite_db.cur.execute(
                'INSERT INTO clot (img, name, size, ids, quantity) VALUES (?, ?, ?, ?, ?)',
                (photo1, name, size, product_id, quantity))
            sqlite_db.base.commit()
            await message.reply("Вы успешно добавили новый продукт!")
        except:
            await message.answer('Ошибка базы данных!!!')

################################################# Add ACSES #################################################

class FSMAdmin2(StatesGroup):
    photo1 = State()
    name = State()
    quantity = State()
    size = State()
    ids = State()


# @dp.message_handler(commands=['add_acses'], state=None)
async def cm_start2(message: types.Message):
    if ID3 == True:
        await FSMAdmin2.photo1.set()
        await message.reply('Загрузи фото аксессуара:')

# @dp.message_handler(content_types=['photo'], state=FSMAdmin2.photo1)
async def load_photo2(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['photo1'] = message.photo[0].file_id
        await FSMAdmin2.next()
        await message.reply("Теперь введи название:")

# @dp.message_handler(state=FSMAdmin2.name)
async def load_name2(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin2.next()
        await message.reply("Теперь введи количество Аксессуаров которые есть в наличие:")

# @dp.message_handler(state=FSMAdmin2.quantity)
async def load_quantity2(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['quantity'] = message.text
        await FSMAdmin2.next()
        await message.reply("Теперь введи размер:")

# @dp.message_handler(state=FSMAdmin2.size)
async def load_size2(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['size'] = message.text

        await state.finish()

        global product_id
        product_id += 1

        photo1 = data['photo1']
        name = data['name']
        size = data['size']
        quantity = data['quantity']

        try:
            sqlite_db.cur.execute(
                'INSERT INTO acses (img, name, size, ids, quantity) VALUES (?, ?, ?, ?, ?)',
                (photo1, name, size, product_id, quantity))
            sqlite_db.base.commit()
            await message.reply("Вы успешно добавили новый продукт!")
        except:
            await message.answer('Ошибка базы данных!!!')

################################################# Add ACSES #################################################

class FSMAdmin3(StatesGroup):
    photo1 = State()
    name = State()
    quantity = State()
    size = State()
    ids = State()


# @dp.message_handler(commands=['add_obyv'], state=None)
async def cm_start3(message: types.Message):
    if ID3 == True:
        await FSMAdmin3.photo1.set()
        await message.reply('Загрузи фото обуви')

# @dp.message_handler(content_types=['photo'], state=FSMAdmin3.photo1)
async def load_photo3(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['photo1'] = message.photo[0].file_id
        await FSMAdmin3.next()
        await message.reply("Теперь введи название:")

# @dp.message_handler(state=FSMAdmin3.name)
async def load_name3(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin3.next()
        await message.reply("Теперь введи количество пар:")

# @dp.message_handler(state=FSMAdmin3.quantity)
async def load_quantity3(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['quantity'] = message.text
        await FSMAdmin3.next()
        await message.reply("Теперь введи размер:")

# @dp.message_handler(state=FSMAdmin3.size)
async def load_size3(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['size'] = message.text

        await state.finish()

        global product_id
        product_id += 1

        photo1 = data['photo1']
        name = data['name']
        size = data['size']
        quantity = data['quantity']

        try:
            sqlite_db.cur.execute(
                'INSERT INTO obyv (img, name, size, ids, quantity) VALUES (?, ?, ?, ?, ?)',
                (photo1, name, size, product_id, quantity))
            sqlite_db.base.commit()
            await message.reply("Вы успешно добавили новый продукт!")
        except:
            await message.answer('Ошибка базы данных!!!')

############################################################# ПОИСК ЮЗЕРА И ИЗМ СТАТУСА #############################################################
class Search_class(StatesGroup):
    user = State()
    status = State()

async def func_search(message: types.Message):
    if ID3 == True:

        await Search_class.user.set()
        await message.reply('Введи имя пользователя без @')

async def input_search(message: types.Message, state):
    async with state.proxy() as data:
        data['user'] = message.text
        await Search_class.next()
        await message.reply("Теперь введи количество пар:")

async def input_status(message: types.Message, state: FSMContext):
    if ID3 == True:
        async with state.proxy() as data:
            data['status'] = message.text

        await state.finish()


        user = data['user']
        status = data['status']

        sqlite_db.cur.execute("UPDATE zakazy SET check_status=? WHERE user=?", (status, user))
        sqlite_db.base.commit()
        await bot.send_message(message.from_user.id, f'Успешно изменнен статус на: {status}')


############################################################# ALL FUNC #############################################################

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(autor_admin, commands=['admin'])
    dp.register_message_handler(sql_read, commands='all_admin')
    dp.register_message_handler(cm_start4, commands='add_admin', State=None)
    dp.register_message_handler(load_admin_id, state=FSMAdmin1.admin_id)

    dp.register_message_handler(cm_start1, commands='add_clot', state=None)
    dp.register_message_handler(load_photo1, content_types=['photo'], state=FSMAdmin.photo1)
    dp.register_message_handler(load_name1, state=FSMAdmin.name)
    dp.register_message_handler(load_quantity1, state=FSMAdmin.quantity)
    dp.register_message_handler(load_size1, state=FSMAdmin.size)

    dp.register_message_handler(cm_start2, commands='add_acses', state=None)
    dp.register_message_handler(load_photo2, content_types=['photo'], state=FSMAdmin2.photo1)
    dp.register_message_handler(load_name2, state=FSMAdmin2.name)
    dp.register_message_handler(load_quantity2, state=FSMAdmin2.quantity)
    dp.register_message_handler(load_size2, state=FSMAdmin2.size)

    dp.register_message_handler(cm_start3, commands='add_obyv', state=None)
    dp.register_message_handler(load_photo3, content_types=['photo'], state=FSMAdmin3.photo1)
    dp.register_message_handler(load_name3, state=FSMAdmin3.name)
    dp.register_message_handler(load_quantity3, state=FSMAdmin3.quantity)
    dp.register_message_handler(load_size3, state=FSMAdmin3.size)

    dp.register_message_handler(func_search, commands=['search'], state=None)
    dp.register_message_handler(input_search, state=Search_class.user)
    dp.register_message_handler(input_status, state=Search_class.status)

