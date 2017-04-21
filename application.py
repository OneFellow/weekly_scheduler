import os
import calendar
import datetime

from widgets import addTime


def main_menu():
	os.system("cls")
	
	startDate = "none"
	skipDates = []
	schedule = []
	savedPath = ""
	
	while True:
		os.system("cls")
		print("Start date:", startDate)
		printDates(skipDates, "Skip Dates")
		printDates(schedule, "Scheduele")
		print("-------------------------------\n")
		print("1: Set start date")
		print("2: Input skip date")
		print("3: Remove skip date")
		print("4: Create schedule")
		print("5: Save schedule")
		print("\t", savedPath)
		print("0: Terminate application")
		
		ans = input("--> ")
		
		if ans == "0":
			break
		elif ans == "1":
			startDate = createDate()
		elif ans == "2":
			skipDates.append(createDate())
		elif ans == "3":
			removeDate(skipDates)
		elif ans == "4":
			schedule = createSched(startDate, skipDates)
		elif ans == "5":
			savedPath = saveSchedule(startDate, skipDates, schedule)
			
def printDates(array, title):

	if len(array) == 0:
		print(title + ": none")
	else:
		print(title + ":")
		for i in array:
			print("\t" + str(array.index(i)+1) + ":", i)
			

def createDate():
	year = addTime.input_year()
	month = addTime.input_month()
	day = addTime.input_day()
	
	while True:
		if month == 2 and day == 29 and calendar.isleap(year):
			break
		elif month == 2 and day > 28:
			print("Invalid day")
			day = addTime.input_day()
		else:
			break
	return datetime.date(year, month, day)
	
def removeDate(array):
	if len(array) == 0:
		pass
	elif len(array) == 1:
		x = int(input("Remove date ("+ str(len(array)) + "): "))
		tryRemove(x, array)
	else:
		x = int(input("Remove date (1-" + str(len(array)) + "): "))
		tryRemove(x, array)
		
def tryRemove(i, array):
	try:
		del array[i-1]
	except IndexError:
		pass
		

def createSched(fDate, skipped=0):
	repeat = int(input("How many reoccuring weeks? "))
	result = [fDate]
	for i in range(repeat - 1):
		fDate += datetime.timedelta(weeks=1)
		if fDate in skipped:
			fDate += datetime.timedelta(weeks=1)
		result.append(fDate)
		print(result)
	return result
	
def saveSchedule(name, skipped, schedule):
	path = "saved/" + str(name) + ".txt"
	f = open(path, 'w')
	path = ""
	f.write("Scheduele for start date " + str(name) + "\n\n")
	writeDates(f, "Skip Dates:\n", skipped)
	writeDates(f, "Scheduele:\n", schedule)
	f.close()
	return str(os.path.realpath(path)) + "\\saved\\" + str(name) + ".txt"

def writeDates(oFile, title, array):
	if len(array) == 0:
		oFile.write(title + ": none")
	else:
		oFile.write(title)
		for i in array:
			oFile.write("\t" + str(i) + "\n")
		oFile.write("\n")
	

if __name__ == "__main__":
	main_menu()
