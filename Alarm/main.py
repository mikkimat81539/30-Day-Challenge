# CREATE AN ALARM THAT IS A GUI USING PYQT

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import *

import sys

# You need one (and only one) QApplication instance per application.
# app = QApplication(sys.argv) # # Pass in sys.argv to allow command line arguments for your app.

#sys.argv contains at least one element (the script name)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Alarm")
		self.setFixedSize(QSize(500, 600))
		self.setStyleSheet("background-color: #ca82d1;") # Color format similar to css
		self.container = QWidget()
		self.setCentralWidget(self.container)

		self.layout = QGridLayout(self.container)
		self.layout.setContentsMargins(0, 0, 0, 0)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

	def Textbox(self):
		# Here we will input our time
		hourField = QLineEdit()
		minuteField = QLineEdit()

		hourField.setMaxLength(2)
		minuteField.setMaxLength(2)

		hourField.setFixedSize(QSize(90, 50))
		minuteField.setFixedSize(QSize(90, 50))

		hourField.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		minuteField.setAlignment(Qt.AlignmentFlag.AlignHCenter)

		textContainer = QWidget()
		hbox = QHBoxLayout(textContainer)
		hbox.addWidget(hourField)
		hbox.addWidget(minuteField)
		hbox.setAlignment(Qt.AlignmentFlag.AlignCenter)

		self.layout.addWidget(textContainer, 1, 1, 1, 1)

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
		pass

app = QApplication([])


# Create a Qt widget, which will be our window.
screen = MainWindow()

# DRAW WIDGETS
screen.Labeling()
screen.Textbox()

screen.show() # Windows are hidden by default so you have to show it.

# Start the event loop.
app.exec()
