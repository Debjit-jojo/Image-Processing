import numpy as np
import cv2 as cv

# Read the image in grayscale
img = cv.imread('Messi Img.png', 0)

# Get image dimensions
rows, cols = img.shape

# Rotate the image by 30 degrees with a scale of 0.6
rotation_matrix = cv.getRotationMatrix2D((cols / 2, rows / 2), 30, 0.6)

# Apply the rotation
img_rotation = cv.warpAffine(img, rotation_matrix, (cols, rows))

# Display the rotated image
cv.imshow('Rotated Image CS24202', img_rotation)

# Save the output image
cv.imwrite('rotation_out.jpg', img_rotation)

cv.waitKey(0)
cv.destroyAllWindows()