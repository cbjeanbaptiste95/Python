import cv2
import numpy as np

my_image = cv2.imread('C:\Users\Dawen\Desktop\code\pudge.png')          ##read image
gray_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)                 ##convert my_image to gray image, store as "gray_image"

##create 2 seperate display windows to show the images
cv2.imshow("gray scale", gray_image)                                    ##display gray image
cv2.imshow("pudge", my_image)                                           ##display original




cv2.waitKey(0)
cv2.destroyAllWindows
del my_image
