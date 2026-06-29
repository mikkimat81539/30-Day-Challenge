from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Delete Test")
		self.setFixedSize(500, 300)
		self.setStyleSheet("background-color: pink")


app = QApplication([])

screen = MainWindow()

screen.show()

app.exec()
