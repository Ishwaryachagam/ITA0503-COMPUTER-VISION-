import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()
path = filedialog.askopenfilename()
root.destroy()

image = cv2.imread(path)

if image is not None:
    text = input("Enter text: ")

    cv2.putText(image, text, (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 0, 255), 2)

    cv2.imshow("Text on Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not selected or unable to read!")
