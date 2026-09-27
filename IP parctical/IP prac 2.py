# import cv2, numpy and matplotlib libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\debji\PycharmProjects\PythonProject1\WhatsApp-Image-2023-03-24-at-14.52.58 (1).jpeg")

# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Displaying image using plt.imshow() method
plt.imshow(RGB_img)

# hold the window
plt.waitforbuttonpress()
plt.close("all")
