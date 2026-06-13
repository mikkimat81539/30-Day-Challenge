from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QGridLayout, QPushButton
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Delete Button Test") # Title of screen
		self.setFixedSize(500, 300) # Set screen size
		self.setStyleSheet("background-color: #99c3c7")

		central = QWidget()
		self.setCentralWidget(central)

		self.layout = QGridLayout() # create layout
		central.setLayout(self.layout) # set layout

	def Button(self):
		button = QPushButton("Delete button")
		button.setFixedSize(150, 20)
		button.setCursor(Qt.CursorShape.PointingHandCursor)

		self.layout.addWidget(button, 0, 0)

app = QApplication([]) # initalize application

screen = MainWindow() # define screen

# Draw Widets ont screen
screen.Button()

screen.show() # show screen

app.exec() # execute application 
