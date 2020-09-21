import cv2 
img =  cv2.imread(r"images\res1.jpg")
cv2.line(img,(50,50),(150,150),(255,100,100),7)
cv2.rectangle(img,(50,50),(150,150),(255,120,100),3)
cv2.circle(img,(100,100),55,(255,120,100),-1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Uzaktan Egitim",(50,50),font,1,(200,255,155),2,cv2.LINE_AA)

cv2.imshow("Resim",img)
cv2.waitKey(0)
cv2.destroyAllWindows()