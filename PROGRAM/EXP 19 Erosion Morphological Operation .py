import cv2
import numpy as np
import os
import glob

# Get the folder containing this Python program
folder = os.path.dirname(os.path.abspath(__file__))

# Find image files in the folder
image_files = []
for extension in ("*.jpg", "*.jpeg", "*.png", "*.bmp", "*.webp"):
    image_files.extend(glob.glob(os.path.join(folder, extension)))

if not image_files:
    print("ERROR: No image file found in:", folder)
    print("Place your sample image in this folder.")
else:
    # Read the first image found
    image_path = image_files[0]
    print("Image found:", image_path)

    image = cv2.imread(image_path)

    if image is None:
        print("Unable to read the image.")
    else:
        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert to binary
        _, binary_image = cv2.threshold(
            gray_image, 127, 255, cv2.THRESH_BINARY
        )

        # Create kernel
        kernel = np.ones((5, 5), np.uint8)

        # Apply erosion
        eroded_image = cv2.erode(
            binary_image, kernel, iterations=1
        )

        # Display results
        cv2.imshow("Original Image", image)
        cv2.imshow("Binary Image", binary_image)
        cv2.imshow("Eroded Image", eroded_image)

        # Save output
        cv2.imwrite(
            os.path.join(folder, "eroded_image.jpg"),
            eroded_image
        )

        cv2.waitKey(0)
        cv2.destroyAllWindows()
