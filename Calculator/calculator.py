# MAKE A CALCULATOR IN PYTHON GUI
import PyQt6, sys

from PyQt6.QtWidgets import QMainWindow, QApplication 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator") # Window Title
		self.setStyleSheet("QMainWindow { background-color: #0a0d4a; }") # Window Color

app = QApplication(sys.argv)
screen = MainWindow()
screen.resize(350, 400)
screen.show()
app.exec()
