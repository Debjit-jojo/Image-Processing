import cv2

# Read image directly in grayscale mode
img = cv2.imread('Messi Img.jpg', cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded properly
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Show the grayscale image
    cv2.imshow('Grayscale Image CS24202', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()