import cv2 
img =  cv2.imread(r"images\bookpage.jpg")



cv2.imshow("Resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()