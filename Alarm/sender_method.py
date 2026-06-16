# This file is to test out sender method is pyQt

# Display buttons -- DONE
# When BTN 1 is clicked display -> UNO -- DONE
# When BTN 2 is clicked display -> POOP -- DONE
# When BTN 3 is clicked resize to 500, 300

from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QApplication, QHBoxLayout
from PyQt6.QtCore import Qt

import random

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Sender Method Test")
		self.setMinimumSize(500, 200)
		self.setMaximumSize(500, 850)
		self.setStyleSheet("background-color: #ffffff;")
		# print(self.width()) # This allows me to grab the width of my widget
		# print(self.height()) # This allows me to grab the height of my widget

		self.layout = QHBoxLayout()

		self.widget = QWidget()

		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)

	def Button(self):
		unoBtn = QPushButton("UNO")
		poopBtn = QPushButton("POOP")
		resizeBtn = QPushButton("Resize Me")

		buttonList = [unoBtn, poopBtn, resizeBtn]

		for i in buttonList:
			i.setCursor(Qt.CursorShape.PointingHandCursor)
			self.layout.addWidget(i)	

			i.clicked.connect(self.button_test)
	
	def button_test(self):
		uno_colors = ["red", "yellow", "green", "blue", "#575757"]

		button = self.sender() # tells me who triggered this call?

		if self.layout.indexOf(button) == 0:
			randColor = random.choice(uno_colors)
			self.setStyleSheet(f"background-color: {randColor};") 
			print(button.text())

		elif self.layout.indexOf(button) == 1:
			self.setStyleSheet("background-color: #522303;")
			print(button.text())
	
		elif self.layout.indexOf(button) == 2:
			resizeInc = 10 # increament window
			self.resize(500, self.height() + resizeInc)
			self.setStyleSheet("background-color: #8fd5d9;")
			print(button.text())

		 # print(self.layout.indexOf(button)) # This allows me grab the index of the button I click

		# print(button.text())

		

app = QApplication([])

screen = MainWindow()

# Draw Widgets
screen.Button()

# Show screen
screen.show()

# Execute Application
app.exec()
