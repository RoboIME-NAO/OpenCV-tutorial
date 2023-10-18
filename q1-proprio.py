# Importing opencv
import cv2 as cv

# Importing sys
import sys


# Creating the image object
img = cv.imread("img.jpg")

# Error Handling
if img is None:
    sys.exit("image not found")

# Showing the image as 'imagem'
cv.imshow('imagem',img)

# BONUS: saving the image if 's' key is pressed

k = cv.waitKey(0)
if k == ord('s'):
    cv.imwrite('img.jpg',img)

# Closing all image windows
cv.destroyAllWindows()