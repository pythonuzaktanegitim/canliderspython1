import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,pyqtSignal
from PyQt5 import uic,QtGui,QtCore
from DB import DB

class App(QMainWindow):
    def __init__(self):
        self.win = uic.loadUi(r"GUI\Odev.ui")
        self.iniUI()

    def iniUI(self):
        self.win.button1.clicked.connect(self.tiklandi)
        self.win.show()

    @pyqtSlot()
    def tiklandi(self):
        self.win.lbl.setText("aaaa")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())