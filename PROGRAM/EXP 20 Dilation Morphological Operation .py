import cv2
import numpy as np
from tkinter import Tk, filedialog

# Select an image
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
)
root.destroy()

if path:
    image = cv2.imread(path)

    if image is not None:
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Convert to binary
        _, binary = cv2.threshold(
            gray, 127, 255, cv2.THRESH_BINARY
        )

        # Create kernel
        kernel = np.ones((5, 5), np.uint8)

        # Apply dilation
        dilation = cv2.dilate(binary, kernel, iterations=1)

        # Display images
        cv2.imshow("Original Image", image)
        cv2.imshow("Binary Image", binary)
        cv2.imshow("Dilated Image", dilation)

        cv2.imwrite("dilated_image.jpg", dilation)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("Dilation completed successfully!")
    else:
        print("Unable to read the image!")
else:
    print("No image selected!")
