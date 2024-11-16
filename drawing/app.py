import os 
import cv2 

img = cv2.imread(os.path.join('.' , 'data' , 'sample_whiteb.png'))

line_start = (100,150)
line_end = (300 , 450)
line_color = (0,255,0)
thic = 3
cv2.line(img ,line_start ,line_end,line_color,thic)


cv2.rectangle(img , (200,300) , (450 , 650),(0,0,255),5)

cv2.circle(img , (500,550),15 ,(255,0,0),3)

cv2.putText(img , 'hihiihha' ,(700 , 300) , cv2.FONT_HERSHEY_SIMPLEX ,2 ,(255,100,0) ,2)


cv2.imshow('orginal' , img)

cv2.waitKey(0)
cv2.destroyAllWindows()