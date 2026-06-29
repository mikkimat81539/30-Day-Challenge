# Every button click will create  a label that increments by 1
# Each label will be in same column but different row
# Each label will have a delete button
# I will store each number in a sorteed list (database)

from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# set screen attributes
		self.setWindowTitle("Delete Test")
		self.setFixedSize(500, 300)
		self.setStyleSheet("background-color: pink")

		# Layout Container
		self.container = QWidget()
		self.layout = QGridLayout(self.container)
		self.setCentralWidget(self.container)

		# Button Counter
		self.counter = 1

		self.database = sorted([]) # This is for storing the numbers


	def Label(self):
		pass

	def Increment_Button(self):
		self.button = QPushButton(str(self.counter))
		self.button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		self.button.setFixedSize(100, 50)

		self.layout.addWidget(self.button)

		self.button.clicked.connect(self.button_clicked)

	def button_clicked(self):
		self.counter += 1
		self.button.setText(str(self.counter))


app = QApplication([])

screen = MainWindow()

screen.Increment_Button()

screen.show()

app.exec()
