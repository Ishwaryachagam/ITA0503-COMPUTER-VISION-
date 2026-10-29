import cv2

# Read the input image
image_path = input("Enter image file path: ")
image = cv2.imread(image_path)

# Check whether the image is loaded
if image is None:
    print("Error: Cannot load image.")
    exit()

# Rotate the image 90 degrees clockwise
rotated_image = cv2.rotate(
    image, cv2.ROTATE_90_CLOCKWISE
)

# Display original and rotated images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image - 90 Degrees Clockwise", rotated_image)

# Save the rotated image
cv2.imwrite("rotated_90_clockwise.jpg", rotated_image)

print("Image rotated successfully.")
print("Saved as rotated_90_clockwise.jpg")

# Wait for a key and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()