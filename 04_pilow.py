"""
04_pillow.py

This script displays an image using the Pillow (PIL) library.

Dependency: Pillow (pip install pillow)
"""

# Define the path to the image file
my_image = 'img\image5.png'

# Import necessary library
from PIL import Image  # Import the Image module from Pillow

# Open the image using Pillow
img = Image.open(my_image)  # Open the image file and load it into an Image object

# Display the image using the default image viewer
img.show()

"""
This script utilizes the Pillow (PIL) library to display an image.
It opens the image file specified by my_image and displays it using
 the default image viewer associated with the operating system. 
The script requires the Pillow library, which can be installed via pip (pip install pillow).
"""