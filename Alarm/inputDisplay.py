# GOAL IS TO DISPLAY WHAT IS INPUTTED WHEN BUTTON IS PRESSED

from PyQt6.QtCore import *
from PyQt6.QtGui import *
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

		self.labelList = []

	def Text_Field(self):
#		validator = QRegularExpressionValidator(
#			QRegularExpression(r"-?\d*")
#		)
		self.inputField = QLineEdit()
		self.inputField.setMaxLength(5000)
		self.inputField.setStyleSheet(""" 
			QLineEdit{
				font-size: 30px;
				border: 3px solid black;
			}
		""")
		
		# self.inputField.setValidator(validator)	

		self.layout.addWidget(self.inputField, 0, 0)

	def Labeling(self):
		self.inputLabel = QLabel("")
		text = self.inputField.text() # .text() is used to retrieve string data from user-interface elements like inputs, labels, or buttons

		self.inputLabel.setText(text) # .setText() used to set or change the text displayed by a widget
		self.inputField.clear()

		self.layout.addWidget(self.inputLabel, 2, 0)
		
		self.labelList.append(self.inputLabel.text())
		print(self.labelList)

	def Button(self):
		# If button is pressed display text inside input field

		# CREATE BUTTON
		button = QPushButton("Display Text")
		button.setFixedSize(100, 50)
		button.setCursor(Qt.CursorShape.PointingHandCursor)

		# ADD BUTTON FUNCTIONALITY
		button.clicked.connect(self.Labeling)

		# ADD TO LAYOUT
		self.layout.addWidget(button, 1, 0, alignment=Qt.AlignmentFlag.AlignHCenter)

app = QApplication([])

screen = MainWindow()

screen.Text_Field()
screen.Button()

screen.show()

app.exec()
