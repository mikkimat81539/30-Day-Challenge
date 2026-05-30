# MAKE A CALCULATOR IN PYTHON GUI
import PyQt6, sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator") # Window Title
		self.setStyleSheet("QMainWindow { background-color: #0a0d4a; }") # Window Color
		widget = QLineEdit() # Text Input
		widget.setPlaceholderText("0")

		widget.setFixedSize(200, 30) # width, height

		self.setCentralWidget(widget)


app = QApplication(sys.argv)

# SCREEN
screen = MainWindow()
screen.resize(350, 400)

# INPUT FIELD

# EXECUTE SCREEN
screen.show()
app.exec()
