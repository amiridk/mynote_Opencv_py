import os 
import cv2 

img = cv2.imread(os.path.join('.' , 'data' , 'sample_num.png'))

img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


# below this number would be 0 cuase of binary trsh
threshold = 80 

cap = 255

ret , img_thrs = cv2.threshold(img_gray , threshold  , cap , cv2.THRESH_BINARY)
img_thrs_adap = cv2.adaptiveThreshold(img_gray , cap , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY ,21,30)

cv2.imshow('gray ' , img_gray)
cv2.imshow('thrs' , img_thrs)
cv2.imshow('img_thrs_adap',img_thrs_adap)
cv2.waitKey(0)
cv2.destroyAllWindows()