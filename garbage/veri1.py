from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit
from PyQt5 import uic
from DB import DB

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi("veri1.ui")
        self.ilDoldur()
        self.win.btGonder.clicked.connect(self.kaydet)
        self.win.cmbIl.currentIndexChanged.connect(self.tespit)
        self.win.show()

    def kaydet(self):
        yazi = self.win.txtAd.text()
        db = DB()
        if db.ekleme(yazi) :
            self.win.lblSonuc.setText("Al rite")
        else:
            self.win.lblSonuc.setText("Nope")
        
    
    def ilDoldur(self):
        db = DB()
        liste  = db.ilListele()
        self.win.cmbIl.addItem("Seçiniz")
        for IlKod,IlAd in liste:
            self.win.cmbIl.addItem(IlAd)
    
    def tespit(self):
        self.win.txtAd.setText(str(self.win.cmbIl.currentIndex()))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())