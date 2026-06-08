from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeyEvent, QCursor
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Key Events")
		self.setFixedSize(500, 300)
		self.setStyleSheet("background-color: #914ead;")

	def Button(self):
		# Draw Button
		button = QPushButton("Press Me")
		button.setFixedSize(100, 50)
	
#		button.setStyleSheet("""
#			QPushButton {
#				border: 3px solid black;
#			}
#		""")	

		button.setCursor(Qt.CursorShape.PointingHandCursor)

		self.setCentralWidget(button)

		

# init application
app = QApplication([])

# Draw Screen
screen = MainWindow()

# Draw methods
screen.Button()

# Show screen
screen.show()

# execute application
app.exec()
