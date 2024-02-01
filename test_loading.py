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
    # TODO : 임계값 조절해서 24 fps -> 10 초 240장 
    # TODO : 240장을 영상으로 만들기 
    # TODO : 240장을 GIF로 만들기 
    '''
    (1000,1000)에서 시작 --> 100씩 th1부터 100씩 th2와 번갈아서 100씩 내린다 .(200,200)에서 스탑 


    '''

    # image load
    image = cv2.imread(os.path.join(BASE_IMG_PATH,img_name),cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("Image not found error, please check image path")
    cnt = 0

    for th in range(1000,0,-10):
        # canny parameters setting
        max_th = th     # 0~ 200 까지 200장
        min_th = 400 

        # make image with canny
        canny1 = cv2.Canny(image, threshold1=min_th, threshold2=max_th) # OpenCV 캐니 에지

        cnt += 1 

        # set output path & image name 
        result_name = f'output_canny_{cnt}.png'
        result_path = os.path.join(BASE_OUT_PATH,result_name)

        # make output path if path not exists
        if not os.path.exists(os.path.dirname(BASE_OUT_PATH)):
            os.makedirs(os.path.dirname(BASE_OUT_PATH))

        # save image file 
        cv2.imwrite(result_path,canny1)
        print(f"complete saving image{cnt}")


    assert os.path.exists(result_path) == True


# def test_roberts():


#     assert True

# def test_sobel():

#     assert 1 

# def test_prewitt():

#     assert 1

# def test_laplacian():

#     assert 1
