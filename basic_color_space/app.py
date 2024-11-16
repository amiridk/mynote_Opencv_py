import os 
import cv2

img = cv2.imread(os.path.join('.','basic_color_space' , 'sample.png'))

# BGR2RGB can be switch to gray or HSV or ...

img_rgb=cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

cv2.imshow('img' , img)
cv2.imshow('rgb',img_rgb)
cv2.waitKey(0)
