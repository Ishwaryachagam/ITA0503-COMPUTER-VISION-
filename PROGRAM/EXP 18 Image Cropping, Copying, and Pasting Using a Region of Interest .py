import cv2
import numpy as np

image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found! Keep sample.jpg in the same folder.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((5, 5), np.uint8)

    eroded_image = cv2.erode(gray_image, kernel, iterations=1)

    cv2.imshow("Original Grayscale Image", gray_image)
    cv2.imshow("Eroded Image", eroded_image)

    cv2.imwrite("eroded_image.jpg", eroded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
