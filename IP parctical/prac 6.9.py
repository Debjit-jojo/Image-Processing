import cv2
import numpy as np
import matplotlib.pyplot as plt

# Base clean image (gray background + text)
img = np.ones((256, 256), dtype=np.uint8) * 180

# Add text
cv2.putText(
    img,
    "TEST",
    (60, 150),
    cv2.FONT_HERSHEY_SIMPLEX,
    2,
    50,
    5
)

# Add random noise
noise = np.random.randint(
    0, 50,
    img.shape,
    dtype=np.uint8
)

# Add noise to image
noisy_img = cv2.add(img, noise)

# Save noisy image
cv2.imwrite("Messi Img.png", noisy_img)

# Display noisy image
plt.imshow(noisy_img, cmap="gray")
plt.title("General Noisy Image")
plt.axis("off")
plt.show()