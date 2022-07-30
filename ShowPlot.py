# Use the PyQtGraph library to make a plot and display it

import sys
import numpy as np
import PyQt5.QtWidgets as qtw
import pyqtgraph as qtg

# create app,window and layout for window
app = qtw.QApplication(sys.argv)
window = qtw.QWidget()
window.setWindowTitle("PlotsPlotsPlots")
window.setGeometry(200, 100, 200, 150)
layout = qtw.QVBoxLayout()

x = np.arange(10)
y = x**2
myplot = qtg.plot("Quadratic")
myplot.plot(x,y,'bo')
myplot.draw()

layout.addWidget(myplot)
window.setLayout(layout)
window.show()
sys.exit(app.exec())