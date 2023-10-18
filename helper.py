import cv2
import numpy as np

# Define a callback function for the trackbars
def nothing(x):
    pass

# Create a black image and a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

# Create trackbars for each HSV channel
cv2.createTrackbar('H', 'image', 0, 179, nothing)
cv2.createTrackbar('S', 'image', 0, 255, nothing)
cv2.createTrackbar('V', 'image', 0, 255, nothing)

# Set default HSV values
hsv_default = [0, 0, 0]

while True:
    # Get current HSV values from the trackbars
    h = cv2.getTrackbarPos('H', 'image')
    s = cv2.getTrackbarPos('S', 'image')
    v = cv2.getTrackbarPos('V', 'image')
    
    # Set the HSV values to the default if all are zero
    if h == 0 and s == 0 and v == 0:
        h, s, v = hsv_default
    
    # Update the default HSV values
    hsv_default = [h, s, v]

    # Set the image color based on the current HSV values
    img[:] = [h, s, v]

    # Convert the image color from HSV to BGR
    bgr = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

    # Show the image and wait for a key press
    cv2.imshow('image', bgr)
    k = cv2.waitKey(1) & 0xFF
    
    # Exit if 'q' is pressed
    if k == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()

