import cv2 as cv
import sys

img = cv.imread("img.jpg")

if img is None:
    sys.exit("Could not read image")
cv.imshow("imagem",img)
k = cv.waitKey(0)
if k == ord('s'):
    cv.imwrite('1.jpg',img)
cv.destroyAllWindows()