import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('Messi Img.png')

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

brightness = 10
contrast = 2.3

image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

cv2.imwrite('modified_image.jpg', image2)

plt.subplot(1, 2, 2)
plt.title("Brightness & contrast CS24202")
plt.imshow(image2)

plt.show()