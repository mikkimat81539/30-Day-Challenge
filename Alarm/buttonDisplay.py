from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

import datetime as dt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Mouse Test")
		self.setFixedSize(500, 300)

		self.layout = QVBoxLayout()

	def Button(self):
		# Draw Button
		button = QPushButton("Pressed Me")
		button.setFixedSize(100, 50)
		button.setCursor(Qt.CursorShape.PointingHandCursor)

		# button.setCheckable(True) # makes a button behave like a toggle switch instead of a normal push button.

		# DATETIME
		Hour = dt.datetime.now().hour
		Minutes =  dt.datetime.now().minute

		time_format = dt.time(hour=Hour, minute=Minutes)

		# Text
		Text = QLabel(f"{time_format}")
		Text.setAlignment(Qt.AlignmentFlag.AlignHCenter)
		# Text.hide() # hide text
		Text.setVisible(False)

		
		# Check if buttton is clicked
		button.clicked.connect(lambda: Text.setVisible(True))
	
		# Store Widgets
		self.layout.addWidget(button)
		self.layout.addWidget(Text)

		widget = QWidget()
		widget.setLayout(self.layout)

		self.setCentralWidget(widget)

# INIT APPLICATION
app = QApplication([])

# DRAW
screen = MainWindow()
screen.Button()

screen.show() # DISPLAY SCREEN

app.exec() # EXECUTE APPLICATION
