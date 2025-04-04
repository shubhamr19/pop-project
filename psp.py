import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player settings
player_width, player_height = 100, 20
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 10

# Falling object settings
object_width, object_height = 30, 30
object_x = random.randint(0, WIDTH - object_width)
object_y = -object_height
object_speed = 5

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Update falling object position
    object_y += object_speed

    # Check for collision
    if (player_x < object_x < player_x + player_width or player_x < object_x + object_width < player_x + player_width) and \
            player_y < object_y + object_height < player_y + player_height:
        score += 1
        object_x = random.randint(0, WIDTH - object_width)
        object_y = -object_height

    # Reset object if it falls off screen
    if object_y > HEIGHT:
        object_x = random.randint(0, WIDTH - object_width)
        object_y = -object_height

    # Draw player and object
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
sys.exit()