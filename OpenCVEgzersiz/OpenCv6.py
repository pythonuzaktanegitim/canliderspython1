import cv2
import numpy as np
# img = cv2.imread(r"images\res1.jpg")
# kernel = np.ones((15,15),np.float32)/225
# smooth = cv2.filter2D(img,-1,kernel)
# blur = cv2.GaussianBlur(img,(15,15),0)
# cv2.imshow("efekt",smooth)
# cv2.imshow("blur",blur)
# cv2.imshow("orjinal",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

cap = cv2.VideoCapture(1) # birden fazla kamera olduğu için 1 yoksa 0
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((15,15),np.float32)/225
    smooth = cv2.filter2D(frame,-1,kernel)
    blur = cv2.GaussianBlur(frame,(15,15),0)
    median = cv2.medianBlur(frame,15)


    cv2.imshow("frame",frame)
    
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
