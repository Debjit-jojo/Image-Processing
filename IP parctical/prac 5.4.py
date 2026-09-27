import cv2
import numpy as np

# Load the image
img = cv2.imread(r"C:\Users\debji\PycharmProjects\PythonProject1\goat.jpg")

# Check if image is loaded properly
if img is None:
    print("Error: Image not found or path is incorrect.")
    exit()

# Apply Bilateral Filter
# d = 9, sigmaColor = 75, sigmaSpace = 75
dst = cv2.bilateralFilter(img, 9, 75, 75)

# Display original and filtered images side by side
result = np.hstack((img, dst))
cv2.imshow("Original vs Bilateral Filter CS24194", result)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()