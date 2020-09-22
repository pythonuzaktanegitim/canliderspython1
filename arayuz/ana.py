import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import cv2
from PyQt5.QtGui import QImage,QPixmap
import numpy as np
from PIL import Image
import os
from kameraEgit import KameraEgit


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi(r"arayuz\UI\ana.ui",self)
        self.kaydet.clicked.connect(self.klasorAc)
        self.temizle.clicked.connect(self._temizle)
        self.egitim.clicked.connect(self.Kegit)
        self.show()


    def klasorAc(self):
        try:
            os.mkdir(rf"dataset\{self.txtadi.text()}_{self.txtsoyadi.text()}")
            QMessageBox.information(self,"Bilgi","Klasör Oluşturuldu",QMessageBox.Ok)
            egitKamera = KameraEgit(f"{self.txtadi.text()}_{self.txtsoyadi.text()}")
            egitKamera.win.show()
        except FileExistsError:
            QMessageBox.warning(self,"Kayıt Hatası","Bu kayıt zaten var",QMessageBox.Ok)

    def _temizle(self):
        self.txtadi.setText("")
        self.txtsoyadi.setText("")

    def Kegit(self):
        egitKamera = KameraEgit()
        egitKamera.win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyg = App()
    sys.exit(app.exec_())
