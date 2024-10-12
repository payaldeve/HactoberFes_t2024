import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dance Challenge Game")

# Load fonts
font = pygame.font.SysFont(None, 55)

# Game variables
score = 0
game_running = True

# Function to display score
def display_score(score):
    score_surface = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_surface, (10, 10))

# Main game loop
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Clear the screen
    screen.fill(WHITE)

    # Display score
    display_score(score)

    # Simulate scoring (for demonstration purposes)
    if random.randint(1, 100) > 95:  # Random chance to score
        score += 1

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(FPS)

# Quit Pygame
pygame.quit()
