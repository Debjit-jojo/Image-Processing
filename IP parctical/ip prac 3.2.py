import numpy as np
import cv2 as cv

# Read the image in grayscale
img = cv.imread(r'Messi Img.png', 0)

# Get image dimensions
rows, cols = img.shape

# Reflection matrix (vertical reflection)
M = np.float32([[1,  0,    0],
                [0, -1, rows],
                [0,  0,    1]])

# Apply perspective transformation
reflected_img = cv.warpPerspective(img, M, (cols, rows))

# Display the reflected image
cv.imshow('Reflected Image CS24202', reflected_img)

# Save the output image
cv.imwrite('reflection_out.jpg', reflected_img)

cv.waitKey(0)
cv.destroyAllWindows()