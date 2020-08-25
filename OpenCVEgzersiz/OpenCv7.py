import cv2
import numpy as np

cap = cv2.VideoCapture(1) # birden fazla kamera olduğu için 1 yoksa 0
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    template = cv2.imread("ekran.jpg",cv2.IMREAD_GRAYSCALE)
    w,h = template.shape[::-1]
    
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    th = 0.5
    loc = np.where(res>=th)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,255,255),1)

    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
