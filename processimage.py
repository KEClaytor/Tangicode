# Process the image we acquired
from cv2 import *
import numpy as np
from matplotlib import pyplot as plt
from util_image import show_image_window

# Read the image we saved
img = imread('testnew.jpg',0)
# Segment into blocks
# Threshold to pick the blocks from the background
ret,threshold = threshold(img,127,255,THRESH_BINARY)
show_image_window(threshold)

# Now isolate the blocks

# Create a block object for each block and fill it in as much as we can
