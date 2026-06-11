# CREATE AN ALARM THAT IS A GUI USING PYQT

"""Create Delete buttons for all times to delete from UI and labelList.
Figure out how to prevent UI and list from adding additinoal times past 6"""


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPalette, QIntValidator
from PyQt6.QtWidgets import *

import sys, re

# You need one (and only one) QApplication instance per application.
# app = QApplication(sys.argv) # # Pass in sys.argv to allow command line arguments for your app.

#sys.argv contains at least one element (the script name)

# print(help(Button))

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Alarm")
		self.setFixedSize(QSize(500, 400))
		self.setStyleSheet("background-color: #9c8649;") # Color format similar to css
		self.container = QWidget()
		self.setCentralWidget(self.container)

		self.layout = QGridLayout(self.container)
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setAlignment(Qt.AlignmentFlag.AlignTop)

		self.labelList = []
		self.rowCount = 3

	def Textbox(self):
		# Here we will input our time
		style = """
			QLineEdit {
			border: 3px solid black;
			border-radius: 6px;
		}"""

		validator = QIntValidator(0, 59)

		self.hourField = QLineEdit()

		colon = QLabel(":")
		font = colon.font() # initialize font
		font.setPointSize(30) # Set the size
		colon.setFont(font) # Setting the font

		self.minuteField = QLineEdit()

		self.hourField.setValidator(validator)
		self.minuteField.setValidator(validator)

		self.hourField.setStyleSheet(style)
		self.minuteField.setStyleSheet(style)

		self.hourField.setMaxLength(2)
		self.minuteField.setMaxLength(2)

		self.hourField.setFixedSize(QSize(90, 50))
		self.minuteField.setFixedSize(QSize(90, 50))
		colon.setFixedHeight(50)

		self.hourField.setAlignment(Qt.AlignmentFlag.AlignCenter)
		self.minuteField.setAlignment(Qt.AlignmentFlag.AlignCenter)
		colon.setAlignment(Qt.AlignmentFlag.AlignCenter)


		textContainer = QWidget()
		hbox = QHBoxLayout(textContainer)

		hbox.addWidget(self.hourField, alignment=Qt.AlignmentFlag.AlignVCenter)
		hbox.addWidget(colon, alignment=Qt.AlignmentFlag.AlignVCenter)
		hbox.addWidget(self.minuteField, alignment=Qt.AlignmentFlag.AlignVCenter)

		hbox.setSpacing(8)

		self.layout.addWidget(textContainer, 1, 1, alignment=Qt.AlignmentFlag.AlignCenter)

	def Title_Label(self):
		# Here we will put any necessary text (Ex: the colon (:), title)
		title = QLabel("24 HOUR ALARM")	

		font = title.font() # initialize font
		font.setPointSize(30) # Set the size
		title.setFont(font) # Setting the font
		title.setStyleSheet("color: black;") # Font color		
		title.setContentsMargins(0, 0, 0, 0)

		self.layout.addWidget(title, 0, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)

	def inputField(self):
		if len(self.labelList) >= 6:
			self.popup = QWidget()
			self.popup.setWindowFlags(Qt.WindowType.Dialog)
			self.popup.setFixedSize(QSize(400, 150))

			popup_label = QLabel("Maximum alarms you can set are 6")
		
			popup_font = popup_label.font() # initialize font
			popup_font.setPointSize(18) # Set the size
			popup_label.setFont(popup_font)
	
			popup_layout = QVBoxLayout()
			popup_layout.addWidget(popup_label, alignment=Qt.AlignmentFlag.AlignHCenter)

			self.popup.setLayout(popup_layout)

			self.popup.show()


		hourText = self.hourField.text()
		minText = self.minuteField.text()

		if hourText == "" or minText == "":
			return

		elif int(hourText) >= 24 or int(minText) >= 60:
			return

		elif len(minText) != 2:
			return

		timeLabel = QLabel(f"{hourText}:{minText}")

		if len(self.labelList) >= 6:
			print("To Many Alarms")
			return
		else:
			self.labelList.append(timeLabel.text())
			print(self.labelList)


			self.layout.addWidget(timeLabel, self.rowCount, 0)
			self.rowCount += 1

			self.hourField.clear()
			self.minuteField.clear()

			font = timeLabel.font() # initialize font
			font.setPointSize(20) # Set the size
			timeLabel.setFont(font) # Setting the font
			timeLabel.setStyleSheet("color: black;") # Font color		
	

	def Buttons(self):
		# Here will be the buttons to save alarm
		save = QPushButton("Set Alarm")
		save.setCursor(Qt.CursorShape.PointingHandCursor)
		self.layout.addWidget(save, 2, 1, alignment=Qt.AlignmentFlag.AlignTop)

		save.clicked.connect(self.inputField)

app = QApplication([])

# Create a Qt widget, which will be our window.
screen = MainWindow()

# DRAW WIDGETS
screen.Title_Label()
screen.Textbox()
screen.Buttons()

screen.show() # Windows are hidden by default so you have to show it.

# Start the event loop.
app.exec()
