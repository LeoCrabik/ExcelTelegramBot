from os import write
from aiogram import types
from dispatcher import dp
from dispatcher import bot
import config
import keyboards as kb
from handlers import personal_actions as pa
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@dp.callback_query_handler(lambda call: call.data == "Can_Insert_Names")
async def proccess_callback_can_insert_names(callback : types.CallbackQuery):
	config.CAN_INSERT_NAMES = True
	await callback.message.delete()
	if config.LANG_EN:
		await callback.message.answer("You can start enter the names", reply_markup=kb.keyboard2_en)
	else:
		await callback.message.answer("Теперь можете вводить имена", reply_markup=kb.keyboard2_ru)
	await callback.answer()
	#await bot.answer_callback_query(callback_query_id=call.id, text="Теперь можешь вводить имена")

@dp.callback_query_handler(lambda call: call.data == "Can_Download_Preresult")
async def proccess_callback_can_download_preresult(callback: types.CallbackQuery):
	await callback.message.delete()
	if config.LANG_EN:
		await callback.message.answer("Wish I could help you ;)")
	else:
		await callback.message.answer("Надеюсь, что смог помочь ;)")
	await bot.send_document(callback.message.chat.id, open(pa.Paths.PreresultFilePath, 'rb'))
	await callback.answer()

@dp.callback_query_handler(lambda call: call.data == "En_Lang")
async def change_to_en_lang(callback: types.CallbackQuery):
	config.LANG_EN = True
	await callback.message.delete()
	await callback.message.answer("Choose next step", reply_markup=kb.start)

@dp.callback_query_handler(lambda call: call.data == "Ru_Lang")
async def change_to_ru_lang(callback: types.CallbackQuery):
	config.LANG_EN = False
	await callback.message.delete()
	await callback.message.answer("Выберете следующий шаг", reply_markup=kb.start)