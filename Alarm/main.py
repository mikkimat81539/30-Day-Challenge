# BUILD AN ALARM CLI IN 24 HOUR FORMAT

import datetime as dt

try:
	timeInput = input("Enter a time: ")

	timeFormat = dt.datetime.strptime(f'{timeInput}','%H:%M')

	scheduled = timeFormat.strftime('%H:%M')

except ValueError:
	print("Invalid Input")

while True:
	if scheduled == dt.datetime.now().strftime('%H:%M'):
		print("Wake Up")
