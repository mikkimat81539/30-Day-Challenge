# BUILD AN ALARM CLI IN 24 HOUR FORMAT

import pygame, time
import datetime as dt

pygame.mixer.init()
pygame.mixer.music.load("blk_man_yelling.mp3")


try:
	timeInput = input("Enter a time (24 hour Clock): ")

	timeFormat = dt.datetime.strptime(f'{timeInput}','%H:%M')

	scheduled = timeFormat.strftime('%H:%M')

except ValueError:
	print("Invalid Input")

while True:
	if scheduled == dt.datetime.now().strftime('%H:%M'):
		pygame.mixer.music.play()
		time.sleep(8)
		break

	time.sleep(1)


