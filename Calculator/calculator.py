# MAKE A CALCULATOR IN PYTHON GUI
import PyQt6, sys

from PyQt6.QtWidgets import QMainWindow, QApplication 

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Calculator")

app = QApplication(sys.argv)
screen = MainWindow()
screen.resize(450, 500)
screen.show()
app.exec()
