import cv2

def play_video_reverse_slow(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    if not cap.isOpened():
        print("Error: Video file not found!")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion Video", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

play_video_reverse_slow(
    r"C:\Users\ishwa\OneDrive\Desktop\COMPUTER VISION\EXP 39\sample.mp4"
)
