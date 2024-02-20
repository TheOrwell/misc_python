import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Click to Attack")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Enemy attributes
enemy_radius = 50
enemy_color = RED
enemy_max_health = 100
enemy_health = enemy_max_health
enemy_position = (WIDTH // 2, HEIGHT // 2)
enemy_alive = True  # Boolean flag to indicate if the enemy is alive

# Health bar attributes
health_bar_length = 100
health_bar_height = 10
health_bar_color = RED
health_bar_border_color = BLACK

# Game loop
running = True
while running:
    screen.fill(WHITE)

    if enemy_alive:
        # Draw the enemy
        pygame.draw.circle(screen, enemy_color, enemy_position, enemy_radius)

        # Calculate health bar position
        health_bar_x = enemy_position[0] - health_bar_length // 2
        health_bar_y = enemy_position[1] - enemy_radius - 20

        # Draw health bar border
        pygame.draw.rect(screen, health_bar_border_color, (health_bar_x - 1, health_bar_y - 1, health_bar_length + 2, health_bar_height + 2))

        # Calculate health bar width based on current health
        health_width = int((enemy_health / enemy_max_health) * health_bar_length)
        health_bar_rect = pygame.Rect(health_bar_x, health_bar_y, health_width, health_bar_height)

        # Draw health bar
        pygame.draw.rect(screen, health_bar_color, health_bar_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and enemy_alive:
            # Check if the click was on the enemy
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - enemy_position[0]) ** 2 + (mouse_y - enemy_position[1]) ** 2) ** 0.5
            if distance <= enemy_radius:
                # Deal damage to the enemy
                enemy_health -= 10
                if enemy_health <= 0:
                    enemy_alive = False
                    print("Enemy Destroyed!")
                else:
                    print(f"Enemy Health: {enemy_health}")

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
