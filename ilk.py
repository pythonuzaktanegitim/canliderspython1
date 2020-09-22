from PyQt5.QtWidgets import QApplication,QMainWindow,QLineEdit,QMessageBox
from PyQt5 import uic
from DB import DB
from kamera import Kamera as cam2
from kamera2 import Kamera as cam1

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.win = uic.loadUi(r"GUI\ilk.ui")
        self.ilDoldur()
        self.win.cmbIL.currentIndexChanged.connect(self.ilceDoldur)
        self.win.btKaydet.clicked.connect(self.kaydet)
        self.win.btKamera.clicked.connect(self.kameraAc)
        self.win.btKamera_2.clicked.connect(self.kameraAc2)
        self.cam = cam1()
        self.cam2 = cam2()
        self.win.show()
       

    def ilceDoldur(self):
        db = DB()
        self.win.cmbILCE.clear()
        liste = db.ilceListele(self.win.cmbIL.currentIndex())
        self.win.cmbILCE.addItem("Seçiniz")
        for IlceKod,IlceAd in liste:
            self.win.cmbILCE.addItem(IlceAd)
        

    def kameraAc(self):
        self.cam.adiSoyadi = self.adi+"_"+self.soyadi
        self.cam.olustur()
        self.cam.widg.show()
       
    def kameraAc2(self):
        self.cam2.widg.show()
       


    def ilDoldur(self):
        db = DB()
        liste  = db.ilListele()
        self.win.cmbIL.addItem("Seçiniz")
        for IlKod,IlAd in liste:
            self.win.cmbIL.addItem(IlAd)

    def kaydet(self):
        self.adi = self.win.txtAdi.text()
        self.soyadi = self.win.txtSoyadi.text()                            
        il = self.win.cmbIL.currentIndex()
        ilce = self.win.cmbILCE.currentIndex()
        db = DB()
        if db.PersonelEkleme(self.adi,self.soyadi,il,ilce):
            QMessageBox.information(self,"Bilgi","Bilgileriniz başarıyla kaydedildi")
            self.win.btKamera.setEnabled(True)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())