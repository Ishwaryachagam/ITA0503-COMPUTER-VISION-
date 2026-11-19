import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

image = np.ones((height, width, 3), dtype=np.uint8) * 255

center = (width // 2, height // 2)
radius = min(width, height) // 4

cv2.circle(image, center, radius, (0, 0, 255), 2)

cv2.imshow("Circle Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
