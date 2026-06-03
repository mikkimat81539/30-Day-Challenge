# BUILD AN ALARM CLI IN 24 HOUR FORMAT

import datetime

import datetime as dt

try:
	timeInput = input("Enter a time: ")

	timeFormat = dt.datetime.strptime(f'{timeInput}','%H:%M')

	print(timeFormat.strftime('%H:%M'))

except ValueError:
	print("Invalid Input")
