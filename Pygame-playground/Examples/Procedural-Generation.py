#  player represented by a red rectangle. We track the player's position using the player_x and player_y variables.
#
# Inside the main game loop, we handle the player's movement using the arrow keys. We check for key presses using pygame.key.get_pressed() and update the player's position accordingly while ensuring they don't move outside the boundaries of the grid.
#
# We draw the player's rectangle on the screen using pygame.draw.rect() with a red color. The position of the rectangle is calculated based on the player's grid position and the TILE_SIZE.
# This code sets up a grid-based world with randomly generated tiles representing different types of terrain (grass, water, sand). The screen is divided into a grid, and each cell in the grid represents a tile. We use Pygame's pygame.draw.rect() function to draw rectangles of different colors for each type of tile.
#
# The world is represented by a 2D list (world_grid) where each element represents the type of tile at that position. During initialization, each cell in world_grid is assigned a random tile type.
#
# The program continuously loops, updating the display and checking for events such as quitting the game.


import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // TILE_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // TILE_SIZE
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
GREEN = (50, 255, 50)
BROWN = (139, 69, 19)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Procedurally Generated World")

# Generate the world grid
world_grid = [[random.choice([0, 1, 2]) for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Tile types: 0 - grass, 1 - water, 2 - sand

# Player variables
player_x = GRID_WIDTH // 2
player_y = GRID_HEIGHT // 2

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= .25
    elif keys[pygame.K_DOWN] and player_y < GRID_HEIGHT - 1:
        player_y += .25
    elif keys[pygame.K_LEFT] and player_x > 0:
        player_x -= .25
    elif keys[pygame.K_RIGHT] and player_x < GRID_WIDTH - 1:
        player_x += .25

    # Clear the screen
    screen.fill(WHITE)

    # Draw the world
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            tile_type = world_grid[y][x]
            tile_color = None
            if tile_type == 0:
                tile_color = GREEN
            elif tile_type == 1:
                tile_color = BLUE
            elif tile_type == 2:
                tile_color = BROWN

            pygame.draw.rect(screen, tile_color, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Draw the player
    player_rect = pygame.Rect(player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, (255, 0, 0), player_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
