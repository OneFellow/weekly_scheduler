import datetime
import os

os.system("cls")


def input_year():
	while True:
		year_x = input("Input year: ")
		if 0 < len(year_x) <= 4 and year_x.isdigit():
			return int(year_x)
			
def input_month():
	while True:
		month_x = input("Input month: ")
		if 0 < len(month_x) <= 2 and month_x.isdigit():
			if 0 < int(month_x) < 13:
				return int(month_x)

def input_day():
	while True:
		day_x = input("Input day: ")
		if 0 < len(day_x) <= 2 and day_x.isalnum():
			if 0 < int(day_x) < 31:
				return int(day_x)