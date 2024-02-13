# In this game, the player and the enemy take turns attacking each other. The player can press the spacebar to attack the
# enemy, and the enemy will automatically attack the player with random damage.
#
# The game ends when either the player or the enemy's HP reaches zero. The game over message will be displayed,
# indicating the outcome of the game.
import pygame
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player and enemy constants
PLAYER_MAX_HP = 100
ENEMY_MAX_HP = 80
PLAYER_ATTACK_DAMAGE = 20
ENEMY_ATTACK_DAMAGE = 15

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Turn-Based Combat Game")

# Fonts
font = pygame.font.Font(None, 36)

# Player and enemy variables
player_hp = PLAYER_MAX_HP
enemy_hp = ENEMY_MAX_HP

# Main game loop
running = True
player_turn = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        if player_turn:
            # Player's turn
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                # Player attacks
                enemy_hp -= PLAYER_ATTACK_DAMAGE
                player_turn = False

                # Check if enemy is defeated
                if enemy_hp <= 0:
                    enemy_hp = 0
                    game_over = True
        else:
            # Enemy's turn
            enemy_damage = random.randint(5, ENEMY_ATTACK_DAMAGE)
            player_hp -= enemy_damage
            player_turn = True

            # Check if player is defeated
            if player_hp <= 0:
                player_hp = 0
                game_over = True

    # Clear the screen
    screen.fill(WHITE)

    # Display player HP
    player_hp_text = font.render(f"Player HP: {player_hp}", True, GREEN)
    screen.blit(player_hp_text, (20, 20))

    # Display enemy HP
    enemy_hp_text = font.render(f"Enemy HP: {enemy_hp}", True, RED)
    screen.blit(enemy_hp_text, (SCREEN_WIDTH - enemy_hp_text.get_width() - 20, 20))

    if game_over:
        # Display game over message
        game_over_text = font.render("Game Over", True, RED)
        screen.blit(game_over_text, ((SCREEN_WIDTH - game_over_text.get_width()) // 2, (SCREEN_HEIGHT - game_over_text.get_height()) // 2))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
