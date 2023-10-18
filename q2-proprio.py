# Importing opencv
import cv2 as cv

# Importing numpy
import numpy as np

# Importing sys
import sys


# Creating the image object
img = cv.imread("img.jpg")

if img is None:
    sys.exit("image not found")

# Rotating image
rot = cv.rotate(img,cv.ROTATE_180)

# Showing rotated image
cv.imshow("rotated image", rot)
cv.waitKey(0)

# Concatenating images on the right
cat = np.concatenate((img,rot), axis=1)
cv.imshow("concatenated images",cat)
cv.waitKey(0)

# Concatenating bottom
cat2 = np.concatenate((img,rot),axis=0)
cv.imshow("bottom concat", cat2)
cv.waitKey(0)

cv.destroyAllWindows()