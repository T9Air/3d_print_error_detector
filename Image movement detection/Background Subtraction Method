import cv2
import os

# Image detection function

# diff_percentage: how much pixels should be different (in %) to register that there was a movement. Use decimals
def detect_movement_background_subtraction(image1, image2, diff_percentage):
    # Create background subtractor object
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()
    
    # Apply background subtraction to the images
    fg_mask = bg_subtractor.apply(image1)
    fg_mask = bg_subtractor.apply(image2)

    # Get height and width of images
    mask_height = fg_mask.shape[0]
    mask_width = fg_mask.shape[1]

    # Calculate num. of pixels in mask
    total_pixels = mask_height * mask_width

    # Count num. of changed pixels
    changed_pixels = cv2.countNonZero(fg_mask)
    
    # Check if movement is detected
    if (changed_pixels / total_pixels) > diff_percentage:
        return "Movement detected"
    else:
        return "No movement detected"

# REPLACE IMAGE PATHS WITH YOUR IMAGES

image1 = cv2.imread('image_path.jpg')
image2 = cv2.imread('image2_path.jpg')

# Print results

result = detect_movement_background_subtraction(image1, image2, .5)

# REMOVE THESE LINES WHEN FINISHED SCRIPT, ONLY FOR TESTING

if result == "No movement detected":
    os.remove('remove1.jpg')
if result == "Movement detected":
    os.remove('remove2.jpg')
