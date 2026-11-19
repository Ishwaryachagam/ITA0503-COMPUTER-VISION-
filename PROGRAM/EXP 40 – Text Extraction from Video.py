
import cv2
import pytesseract
import os

# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Video file name
video_path = "sample.mp4"

# Check whether video exists
if not os.path.exists(video_path):
    print("Error: Video file not found!")
    print("Make sure sample.mp4 is in the same folder as this Python file.")
    exit()

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video!")
    exit()

print("Text extraction started!")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Extract text
    text = pytesseract.image_to_string(gray)

    if text.strip():
        print("\nExtracted Text:")
        print(text.strip())

    # Display video
    cv2.imshow("Text Extraction from Video", frame)

    # Press Q to stop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Text extraction completed!")
