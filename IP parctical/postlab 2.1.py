import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r'C:\Users\debji\PycharmProjects\PythonProject1\goat.jpg', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred_image, 50, 150)

    # Display images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Edge Detected Image CS24202')
    plt.imshow(edges, cmap='gray')
    plt.axis('off')

    plt.show()