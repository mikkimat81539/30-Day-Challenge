from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

import datetime as dt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Mouse Test")
		self.setFixedSize(500, 300)

	def Button(self):
		button = QPushButton("Pressed Me")
		button.setFixedSize(100, 50)
		button.setCursor(Qt.CursorShape.PointingHandCursor)

		# Check if button was click
		# button.setCheckable(True) # makes a button behave like a toggle switch instead of a normal push button.

		# DATETIME
		Hour = dt.datetime.now().hour
		Minutes =  dt.datetime.now().minute

		button.clicked.connect(lambda: print(f"{Hour}:{Minutes}"))
	
		self.setCentralWidget(button)

# INIT APPLICATION
app = QApplication([])

# DRAW
screen = MainWindow()
screen.Button()

screen.show() # DISPLAY SCREEN

app.exec() # EXECUTE APPLICATION
