# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np
import functools
  
# main window
# which inherits QDialog
class Window(QDialog):
      
    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
  
        # a figure instance to plot on
        self.figure = plt.figure()
  
        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)
  
        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # make a bunch of line edits for coefficients       
        self.C0Label = QLabel("C0")
        self.C0Val = QLineEdit("0")
        self.C1Label = QLabel("C1")
        self.C1Val = QLineEdit("1")
        self.C2Label = QLabel("C2")
        self.C2Val = QLineEdit("0")
        self.C3Label = QLabel("C3")
        self.C3Val = QLineEdit("0")
    
        # Just some button connected to 'plot' method
        self.plotButton = QPushButton('Plot')
          
        # adding action to the button
        self.plotButton.clicked.connect(self.plot)

        # create horizontal array of widgets to go below plot
        coefficients = QHBoxLayout()
        coefficients.addWidget(self.C0Label)
        coefficients.addWidget(self.C0Val)
        coefficients.addWidget(self.C1Label)
        coefficients.addWidget(self.C1Val)
        coefficients.addWidget(self.C2Label)
        coefficients.addWidget(self.C2Val)
        coefficients.addWidget(self.C3Label)
        coefficients.addWidget(self.C3Val)
        coefficients.addWidget(self.plotButton)

        # creating a Vertical Box layout
        layout = QVBoxLayout()
          
        # adding tool bar to the layout
        layout.addWidget(self.toolbar)
          
        # adding canvas to the layout
        layout.addWidget(self.canvas)
          
        # adding push button to the layout
        layout.addLayout(coefficients)
          
        # setting layout to the main window
        self.setLayout(layout)
  
    # action called by the push button
    def plot(self):
          
        xdata = np.linspace(-10,10,100)
        ydata = float(self.C0Val.text()) + float(self.C1Val.text())*xdata + float(self.C2Val.text())*(xdata**2) + float(self.C3Val.text())*(xdata**3)
  
        # clearing old figure
        self.figure.clear()
  
        # create an axis
        ax = self.figure.add_subplot(111)
  
        # plot data
        ax.plot(xdata, ydata, 'o')
  
        # refresh canvas
        self.canvas.draw()
  
# driver code
if __name__ == '__main__':
      
    # creating apyqt5 application
    app = QApplication(sys.argv)
  
    # creating a window object
    main = Window()
      
    # showing the window
    main.show()
  
    # loop
    sys.exit(app.exec_())