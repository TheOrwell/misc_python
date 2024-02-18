import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 32
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("SimpleRPG")     # Sets window title
clock = pygame.time.Clock()

# --------------------- Player ---------------------
player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill(GREEN)
# A variable that helps us know where the player is on the screen, and track it.
player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
player_speed = 3

# Combat Variables
attacking = False
attack_cooldown = 0
ATTACK_COOLDOWN_MAX = 30
attack_dmg = 20


def playerMove():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Up movement
        player_rect.y -= player_speed
    if keys[pygame.K_a]:  # Left movement
        player_rect.x -= player_speed
    if keys[pygame.K_s]:  # Down movement
        player_rect.y += player_speed
    if keys[pygame.K_d]:  # Right movement
        player_rect.x += player_speed


# --------------------- Enemy ---------------------
enemy_frames = [
    pygame.image.load("Goblin.png").convert_alpha(),
    pygame.image.load("Goblin2.png").convert_alpha(),
]

# Set up animation variables
frame_index = 0
animation_speed = 0.2  # Adjust this value to control the speed of the animation
animation_timer = 0
scale_factor = 1.5

# Resize the enemy frames
for i in range(len(enemy_frames)):
    width = int(enemy_frames[i].get_width() * scale_factor)
    height = int(enemy_frames[i].get_height() * scale_factor)
    enemy_frames[i] = pygame.transform.scale(enemy_frames[i], (width, height))

enemy_image = pygame.image.load("Goblin.png").convert_alpha()
enemy_image = pygame.transform.scale(enemy_image, (64, 64))

# A variable that helps us know where the enemy is on the screen, and track it.
enemy_rect = enemy_image.get_rect()
enemy_rect.center = (100, 100)
enemy_max_hp = 50
enemy_hp = enemy_max_hp

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Space bar down
                if not attacking and attack_cooldown == 0 and player_rect.colliderect(enemy_rect):
                    attacking = True

    animation_timer += clock.get_time() / 1000.0  # Convert milliseconds to seconds
    if animation_timer >= animation_speed:
        frame_index = (frame_index + 1) % len(enemy_frames)
        animation_timer = 0

    playerMove()

    if attacking:
        if enemy_rect.colliderect(player_rect):
            print("Player attacks enemy!")
            enemy_hp -= attack_dmg

            if enemy_hp <= 0:
                print("Enemy defeated!")
                # Respawn a new enemy
                enemy_hp = enemy_max_hp
                enemy_rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
            attacking = False
            attack_cooldown = ATTACK_COOLDOWN_MAX
    elif attack_cooldown > 0:
        attack_cooldown -= 1

    screen.fill(WHITE)

    # Draw player and enemy
    screen.blit(player_image, player_rect)
    # screen.blit(enemy_image, enemy_rect)

    # Draw the current frame of the animation
    current_frame = enemy_frames[frame_index]
    screen.blit(current_frame, enemy_rect)

    # Draw enemy health bar
    pygame.draw.rect(screen, RED, (enemy_rect.left, enemy_rect.top - 15, TILE_SIZE, 5))
    pygame.draw.rect(screen, GREEN, (enemy_rect.left, enemy_rect.top - 15, TILE_SIZE * (enemy_hp / enemy_max_hp), 5))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
