import cv2
import numpy as np

image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found! Keep sample.jpg in the same folder.")
else:
    rows, cols, ch = image.shape

    matrix = np.float32([[1, 0, 100], [0, 1, 50]])

    translated_image = cv2.warpAffine(image, matrix, (cols, rows))

    cv2.imshow("Original Image", image)
    cv2.imshow("Translated Image", translated_image)

    cv2.imwrite("translated_image.jpg", translated_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
