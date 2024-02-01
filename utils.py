# Edge detection algorithm : Canny 
# source file 
import cv2
import os 
import imageio


def load_img(img_dir):
    '''
    input : your image file directory 
    output : opencv image 
    '''
    # image load
    image = cv2.imread(img_dir,cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("Image not found error, please check image path")

    return image

def canny_make(image, reduction_rate = 10):
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
        vid_frames.append(canny1)

        cnt += 1 
        if cnt % 2 == 1: # 홀수번째, th1 감소 
            min_th -= reduction_rate
        elif cnt % 2 == 0:
            max_th -= reduction_rate

    return vid_frames


def make_frames(image, method = 'canny'):
    '''
    input : openCV image  (image = cv2.imread())
    output : frame list to make gif
    '''
    if method == 'canny':
        frames = canny_make(image, reduction_rate = 10)
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

