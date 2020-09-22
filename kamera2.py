from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import cv2
from PyQt5.QtGui import QImage,QPixmap
from PIL import Image
import os,json
import numpy as np

class Kamera(QWidget):
    def __init__(self):
        super().__init__()
        self.widg = uic.loadUi("GUI\kamera.ui")
        self.timer = QTimer()
        self.adiSoyadi = None
        self.widg.btKapat.clicked.connect(self.kapat)
        self.widg.btKamera.clicked.connect(self.btClick)



    def kapat(self):
        self.cam.release()
        self.timer.stop()
        self.widg.close()


    def btClick(self):
        if not self.timer.isActive():
            self.cam = cv2.VideoCapture(1)
            self.timer.start(3)
            self.KameraAc()
        else:
            self.cam.release()
            self.timer.stop()

    def olustur(self):
        try:
            if self.adiSoyadi:
                os.mkdir(os.getcwd()+os.sep+"dataset"+os.sep+self.adiSoyadi)
        except Exception as hata:
            print(hata)



    def KameraAc(self):
        face_cascade = cv2.CascadeClassifier(
            "cascades\haarcascade_frontalface_default.xml")
        eye_cascade = cv2.CascadeClassifier("cascades\haarcascade_eye.xml")
        say = 0
        while 1:
            ret, frame = self.cam.read()
            buyumeFaktor = 1.0
            frame = cv2.resize(frame, None, fx=buyumeFaktor,
                               fy=buyumeFaktor, interpolation=cv2.INTER_AREA)

            #######################Tespit Etme##############################
            gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gri, 1.3, 5)

            for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    roi_gray = gri[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]
                    say += 1
                    path = os.getcwd()+os.sep+"dataset"+os.sep+self.adiSoyadi
                    cv2.imwrite(path+"\\"+str(say)+".jpg", gri[y:y+h, x:x+w])
                    eyes = eye_cascade.detectMultiScale(roi_gray)
                    for (ex, ey, ew, eh) in eyes:
                            cv2.rectangle(roi_color, (ex, ey),
                                          (ex+ew, ey+eh), (255, 0, 0), 2)
            ###################################################################

            ############Yansıtma###################################
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            step = channel*width
            qImg = QImage(frame.data, width, height,
                          step, QImage.Format_RGB888)
            self.widg.kamera.setPixmap(QPixmap.fromImage(qImg))
            ####################################################
            k = cv2.waitKey(100) & 0xFF
            if k == 27:
                break
            elif say >= 50:
                break

        self.cam.release()
        self.timer.stop()
        egitim = Egitim()
        egitim.egit()
        self.widg.close()



class Egitim():

    def __init__(self):
        self.yol = 'dataset'
        self.tani = cv2.face.LBPHFaceRecognizer_create()
        self.detector = cv2.CascadeClassifier("cascades\haarcascade_frontalface_default.xml")

    def getImageAndLabels(self):
        faceSamples = []
        ids = []
        labels = []
        folders = os.listdir(self.yol)
        dictionary = {}

        for i,kl in enumerate(folders):
            dictionary[kl]=int(i)

        f = open("ids.json","w")
        a = json.dump(dictionary,f)
        f.close()

        for kl in folders:
            for res in os.listdir(os.path.join(yol,kl)):
                PIL_img = Image.open(os.path.join(yol,kl,res)).convert('L')
                img_numpy = np.array(PIL_img,'uint8')
                id = int(dictionary[kl])
                faces = detector.detectMultiScale(img_numpy)
                for (x,y,w,h) in faces:
                    faceSamples.append(img_numpy[y:y+h,x:x+w])
                    ids.append(id)
        return faceSamples,ids

    def egit(self):
        faces,ids = self.getImageAndLabels(self.yol)
        tani.train(faces,np.array(ids))
        tani.write('trainer.yml')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ex = Kamera()
    ex.widg.show()
    sys.exit(app.exec_())
