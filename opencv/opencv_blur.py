import cv2
import numpy as np

my_image = cv2.imread("C:\Users\Dawen\Desktop\code\Tuskar.png")
blurred = cv2.blur(my_image,(15,15),0)
G_blurred = cv2.GaussianBlur(my_image, (15,15),0)
cv2.imshow("blurred image", blurred)
cv2.imshow("gausian blurred image", G_blurred)
cv2.waitKey(1)
cv2.destroyAllWindows


 ##      output : https://github.com/DzouOnionGardener/OnionPy/blob/master/blur%20vs%20g-blur.png          ##
