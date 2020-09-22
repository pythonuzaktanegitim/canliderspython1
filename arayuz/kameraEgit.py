import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import QTimer
from PyQt5 import uic
import cv2
from PyQt5.QtGui import QImage,QPixmap
import numpy as np
from PIL import Image
import os


class KameraEgit(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.devam = True
        self.initUI()

    def initUI(self):
        self.win = uic.loadUi(r"arayuz\UI\kameraTanit.ui")
        self.win.btKamera.clicked.connect(self.kameraAc)
        self.win.btKapat.clicked.connect(self.Kapat)
        


    def kameraAc(self):
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(1)
            self.timer.start(3)
            self.Kamera()
        else:
            self.cap.release()
            self.timer.stop()
        

    def Kapat(self):
        if self.timer.isActive():
            self.devam = False

    def Kamera(self):
        while self.devam:
            ret,frame = self.cap.read()
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            height,width,channel = frame.shape  # (1024,768,3)
            step = channel*width
            qImg = QImage(frame.data,width,height,step,QImage.Format_RGB888)
            self.win.lblKamera.setPixmap(QPixmap.fromImage(qImg))

            if (cv2.waitKey(1) & 0xFF == ord("ç")):
                break

        self.win.lblKamera.setText("")
        self.cap.release()
        self.timer.stop()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyg = KameraEgit()
    uyg.show()
    sys.exit(app.exec_())
