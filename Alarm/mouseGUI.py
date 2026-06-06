from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Mouse Test")
		self.setFixedSize(500, 300)

	def Button(self):
		button = QPushButton("Pressed Me")
		button.setFixedSize(100, 50)
		button.setCursor(Qt.CursorShape.PointingHandCursor)

		# Check if button was click
		button.setCheckable(True)
		button.clicked.connect(lambda: print("Pressed"))
	
		self.setCentralWidget(button)

# INIT APPLICATION
app = QApplication([])

# DRAW
screen = MainWindow()
screen.Button()

screen.show() # DISPLAY SCREEN

app.exec() # EXECUTE APPLICATION
