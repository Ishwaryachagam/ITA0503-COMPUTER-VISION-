import cv2
import matplotlib.pyplot as plt

# Read the input image
image = cv2.imread("sample.jpg")

# Check whether image is loaded
if image is None:
    print("Error: Image not found. Check the image path.")
    exit()

# Calculate and display histogram for Blue, Green and Red channels
colors = ('b', 'g', 'r')

for i, color in enumerate(colors):
    histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histogram, color=color)
    plt.xlim([0, 256])

plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()
