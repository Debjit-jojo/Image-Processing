import numpy as np
import cv2 as cv

# Read the image in grayscale
img = cv.imread('Messi Img.png', 0)

# Get image dimensions
rows, cols = img.shape

# Shearing matrix
M = np.float32([[1, 0.5, 0],
                [0, 1,   0],
                [0, 0,   1]])

# Apply shearing transformation
sheared_img = cv.warpPerspective(img, M, (int(cols * 1.5), int(rows * 1.5)))

# Display the sheared image
cv.imshow('Sheared Image CS24202', sheared_img)

cv.waitKey(0)
cv.destroyAllWindows()