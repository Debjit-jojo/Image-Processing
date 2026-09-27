import cv2
import numpy as np

image1 = cv2.imread(r"C:\Users\debji\PycharmProjects\PythonProject1\messi Img.jpg")
image2 = cv2.imread(r"C:\Users\debji\PycharmProjects\PythonProject1\goat.jpg")

weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0)

cv2.imshow("CS24202", weightedSum)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
