import os 

File_List = []

def DataSearch(Path):
	global File_List
	File_List = os.listdir(Path)
	#print(File_List)
	print(File_List)
	for i in  range(0,len(File_List)):
		print(str(i+1)+": " + File_List[i])


DataSearch("C:/Users/User/Desktop/Python Projects/Yuyusha_Telegram_Bot/data/420038215/result")

