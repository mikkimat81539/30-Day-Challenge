# CREATE AN ALARM THAT IS A GUI USING PYQT

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

import sys

# You need one (and only one) QApplication instance per application.
# app = QApplication(sys.argv) # # Pass in sys.argv to allow command line arguments for your app.

#sys.argv contains at least one element (the script name)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Alarm")
		self.setFixedSize(QSize(500, 600))
		self.setStyleSheet("background-color: blue;") # Color format similar to css

	def Textbox(self):
		# Here we will input our time
		pass

	def Labeling(self):
		# Here we will put any necessary text (Ex: the colon (:), title)
		title = QLabel("Hello")	

		font = title.font() # initialize font
		font.setPointSize(30) # Set the size
		title.setFont(font) # Setting the font
		title.setStyleSheet("color: white;") # Font color		

		# Set Label Widget
		self.setCentralWidget(title)

	def Buttons(self):
		# Here will be the buttons to save alarm
		pass

app = QApplication([])


# Create a Qt widget, which will be our window.
screen = MainWindow()

# DRAW WIDGETS
screen.Labeling()

screen.show() # IMPORTANT!!!!! Windows are hidden by default so you have to show it.

# Start the event loop.
app.exec()
