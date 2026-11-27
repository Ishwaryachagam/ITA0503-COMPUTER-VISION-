
import cv2
import numpy as np

# Read image
image = cv2.imread("sample.jpeg")

if image is None:
    print("Image not found")
    exit()

points = []

# Mouse click function
def select_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 4:
            points.append([x, y])
            print("Selected Point:", x, y)

            cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Select Four Points", image)

# Display image
cv2.imshow("Select Four Points", image)
cv2.setMouseCallback("Select Four Points", select_points)

print("Click four points in order:")
print("1. Top Left")
print("2. Top Right")
print("3. Bottom Right")
print("4. Bottom Left")

cv2.waitKey(0)
cv2.destroyAllWindows()

# Check four points
if len(points) != 4:
    print("Please select exactly four points")
    exit()

# Convert points into NumPy array
src_points = np.float32(points)

# Destination points
width = 500
height = 400

dst_points = np.float32([
    [0, 0],
    [width, 0],
    [width, height],
    [0, height]
])

# Calculate perspective transformation matrix
matrix = cv2.getPerspectiveTransform(
    src_points, dst_points
)

print("Transformation Matrix:")
print(matrix)

# Apply perspective transformation
result = cv2.warpPerspective(
    image, matrix, (width, height)
)

# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", result)

# Save output
cv2.imwrite("perspective_output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
