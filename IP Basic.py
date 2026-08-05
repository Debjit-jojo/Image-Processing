import cv2
import numpy as np

img = cv2.imread('Messi Img.png', 0)

if img is not None:
    negative = 255 - img
    combined = np.hstack((img, negative))
    cv2.imshow('Original (Left) vs Negative (Right) CS24202', combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Image not found!")


2. 

import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('Messi Img.png')

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

brightness = 10
contrast = 3.3

image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness)

cv2.imwrite('modified_image.jpg', image2)

plt.subplot(1, 2, 2)
plt.title("Brightness & contrast CS24202")
plt.imshow(image2)

plt.show()

3. 
import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('Messi Img.png')

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharpened_image = cv2.filter2D(image, -1, kernel)

cv2.imwrite('sharpened_image.jpg', sharpened_image)

plt.subplot(1, 2, 2)
plt.title("Sharpening CS24202")
plt.imshow(sharpened_image)

plt.show()

4.
 import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('Messi Img.png')

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image)

sharpened_image2 = cv2.Laplacian(image, cv2.CV_64F)

cv2.imwrite('Laplacian_sharpened_image.jpg', sharpened_image2)

plt.subplot(1, 2, 2)
plt.title("Laplacian Sharpening CS24202")
plt.imshow(sharpened_image2)
plt.show()
