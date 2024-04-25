"""
01_matplotlib.py

This script demonstrates how to display an image using Matplotlib.

"""

# Define the path to the image file
my_image = 'img\image5.png'

# Import necessary libraries
import matplotlib.pyplot as plt  # Importing matplotlib for plotting
import matplotlib.image as mpimg  # Importing matplotlib's image module

# Load the image using Matplotlib
img = mpimg.imread(my_image)  # Read the image file and load it into an array

# Display the image
plt.imshow(img)  # Display the image
plt.axis('off')  # Turn off the axes
plt.show()       # Show the image

