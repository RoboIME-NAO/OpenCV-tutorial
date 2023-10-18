import cv2
import numpy as np

# Define a function to create a mask for a specified color
def create_mask(image, color_lower, color_upper):
    # Convert image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # Define the range of colors to mask
    mask = cv2.inRange(hsv_image, color_lower, color_upper)
    return mask

# Define a function to update the mask based on the trackbar values
def update_mask(x):
    # Get the current trackbar values
    h_min = cv2.getTrackbarPos('H_min', 'Mask')
    s_min = cv2.getTrackbarPos('S_min', 'Mask')
    v_min = cv2.getTrackbarPos('V_min', 'Mask')
    h_max = cv2.getTrackbarPos('H_max', 'Mask')
    s_max = cv2.getTrackbarPos('S_max', 'Mask')
    v_max = cv2.getTrackbarPos('V_max', 'Mask')
    # Define the lower and upper bounds for the color to mask
    color_lower = np.array([h_min, s_min, v_min])
    color_upper = np.array([h_max, s_max, v_max])
    # Create the mask for the specified color
    mask = create_mask(image, color_lower, color_upper)
    # Show the resulting mask
    cv2.imshow('Mask', mask)

# Read an image
image = cv2.imread('img.jpg')

# Create a window to display the mask
cv2.namedWindow('Mask')

# Create trackbars for the lower and upper bounds of the color to mask
cv2.createTrackbar('H_min', 'Mask', 0, 179, update_mask)
cv2.createTrackbar('S_min', 'Mask', 0, 255, update_mask)
cv2.createTrackbar('V_min', 'Mask', 0, 255, update_mask)
cv2.createTrackbar('H_max', 'Mask', 179, 179, update_mask)
cv2.createTrackbar('S_max', 'Mask', 255, 255, update_mask)
cv2.createTrackbar('V_max', 'Mask', 255, 255, update_mask)

# Initialize the mask with the default values
update_mask(0)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
