import cv2
import numpy as np

img =  cv2.imread(r"images\res1.jpg",cv2.IMREAD_COLOR)

px = img[250:300,250:300]
img[350:400,350:400]= px
img[250:300,250:300] = [1,1,1]

cv2.imshow("Resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()