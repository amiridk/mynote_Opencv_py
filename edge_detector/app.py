import os 
import cv2 
import numpy as np
img = cv2.imread(os.path.join('.' , 'data' , 'sample_hum.png'))

min = 50
max = 100

img_edge = cv2.Canny(img , min ,max)

img_edge_d = cv2.dilate(img_edge , np.ones((3,3) , dtype=np.int8) )
img_edge_e = cv2.erode(img_edge_d , np.ones((3,3) , dtype=np.int8))


cv2.imshow('orginal' , img)
cv2.imshow('edges' , img_edge)
cv2.imshow('img_edge_d' , img_edge_d)
cv2.imshow('img_edge_e' , img_edge_e)




cv2.waitKey(0)
cv2.destroyAllWindows()