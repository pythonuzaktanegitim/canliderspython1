import sys
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from DB import DB


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 örnek window'
        self.left = 60
        self.top =  70
        self.width = 320
        self.height = 240
        self.initUI()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.button = QPushButton("BT 1",self)
        self.button.clicked.connect(self.tiklandi)
        self.button.move(10,20)
        
        self.button1 = QPushButton("BT 2",self)
        self.button1.clicked.connect(self.tiklandi)
        self.button1.move(10,40)

        self.button2 = QPushButton("BT 3",self)
        self.button2.clicked.connect(self.tiklandi)
        self.button2.move(10,60)

        self.txtBox = QLineEdit(self)
        self.txtBox.move(10,80)
        self.txtBox.textChanged.connect(self.textControl)

        self.lbl = QLabel(self)
        self.lbl.move(10,100)

        self.show()

    def tiklandi(self):
        girilen =  self.txtBox.text()
        if self.sender() is self.button:
            self.lbl.setText(girilen)
        elif self.sender() is self.button1:
            self.lbl.setText(girilen*2)
        elif self.sender() is self.button2:
            self.lbl.setText(girilen*3)
        self.lbl.adjustSize()
        db = DB()
        db.ekleme(self.lbl.text())

    def textControl(self):
        girilen = self.txtBox.text()
        girilen = girilen.upper()
        self.txtBox.setText(girilen)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
