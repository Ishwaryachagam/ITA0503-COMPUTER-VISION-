import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
path = filedialog.askopenfilename()
root.destroy()

image = cv2.imread(path)

if image is not None:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([0, 50, 50])
    upper = np.array([120, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    foreground = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Original Image", image)
    cv2.imshow("Foreground Subtracted", foreground)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or unable to read!")
