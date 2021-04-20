import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# blank = np.zeros((500,500),dtype = 'uint8')
# cv.imshow('Blank',blank) 

img = cv.imread('abhiyaan_opencv_qn1.png')
hsv_orginal = cv.cvtColor(img, cv.COLOR_BGR2HSV)

grass = cv.imread("neg.jpg")
hsv_grass = cv.cvtColor(grass, cv.COLOR_BGR2HSV)


hue, saturation, value = cv.split(hsv_grass)

grass_hist = cv.calcHist([hsv_grass], [0,1], None, [180, 256], [0, 180, 0, 256])
mask = cv.calcBackProject([hsv_orginal], [0, 1], grass_hist, [0, 180, 0, 256], 1)



# Filtering remove noise
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
mask = cv.filter2D(mask, -1, kernel)
_, mask = cv.threshold(mask, 100, 255, cv.THRESH_BINARY)

mask = cv.merge((mask, mask, mask))
result = cv.bitwise_and(img, mask)

cv.imshow("Mask", mask)
cv.imshow("Original image", img)
cv.imshow("Result", result)
cv.imshow("Grass", grass)


#########
##########
#######

grass2 = cv.imread("neg2.jpg")
hsv_grass2 = cv.cvtColor(grass2, cv.COLOR_BGR2HSV)


hue, saturation, value = cv.split(hsv_grass2)

grass_hist2 = cv.calcHist([hsv_grass2], [0,1], None, [180, 256], [0, 180, 0, 256])
mask2 = cv.calcBackProject([hsv_orginal], [0, 1], grass_hist2, [0, 180, 0, 256], 1)



# Filtering remove noise
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
mask2 = cv.filter2D(mask2, -1, kernel)
_, mask2 = cv.threshold(mask2, 100, 255, cv.THRESH_BINARY)

mask2 = cv.merge((mask2, mask2, mask2))
result2 = cv.bitwise_and(result, mask2)

cv.imshow("Result2", result2)
cv.imshow("Mask", mask)
###########


cv.waitKey(0)
cv.destroyAllWindows()