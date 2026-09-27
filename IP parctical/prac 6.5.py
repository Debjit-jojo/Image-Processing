import cv2
import matplotlib.pyplot as plt

# Read noisy image in grayscale
img = cv2.imread("Messi Img.png", 0)

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Apply Non-local Means Denoising
restored = cv2.fastNlMeansDenoising(img, None,30,7,21)

# Show original noisy image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Noisy Image")
plt.axis("off")

# Show restored image
plt.subplot(1, 2, 2)
plt.imshow(restored, cmap='gray')
plt.title("Restored (Non-local Means) CS24202")
plt.axis("off")

plt.tight_layout()
plt.show()