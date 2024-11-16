import os 
import cv2 


img = cv2.imread(os.path.join('.', 'basic_ops' , 'sample.png'))

cv2.imshow('img' , img)
print(img.shape)

croped = img[220 :740 ,320 :900 ]
cv2.imshow('croped',croped)

cv2.waitKey(0)