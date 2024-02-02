'''
Test code for loading window content using openCV edge detection algorithm 
input : original image 
- edge detection to multiple thresholds -> detected gray scale images
- transform into gif file 
output : gif file 
'''
from utils import *

# TODO : 로버츠(Roberts) 마스크
# TODO : 프리윗(Prewitt) 마스크
# TODO : 소벨(Sobel) 마스크
# TODO : 라플라시안 에지 검출
# TODO : Canny 함수화 


BASE_IMG_PATH = "./images"
BASE_OUT_PATH  = "./outputs"

# your image file name 
img_name = "landscape0.png"


# def test_loading():
    
#     input_img_path = os.path.join(BASE_IMG_PATH,img_name)
#     out_vid_path = os.path.join(BASE_OUT_PATH,img_name.split('.')[0]+'.gif')
        
#     img = load_img(img_dir = input_img_path)
#     frames = make_frames(image = img, method = "canny")
#     flag = save_gif_file(frames = frames, save_dir = out_vid_path)

#     assert flag


def test_sobel_mask():
    input_img_path = os.path.join(BASE_IMG_PATH,img_name)
    out_vid_path = os.path.join(BASE_OUT_PATH,img_name.split('.')[0]+'.gif')
    img = load_img(img_dir=input_img_path)
    # ---------------------- implement sobel mask ----------------

    # OpenCV 제공 소벨 에지 계산
    # x방향 미분 - 수직 마스크, ksize는 커널의 크기
    dst1 = cv2.Sobel(np.float32(img), cv2.CV_32F, 1, 0, scale=1, ksize = 3)
    # y방향 미분 - 수평 마스크
    dst2 = cv2.Sobel(np.float32(img), cv2.CV_32F, 0, 1, scale=1, ksize = 3) 
    dst1 = cv2.convertScaleAbs(dst1) # 절댓값 및 uint8 변환
    dst2 = cv2.convertScaleAbs(dst2)

    # 두 이미지 합치기
    merged_image = cv2.addWeighted(dst1, 0.5, dst2, 0.5, 0)
    cv2.imwrite('./outputs/sobel.png', merged_image)

    assert os.path.exists('./outputs/sobel.png') == True