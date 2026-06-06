# GOAL IS TO DISPLAY WHAT IS INPUTTED WHEN BUTTON IS PRESSED

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Display Input")
		self.setFixedSize(500, 300)
		self.setStyleSheet("background-color: #9c8649;")

		self.layout = QVBoxLayout()

	def Text_Field(self):
		inputField = QLineEdit()
		inputField.setMaxLength(10)
		inputField.setStyleSheet(""" 
			QLineEdit{
				border: 3px solid black;
			}
		""")

		inputField.setContentsMargins(0, 0, 0, 0)
		self.layout.addWidget(inputField, alignment=Qt.AlignmentFlag.AlignTop)
		
		widget = QWidget()
		widget.setLayout(self.layout)
		self.setCentralWidget(widget)

	def Button(self):
		pass

app = QApplication([])

screen = MainWindow()

screen.Text_Field()

screen.show()

app.exec()
