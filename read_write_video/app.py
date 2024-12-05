import cv2
import os

video_path = os.path.join('.' , 'read_write_video' , 'sample.mp4')

video= cv2.VideoCapture(video_path)

ret= True

while ret :
    ret , frame =video.read()
    if ret:
        cv2.imshow('frame_video' , frame)
        cv2.waitKey(125)
video.release()
cv2.destroyAllWindows()