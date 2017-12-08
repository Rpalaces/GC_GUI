import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                QLineEdit, QHBoxLayout, QVBoxLayout, QComboBox)
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image

count = 1
 
class Main(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initUI()
 
    def initUI(self):
 
        centralwidget = QtGui.QWidget()
 
        self.add = QtGui.QPushButton("Add")
         
 
        self.grid = QtGui.QGridLayout()
         
        self.grid.addWidget(self.add,0,0)
 
        centralwidget.setLayout(self.grid)
 
        self.setCentralWidget(centralwidget)
 
 
    #---------Window settings --------------------------------
         
        self.setGeometry(300,300,280,170)
        self.setWindowTitle("")
        self.setWindowIcon(QtGui.QIcon(""))
        self.setStyleSheet("background-color:")
        self.show()
 
def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
 
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()