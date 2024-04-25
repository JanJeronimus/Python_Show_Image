"""
05_tkinter.py

This script displays an image using the Tkinter library with the help of Pillow (PIL).

Dependency: Pillow (pip install pillow)
"""

# Define the path to the image file
my_image = 'img\image5.png'

# Import necessary libraries
import tkinter as tk  # Import the Tkinter library
from PIL import Image, ImageTk  # Import modules from Pillow (PIL)

# Create a Tkinter root window
root = tk.Tk()

# Open the image using Pillow
img = Image.open(my_image)

# Convert the image to a Tkinter-compatible format
img = ImageTk.PhotoImage(img)

# Create a label widget to display the image
label = tk.Label(root, image=img)

# Pack the label widget into the root window
label.pack()

# Start the Tkinter event loop
root.mainloop()

"""
This script utilizes the Tkinter library to display an image in a GUI window.
It first opens the image file specified by my_image using Pillow (PIL), converts
 it to a format compatible with Tkinter, creates a label widget to display the image,
 and packs the label widget into the Tkinter root window. 
The script requires the Pillow library, which can be installed via pip (pip install pillow).
"""
