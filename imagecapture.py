# Capture an image using openCV and write out
from cv2 import *

# initialize the camera
def take_image(cindex = 1)
    cindex = 1
    cam = VideoCapture(cindex)   # 0 -> index of camera
    s, img = cam.read()
    imwrite("filename.jpg",img) #save image

#if s:    # frame captured without any errors
#    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
#    imshow("cam-test",img)
#    waitKey(0)
#    destroyWindow("cam-test")
#    imwrite("filename.jpg",img) #save image

