import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
FONT_SIZE = 48
font = pygame.font.SysFont(None, FONT_SIZE)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller")

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Main game loop
def main():
    roll_result = None
    rolling = False
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not rolling:
                    rolling = True
                    roll_result = None

        if rolling:
            roll_result = roll_dice()
            rolling = False

        if roll_result is not None:
            # Display the roll result
            text = font.render(f"Rolled: {roll_result}", True, BLACK)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)  # Limit frame rate to 30 FPS

if __name__ == "__main__":
    main()
