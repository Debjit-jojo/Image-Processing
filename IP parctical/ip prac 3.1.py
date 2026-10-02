import numpy as np
import cv2 as cv

# Read the image in grayscale
img = cv.imread(r'C:\Users\debji\PycharmProjects\PythonProject1\messi Img.jpg', 0)

# Get image dimensions
rows, cols = img.shape

# Translation matrix (move 100 pixels right and 50 pixels down)
M = np.float32([[1, 0, 150],
                [0, 1, 100]])

# Apply affine transformation
dst = cv.warpAffine(img, M, (cols, rows))

# Display the translated image
cv.imshow('Translated Image CS24202', dst)
cv.waitKey(0)
cv.destroyAllWindows()
