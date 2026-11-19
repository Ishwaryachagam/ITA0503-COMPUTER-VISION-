import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
path = filedialog.askopenfilename()
root.destroy()

image = cv2.imread(path, 0)

if image is not None:
    _, segmented = cv2.threshold(
        image, 127, 255, cv2.THRESH_BINARY
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Segmented Image", segmented)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or unable to read!")
