'''
Test code for loading window content using openCV edge detection algorithm 
input : original image 
- edge detection to multiple thresholds -> detected gray scale images
- transform into gif file 
output : gif file 
'''
from utils import *

BASE_IMG_PATH = "./images"
BASE_OUT_PATH  = "./outputs"

# your image file name 
img_name = "abstract0.png"


def test_loading():
    
    input_img_path = os.path.join(BASE_IMG_PATH,img_name)
    out_vid_path = os.path.join(BASE_OUT_PATH,img_name.split('.')[0]+'.gif')
        
    img = load_img(img_dir = input_img_path)
    frames = make_frames(image = img, method = "sobel")
    flag = save_gif_file(frames = frames, save_dir = out_vid_path)

    assert flag
