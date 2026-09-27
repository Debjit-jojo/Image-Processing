import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Messi Img.png')

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

filtered_image = cv2.medianBlur(image, 11)

cv2.imwrite('Median_Blur.jpg', filtered_image)

plt.subplot(1, 2, 2)
plt.title("Median Blur CS24202")
plt.imshow(filtered_image)

plt.show()