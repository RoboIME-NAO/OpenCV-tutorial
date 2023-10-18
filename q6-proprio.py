import cv2 as cv
import numpy as np


# Creating hsv image object
img = cv.imread("img.jpg")
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

# Defining the range of color of the mask (ask the internet's help for this one XD)
upper = cv.cvtColor(np.uint8([[[255,215,0]]]),cv.COLOR_BGR2HSV)
lower = cv.cvtColor(np.uint8([[[255,69,0]]]),cv.COLOR_BGR2HSV)

# Creating the mask using the specified range
mask = cv.inRange(hsv, (12, 0, 0), (179, 255, 255))

# Bitwise and with the original image (to force white to the intersection and black to the rest)
cv.bitwise_and(hsv,hsv,mask=mask)

cv.imshow("mask",mask)
cv.waitKey(0)