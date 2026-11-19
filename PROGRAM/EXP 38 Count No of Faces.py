
import cv2
import tkinter as tk
from tkinter import filedialog

print("Face Detection Program Started!")

# Open image selection window
root = tk.Tk()
root.withdraw()
root.attributes("-topmost", True)

print("Please select an image...")

image_path = filedialog.askopenfilename(
    parent=root,
    title="Choose an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png *.bmp")
    ]
)

root.destroy()

if not image_path:
    print("No image selected!")
    input("Press Enter to exit...")
    raise SystemExit

print("Selected image:", image_path)

# Read image
image = cv2.imread(image_path)

if image is None:
    print("ERROR: Unable to read image!")
    input("Press Enter to exit...")
    raise SystemExit

print("Image loaded successfully!")

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("ERROR: Face detection model not loaded!")
    raise SystemExit

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Count faces
face_count = len(faces)

print("Number of faces detected:", face_count)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3
    )

# Display image
cv2.namedWindow("Face Detection Result", cv2.WINDOW_NORMAL)
cv2.imshow("Face Detection Result", image)

print("Image displayed! Press any key on the image window to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Program completed successfully!")
input("Press Enter to exit...")
