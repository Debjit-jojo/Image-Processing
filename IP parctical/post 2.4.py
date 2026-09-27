import cv2

# Read the image
img = cv2.imread(r'C:\Users\debji\PycharmProjects\PythonProject1\goat.jpg')

# Set Canny parameters
t_lower = 100
t_upper = 200
aperture_size = 5
L2Gradient = True

# Apply Canny Edge Detection
edge = cv2.Canny(
    img,
    t_lower,
    t_upper,
    apertureSize=aperture_size,
    L2gradient=L2Gradient
)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Edge", edge)

cv2.waitKey(0)
cv2.destroyAllWindows()