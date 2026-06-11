from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QKeySequence, QShortcut
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
	
		button.setCursor(Qt.CursorShape.PointingHandCursor)
		
		button.clicked.connect(lambda: print("Button clicked"))

		keyConnect = QShortcut(QKeySequence("a"), self)
		keyConnect.activated.connect(lambda: button.animateClick())

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
