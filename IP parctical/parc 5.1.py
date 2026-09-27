import cv2

# Step 1: Read the input image
# Replace 'protein_image.png' with the path to your image file
image = cv2.imread('')

# Step 2: Set the kernel size
# Must be an odd positive integer (e.g., 3, 5, 7)
kernel_size = 5

# Step 3: Apply the median filter
filtered_image = cv2.medianBlur(image, kernel_size)

# Step 4: Display the original and noise-filtered images
cv2.imshow('Original Image(CS24194)', image)
cv2.imshow('Filtered Image (Median Blur)', filtered_image)

# Step 5: Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
