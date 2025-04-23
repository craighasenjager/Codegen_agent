import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Clock
clock = pygame.time.Clock()

def draw_rect(color, position):
    """Draw a rectangle on the screen."""
    rect = pygame.Rect(position[0], position[1], CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)

def random_position():
    """Generate a random position for food."""
    x = random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE
    y = random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
    return (x, y)

def main():
    # Initial snake setup
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = RIGHT
    food_position = random_position()
    score = 0

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != DOWN:
                    direction = UP
                elif event.key == pygame.K_DOWN and direction != UP:
                    direction = DOWN
                elif event.key == pygame.K_LEFT and direction != RIGHT:
                    direction = LEFT
                elif event.key == pygame.K_RIGHT and direction != LEFT:
                    direction = RIGHT

        # Move snake
        new_head = (snake[0][0] + direction[0] * CELL_SIZE, snake[0][1] + direction[1] * CELL_SIZE)
        snake.insert(0, new_head)

        # Check for collision with food
        if snake[0] == food_position:
            score += 1
            food_position = random_position()
        else:
            snake.pop()

        # Check for collision with boundaries
        if (snake[0][0] < 0 or snake[0][0] >= SCREEN_WIDTH or
            snake[0][1] < 0 or snake[0][1] >= SCREEN_HEIGHT):
            break

        # Check for collision with itself
        if snake[0] in snake[1:]:
            break

        # Draw everything
        screen.fill(BLACK)
        draw_rect(RED, food_position)
        for segment in snake:
            draw_rect(GREEN, segment)

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render(f'Score: {score}', True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    # Game over
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()