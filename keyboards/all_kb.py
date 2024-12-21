from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


keyboard1 = InlineKeyboardMarkup(row_width=2)
keyboard1.add(InlineKeyboardButton(text='Наш товар', callback_data='tovar'),
              InlineKeyboardButton(text='Поддержка', callback_data='support'))

keyboard2 = InlineKeyboardMarkup(row_width=2)
keyboard2.add(InlineKeyboardButton(text='Одежда', callback_data='clot'),
              InlineKeyboardButton(text='Аксессуары', callback_data='acses'),
              InlineKeyboardButton(text='Обувь', callback_data='obyv'))

keyboard3 = InlineKeyboardMarkup(row_width=1)
keyboard3.add(InlineKeyboardButton(text='Заказать', callback_data='zakaz_clot'))

keyboard4 = InlineKeyboardMarkup(row_width=1)
keyboard4.add(InlineKeyboardButton(text='Заказать', callback_data='zakaz_acses'))

keyboard5 = InlineKeyboardMarkup(row_width=1)
keyboard5.add(InlineKeyboardButton(text='Заказать', callback_data='zakaz_obyv'))


btn_admin1 = KeyboardButton('/add_clot')
btn_admin2 = KeyboardButton('/add_acses')
btn_admin3 = KeyboardButton('/add_obyv')

btn_admin4 = KeyboardButton('/add_admin')
btn_admin5 = KeyboardButton('/all_admin')

kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin.add(btn_admin1, btn_admin2, btn_admin3)
kb_admin.add(btn_admin4, btn_admin5)

