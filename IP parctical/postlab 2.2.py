import cv2

# Read the image
img = cv2.imread(r'C:\Users\debji\PycharmProjects\PythonProject1\goat.jpg')

# Check if image is loaded
if img is None:
    print("Error: Image not found or unable to load.")
else:
    # Set threshold values
    t_lower = 100
    t_upper = 200
    aperture_size = 5

    # Apply Canny Edge Detection
    edge = cv2.Canny(img, t_lower, t_upper,
                     apertureSize=aperture_size)

    # Display original and edge images
    cv2.imshow('Original', img)
    cv2.imshow('Edge', edge)

    cv2.waitKey(0)
    cv2.destroyAllWindows()