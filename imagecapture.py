# Capture an image using openCV and write out
from cv2 import *

# initialize the camera
def take_image(cindex):
    cam = VideoCapture(cindex)   # 0 -> index of camera
    s, img = cam.read()
    return img

