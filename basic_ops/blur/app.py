import os 
import cv2  

img = cv2.imread(os.path.join('.' ,'data' ,'sample_hum.png'))

k_size = 16

blury_img = cv2.blur(img ,(k_size , k_size))
# more_advanced_blur = cv2.GaussianBlur(img , (k_size , k_size) , 1)
# img_median = cv2.medianBlur(img , k_size)
cv2.imshow('orginal' , img)
cv2.imshow('blury' , blury_img)
# cv2.imshow('advanced' , more_advanced_blur)
# cv2.imshow('median' , img_median)
cv2.waitKey(0)