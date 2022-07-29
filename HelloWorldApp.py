# Hello World App

import sys

# import widgets from PyQt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

# create an instance of my application
app = QApplication(sys.argv)
app.setStyle('Breeze')

# create the GUI
window = QWidget()
window.setWindowTitle("My App")
window.setGeometry(100, 100, 280, 80) # window size and location (x, y, width, height)
HelloMsg = QLabel("<h1>Hello World!</h1>", parent = window)
HelloMsg.move(60,20)

# show the app window
window.show()

# send control to app
sys.exit(app.exec_())