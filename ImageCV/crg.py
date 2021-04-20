import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread("abhiyaan_opencv_qn1.png")


kernel = np.ones((5,5),np.uint8)
kernel_ = np.ones((5,5),np.float32)/25
# lower_orange = np.uint8([[[0, 30, 150]]])
# upper_orange = np.uint8([[[255, 100, 255]]])

hist = cv2.calcHist([image], [1, 2], None, [256, 256], [30,100,150,256])
mask = cv2.calcBackProject([image], [1, 2], hist, [30, 100, 150, 256], 1)
# The below two commented statements are optional we shld do trial and error to see which finds the best contour. If u want u can uncomment those 2 lines and see the output
mask = cv2.filter2D(mask,-1,kernel_)
mask = cv2.dilate(mask, kernel, iterations=2)
new = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("new", new)
cv2.waitKey(0)
cv2.destroyAllWindows()