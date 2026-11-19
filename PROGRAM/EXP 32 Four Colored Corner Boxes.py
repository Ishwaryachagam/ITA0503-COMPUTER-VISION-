import numpy as np
import cv2

def create_colored_corners(image_size):

    height, width = image_size

    # Create a white image
    image = np.ones(
        (height, width, 3), dtype=np.uint8
    ) * 255

    # Calculate box size
    box_h, box_w = height // 10, width // 10

    # Define corner regions and colors
    image[:box_h, :box_w] = [0, 0, 0]       # Black
    image[:box_h, -box_w:] = [255, 0, 0]    # Blue
    image[-box_h:, :box_w] = [0, 255, 0]    # Green
    image[-box_h:, -box_w:] = [0, 0, 255]   # Red

    # Display image
    cv2.imshow("Colored Corners Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
user_width = int(input("Enter image width: "))
user_height = int(input("Enter image height: "))

create_colored_corners((user_height, user_width))
