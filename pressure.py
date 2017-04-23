import threading
import sys, time
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import psutil
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
	# create vbox
        self.main_layout = QVBoxLayout()
	# create run button
        run_button = QPushButton("Run")
        run_button.clicked.connect(self.run)      
        self.main_layout.addWidget(run_button)
	# create cancel button
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel)      
        self.main_layout.addWidget(cancel_button)
	# font
        font = QFont()
        font.setPointSize(32) 
        font.bold()
	# pressure label
	pressureLabel = QLabel()
        pressureLabel.setFont(font)
        pressureLabel.setAlignment(Qt.AlignCenter)
	self.main_layout.addWidget(pressureLabel)
	
	central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

    def myEvenListener(self,stop_event):
        state = True
	testingCount = 0.231321321321
        while state and not stop_event.isSet():
	    testingCount = testingCount + .03213 
	    self.main_layout.itemAt(2).widget().setText(str(testingCount) + " kPa")
            time.sleep(1)
    # start the thread
    def run(self):
        self.stop_event=threading.Event()
        self.c_thread=threading.Thread(target=self.myEvenListener, args=(self.stop_event,))
        self.c_thread.start()       
    # end the thread
    def cancel(self):
        self.stop_event.set()
        self.close()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(640, 480)
    window.setWindowTitle("Well pressure level detection")
    window.show()
    app.exec_()

main()

def kill_proc_tree(pid, including_parent=True):    
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()

me = os.getpid()
kill_proc_tree(me)
