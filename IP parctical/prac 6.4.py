import cv2
import matplotlib.pyplot as plt

# Read noisy image in grayscale
img = cv2.imread("Messi Img.png", 0)

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Apply Median Filter
restored = cv2.medianBlur(img, 5)

# Show original noisy image
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Salt & Pepper Noise")
plt.axis("off")

# Show restored image
plt.subplot(1, 2, 2)
plt.imshow(restored, cmap='gray')
plt.title("Restored (Median Filter) CS24217")
plt.axis("off")

plt.tight_layout()
plt.show()