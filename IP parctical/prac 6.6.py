import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read scratched/damaged image
img = cv2.imread("Messi Img.png", 0)

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Create mask (white = damaged parts)
mask = np.zeros(img.shape, np.uint8)

# Mark the damaged/scratched area
mask[50:80, 50:150] = 255

# Inpaint damaged regions using TELEA method
restored = cv2.inpaint(
    img,
    mask,
    3,
    cv2.INPAINT_TELEA
)

# Show damaged image
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Damaged Image")
plt.axis("off")

# Show mask
plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title("Mask")
plt.axis("off")

# Show restored image
plt.subplot(1, 3, 3)
plt.imshow(restored, cmap='gray')
plt.title("Restored (Inpainting)")
plt.axis("off")

plt.tight_layout()
plt.show()