import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Set up fonts
FONT_SIZE = 48
font = pygame.font.SysFont(None, FONT_SIZE)

# Set up the dice
dice_images = [
    pygame.image.load("dice1.png"),
    pygame.image.load("dice2.png"),
    pygame.image.load("dice3.png"),
    pygame.image.load("dice4.png"),
    pygame.image.load("dice5.png"),
    pygame.image.load("dice6.png")
]

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Roller")

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Main game loop
def main():
    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    roll_result = roll_dice()
                    dice_image = dice_images[roll_result - 1]
                    screen.blit(dice_image, (WIDTH // 2 - dice_image.get_width() // 2, HEIGHT // 2 - dice_image.get_height() // 2))

                    # Display the roll result
                    text = font.render(f"Rolled: {roll_result}", True, BLACK)
                    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + dice_image.get_height() // 2 + 20))
                    screen.blit(text, text_rect)

        pygame.display.flip()

if __name__ == "__main__":
    main()
