import cv2
import numpy as np

def detect_object(template_path, input_image_path):

    # Read the template image in grayscale
    template = cv2.imread(template_path, 0)

    # Read the input image
    img = cv2.imread(input_image_path)

    # Check if images are loaded
    if template is None:
        print("Error: Template image not found.")
        return

    if img is None:
        print("Error: Input image not found.")
        return

    # Convert input image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Get width and height of template
    w, h = template.shape[::-1]

    # Perform template matching
    res = cv2.matchTemplate(
        gray_img,
        template,
        cv2.TM_CCOEFF_NORMED
    )

    # Set matching threshold
    threshold = 0.8

    # Find locations where match is above threshold
    loc = np.where(res >= threshold)

    # Draw rectangles around matched objects
    for pt in zip(*loc[::-1]):
        cv2.rectangle(
            img,
            pt,
            (pt[0] + w, pt[1] + h),
            (0, 255, 255),
            2
        )

    # Display the result
    cv2.imshow("Detected Objects", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Provide paths to template and input images
template_path = r"C:\Users\debji\PycharmProjects\PythonProject1\cricket team 2.png"
input_image_path = r"C:\Users\debji\PycharmProjects\PythonProject1\cricket team.png"

# Detect the object
detect_object(template_path, input_image_path)
