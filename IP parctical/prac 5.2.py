import cv2
import numpy as np

# Read the input image
img = cv2.imread(r"C:\Users\debji\PycharmProjects\PythonProject1\goat.jpg")

# Check if image is loaded successfully
if img is None:
    print("Error: Image not found.")
    exit()

# Apply Gaussian Blur
dst = cv2.GaussianBlur(img, (5, 5), 0)

# Display original and blurred images side by side
result = np.hstack((img, dst))
cv2.imshow("Original vs Gaussian Blur CS24194", result)

# Wait for key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()