import cv2
import numpy as np

cap = cv2.VideoCapture(1) # birden fazla kamera olduğu için 1 yoksa 0
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow("frame",gray)
    
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()

