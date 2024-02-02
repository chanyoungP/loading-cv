# Edge detection algorithm : Canny 
# source file 
import cv2
import os 
import imageio
import numpy as np

def load_img(img_dir):
    '''
    input : your image file directory 
    output : opencv image 
    '''
    # image load
    image = cv2.imread(img_dir,cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("Image not found error, please check image path")

    return image

def sobel_make(image, growth_rate = 0.01, back_ground = "white"):
    '''
    - sobel has one threshold that is a scale parameter 
    - we set scale parameter's range 0~1 
    - growth_rate 0.01
    - we have x-direction , y-direction images so we have 200 images to make gif
    '''
    
    # ------------- setting -----------
    cnt = 0
    weight_x = 0
    weight_y = 0
    vid_frames = []
    # ------------- sobel  -----------
    while weight_x < 1 or weight_y < 1:

    # OpenCV 제공 소벨 에지 계산    
        # x-direction differentiation - vertical mask
        dst1 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, scale=weight_x, ksize = 3)
        # y-direction differentiation - horizontal mask
        dst2 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, scale=weight_y, ksize = 3) 
        
        # --> Convert absolute value and uint8 
        dst1 = cv2.convertScaleAbs(dst1)
        dst2 = cv2.convertScaleAbs(dst2)

        # combine x-direction, y-direction mask iamge
        merged_image = cv2.addWeighted(dst1, 0.5, dst2, 0.5, 0)
        
        # count image
        cnt += 1
        
        # check back ground color and change 
        if back_ground == 'white':
            sobel_inverted = cv2.bitwise_not(merged_image)
            vid_frames.append(sobel_inverted)
        elif back_ground == 'black':
            vid_frames.append(merged_image)
        else:
            raise ValueError("Wrong input value, there only two input black, white")

        # threshold change 
        if cnt % 2 == 1: 
            weight_x += growth_rate
        elif cnt % 2 == 0:
            weight_y += growth_rate

    return vid_frames



def canny_make(image, reduction_rate = 10, back_ground = "white"):
    '''
    - using canny algorithm, edge detection 
    - input : your image
    - output : detected frames list with multiple thresholds

    --
    - canny
        - threshold1 : range(1000 -> 200)
        - threshold2 : range(1000 -> 200)
        - decrease (1000,1000) -> (900,1000) -> (900,900) -> (800,900) ... 
    - reduction_rate : control the decrease rate of threshold 
    '''
    # setting 
    cnt = 0
    min_th = 1000 
    max_th = 1000

    # set output list 
    vid_frames = []

    while min_th > 200 or max_th > 200:

        # make image with canny
        canny1 = cv2.Canny(image, threshold1=min_th, threshold2=max_th) # OpenCV canny 
        
        if back_ground == 'white':
            canny1_inverted = cv2.bitwise_not(canny1)
            vid_frames.append(canny1_inverted)
        elif back_ground == 'black':
            vid_frames.append(canny1)
        else:
            raise ValueError("Wrong input value, there only two input black, white")
        cnt += 1 
        if cnt % 2 == 1: # 홀수번째, th1 감소 
            min_th -= reduction_rate
        elif cnt % 2 == 0:
            max_th -= reduction_rate

    return vid_frames


def make_frames(image, method = "canny"):
    '''
    input : openCV image  (image = cv2.imread())
    output : frame list to make gif
    '''
    if method == 'canny':
        frames = canny_make(image, reduction_rate = 10, back_ground='white')
    
    elif method == 'sobel':
        frames = sobel_make(image, growth_rate = 0.01, back_ground = 'white')
    else:
        print("NOT IMPLEMENT")

    return frames


def save_gif_file(frames, save_dir = './output.gif'):
    '''
    - Save frames to gif file in your save_dir 
    '''
    with imageio.get_writer(save_dir, mode="I") as writer: # mode : A string containing the modes that this format can handle ('iIvV'),“i” for an image, “I”
        for f in frames:
            writer.append_data(f) # save frame to gif

    if os.path.exists(save_dir):
        return True
    else:
        print("saving fail")
        return False

