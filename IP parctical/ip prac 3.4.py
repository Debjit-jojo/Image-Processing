import numpy as np
import cv2 as cv

# Read the image in grayscale
img = cv.imread('Messi Img.png', 0)

# Get image dimensions
rows, cols = img.shape

# Shrink the image to 250 × 200 pixels
img_shrinked = cv.resize(img, (250, 200), interpolation=cv.INTER_AREA)
cv.imshow('Shrinked Image CS24202', img_shrinked)

# Enlarge the shrinked image by 1.5 times
img_enlarged = cv.resize(
    img_shrinked,
    None,
    fx=1.5,
    fy=1.5,
    interpolation=cv.INTER_CUBIC
)
cv.imshow('Enlarged Image CS24202', img_enlarged)

cv.waitKey(0)
cv.destroyAllWindows()