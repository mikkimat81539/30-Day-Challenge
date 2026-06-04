# CREATE AN ALARM THAT IS A GUI USING PYQT

from PyQt6.QtWidgets import QApplication, QWidget

import sys

# You need one (and only one) QApplication instance per application.
# app = QApplication(sys.argv) # # Pass in sys.argv to allow command line arguments for your app.

#sys.argv contains at least one element (the script name)

app = QApplication(["Alarm"])


# Create a Qt widget, which will be our window.
window = QWidget()

window.show() # IMPORTANT!!!!! Windows are hidden by default so you have to show it.

# Start the event loop.
app.exec()
