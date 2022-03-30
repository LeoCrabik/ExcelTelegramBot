from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

#Insert_Names = KeyboardButton('Ввести имена', callback_data = "Can_Insert_Names")
#Download_Preresult = KeyboardButton('Скачать обработанный файл', callback_data = "Can_Download_Preresult")

#irst_kb = ReplyKeyboardMarkup(
#	resize_keyboard=True, one_time_keyboard=True
#).row(
#	Insert_Names, Download_Preresult
#)

buttons = [
	types.InlineKeyboardButton(text="Ввести имена", callback_data = "Can_Insert_Names"),
	types.InlineKeyboardButton(text="Скачать обработанный файл", callback_data = "Can_Download_Preresult")
]
keyboard1 = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard = True)
keyboard1.add(*buttons)

keyboard2 = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard = True)
keyboard2.add(buttons[1])

btn_stop = KeyboardButton('/stop')
stop = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
stop.add(btn_stop)

btn_start = KeyboardButton('/start')
btn_info = KeyboardButton('/info')
start = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True, row_width=1)
start.add(btn_start, btn_info)