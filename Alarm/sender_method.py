# This file is to test out sender method is pyQt
# Display buttons
# When BTN 1 is clicked display -> UNO
# When BTN 2 is clicked display -> POOP
# When BTN 3 is clicked resize to 500, 200

from PyQt6.QtWidgets import QWidget, QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Sender Method Test")
		self.setFixedSize(500, 550)
		# print(self.width()) # This allows me to grab the width of my widget
		# print(self.height()) # This allows me to grab the height of my widget



app = QApplication([])

screen = MainWindow()

# Show screen
screen.show()

# Execute Application
app.exec()
