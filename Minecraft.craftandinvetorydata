# Import pygame and random modules
import pygame
import random

# Define some colors and constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)

# Define the size of each block
BLOCK_SIZE = 20

# Define the size of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define the number of blocks in each row and column
ROW_COUNT = WINDOW_HEIGHT // BLOCK_SIZE
COL_COUNT = WINDOW_WIDTH // BLOCK_SIZE

# Define the speed of the camera movement
CAMERA_SPEED = 5

# Define the speed of the sprite movement
SPRITE_SPEED = 2

# Define the size of the inventory and crafting menu
INVENTORY_WIDTH = 200
INVENTORY_HEIGHT = 400
CRAFTING_WIDTH = 200
CRAFTING_HEIGHT = 200

# Define the font size for the text
FONT_SIZE = 16

# Initialize pygame and create a window
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Minecraft-like game")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Create a list to store the blocks
blocks = []

# Create a function to generate a random terrain of blocks
def generate_terrain():
    # Loop through each row and column
    for row in range(ROW_COUNT):
        # Create a list to store the blocks in each row
        row_blocks = []
        for col in range(COL_COUNT):
            # Generate a random number between 0 and 1
            rand = random.random()
            # If the random number is less than 0.4, create a grass block
            if rand < 0.4:
                color = GREEN
            # If the random number is between 0.4 and 0.6, create a dirt block
            elif rand < 0.6:
                color = BROWN
            # If the random number is between 0.6 and 0.8, create a stone block
            elif rand < 0.8:
                color = GRAY
            # If the random number is between 0.8 and 0.9, create a water block
            elif rand < 0.9:
                color = BLUE
            # If the random number is greater than or equal to 0.9, create an empty block
            else:
                color = BLACK
            # Append the block to the row list
            row_blocks.append(color)
        # Append the row list to the blocks list
        blocks.append(row_blocks)

# Call the function to generate the terrain
generate_terrain()

# Create variables to store the camera position
camera_x = 0
camera_y = 0

# Create a class to represent a sprite
class Sprite(pygame.sprite.Sprite):
    # Initialize the sprite with an image and a position
