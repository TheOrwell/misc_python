import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 30  # Size of each grid cell
FPS = 30

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# Define Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self, dx, dy):
        # Move the player by fixed increments (grid-based movement)
        self.rect.x += dx * GRID_SIZE
        self.rect.y += dy * GRID_SIZE

        # Keep player within the screen boundaries
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))


# Define NPC class
class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple RPG - Grid Based Movement")

# Create sprites group
all_sprites = pygame.sprite.Group()

# Create player object
player = Player()
all_sprites.add(player)

# Create NPCs
npc1 = NPC(200, 200)
npc2 = NPC(400, 300)
all_sprites.add(npc1, npc2)

# Set up the game loop
clock = pygame.time.Clock()
running = True
while running:
    # Keep loop running at the right speed
    clock.tick(FPS)

    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    dx, dy = 0, 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dx = -.5
    if keys[pygame.K_RIGHT]:
        dx = .5
    if keys[pygame.K_UP]:
        dy = -.5
    if keys[pygame.K_DOWN]:
        dy = .5

    player.update(dx, dy)

    # Render (draw)
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # After drawing everything, flip the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
