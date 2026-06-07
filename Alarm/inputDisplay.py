# GOAL IS TO DISPLAY WHAT IS INPUTTED WHEN BUTTON IS PRESSED

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Display Input")
		self.setFixedSize(500, 300)
		self.setStyleSheet("background-color: #9c8649;")

		self.layout = QGridLayout()
		widget = QWidget()
		widget.setLayout(self.layout)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setSpacing(20)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

		self.setCentralWidget(widget)

	def Text_Field(self):
		inputField = QLineEdit()
		inputField.setMaxLength(10)
		inputField.setStyleSheet(""" 
			QLineEdit{
				border: 3px solid black;
			}
		""")

		self.layout.addWidget(inputField, 0, 0)
		
	def Button(self):
		# If button is pressed display text inside input field

		# CREATE BUTTON
		button = QPushButton("Display Text")
		button.setFixedSize(100, 50)
	
		# ADD TO LAYOUT
		self.layout.addWidget(button, 1, 0, alignment=Qt.AlignmentFlag.AlignHCenter)

app = QApplication([])

screen = MainWindow()

screen.Text_Field()
screen.Button()

screen.show()

app.exec()
