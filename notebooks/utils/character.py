import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import functools

# Arguments (replace with actual paths)
# license_plate_recognition.py

args = {
    "image": "..\\output\\image\\cropped_image.jpg",
    "model": "D:\\Python_Code\\PYTHON_Nam4_HK1\\ANPR\\model\\char_model_01.h5"
}


def show_image(image, title="Image", cmap=None):
    
    plt.figure(figsize=(6, 6))
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis("off")  # Hide axes
    plt.show()


# Read the image and convert to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display grayscale image
# show_image(gray, title="Grayscale Image", cmap='gray')

# Load the pre-trained model
char_model = load_model(args["model"])

# Apply Gaussian blurring and thresholding
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 45, 15)

# Display blurred and thresholded images
# show_image(blurred, title="Blurred Image", cmap='gray')
# show_image(thresh, title="Thresholded Image", cmap='gray')

# Perform connected components analysis
_, labels = cv2.connectedComponents(thresh)
mask = np.zeros(thresh.shape, dtype="uint8")
total_pixels = image.shape[0] * image.shape[1]
lower = total_pixels // 70
upper = total_pixels // 20

# Filter components based on size
for (i, label) in enumerate(np.unique(labels)):
    if label == 0:
        continue
    labelMask = np.zeros(thresh.shape, dtype="uint8")
    labelMask[labels == label] = 255
    numPixels = cv2.countNonZero(labelMask)
    if lower < numPixels < upper:
        mask = cv2.add(mask, labelMask)

# Find contours and bounding boxes
cnts, _ = cv2.findContours(
    mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
boundingBoxes = [cv2.boundingRect(c) for c in cnts]

# Sort bounding boxes from left-to-right, top-to-bottom


def compare(rect1, rect2):
    if abs(rect1[1] - rect2[1]) > 10:
        return rect1[1] - rect2[1]
    return rect1[0] - rect2[0]


boundingBoxes = sorted(boundingBoxes, key=functools.cmp_to_key(compare))

# Constants
TARGET_WIDTH = 128
TARGET_HEIGHT = 128
chars = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

# Recognize characters from bounding boxes
vehicle_plate = ""
for rect in boundingBoxes:
    x, y, w, h = rect
    crop = mask[y:y + h, x:x + w]
    crop = cv2.bitwise_not(crop)

    rows, columns = crop.shape
    paddingY = (TARGET_HEIGHT -
                rows) // 2 if rows < TARGET_HEIGHT else int(0.17 * rows)
    paddingX = (
        TARGET_WIDTH - columns) // 2 if columns < TARGET_WIDTH else int(0.45 * columns)

    crop = cv2.copyMakeBorder(crop, paddingY, paddingY,
                              paddingX, paddingX, cv2.BORDER_CONSTANT, None, 255)
    crop = cv2.cvtColor(crop, cv2.COLOR_GRAY2RGB)
    crop = cv2.resize(crop, (TARGET_WIDTH, TARGET_HEIGHT))
    crop = crop.astype("float") / 255.0
    crop = np.expand_dims(img_to_array(crop), axis=0)

    prob = char_model.predict(crop)[0]
    idx = np.argmax(prob)
    vehicle_plate += chars[idx]
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(image, chars[idx], (x, y + 15), 0, 0.8, (0, 0, 255), 2)
show_image(image, title="Final Image with Predictions")
print("Vehicle plate: " + vehicle_plate)
