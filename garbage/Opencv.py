import cv2
import numpy as np

# face_cascade = cv2.CascadeClassifier(r"C:\Users\vektorel\Documents\GitHub\Python15Desktop\haarcascade_frontalface_default.xml")

# img = cv2.imread('2.jpg')
# gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gri,1.5,6)

# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
# cv2.imshow('img',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)

while(1):
    try:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


        dus_red = np.array([30,150,50])
        yuk_red = np.array([255,255,180])

        mask = cv2.inRange(hsv,dus_red,yuk_red)
        res = cv2.bitwise_and(frame,frame,mask=mask)

        # kernel = np.ones((15,15),np.float32)/225

        # smoothed = cv2.filter2D(frame,-2,kernel)
       
        # blur = cv2.GaussianBlur(frame,(15,15),0)    

        # median = cv2.medianBlur(frame,15)

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('Res',res)
        # cv2.imshow('res1',blur)
        # cv2.imshow('res2',smoothed)
        # cv2.imshow('res3',median)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    except:
        break
cv2.destroyAllWindows()
cap.release()


# img = cv2.imread('indir.jpg')

# hsvColor = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# # grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # px = grayscaled[0:50,0:50]
# # print(px)
# # th = cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
# # retval ,th = cv2.threshold(hsvColor,20,255,cv2.THRESH_BINARY)

# dus_red = np.array([30,150,50])
# yuk_red = np.array([255,255,180])

# maske = cv2.inRange(hsvColor,dus_red,yuk_red)
# res = cv2.bitwise_and(img,img,mask=maske)

# cv2.imshow('resim',img)
# cv2.imshow('hsv',maske)
# cv2.imshow('hsv2',res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


