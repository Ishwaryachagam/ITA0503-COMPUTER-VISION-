import cv2

# Load the trained watch classifier
watch_cascade = cv2.CascadeClassifier("watch_cascade.xml")

# Check whether the classifier loaded
if watch_cascade.empty():
    print("Error: watch_cascade.xml not found or invalid.")
    exit()

# Read an image containing a watch
image = cv2.imread("watch.jpeg")

if image is None:
    print("Error: Cannot find watch.jpeg")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect watches
watches = watch_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected watches
for (x, y, w, h) in watches:
    cv2.rectangle(
        image,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

# Display the result
if len(watches) > 0:
    print("Watch detected:", len(watches))
else:
    print("No watch detected.")

cv2.imshow("Watch Recognition", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
