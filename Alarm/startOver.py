from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Delete Button Test") # Title of screen
		self.setFixedSize(500, 300) # Set screen size
		self.setStyleSheet("background-color: #c3c9c9")

app = QApplication([]) # initalize application

screen = MainWindow() # define screen

screen.show() # show screen

app.exec() # execute application 
