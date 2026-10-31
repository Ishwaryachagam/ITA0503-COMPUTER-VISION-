import cv2
import numpy as np

# Read the input image
image = cv2.imread("sample.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Cannot find sample.jpeg")
    exit()

# Create the kernel
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5)
)

# Apply black-hat operation
blackhat_image = cv2.morphologyEx(
    image, cv2.MORPH_BLACKHAT, kernel
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Operation", blackhat_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
