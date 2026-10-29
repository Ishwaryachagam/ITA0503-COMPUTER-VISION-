import cv2

# Read the input image
image = cv2.imread("image.jpg")

# Check whether the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Flip the image horizontally
    flipped_image = cv2.flip(image, 1)

    # Rotate the image by 180 degrees
    rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_180)

    # Display the original and transformed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated 180-degree Clockwise Along Y-axis", rotated_image)

    # Save the transformed image
    cv2.imwrite("rotated_image.jpg", rotated_image)

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Image rotated successfully!")
    print("Saved as rotated_image.jpg")
