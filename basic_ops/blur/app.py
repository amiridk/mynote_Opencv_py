import os 
import cv2  

img = cv2.imread(os.path.join('.' ,'data' ,'sample_hum.png'))

k_size = 7

blury_img = cv2.blur(k_size , k_size)

cv2.imshow('orginal' , img)

cv2.waitKey(0)