# Every button click will create  a label that increments by 1
# Each label will be in same column but different row
# Each label will have a delete button
# I will store each number in a sorteed list (database)

from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Delete Test")
		self.setFixedSize(500, 300)
		self.setStyleSheet("background-color: pink")

		self.database = sorted([]) # This is for storing the numbers
		print(self.database)


	def Increment_Buttons(self):
		pass



app = QApplication([])

screen = MainWindow()

screen.show()

app.exec()
