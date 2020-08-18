import cv2 
img =  cv2.imread(r"images\res1.jpg")
cv2.imshow("Resim",img)
print(img)
print("img",img.shape)

gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Siyah Beyaz",gri)
print(gri)
print("gri",gri.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()