import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar2 = QProgressBar(self)
        self.pbar.setStyleSheet("""
            .QProgressBar {
                border: 1px solid cyan;
                border-radius: 7px;
                text-align: center;
                background-color: rgb(0,0,0);
                }
            .QProgressBar::chunk {
                background-color: #05B8CC;
                }
            """)
        self.pbar2.setStyleSheet("""
            .QProgressBar {
                border: 1px solid cyan;
                border-radius: 7px;
                text-align: center;
                background-color: rgb(0,0,0);
                }
            .QProgressBar::chunk {
                background-color: rgb(255,0,0);
                }
            """)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar2.setGeometry(30, 70, 200, 25)
        self.btn = QPushButton('Start', self)
        self.btn.move(40, 100)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.timer2 = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        
        
    def timerEvent(self, e):
      
        minTemp = 37;
        maxTemp = 73;
        if self.step >= minTemp:
            
            self.timer.stop()
            self.btn.setText('Finished')
            return

        if self.step >= maxTemp:
            
            self.timer2.stop()
            self.btn.setText('Finished')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        self.pbar2.setValue(self.step)
        

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')

        if self.timer2.isActive():
            self.timer2.stop()
            self.btn.setText('Start')
        else:
            self.timer2.start(100, self)
            self.btn.setText('Stop')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())