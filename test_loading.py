import cv2
import numpy
import os 
from datetime import datetime


# 로버츠(Roberts) 마스크
# 프리윗(Prewitt) 마스크
# 소벨(Sobel) 마스크
# 라플라시안 에지 검출
# 캐니 에지 검출 (default)
# gif max frame 은 200  fps 32로 하고 진행 
# 영상으로 ,,, ?


# Setting 

    ## 이미지 가져오기 
BASE_IMG_PATH = "./images"
img_name = "human0.png"
BASE_OUT_PATH  = "./outputs"

    ## timestamp 
timestamp = datetime.now().strftime("%m%d%H%M%S")





def test_canny():
    # canny test for image -> image 1 
    '''
    최소 임계값: 엣지 검출 결과에 영향을 미치는 가장 작은 값입니다. 이 값보다 작은 엣지는 검출되지 않습니다.
    최대 임계값: 엣지 검출 결과에 영향을 미치는 가장 큰 값입니다. 이 값보다 큰 엣지는 검출되지 않습니다.
    임계값은 이미지에 따라 다르게 선택될 수 있습니다. 일반적으로는 다음과 같은 범위를 사용합니다:

    최소 임계값: 0 ~ 100
    최대 임계값: 100 ~ 200
    '''

    # image load
    image = cv2.imread(os.path.join(BASE_IMG_PATH,img_name),cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("Image not found error, please check image path")

    # canny parameters setting 
    th1 = 0
    th2 = 0
    # make image with canny 
    canny1 = cv2.Canny(image, th1, th2) # OpenCV 캐니 에지

    # set output path & image name 
    result_name = f'output_canny_{timestamp}.png'
    result_path = os.path.join(BASE_OUT_PATH,result_name)

    # make output path if path not exists
    if not os.path.exists(os.path.dirname(BASE_OUT_PATH)):
        os.makedirs(os.path.dirname(BASE_OUT_PATH))

    # save image file 
    cv2.imwrite(result_path,canny1)
    print("complete saving image")


    assert os.path.exists(result_path) == True


# def test_roberts():


#     assert True

# def test_sobel():

#     assert 1 

# def test_prewitt():

#     assert 1

# def test_laplacian():

#     assert 1
