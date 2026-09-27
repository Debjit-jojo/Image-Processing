import cv2
import numpy as np

# ---------------------------------------
# PART 1: Generate Mask & Restore using TELEA
# ---------------------------------------

# Step 1: Read the damaged image
damaged_img = cv2.imread("dog img1.jpg")

# Check if image is loaded
if damaged_img is None:
    print("Error: Damaged image not found!")
    exit()

# Step 2: Create mask from damaged image
height, width = damaged_img.shape[:2]

mask = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        if damaged_img[i, j].sum() > 0:
            mask[i, j] = [0, 0, 0]
        else:
            mask[i, j] = [255, 255, 255]

# Convert mask to grayscale
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

# Save generated mask
cv2.imwrite("generated_mask.jpg", mask_gray)

# Step 3: Perform inpainting using TELEA method
restored_telea = cv2.inpaint(
    damaged_img,
    mask_gray,
    3,
    cv2.INPAINT_TELEA
)


# ---------------------------------------
# PART 2: Use Predefined Mask & Restore using NS
# ---------------------------------------

# Step 4: Read damaged image again
img = cv2.imread("dog img1.jpg")

# Step 5: Load predefined mask
mask_predefined = cv2.imread("dog img1.jpg", 0)

# Check if mask is loaded
if mask_predefined is None:
    print("Error: Predefined mask not found!")
    exit()

# Step 6: Inpaint using Navier-Stokes method
restored_ns = cv2.inpaint(
    img,
    mask_predefined,
    3,
    cv2.INPAINT_NS
)


# ---------------------------------------
# Save Results
# ---------------------------------------

cv2.imwrite("restored_telea.png", restored_telea)
cv2.imwrite("restored_ns.png", restored_ns)


# ---------------------------------------
# Display Results
# ---------------------------------------

cv2.imshow("Original Damaged Image", damaged_img)
cv2.imshow("Generated Mask", mask_gray)
cv2.imshow("Restored (Telea)", restored_telea)
cv2.imshow("Predefined Mask", mask_predefined)
cv2.imshow("Restored (Navier-Stokes)", restored_ns)

cv2.waitKey(0)
cv2.destroyAllWindows()