import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread(r"C:\Users\debji\PycharmProjects\PythonProject1\WhatsApp-Image-2023-03-24-at-14.52.58 (1).jpeg")
plt.title("CS24242")
plt.imshow(img)
plt.waitforbuttonpress()
plt.close("all")
