# GOAL IS TO DISPLAY WHAT IS INPUTTED WHEN BUTTON IS PRESSED

from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Display Input")
		self.setFixedSize(500, 300)
		self.setStyleSheet("background-color: #9c8649;")

app = QApplication([])

screen = MainWindow()

screen.show()

app.exec()
