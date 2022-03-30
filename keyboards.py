from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types
import config

buttons_ru = [
	types.InlineKeyboardButton(text="Ввести имена", callback_data = "Can_Insert_Names"),
	types.InlineKeyboardButton(text="Скачать обработанный файл", callback_data = "Can_Download_Preresult")
]
buttons_en = [
	types.InlineKeyboardButton(text="Enter the names", callback_data = "Can_Insert_Names"),
	types.InlineKeyboardButton(text="Download edited file", callback_data = "Can_Download_Preresult")
]
keyboard1_ru = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard = True)
keyboard1_ru.add(*buttons_ru)
keyboard1_en = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard = True)
keyboard1_en.add(*buttons_en)

keyboard2_ru = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard = True)
keyboard2_ru.add(buttons_ru[1])
keyboard2_en = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard = True)
keyboard2_en.add(buttons_en[1])

#langbuttons = [
#	types.InlineKeyboardButton(text="En", callback_data="En_Lang")
#	types.InlineKeyboardButton(text="Ru", callback_data="Ru_Lang")
#]
langbuttons = [
	types.InlineKeyboardButton(text="En", callback_data = "En_Lang"),
	types.InlineKeyboardButton(text="Ru", callback_data = "Ru_Lang")
]
langkb = types.InlineKeyboardMarkup(row_width=1, one_time_keyboard = True)
langkb.add(*langbuttons)

btn_stop = KeyboardButton('/stop')
stop = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
stop.add(btn_stop)

btn_start = KeyboardButton('/excel')
btn_info = KeyboardButton('/info')
start = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True, row_width=1)
start.add(btn_start, btn_info)