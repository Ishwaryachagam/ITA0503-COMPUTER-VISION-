
import cv2

# Read the image
image = cv2.imread("sample.jpeg")

# Check whether image is loaded
if image is None:
    print("Image not found")
    exit()

# Convert image into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny Edge Detection
edges = cv2.Canny(blur, 100, 200)

# Display original image
cv2.imshow("Original Image", image)

# Display edge detected image
cv2.imshow("Canny Edge Detection", edges)

# Save the output
cv2.imwrite("canny_output.jpg", edges)

# Wait and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
