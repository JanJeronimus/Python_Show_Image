"""
06_webbrowser1.py

This script demonstrates how to open an HTML file containing an image in the default web browser.

"""

# Define the path to the image file
my_image = 'img/image1.png'

import webbrowser

def display_image_in_browser(html_file):
    webbrowser.open_new_tab(html_file)

# Create an HTML file to display the image
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Display Image</title>
</head>
<body>
    <img src="{my_image}" alt="Image">
</body>
</html>
"""

# Write the HTML content to a temporary file
with open('temp_image_display.html', 'w') as f:
    f.write(html_content)

# Open the HTML file in the default web browser
display_image_in_browser('temp_image_display.html')
