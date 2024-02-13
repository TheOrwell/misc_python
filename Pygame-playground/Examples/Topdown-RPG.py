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
pygame.display.set_caption("Top-Down RPG Combat")
clock = pygame.time.Clock()

# Player
player_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
player_image.fill(GREEN)
player_rect = player_image.get_rect()
player_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
player_speed = 5

# Enemy
enemy_image = pygame.Surface((TILE_SIZE, TILE_SIZE))
enemy_image.fill(RED)
enemy_rect = enemy_image.get_rect()
enemy_rect.center = (100, 100)
enemy_max_hp = 50
enemy_hp = enemy_max_hp

# Combat variables
attacking = False
attack_cooldown = 0
ATTACK_COOLDOWN_MAX = 30
attack_damage = 20

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if not attacking and attack_cooldown == 0 and player_rect.colliderect(enemy_rect):
                    attacking = True

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Handle attacking
    if attacking:
        if enemy_rect.colliderect(player_rect):
            print("Player attacks enemy!")
            enemy_hp -= attack_damage
            if enemy_hp <= 0:
                print("Enemy defeated!")
                # Reset enemy
                enemy_hp = enemy_max_hp
                enemy_rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
        attacking = False
        attack_cooldown = ATTACK_COOLDOWN_MAX
    elif attack_cooldown > 0:
        attack_cooldown -= 1

    # Clear the screen
    screen.fill(WHITE)

    # Draw player and enemy
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)

    # Draw enemy health bar
    pygame.draw.rect(screen, RED, (enemy_rect.left, enemy_rect.top - 10, TILE_SIZE, 5))
    pygame.draw.rect(screen, GREEN, (enemy_rect.left, enemy_rect.top - 10, TILE_SIZE * (enemy_hp / enemy_max_hp), 5))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
