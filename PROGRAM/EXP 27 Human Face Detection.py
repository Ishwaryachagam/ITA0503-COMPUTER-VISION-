import cv2
import os

image_path = "sample.jpeg"

image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cascade_path = os.path.join(
        cv2.data.haarcascades,
        "haarcascade_frontalface_default.xml"
    )

    face_cascade = cv2.CascadeClassifier(cascade_path)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    print("Number of faces detected:", len(faces))

    cv2.imshow("Human Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
