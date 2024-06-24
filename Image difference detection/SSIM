#REPLACE IMAGE PATHS WITH THE PATH TO YOUR IMAGES

# Import necessary libraries
import cv2
import numpy as np

from skimage.metrics import structural_similarity as ssim

# Load the image
image = cv2.imread('image_path.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the second image
image2 = cv2.imread('image2_path.jpg')

# Convert the second image to grayscale
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

gray = cv2.resize(gray, (507, 492))    
gray2 = cv2.resize(gray2, (507, 492))

(score, diff) = ssim(gray, gray2, full=True)
diff = (diff * 255).astype("uint8")
print("Structural Similarity Index: {}".format(score))

# Compare the two outlined objects
if score > .75:
    print("The outlined objects in the two images are the same.")
else:
    print("The outlined objects in the two images are different.")
    
#THE REST OF THE CODE IS ONLY TO VISUALIZE THE OUTLINES

# Apply edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a blank image
outlined_image = np.zeros_like(image)
cv2.drawContours(outlined_image, contours, -1, (0, 255, 0), 2)

# Export the outlined object
cv2.imwrite('outlined_image_path.jpg', outlined_image)

# Apply edge detection on the second image
edges2 = cv2.Canny(gray2, 50, 150)

# Find contours in the second image
contours2, _ = cv2.findContours(edges2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a blank image for the second image
outlined_image2 = np.zeros_like(image2)
cv2.drawContours(outlined_image2, contours2, -1, (0, 255, 0), 2)

# Export the outlined object from the second image
cv2.imwrite('outlined_image2_path.jpg', outlined_image2)
