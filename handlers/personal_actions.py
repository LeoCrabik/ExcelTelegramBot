from aiogram import types
from dispatcher import dp
from dispatcher import bot
from aiogram.types import ContentTypes
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import config
import newdefs as nd
import keyboards as kb 
import math
import os

class FSMAdmin(StatesGroup):
	NameColumn_name = State()
	BalanceColumn_name = State()

class ColumnNames:
	Title_of_Names = None
	Title_of_Balance = None

class ColumnsIDs:
	NameRaw = 1
	NameColumn = 1
	BalanceRaw = 1 
	BalanceColumn = 1

class TableData:
	Name_list = []
	Balance_list = []

Now_date = None
class Paths:
	FilePath = None
	PreresultFilePath = None
	FinalFilePath = None
	FinalPath = None
	File_List=[]

@dp.message_handler(commands=["start"])
async def setlink_command(message: types.Message):
	#config.WAITING_FOR_FILE = True 
	await message.answer("Hello, " + message.from_user.first_name + ". Please choose your language", reply_markup=kb.langkb)
	#await message.answer("Привет, " + message.from_user.first_name + ". Пожалуйста, загрузи файл")


@dp.message_handler(commands=["info"])
async def setlink_command(message: types.Message):
	Paths.FinalPath = "data/" + str(message.from_user.id) + "/result/"
	Paths.File_List = os.listdir(Paths.FinalPath)
	for i in  range(0,len(Paths.File_List)):
		await message.answer(str(i+1)+": " + Paths.File_List[i])
		print(str(i+1)+": " + Paths.File_List[i])
	if config.LANG_EN:
		await message.answer("Enter number of file to download")
	else:
		await message.answer("Введите цифру файла, который хотите скачать")
	config.CAN_ENTER_NUMBER=True

@dp.message_handler(commands=["excel"])
async def setlink_command(message: types.Message):
	config.WAITING_FOR_FILE = True 
	if config.LANG_EN:
		await message.answer("Upload the file")
	else:
		await message.answer("Пожалуйста, загрузи файл")

@dp.message_handler(content_types=ContentTypes.DOCUMENT, state=None)
async def doc_handler(message: types.Message):
	global Now_date
	if (document := message.document) and (config.WAITING_FOR_FILE):
		Now_date=str(nd.Nowdate())
		Paths.FilePath ="data/" + str(message.from_user.id) + "/received/" + Now_date + ".xlsx"
		Paths.PreresultFilePath ="data/" + str(message.from_user.id) + "/received/" + Now_date + "_preresult.xlsx"
		Paths.FinalFilePath ="data/" +  str(message.from_user.id) + "/result/" + Now_date + "_final.xlsx"
		Paths.FinalPath ="data/" +  str(message.from_user.id) + "/result/"
		await document.download(destination_file=Paths.FilePath)
		await FSMAdmin.NameColumn_name.set()
		if config.LANG_EN:
			await message.answer("Enter the title of column with names")
		else:
			await message.answer("Введите название колонки с именами")

@dp.message_handler(state=FSMAdmin.NameColumn_name)
async def load_namecolumn(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['NameColumn_name'] = message.text
	await FSMAdmin.BalanceColumn_name.set()
	if config.LANG_EN:
		await message.answer("Enter the title of column with balance")
	else:
		await message.answer("Теперь введите название колонки с балансом")

@dp.message_handler(state=FSMAdmin.BalanceColumn_name)
async def load_balancecolumn(message: types.Message, state: FSMContext):
	global Now_date
	async with state.proxy() as data:
		data['BalanceColumn_name'] = message.text
	async with state.proxy() as data:
		#await message.answer(str(data))
		ColumnNames.Title_of_Balance = data['BalanceColumn_name']
		ColumnNames.Title_of_Names = data['NameColumn_name']
	await state.finish()
	config.IS_DATA_INSETED = True
	if config.LANG_EN:
		await message.answer("Choose next step", reply_markup=kb.keyboard1_en)
	else:
		await message.answer("Выберете, что делать дальше", reply_markup=kb.keyboard1_ru)
	nd.Preresult(ColumnNames.Title_of_Names, ColumnNames.Title_of_Balance)


@dp.message_handler()
async def tablesdata(message: types.Message):
	if config.CAN_INSERT_NAMES:
		if message.text != "/stop":
			if config.LANG_EN:
				await message.answer("Summary balance of " + message.text +" is "+ str(math.ceil(nd.DataProcessing(message.text)*100)/100))
				await message.answer("Enter another name", reply_markup=kb.stop)
			else:
				await message.answer("Суммарный баланс " + message.text +": "+ str(math.ceil(nd.DataProcessing(message.text)*100)/100))
				await message.answer("Введите следующее имя" , reply_markup=kb.stop)
		else:
			try: 
				os.mkdir(Paths.FinalPath)
			except:
				pass
			nd.DataProcessingFinal()
			await bot.send_document(message.chat.id, open(Paths.FinalFilePath, 'rb'))
			config.CAN_INSERT_NAMES=False
			if config.LANG_EN:
				await message.answer("Wish I could help you ;)", reply_markup=kb.start)
			else:
				await message.answer("Надеюсь, смог помочь ;)" , reply_markup=kb.start)		
	elif config.CAN_ENTER_NUMBER:
		await bot.send_document(message.chat.id, open(Paths.FinalPath+Paths.File_List[int(message.text)-1], 'rb'))
		if config.LANG_EN:
			await message.answer("Wish I could help you ;)", reply_markup=kb.start)
		else:
			await message.answer("Надеюсь, смог помочь ;)" , reply_markup=kb.start)	
		config.CAN_ENTER_NUMBER=False




#@dp.message_handler(content_types=ContentTypes.Message)
#async def 