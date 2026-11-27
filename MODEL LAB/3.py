
import cv2

# Read image
image = cv2.imread("sample.jpeg")

if image is None:
    print("Image not found")
    exit()

# Select rectangular ROI
roi = cv2.selectROI("Select ROI", image)

# Get ROI coordinates
x, y, w, h = roi

# Check selection
if w == 0 or h == 0:
    print("No region selected")
    exit()

# Copy selected region
cropped = image[y:y+h, x:x+w].copy()

# Destination location
new_x = 50
new_y = 50

# Check destination boundaries
if new_x + w <= image.shape[1] and new_y + h <= image.shape[0]:

    # Paste ROI at new location
    image[new_y:new_y+h, new_x:new_x+w] = cropped

    # Display modified image
    cv2.imshow("Modified Image", image)

    # Save output
    cv2.imwrite("roi_output.jpg", image)

    print("ROI copied and pasted successfully")

else:
    print("Destination location is outside image boundaries")

cv2.waitKey(0)
cv2.destroyAllWindows()
