import cv2
import numpy as np
# cap = cv2.VideoCapture("videooo.mp4")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
cap = cv2.VideoCapture(0)

while(1):
    try:
        _, frame = cap.read()
#####################################
        gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gri,1.3,5)

        for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                roi_gray = gri[y:y+h,x:x+w]
                roi_color = frame[y:y+h,x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

        cv2.imshow("Res",frame)
####################################
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    except:
        break
cv2.destroyAllWindows()
cap.release()
