import backend
from PyQt5 import QtWidgets,uic
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()
        #add atitle
        self.setWindowTitle('Ferrari location')
        
        #set vertical layout
        self.setLayout(QtWidgets.QVBoxLayout())
        
        
        self.show()
        



app = QtWidgets.QApplication([])

mainWin=MainWindow()






