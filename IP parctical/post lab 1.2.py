import cv2

# Read the image
image = cv2.imread('Messi Img.jpg')

# Check if image is loaded properly
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # Split the image into B, G, R channels
    B, G, R = cv2.split(image)

    # Show the original image
    cv2.imshow("Original CS24202", image)
    cv2.waitKey(0)

    # Show Blue channel
    cv2.imshow("Blue CS24202", B)
    cv2.waitKey(0)

    # Show Green channel
    cv2.imshow("Green CS24202", G)
    cv2.waitKey(0)

    # Show Red channel
    cv2.imshow("Red CS24202", R)
    cv2.waitKey(0)

    cv2.destroyAllWindows()