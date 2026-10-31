import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpeg")

if image is None:
    print("Error: Cannot find sample.jpeg")
    exit()

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create the kernel
kernel = np.ones((5, 5), np.uint8)

# Apply top-hat operation
top_hat_image = cv2.morphologyEx(
    gray_image, cv2.MORPH_TOPHAT, kernel
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Operation", top_hat_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
