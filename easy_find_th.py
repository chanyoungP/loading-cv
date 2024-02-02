'''
Threshold 값을 쉽게 찾기 위해서 openCV 윈도우와 트랙바를 활용하는 코드
값을 찾기 위한 코드로 실제 서비스에서는 필요하지 않음.
'''

import cv2
import numpy as np
import os 
from datetime import datetime


BASE_IMG_PATH = "./images"
img_name = "human0.png"
BASE_OUT_PATH  = "./outputs"

# image load
image = cv2.imread(os.path.join(BASE_IMG_PATH,img_name),cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("Image not found error, please check image path")

def canny_find_th(image):

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

def sobel_find_th(image):
# sobel은 weight_th 와 add_th 두 개가 있는데 확인 결과 weight th는 0~1로 가야할거 같고 add_th는 제거 
    # x 방향 100장 y방향 100장 따로따로 해야할 듯 
    def nothing(x):
        pass

    cv2.namedWindow('image')
    cv2.createTrackbar('weight_th_x', 'image', 0, 100, nothing)
    cv2.createTrackbar('weight_th_y', 'image', 0, 100, nothing)

    while True:
        weight_th_x = cv2.getTrackbarPos('weight_th_x', 'image') / 100
        weight_th_y = cv2.getTrackbarPos('weight_th_y', 'image') / 100

        # x방향 미분 - 수직 마스크, ksize는 커널의 크기
        dst1 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, scale=weight_th_x,delta=1, ksize = 3)
        # y방향 미분 - 수평 마스크
        dst2 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, scale=weight_th_y, delta=1, ksize = 3) 
        dst1 = cv2.convertScaleAbs(dst1) # 절댓값 및 uint8 변환
        dst2 = cv2.convertScaleAbs(dst2)
        
        # 두 이미지 합치기
        merged_image = cv2.addWeighted(dst1, 0.5, dst2, 0.5, 0)

        cv2.imshow('image', merged_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()




sobel_find_th(image=image)
