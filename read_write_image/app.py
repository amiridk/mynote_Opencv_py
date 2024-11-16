import os
import cv2

img_path = os.path.join('.' , 'read_write_image' , 'sample.png')

img = cv2.imread(img_path)

cv2.imwrite(os.path.join('.' , 'read_write_image' ,'sample_out.png'),img)

cv2.imshow("frame" , img)

cv2.waitKey(0)

