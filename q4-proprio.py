import cv2 as cv

# Importing numpy to create the black screen
import numpy as np


# Creating an array 512 X 512 filled with (0,0,0) representing the RGB color black
screen = np.zeros((512,512,3))

# Creating the rectangle
cv.rectangle(screen,(256,256),(512,512),(0,0,255),20)

# Creating the circle
cv.circle(screen,((512+256)//2,(512+256)//2),(512-256)//2,(255,0,0),-1)

# Creating the ellipse
cv.ellipse(screen,(128,(512+256)//2),(50,20),0,0,360,(0,255,0),-1)

# Creating the line
cv.line(screen,(0,0),(512,512),(0,127,127),50)

# Generating text
cv.putText(screen,"RoboIme",(0,128), cv.FONT_ITALIC, 3.5, (127,0,127), 10, cv.LINE_AA)


cv.imshow("canva",screen)
cv.waitKey(0)