'''
Test code for loading window content using openCV edge detection algorithm 
input : original image 
- edge detection to multiple thresholds -> detected gray scale images
- transform into gif file 
output : gif file 
'''
import cv2
import numpy
import os 
import imageio

# TODO : 로버츠(Roberts) 마스크
# TODO : 프리윗(Prewitt) 마스크
# TODO : 소벨(Sobel) 마스크
# TODO : 라플라시안 에지 검출



##############################
########### SETTING ##########
##############################

## Set default path 
BASE_IMG_PATH = "./images"
BASE_OUT_PATH  = "./outputs"

# your image file name 
img_name = "human0.png"


##############################
########### CANNY TEST #######
##############################

def test_canny():

    # image load
    image = cv2.imread(os.path.join(BASE_IMG_PATH,img_name),cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("Image not found error, please check image path")

    cnt = 0
    min_th = 1000 
    max_th = 1000

    vid_frames = []
#    (1000,1000)에서 시작 --> 100씩 th1부터 100씩 th2와 번갈아서 100씩 내린다 .(200,200)에서 스탑 
    while min_th > 200 or max_th > 200:
    # canny parameters setting

        # make image with canny
        canny1 = cv2.Canny(image, threshold1=min_th, threshold2=max_th) # OpenCV 캐니 에지
        vid_frames.append(canny1)

        cnt += 1 
        # 1,2 둘다 1000에서 시작 (900, 1000) -> (900, 900) -> (800,900)
        if cnt % 2 == 1: # 홀수번째, th1 감소 
            min_th -= 10
        elif cnt % 2 == 0:
            max_th -= 10

        # # set output path & image name 
        # result_name = f'output_canny_{cnt}.png'
        # result_path = os.path.join(BASE_OUT_PATH, result_name)

        # # make output path if path not exists
        # if not os.path.exists(os.path.dirname(BASE_OUT_PATH)):
        #     os.makedirs(os.path.dirname(BASE_OUT_PATH))

        # # save image file 
        # cv2.imwrite(result_path,canny1)
        # print(f"complete saving image{cnt}")
        # print(f"th1 {min_th} th2 {max_th}")

    #Set output gif path
    out_vid_path = os.path.join(BASE_OUT_PATH,img_name.split('.')[0]+'.gif')

    # make output path if path not exists
    if not os.path.exists(os.path.dirname(BASE_OUT_PATH)):
        os.makedirs(os.path.dirname(BASE_OUT_PATH))

    # saving gif file 
    print("Saving GIF file")
    with imageio.get_writer(out_vid_path, mode="I") as writer: # mode : A string containing the modes that this format can handle ('iIvV'),“i” for an image, “I”
        for frame in vid_frames:
            writer.append_data(frame) # save frame to gif

        
    assert os.path.exists(out_vid_path) == True


# def test_roberts():


#     assert True

# def test_sobel():

#     assert 1 

# def test_prewitt():

#     assert 1

# def test_laplacian():

#     assert 1
