"""
03_pygame.py

This script displays an image using the Pygame library.

"""

# Define the path to the image file
my_image = 'img\image5.png'

# Import necessary library
import pygame  # Import Pygame library

# Initialize Pygame
pygame.init()

# Load the image using Pygame
img = pygame.image.load(my_image)

# Create a display window with the same size as the image
screen = pygame.display.set_mode(img.get_size())

# Blit (draw) the image onto the screen at position (0, 0)
screen.blit(img, (0, 0))

# Update the display
pygame.display.flip()

# Main event loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        # If the user closes the window, set running to False to exit the loop
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
