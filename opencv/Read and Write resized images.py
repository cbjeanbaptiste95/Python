import cv2
import numpy as np
from cv2 import imwrite

img = cv2.imread('C:\Users\Dawen\Desktop\code\green.png')  ##read image from source

resxtwo = cv2.resize(img,None,None, fx=2, fy=2,interpolation = cv2.INTER_AREA)  ##orginal image size multipled by 2 in X & Y dimensions
resdivtwo = cv2.resize(img,None,None, fx=0.5, fy=0.5,interpolation = cv2.INTER_AREA)## '       '     divided by (1/2) in X & Y dimensions


cv2.imwrite('green_resize_mult2.png',resxtwo)   ###saved as resized x2 file
cv2.imwrite('green_resize_div2.png',resdivtwo)  ###saved as resized /2 file


##read-resize-write: success
