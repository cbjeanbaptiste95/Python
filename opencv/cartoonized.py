import numpy
import cv2



img_color = cv2.imread('C:\Users\MyComputer-DZ\Desktop\Code\Python\Pudge.png')
img_rgb = img_color

## blur and convert to gray image
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 7)

### find edges on image
img_edge = cv2.adaptiveThreshold(img_blur, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 9, 2)
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

## display image
cv2.namedWindow("my image")
cv2.imshow("edges of pudge", img_edge)
## save output image
cv2.imwrite('edged_out_pudge.png', img_edge)
## await response & release resources
cv2.waitKey(0)
cv2.destroyAllWindows

## output image : https://github.com/DzouOnionGardener/OnionPy/blob/master/edged_out_pudge.png
