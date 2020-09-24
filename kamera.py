from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import cv2
from PyQt5.QtGui import QImage,QPixmap
import numpy as np
from PIL import Image
import os,json


class Kamera(QWidget):
    def __init__(self):
        super().__init__()
        self.widg = uic.loadUi("GUI\kamera.ui")
        self.timer = QTimer()
        self.widg.btKapat.clicked.connect(self.kapat)
        self.widg.btKamera.clicked.connect(self.btClick)

    def kapat(self):
        self.cam.release()
        self.timer.stop()
        self.widg.close()



    def btClick(self):
        if not self.timer.isActive():
            self.cam = cv2.VideoCapture(0)
            self.timer.start(3)
            self.KameraAc()
        else:
            self.cam.release()
            self.timer.stop()

        

    def KameraAc(self):
        tani = cv2.face.LBPHFaceRecognizer_create()
        tani.read('trainer.yml')
        detector = cv2.CascadeClassifier("cascades\haarcascade_frontalface_default.xml")
        font = cv2.FONT_HERSHEY_SIMPLEX
        id = 0
        dictionary = {}
        names = []
        dosya = open('ids.json',"r")
        dictionary = json.load(dosya)

        face_cascade = cv2.CascadeClassifier("cascades\haarcascade_frontalface_default.xml")
        eye_cascade = cv2.CascadeClassifier("cascades\haarcascade_eye.xml")
        while 1:
            ret,frame = self.cam.read()
            buyumeFaktor = 1.0
            frame = cv2.resize(frame,None,fx=buyumeFaktor,
            fy=buyumeFaktor,interpolation=cv2.INTER_AREA)
            
            #######################Tespit Etme##############################
            gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gri,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

            for (x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    # roi_gray = gri[y:y+h,x:x+w]
                    # roi_color = frame[y:y+h,x:x+w]
                    # eyes = eye_cascade.detectMultiScale(roi_gray)

                    id,oran = tani.predict(gri[y:y+h,x:x+w])
                    print(id)

                    if oran>70:
                        id = names[id]
                    else:
                        id = "Bilinmiyor"

                    cv2.putText(frame,str(id),(x+5,y-5),font,1,(255,255,255),2)

                    # for (ex,ey,ew,eh) in eyes:
                    #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
            ###################################################################

            ############Yansıtma###################################
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            height,width,channel = frame.shape
            step = channel*width
            qImg = QImage(frame.data,width,height,step,QImage.Format_RGB888)
            self.widg.kamera.setPixmap(QPixmap.fromImage(qImg))
            ####################################################
            k = cv2.waitKey(100) & 0xFF
            if k == 27:
                break

        self.cam.release()
        self.timer.stop()


class Tanima():
    def __init__(self):
        self.tani = cv2.face.LBPHFaceRecognizer_create()
        self.tani.read('trainer.yml')
        self.detector = cv2.CascadeClassifier("cascades\haarcascade_frontalface_default.xml")


    def tani(self):
        font = cv2.FONT_HERSHEY_SIMPLEX
        id = 0

        dictionary = {}
        names = []
        dosya = open('ids.json',"r")
        dictionary = json.load(dosya)
        cam = cv2.VideoCapture(0)

        for key,values in dictionary.items():
            names.append(key)

        while True:
            ret,cerceve = cam.read()
            cerceve = cv2.flip(cerceve,1)
            gri = cv2.cvtColor(cerceve,cv2.COLOR_BGR2GRAY)

            faces = detector.detectMultiScale(gri,scaleFactor=1.5,minNeighbors=5)
            for (x,y,w,h) in faces:
                cv2.rectangle(cerceve,(x,y),(x+w,y+h),(0,255,0),2)
                id,oran = tani.predict(gri[y:y+h,x:x+w])
                print(id)

                if oran<70:
                    id = names[id]
                else:
                    id = "Bilinmiyor"

                cv2.putText(cerceve,str(id),(x+5,y-5),font,1,(255,255,255),2)
            cv2.imshow('KAmera',cerceve)
            k = cv2.waitKey(100) & 0xFF
            if k == 27:
                break
            
        cam.release()
        cv2.destroyAllWindows()    


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Kamera()
    ex.widg.show()
    sys.exit(app.exec_())