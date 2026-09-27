import cv2 as cv
import numpy as np

# Read the image in grayscale
img = cv.imread('Messi Img.png', 0)

# Crop the image (rows 100 to 300, columns 100 to 300)
cropped_img = img[100:300, 100:300]

# Display the cropped image
cv.imshow('Cropped Image', cropped_img)

# Save the cropped image
cv.imwrite('cropped_out.jpg', cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()