import cv2 
import os 
import mediapipe as mp
# import argparse

def process_image(img , face_detection):
    H ,W , _ = img.shape
    img_rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    if out.detections is not None : 
        for detection in out.detections:
            location_data = detection.location_data 
            bbox = location_data.relative_bounding_box
            x1,y1,w,h = bbox.xmin ,bbox.ymin , bbox.width  , bbox.height

        x1 = int(x1 * W)
        y1 = int(y1 * H)
        w = int(w * W)
        h = int(h * H)
            
            
        img[y1:y1+h , x1:x1+w,:] = cv2.blur(img[y1:y1+h , x1:x1+w,:] , (50,50) )
    return img


# arggs=argparse.ArgumentParser()
# arggs.add_argument('--model',default='image')




mp_face_detection = mp.solutions.face_detection


with mp_face_detection.FaceDetection(min_detection_confidence =0.4 , model_selection=0) as face_detection :
   cap = cv2.VideoCapture(0)
   
   while True:
       ret,frame=cap.read()
       frame = process_image(frame , face_detection)
       cv2.imshow('frame' , frame)
       
       if cv2.waitKey(1) & 0xff == ord('q'):
           break
         
   
cap.release()        