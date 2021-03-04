import sys
import pygame

# Constants
SIZE = WIDTH, HEIGHT = 800, 800
TITLE = 'Visualizer'

# Initialize game
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Main game loop
while True:
    # Handle events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw red background on screen
    screen.fill(pygame.Color(255,0,0))
    pygame.display.update()
