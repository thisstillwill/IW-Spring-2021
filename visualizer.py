import sys
import pygame
from pygame.constants import KMOD_CTRL
from pygame.cursors import tri_right

# Game settings
SIZE = WIDTH, HEIGHT = 800, 800
TITLE = 'Visualizer'
ROWS = 8
COLS = 8
BORDER = 4
w = WIDTH / COLS
h = HEIGHT / ROWS
# Constants
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
BLACK = pygame.Color(0, 0, 0)

# A single vertex in the graph
class Node:
    def __init__(self, x, y) -> None:
        # Position on screen
        self.x = x
        self.y = y
        # Neighboring vertices
        self.neighbors = []
        # Is blocked
        self.blocked = False
    def draw(self):
        color = BLACK if self.blocked else WHITE
        pygame.draw.rect(screen, color, (self.x * w + BORDER, self.y * h + BORDER, w - BORDER, h - BORDER))
        pygame.display.update()

# Handle mouse click
def handleMouseClick(x, block):
    t = x[0]
    w = x[1]
    g1 = t // (WIDTH // COLS)
    g2 = w // (HEIGHT // ROWS)
    node = graph[g1][g2]
    node.blocked = True if block else False
    node.draw()

# Initialize game
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Create nodes
screen.fill(GREY)
graph = [[0 for c in range(COLS)] for r in range(ROWS)]
for i in range(COLS):
        for j in range(ROWS):
            graph[i][j] = Node(i, j)
            graph[i][j].draw()

# Main game loop
while True:
    # Handle events
    events = pygame.event.get()
    for event in events:
        mods = pygame.key.get_mods()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif (pygame.mouse.get_pressed()[1] or mods & 
        pygame.KMOD_CTRL and pygame.mouse.get_pressed()[0]):
            mousePosition = pygame.mouse.get_pos()
            handleMouseClick(mousePosition, False)
        elif pygame.mouse.get_pressed()[0]:
            mousePosition = pygame.mouse.get_pos()
            handleMouseClick(mousePosition, True)
