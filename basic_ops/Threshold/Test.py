import cv2
import easyocr
import matplotlib.pyplot as plt
import os
# Set Tesseract configs for Farsi


img = cv2.imread(os.path.join('.' , 'data' , 'sample_num.png'))

img_gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


# below this number would be 0 cuase of binary trsh
threshold = 80 

cap = 255

ret , img_thrs = cv2.threshold(img_gray , threshold  , cap , cv2.THRESH_BINARY)
img_thrs_adap = cv2.adaptiveThreshold(img_gray , cap , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY ,21,30)


img = img_thrs


reader = easyocr.Reader(['fa'], gpu=False)

text_detections = reader.readtext(img)
threshold = 0.25

# Function to draw bounding boxes around detected text
def draw_bounding_boxes(image, detections, threshold=0.25):
    for bbox, text, score in detections:
        if score > threshold:
            cv2.rectangle(image, tuple(map(int, bbox[0])), tuple(map(int, bbox[2])), (0, 255, 0), 5)
            cv2.putText(image, text, tuple(map(int, bbox[0])), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.65, (255, 0, 0), 2)

# Draw bounding boxes on the image
draw_bounding_boxes(img, text_detections, threshold)

# Display the image with detected text
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGBA))
plt.axis('off')  # Hide axes
plt.show()