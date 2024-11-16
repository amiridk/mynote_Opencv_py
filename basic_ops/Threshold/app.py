import os 
import cv2 

img = cv2.imread(os.path.join('.' , 'data' , 'sample_hum.png'))

img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


# below this number would be 0 cuase of binary trsh
threshold = 80 

cap = 255

ret , img_thrs = cv2.threshold(img_gray , threshold  , cap , cv2.THRESH_BINARY)


cv2.imshow('gray ' , img_gray)
cv2.imshow('thrs' , img_thrs)

cv2.waitKey(0)
cv2.destroyAllWindows()