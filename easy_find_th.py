import cv2
import numpy
import os 
from datetime import datetime


BASE_IMG_PATH = "./images"
img_name = "human0.png"
BASE_OUT_PATH  = "./outputs"

# image load
image = cv2.imread(os.path.join(BASE_IMG_PATH,img_name),cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Image not found error, please check image path")




import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('threshold1', 'image', 100, 1000, nothing)
cv2.createTrackbar('threshold2', 'image', 100, 1000, nothing)

while True:
    threshold1 = cv2.getTrackbarPos('threshold1', 'image')
    threshold2 = cv2.getTrackbarPos('threshold2', 'image')

    edges = cv2.Canny(image, threshold1, threshold2)

    cv2.imshow('image', edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()


'''
th1 은 무조건 큰 값에서 살짝 내리고 
th2 도 무조건 큰 값에서 살짝 내리고 

'''