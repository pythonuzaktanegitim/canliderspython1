from tools.iban import DogrulamaTool
from PyQt5.QtWidgets import QApplication, \
    QWidget,QPushButton, QLineEdit, QLabel


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
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.bt1 = QPushButton("Doğrulama",self)
        self.bt1.setGeometry(10,20,60,20)

        self.txtIban = QLineEdit(self)
        self.txtIban.setGeometry(10,60,100,20)

        self.lblSonuc = QLabel(self)
        self.lblSonuc.setGeometry(10,90,100,20)

        self.bt1.clicked.connect(self.dogrula)
        self.show()
    
    def dogrula(self):
        iban = self.txtIban.text()
        arac1 = DogrulamaTool(iban)
        if arac1.ibanDogrulama():
            self.lblSonuc.setText("IBAN Doğru")
        else:
            self.lblSonuc.setText("IBAN Yanlış")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())