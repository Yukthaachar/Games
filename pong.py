import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
BALL_SIZE = 20

# Colors
NEON_GREEN = (57, 255, 20)
NEON_ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game!")

font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()

# Paddle class
class Paddle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = color
        self.speed = 5

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.y > 0:
            self.y -= self.speed
        if keys[down_key] and self.y < HEIGHT - self.height:
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Ball class
class Ball:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.size = BALL_SIZE
        self.color = WHITE
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off top and bottom walls
        if self.y <= 0 or self.y >= HEIGHT - self.size:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def reset(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed_x *= -1  # Switch direction after a score

# Initialize paddles and ball
player1 = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, NEON_GREEN)
player2 = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, NEON_ORANGE)
ball = Ball()

# Scores
score1 = 0
score2 = 0

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddles
    player1.move(pygame.K_w, pygame.K_s)
    player2.move(pygame.K_UP, pygame.K_DOWN)

    # Move ball
    ball.move()

    # Collision with paddles
    if (player1.x < ball.x < player1.x + player1.width and
        player1.y < ball.y + ball.size and ball.y < player1.y + player1.height):
        ball.speed_x *= -1

    if (player2.x < ball.x + ball.size < player2.x + player2.width and
        player2.y < ball.y + ball.size and ball.y < player2.y + player2.height):
        ball.speed_x *= -1

    # Scoring
    if ball.x <= 0:
        score2 += 1
        ball.reset()

    if ball.x >= WIDTH:
        score1 += 1
        ball.reset()

    # Draw paddles and ball
    player1.draw()
    player2.draw()
    ball.draw()

    # Draw scores
    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    # Update screen
    pygame.display.flip()

pygame.quit()
sys.exit()
