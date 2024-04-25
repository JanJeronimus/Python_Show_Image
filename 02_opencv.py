"""
02_opencv.py

This script attempts to display an image using OpenCV but may encounter issues.

Dependency: opencv (pip install opencv-python)
"""

# Define the path to the image file
my_image = 'img\image5.png'

# Import necessary library
import cv2  # Import OpenCV library

# Load the image using OpenCV
img = cv2.imread(my_image)  # Read the image file and load it into an array

# Display the image using OpenCV
cv2.imshow('Image', img)  # Display the image in a window titled 'Image'
cv2.waitKey(0)            # Wait for a key press
cv2.destroyAllWindows()   # Close all OpenCV windows


"""
This script attempts to display an image using OpenCV's imshow() function. 
However, it may encounter issues depending on the environment and configuration. 
The script requires the OpenCV library, which can be installed via pip (pip install opencv-python).
"""