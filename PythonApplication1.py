import cv2
import numpy as np
from cv2 import imwrite

img = cv2.imread('C:\Users\Dawen\Desktop\code\green.png')

##res is the resized version of img, size is multipled by 2 (2*H & 2*W)
res = cv2.resize(img,None,None,fx=2, fy=2,interpolation = cv2.INTER_AREA)

cv2.imwrite('green_resized.png',res)

##read-resize-write: success
