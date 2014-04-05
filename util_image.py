# Uesful image utilities
from cv2 import *

# Show image in new window
def show_image_window(img):
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
