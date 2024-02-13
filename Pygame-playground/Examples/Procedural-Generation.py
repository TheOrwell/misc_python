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
