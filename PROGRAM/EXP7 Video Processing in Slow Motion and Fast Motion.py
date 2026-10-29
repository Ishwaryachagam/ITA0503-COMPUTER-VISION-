import cv2

# Load the input video
video_path = input("Enter video file path: ")
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

print("1. Slow Motion")
print("2. Fast Motion")
choice = input("Enter your choice (1 or 2): ")

# Set playback speed
if choice == "1":
    delay = 100  # Slow motion
elif choice == "2":
    delay = 10   # Fast motion
else:
    print("Invalid choice")
    cap.release()
    exit()

# Read and display video frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()