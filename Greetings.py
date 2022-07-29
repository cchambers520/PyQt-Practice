# This app will have the user select a greeting and then display the greeting

import sys

import PyQt5.QtWidgets as qw

# create a slot function to be connected to signal from button later
def greet():
    msg.setText("<h2>"+greet_type.currentText()+"</h2>")

# create app,window and layout for window
app = qw.QApplication(sys.argv)
window = qw.QWidget()
window.setWindowTitle("Greeter")
window.setGeometry(200, 100, 200, 150)
layout = qw.QVBoxLayout()

greet_type = qw.QComboBox()
greet_type.addItem("Hello")
greet_type.addItem("Sup")
greet_type.addItem("Bonjour")

#greeting = "<h2>Hello</h2>"
greet_btn = qw.QPushButton("Greet")
greet_btn.clicked.connect(greet)

layout.addWidget(greet_type)
layout.addWidget(greet_btn)
msg = qw.QLabel("")
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())