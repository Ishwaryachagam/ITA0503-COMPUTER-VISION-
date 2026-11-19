import cv2
from tkinter import Tk, filedialog

# Select video file
root = Tk()
root.withdraw()

video_path = filedialog.askopenfilename(
    title="Select your video",
    filetypes=[
        ("Video files", "*.mp4 *.avi *.mov *.mkv"),
        ("All files", "*.*")
    ]
)

root.destroy()

if not video_path:
    print("No video selected!")
    exit()

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("ERROR: Cannot open video!")
    print("Try another video file in MP4 or AVI format.")
    exit()

# Background subtractor
background = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=True
)

print("Video opened successfully!")
print("Press Q to stop the video.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video ended.")
        break

    # Resize frame
    frame = cv2.resize(frame, (800, 600))

    # Apply background subtraction
    mask = background.apply(frame)

    # Remove shadows
    _, mask = cv2.threshold(
        mask, 200, 255, cv2.THRESH_BINARY
    )

    # Remove noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Draw bounding boxes
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 1500:
            x, y, w, h = cv2.boundingRect(contour)

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Moving Object",
                (x, max(y - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Display video
    cv2.imshow("Experiment 28 - Vehicle Detection", frame)

    # Press Q to stop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print("Vehicle detection completed!")
