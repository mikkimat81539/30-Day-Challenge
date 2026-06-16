from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QGridLayout, QPushButton
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Delete Button Test") # Title of screen
		self.setFixedSize(500, 700) # Set screen size
		self.setStyleSheet("background-color: #99c3c7")

		central = QWidget()
		self.setCentralWidget(central)

		self.layout = QGridLayout() # create layout
		self.layout.setContentsMargins(0, 0, 0, 0)

		central.setLayout(self.layout) # set layout
		self.rowCount = 0

	def Add_Button(self):
		button = QPushButton("Add Button")
		button.setFixedSize(150, 20)
		button.setCursor(Qt.CursorShape.PointingHandCursor)

		button.clicked.connect(self.Delete_Button)

		self.layout.addWidget(button, 0, 0)

	def Delete_Button(self):
		button = QPushButton("Delete Button")
		button.setFixedSize(150, 20)
		button.setCursor(Qt.CursorShape.PointingHandCursor)

		self.layout.addWidget(button, self.rowCount, 1)
		self.rowCount += 1

		index = self.layout.indexOf(button) # Where is the button stored

		# This allows me to grab based on row, col, spans
		row, column, row_span, col_span = self.layout.getItemPosition(index)

		print(f"The widget is at row index: {row}")
	
app = QApplication([]) # initalize application

screen = MainWindow() # define screen

# Draw Widgets onto screen
screen.Add_Button()

screen.show() # show screen

app.exec() # execute application 
