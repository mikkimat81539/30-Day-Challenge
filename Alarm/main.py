# BUILD AN ALARM CLI

# user inputs time (minutes, hours)
# Use 24 hour format

# 60 minutes = 1 hour
# 0 - 23 for hours

hours = abs(int(input("Enter hours: ")))
minutes = abs(int(input("Enter minutes: ")))

if 0 > hours or hours > 23 or 0 > minutes or minutes > 59:
	print("Invalid Input. Use 24 hour time format")
else:
	test = "{}:{}".format(hours, minutes) 
	print(test)
