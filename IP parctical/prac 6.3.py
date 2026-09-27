import cv2
import matplotlib.pyplot as plt

# Read noisy image in grayscale
img = cv2.imread(r"C:\Users\debji\PycharmProjects\PythonProject1\goat.jpg",0)

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Apply Gaussian Blur
restored = cv2.GaussianBlur(img, (5, 5), 0)

# Show original and restored images
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Gaussian Noisy")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(restored, cmap='gray')
plt.title("Restored (Gaussian Blur)")
plt.axis("off")

plt.tight_layout()
plt.show()