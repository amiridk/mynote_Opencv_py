import os 
import cv2 
img = cv2.imread(os.path.join('.', 'basic_ops' , 'sample.png'))


resized = cv2.resize(img, (500,500))

cv2.imshow('img' , img)
cv2.imshow('resized' , resized)
print(img.shape)
print(resized.shape)
cv2.waitKey(0)