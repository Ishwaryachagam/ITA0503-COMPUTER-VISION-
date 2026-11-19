import cv2

def reverse_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    if not cap.isOpened():
        print("Error: Cannot open video!")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    if len(frames) == 0:
        print("Error: No frames found!")
        return

    print("Total frames:", len(frames))
    print("Playing video in reverse...")

    for frame in reversed(frames):
        cv2.imshow("Reverse Video Playback", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    print("Reverse video playback completed!")

reverse_video("sample.mp4")
