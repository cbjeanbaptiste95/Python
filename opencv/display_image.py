
import numpy as np
import cv2


my_image = cv2.imread("C:\Users\Dawen\Desktop\code\Tuskar.png")   ##read image from source/location
cv2.namedWindow("my image", cv2.WINDOW_AUTOSIZE)                  ##create a name for the window box
cv2.imshow("my image", my_image)                                  ##display image in highgui with name for image
cv2.waitKey(0)                                                    ##awaits keystroke before closing display gui
cv2.destroyWindow                                                 ##destry/close display window (gui)
