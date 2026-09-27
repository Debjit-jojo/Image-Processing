import cv2
import numpy as np
import matplotlib.pyplot as plt

# Base clean image (gray background + rectangle)
img = np.ones((256, 256), dtype=np.uint8) * 127

# Draw rectangle
cv2.rectangle(img, (60, 60), (200, 200), 200, -1)

# Add Salt & Pepper noise
s_p_img = img.copy()

# Number of noise pixels
num_noise = 2000

# Add Salt noise (white pixels)
coords = [
    np.random.randint(0, i, num_noise)
    for i in img.shape
]
s_p_img[coords] = 255

# Add Pepper noise (black pixels)
coords = [
    np.random.randint(0, i, num_noise)
    for i in img.shape
]
s_p_img[coords] = 0

# Save noisy image
cv2.imwrite("Messi Img.png", s_p_img)

# Display noisy image
plt.imshow(s_p_img, cmap="gray")
plt.title("Salt & Pepper Noise")
plt.axis("off")
plt.show()