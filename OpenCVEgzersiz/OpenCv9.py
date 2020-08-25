import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(r"cascades\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(r"cascades\haarcascade_eye.xml")

cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    yuzler = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in yuzler:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    cv2.imshow("yuz",frame)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()


