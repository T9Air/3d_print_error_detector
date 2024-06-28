import cv2
import os
import sys

# Get layer height

layer_height = sys.argv[0]

# Image detection function

def detect_movement_background_subtraction(image1, image2):
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
    if (changed_pixels / total_pixels) > .000000000001:    
        return "Movement detected"
    else:
        return "No movement detected"

# REPLACE IMAGE PATHS WITH YOUR IMAGES
def choose_images():
    image1 = cv2.imread('/home/avraham/3d_print_error_detector/Image-files/frame000079.jpg')
    image2 = cv2.imread('/home/avraham/3d_print_error_detector/Image-files/frame000095.jpg')

    # Print results

    result = detect_movement_background_subtraction(image1, image2)
    if result == "No movement detected":
        os.remove('/home/avraham/3d_print_error_detector/Image-files/frame000001.jpg')
    if result == "Movement detected":
        os.remove('/home/avraham/3d_print_error_detector/Image-files/frame000002.jpg')
    return result
