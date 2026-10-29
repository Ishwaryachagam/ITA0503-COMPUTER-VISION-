import cv2

image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found! Keep sample.jpg in the same folder.")
else:
    watermark_text = "WATERMARK"

    watermarked_image = image.copy()

    cv2.putText(
        watermarked_image,
        watermark_text,
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (0, 255, 0),
        3
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Watermarked Image", watermarked_image)

    cv2.imwrite("watermarked_image.jpg", watermarked_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
