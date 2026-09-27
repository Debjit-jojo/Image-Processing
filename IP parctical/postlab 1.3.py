import cv2

# Read the image
img = cv2.imread('Messi Img.jpg')

# Check if image is loaded properly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Convert BGR image to YCrCb color space
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    # Display the image
    cv2.imshow('YCrCb Image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()