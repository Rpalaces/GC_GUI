import sys
from PyQt5.QtWidgets import (QApplication, QPushButton, QDialog, QProgressBar, QLabel,
                             QLineEdit, QVBoxLayout, QHBoxLayout, QGroupBox)
from PyQt5.QtCore import pyqtSlot, QBasicTimer
from PyQt5.QtGui import QIcon
from target_mactch import find_target, calculation, seq_find
from pcr_gui_class import primer, get_compliment, check_gc_clamps, calc_tm
from math import floor
class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("GC Percentage Calculation")
        self.setGeometry(30, 40, 520, 220)
        self.setWindowIcon(QIcon('icon.png'))     
        self.setStyleSheet("""
            QDialog {
            background-color: rgb(50,50,50);
            }
            """)
        
        self.seq_Input = QLineEdit(self)
        self.seq_Input.setStyleSheet("""
            QLineEdit {
            border: 1px solid cyan;
            color: rgb(255,255,255);
            background-color: rgb(50,50,50);
            }
            """)
        self.start_btn = QPushButton("Calculate", self)
        self.start_btn.setStyleSheet("""
            QPushButton {
            background-color: rgb(70,70,70);
            color: rgb(255,255,255);
            }
            """)
        self.togg_btn = QPushButton("Fahrenheit", self)
        self.togg_btn.setStyleSheet("""
            QPushButton {
            background-color: rgb(70,70,70);
            color: rgb(255,255,255);
            }
            """)
        self.togg_btn.setToolTip("Switch Between Metric and Imperial Units")
        self.togg_btn.setCheckable(True)
        self.togg_btn.clicked[bool].connect(self.changeUnits)
        self.labelPrime = QLabel("Primer:")
        self.labelPrime.setStyleSheet("""
            QLabel {
            color: rgb(255,255,255);
            }
            """)
        self.labelPrime2 = QLabel("Reverse Primer:")
        self.labelPrime2.setStyleSheet("""
            QLabel {
            color: rgb(255,255,255);
            }
            """)
        self.labelkbp = QLabel("Number of Kilobase Pairs:")
        self.labelkbp.setStyleSheet("""
            QLabel {
            color: rgb(255,255,255);
            }
            """)
        self.labelkbp2 = QLabel("Number of Kilobase Pairs:")
        self.labelkbp2.setStyleSheet("""
            QLabel {
            color: rgb(255,255,255);
            }
            """)
        self.labelGC = QLabel("GC Percentage:")
        self.labelGC.setStyleSheet("""
            QLabel {
            color: rgb(255,255,255);
            }
            """)
        self.labelGC2 = QLabel("GC Percentage:")
        self.labelGC2.setStyleSheet("""
            QLabel {
            color: rgb(255,255,255);
            }
            """)
        self.labelTM = QLabel("Temperature:")
        self.labelTM.setStyleSheet("""
            QLabel {
            color: rgb(255,255,255);
            }
            """)
        self.labelTM2 = QLabel("Temperature:")
        self.labelTM2.setStyleSheet("""
            QLabel {
            color: rgb(255,255,255);
            }
            """)
        self.pbar = QProgressBar(self)
        self.pbar2 = QProgressBar(self)
        self.pbar.setStyleSheet("""
            .QProgressBar {
                border: 1px solid cyan;
                border-radius: 7px;
                text-align: center;
                background-color: rgb(50,50,50);
                color: rgb(255,255,255);
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
                background-color: rgb(50,50,50);
                color: rgb(255,255,255);
                }
            .QProgressBar::chunk {
                background-color: #05B8CC;
                }
            """)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar2.setGeometry(30, 40, 200, 25)
        self.timer = QBasicTimer()
        self.step = 0
        self.step2 = 0
        # Create a horizontal layouts
        h_input = QHBoxLayout()
        h_input.addWidget(self.seq_Input)
        h_input.addWidget(self.start_btn)

        h_prime = QHBoxLayout()
        h_prime.addWidget(self.labelPrime)
        h_prime.addWidget(self.labelPrime2)

        h_kbp = QHBoxLayout()
        h_kbp.addWidget(self.labelkbp)
        h_kbp.addWidget(self.labelkbp2)

        h_gc = QHBoxLayout()
        h_gc.addWidget(self.labelGC)
        h_gc.addWidget(self.labelGC2)

        h_pbar = QHBoxLayout()
        h_pbar.addWidget(self.pbar)
        h_pbar.addWidget(self.pbar2)

        h_tm = QHBoxLayout()
        h_tm.addWidget(self.labelTM)
        h_tm.addWidget(self.labelTM2)
        h_tm.addWidget(self.togg_btn)

        #create vertical layout and add horizontal layouts
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_input)
        v_layout.addLayout(h_prime)
        v_layout.addLayout(h_kbp)
        v_layout.addLayout(h_gc)
        v_layout.addLayout(h_pbar)
        v_layout.addLayout(h_tm)

        # Set the layout
        self.setLayout(v_layout)

        # Connect the button to the start_clicked function
        self.start_btn.clicked.connect(self.start_clicked)
        
        # Display the window
        self.show()

    @pyqtSlot()
    def start_clicked(self):
        # Get the string from the text box
        box_text = self.seq_Input.text()
        sequence = seq_find(box_text)
        global gc_list
        gc_list = primer(sequence)
        global perc_one
        global perc_two
        perc_one = gc_list[0][2]
        perc_two = gc_list[1][2]
        #print(gc_list)
        #Changes labels
        prime = gc_list[0][0]
        rev_Prime = gc_list[1][0]
        kbp = (str(gc_list[0][1]))
        kbp2 = (str(gc_list[1][1]))
        tm = (str(gc_list[0][4]))
        tm2 = (str(gc_list[1][4]))
        self.labelPrime.setText(f'Primer: {prime}')
        self.labelPrime2.setText(f'Reverse Primer: {rev_Prime}')
        self.labelkbp.setText(f'Number of Kilobase Pairs: {kbp}')
        self.labelkbp2.setText(f'Number of Kilobase Pairs: {kbp2}')
        self.labelTM.setText(f'Temperature: {tm} Degrees Celsius')
        self.labelTM2.setText(f'Temperature: {tm2} Degrees Celsius')

        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)
    #timer used for progress bars
    def timerEvent(self, e):
        
        global perc_one
        global perc_two
        #adds to progressbar based on amount left to desired fullness
        if self.step < perc_one:
            if perc_one - self.step >= 10:
                self.step = self.step + 10
                self.pbar.setValue(self.step)
                #return
            elif perc_one - self.step < 10 and perc_one - self.step >= 5:
                self.step = self.step + 5
                self.pbar.setValue(self.step)
            elif perc_one - self.step < 5:
                self.step = self.step + 1
                self.pbar.setValue(self.step)

        if self.step2 < perc_two:
            if perc_two - self.step2 >= 10:
                self.step2 = self.step2 + 10
                self.pbar2.setValue(self.step2)
                #return
            elif perc_two - self.step2 <= 10 and perc_two - self.step2 >= 5:
                self.step2 = self.step2 + 5
                self.pbar2.setValue(self.step2)
            elif perc_two - self.step2 < 5:
                self.step2 = self.step2 + 1
                self.pbar2.setValue(self.step2)
        if self.step2 >= perc_two and self.step >= perc_one:

            self.timer.stop()
            return
#used to convert from metric to imperial and back
    def changeUnits(self, pressed):
        
        global gc_list
        source = self.sender()
        temp1 = gc_list[0][4]
        temp2 = gc_list[1][4]
        sttemp1 = str(temp1)
        sttemp2 = str(temp2)
        temp1a = floor(temp1 * 1.8 +32) 
        temp2a = floor(temp2 * 1.8 +32) 
        temp1a = str(temp1a)
        temp2a = str(temp2a)          
        if source.text() == "Fahrenheit":
            self.labelTM.setText(f'Temperature: {temp1a} Degrees Fahrenheit')
            self.labelTM2.setText(f'Temperature: {temp2a} Degrees Fahrenheit')
            self.togg_btn.setText('Celsius')
        elif source.text() == "Celsius":
            self.labelTM.setText(f'Temperature: {sttemp1} Degrees Celsius')
            self.labelTM2.setText(f'Temperature: {sttemp2} Degrees Celsius')
            self.togg_btn.setText('Fahrenheit')
      
        

my_app = QApplication(sys.argv)
a_window = MyWindow()
sys.exit(my_app.exec_())