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
    def __init__(self,adisoyadi):
        super().__init__()
        self.win = uic.loadUi(r"arayuz\UI\kameraEgit.ui")
        self.win.btKamera.clicked.connect(self.kameraAc)
        self.win.btKapat.clicked.connect(self.Kapat)
        self.adisoyadi = adisoyadi
        self.timer = QTimer()
        self.devam = True




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
        face_cascade = cv2.CascadeClassifier("cascades\haarcascade_frontalface_default.xml")
        say = 0
        while 1:
            ret,frame = self.cap.read()
            # frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            
            buyumeFaktor = 1.0
            frame = cv2.resize(frame,None,fx=buyumeFaktor,fy=buyumeFaktor,interpolation=cv2.INTER_AREA)
            gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gri,1.1,5,minSize=(30,30))

            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                if (cv2.waitKey(1) & 0xFF == ord("e")):
                    path = os.getcwd()+os.sep+"dataset"+os.sep+self.adisoyadi
                    cv2.imwrite(path+os.sep+str(say)+".jpg",gri[y:y+h,x:x+w])
                    say += 1
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
        self.win.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    uyg = KameraEgit()
    uyg.win.show()
    sys.exit(app.exec_())
