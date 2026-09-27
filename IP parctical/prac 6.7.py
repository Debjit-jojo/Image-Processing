import cv2
import numpy as np
import matplotlib.pyplot as plt

# Base clean image (gray background + circle)
img = np.ones((256, 256), dtype=np.uint8) * 127

# Draw a gray circle
cv2.circle(img, (128, 128), 60, 200, -1)

# Generate Gaussian noise
noise = np.random.normal(0, 25, img.shape).astype(np.int16)

# Add Gaussian noise to the image
gaussian_noisy = cv2.add(
    img.astype(np.int16),
    noise,
    dtype=cv2.CV_8U
)

# Save noisy image
cv2.imwrite("Messi Img.png", gaussian_noisy)

# Display noisy image
plt.imshow(gaussian_noisy, cmap="gray")
plt.title("Gaussian Noisy Image")
plt.axis("off")
plt.show()