import cv2

# Read the input image
image_path = r"C:\Users\rsree\OneDrive\Desktop\CVLAB\EXP 11\sample.jpg"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found! Check the image path.")
else:
    # Flip the image horizontally
    flipped_image = cv2.flip(image, 1)

    # Rotate the image by 270 degrees clockwise
    rotated_image = cv2.rotate(
        flipped_image,
        cv2.ROTATE_90_COUNTERCLOCKWISE
    )

    # Display the original and rotated images
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated 270-degree Image", rotated_image)

    # Save the output image in the EXP 11 folder
    output_path = r"C:\Users\rsree\OneDrive\Desktop\CVLAB\EXP 11\rotated_image_270.jpg"
    cv2.imwrite(output_path, rotated_image)

    print("Image rotated successfully!")
    print("Output saved as:", output_path)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

