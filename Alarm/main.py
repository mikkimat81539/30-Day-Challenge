# CREATE AN ALARM THAT IS A GUI USING PYQT

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QIntValidator
from PyQt6.QtWidgets import *

import sys

# You need one (and only one) QApplication instance per application.
# app = QApplication(sys.argv) # # Pass in sys.argv to allow command line arguments for your app.

#sys.argv contains at least one element (the script name)

# print(help(Button))

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Alarm")
		self.setFixedSize(QSize(500, 400))
		self.setStyleSheet("background-color: #ca82d1;") # Color format similar to css
		self.container = QWidget()
		self.setCentralWidget(self.container)

		self.layout = QGridLayout(self.container)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

	def Textbox(self):
		# Here we will input our time
		style = """
			QLineEdit {
			border: 3px solid black;
			border-radius: 6px;
		}"""

		validator = QIntValidator(0, 59)

		hourField = QLineEdit()

		colon = QLabel(":")
		font = colon.font() # initialize font
		font.setPointSize(30) # Set the size
		colon.setFont(font) # Setting the font

		minuteField = QLineEdit()

		hourField.setValidator(validator)
		minuteField.setValidator(validator)

		hourField.setStyleSheet(style)
		minuteField.setStyleSheet(style)

		hourField.setMaxLength(2)
		minuteField.setMaxLength(2)

		hourField.setFixedSize(QSize(90, 50))
		minuteField.setFixedSize(QSize(90, 50))
		colon.setFixedHeight(50)

		hourField.setAlignment(Qt.AlignmentFlag.AlignCenter)
		minuteField.setAlignment(Qt.AlignmentFlag.AlignCenter)
		colon.setAlignment(Qt.AlignmentFlag.AlignCenter)


		textContainer = QWidget()
		hbox = QHBoxLayout(textContainer)

		hbox.addWidget(hourField, alignment=Qt.AlignmentFlag.AlignVCenter)
		hbox.addWidget(colon, alignment=Qt.AlignmentFlag.AlignVCenter)
		hbox.addWidget(minuteField, alignment=Qt.AlignmentFlag.AlignVCenter)

		hbox.setSpacing(8)

		self.layout.addWidget(textContainer, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

	def Labeling(self):
		# Here we will put any necessary text (Ex: the colon (:), title)
		title = QLabel("24 HOUR ALARM")	

		font = title.font() # initialize font
		font.setPointSize(30) # Set the size
		title.setFont(font) # Setting the font
		title.setStyleSheet("color: black;") # Font color		
		title.setContentsMargins(0, 0, 0, 0)

		self.layout.addWidget(title, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

	def Buttons(self):
		# Here will be the buttons to save alarm
		save = QPushButton("Set Alarm")
		save.setCursor(Qt.CursorShape.PointingHandCursor)
		self.layout.addWidget(save, 2, 1, alignment=Qt.AlignmentFlag.AlignTop)

app = QApplication([])

# Create a Qt widget, which will be our window.
screen = MainWindow()

# DRAW WIDGETS
screen.Labeling()
screen.Textbox()
screen.Buttons()

screen.show() # Windows are hidden by default so you have to show it.

# Start the event loop.
app.exec()
