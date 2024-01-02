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

# Define the size of the quests and achievements menu
QUESTS_WIDTH = 200
QUESTS_HEIGHT = 400
ACHIEVEMENTS_WIDTH = 200
ACHIEVEMENTS_HEIGHT = 200

# Define the font size for the text
FONT_SIZE = 16

# Define the gravity and friction constants
GRAVITY = 0.1
FRICTION = 0.9

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
