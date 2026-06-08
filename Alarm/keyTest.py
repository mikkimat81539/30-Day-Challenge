from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Key Events")
		self.setFixedSize(500, 300)
		self.setStyleSheet("background-color: #914ead;")

# init application
app = QApplication([])

# Draw Screen
screen = MainWindow()

# Draw methods

# Show screen
screen.show()

# execute application
app.exec()
