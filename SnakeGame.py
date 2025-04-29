# Step1: import libraries
import pygame
import random
import sys               # to exit game

# Step2: To initialize pygame and setup display
pygame.init()

WIDTH = 600           # 600/20=30
HEIGHT = 600          # 600/20=30
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game!")

# Step3: Colors and Clock
PINK = (255, 152, 187)
RED = (200, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Step4: Define Snake and Food
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = "RIGHT"

food = (random.randrange(0, WIDTH//CELL_SIZE)*CELL_SIZE, random.randrange(0, HEIGHT//CELL_SIZE)*CELL_SIZE)  # (0,30)~(0,29)=(0,580)

# Step5: Draw Snake and Food
def snakeDraw(snake):
    for cell in snake:
        pygame.draw.rect(screen, RED, pygame.Rect(cell[0], cell[1], CELL_SIZE, CELL_SIZE))

def foodDraw(food):
    pygame.draw.rect(screen, PINK, pygame.Rect(food[0], food[1], CELL_SIZE, CELL_SIZE))

# Step6: Move the Snake
def snakeMove(snake, snake_direction):
    headX, headY = snake[0]

    if snake_direction == "UP":
        new_head = (headX, headY-CELL_SIZE)
    elif snake_direction == "DOWN":
        new_head = (headX, headY+CELL_SIZE)
    elif snake_direction == "RIGHT":
        new_head = (headX+CELL_SIZE, headY)
    elif snake_direction == "LEFT":
        new_head = (headX-CELL_SIZE, headY)

    snake.insert(0, new_head)

    if new_head == food:
        return True
    else:
        snake.pop()
        return False

# Step7: Check for collision
def collisionCheck(snake):
    head = snake[0]
    # collision with walls
    if head[0] < 0 or head[0] >= WIDTH or head[1] <0 or head[1] >= HEIGHT:
        return True

    # collision with itself
    if head[0] == snake[1:]:
        return True

    return False

# Step8: Game while loop
running = True

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"

    foodEaten = snakeMove(snake, snake_direction)

    if foodEaten == True:
        food = (
            random.randrange(0, WIDTH//CELL_SIZE)*CELL_SIZE, random.randrange(0, HEIGHT//CELL_SIZE)*CELL_SIZE)

    foodDraw(food)
    snakeDraw(snake)

    if collisionCheck(snake):
        running = False

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
