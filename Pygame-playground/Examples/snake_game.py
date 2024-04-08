import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 600
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Set up the snake
snake_block = 10
snake_list = []
snake_length = 1

# Set up the apple
apple_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
apple_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

# Set up the game loop
clock = pygame.time.Clock()
game_over = False
direction = "right"

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"

    # Move the snake
    if direction == "right":
        snake_x = snake_list[-1][0] + snake_block
        snake_y = snake_list[-1][1]
    elif direction == "left":
        snake_x = snake_list[-1][0] - snake_block
        snake_y = snake_list[-1][1]
    elif direction == "up":
        snake_x = snake_list[-1][0]
        snake_y = snake_list[-1][1] - snake_block
    else:
        snake_x = snake_list[-1][0]
        snake_y = snake_list[-1][1] + snake_block

    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)

    # Check if the snake has eaten the apple
    if snake_x == apple_x and snake_y == apple_y:
        apple_x = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
        apple_y = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
        snake_length += 1
    else:
        snake_list.pop(0)

    # Check if the snake has hit the wall or itself
    if snake_x < 0 or snake_x >= window_width or snake_y < 0 or snake_y >= window_height or snake_head in snake_list[:-1]:
        game_over = True

    # Clear the window
    window.fill(black)

    # Draw the snake
    for block in snake_list:
        pygame.draw.rect(window, green, [block[0], block[1], snake_block, snake_block])

    # Draw the apple
    pygame.draw.rect(window, red, [apple_x, apple_y, snake_block, snake_block])

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(15)

# Quit Pygame
pygame.quit()