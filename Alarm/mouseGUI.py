from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

from pynput import mouse

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Mouse Test")
		self.setFixedSize(500, 300)

	def Button(self):
		button = QPushButton("Pressed Me")
		button.setFixedSize(100, 50)
		button.setCursor(Qt.CursorShape.PointingHandCursor)
	
		self.setCentralWidget(button)

# INIT APPLICATION
app = QApplication([])

# DRAW
screen = MainWindow()
screen.Button()

screen.show() # DISPLAY SCREEN

app.exec() # EXECUTE APPLICATION
