# Process the image we acquired
from cv2 import *
import numpy as np
from matplotlib import pyplot as plt
# utilties
from util_image import show_image_window
# Import our custom functions
import imagecapture as ic
import block as blk


def import_patterns():
    up = imread('up.jpg',0)
    down = imread('down.jpg',0)
    left = imread('left.jpg',0)
    right = imread('right.jpg',0)
    return [(up, "up"),(down, "down"),(left, "left"),(right, "right")]

def in_region(test, allpts, w, h):
    reg = False
    for testpt in allpts:
        if ((test[0] > testpt[0]-w/2) and (test[0] < testpt[0]+w/2)) \
                and ((test[1] > testpt[1]-h/2) and (test[1] < testpt[1]+h/2)):
                    reg = True
                    break
    return reg

def segment(img):
    # Read the image we saved
    #img = imread('testnew.jpg',0)
    # Segment into blocks
    # Threshold to pick the blocks from the background
    #ret,thresh = threshold(img,127,255,THRESH_BINARY)
    #show_image_window(thresh)

    patterns = import_patterns()
    # Now isolate the blocks
    img_gray = cvtColor(img, COLOR_BGR2GRAY)

    blocks = []
    blockpts = []
    for template, name in patterns:
        w, h = template.shape[::-1]
        res = matchTemplate(img_gray,template,TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            # make sure the new point is new
            # Do some weedout here
            if not in_region(pt, blockpts, w, h):
                # Create a block object for each block
                newblock = blk.block(pt, None, name)
                blocks.append(newblock)
                blockpts.append(pt)
                # Write out a test image
                rectangle(img, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)
                imwrite('res.png',img)

    return blocks

if __name__ == "__main__":
    img = ic.take_image(1)
    blocks = segment(img)

