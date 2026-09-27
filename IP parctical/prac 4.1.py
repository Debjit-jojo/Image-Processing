import cv2
import numpy as np

img = cv2.imread('Messi Img.png', 0)

if img is not None:
    negative = 255 - img
    combined = np.hstack((img, negative))
    cv2.imshow('Original (Left) vs Negative (Right) CS24202', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found!")