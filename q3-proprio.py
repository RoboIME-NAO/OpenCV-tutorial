# Importing opencv
import cv2 as cv

# Importing sys
import sys


# Creating the image object
img = cv.imread("img.jpg")

if img is None:
    sys.exit("image not found")

# Changing scale to GRAY
gray = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
cv.imshow("gray scale image", gray)

key = cv.waitKey(0)

# Changing to HSV scale
hsv = cv.cvtColor(img,cv.COLOR_RGB2HSV)
cv.imshow("gray scale image", hsv)

key = cv.waitKey(0)

cv.destroyAllWindows()