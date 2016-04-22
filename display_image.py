
import numpy as np
import cv2

my_image = cv2.imread("C:\Users\Dawen\Desktop\code\Tuskar.png")
cv2.namedWindow("my image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("my image", my_image)
cv2.waitKey(0)
cv2.destroyWindow
