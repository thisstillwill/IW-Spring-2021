import sys
from enum import Enum, auto
import pygame
from pygame import cursors
from pygame import key
from pygame import color
from pygame.constants import KMOD_CTRL
from pygame.cursors import tri_right

# Game settings
SIZE = WIDTH, HEIGHT = 800, 800
TITLE = 'Visualizer'
ROWS = 8
COLS = 8
BORDER = 1
w = WIDTH / COLS
h = HEIGHT / ROWS
# Other constants
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)

# All possible gamestates
class GameState(Enum):
    INPUT = auto()
    SEARCH = auto()

# A single vertex in the graph
class Node:
    # All possible node types
    class NodeType(Enum):
        UNBLOCKED = auto()
        BLOCKED = auto()
        START = auto()
        END = auto()
    def __init__(self, x, y) -> None:
        # Position on screen
        self.x = x
        self.y = y
        # Neighboring vertices
        self.neighbors = []
        # Type of node
        self.type = self.NodeType.UNBLOCKED
    def draw(self):
        color = WHITE
        if self.type == self.NodeType.BLOCKED:
            color = BLACK
        elif self.type == self.NodeType.START:
            color = RED
        elif self.type == self.NodeType.END:
            color = BLUE
        pygame.draw.rect(screen, color, (self.x * w + BORDER, self.y * h + BORDER, w - BORDER, h - BORDER))
        pygame.display.update()

# Interact with selected node
def handleMouseClick(x, type):
    t = x[0]
    w = x[1]
    g1 = t // (WIDTH // COLS)
    g2 = w // (HEIGHT // ROWS)
    node = graph[g1][g2]
    node.type = type
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
current_state = GameState.INPUT
while True:
    events = pygame.event.get()
    # Check if user quits the game
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Handle current game state
    if current_state == GameState.INPUT: # Allow user input to edit playfield
        for event in events:
            # Set type of selected node
            mods = pygame.key.get_mods()
            if (pygame.mouse.get_pressed()[1] or mods & 
            pygame.KMOD_CTRL and pygame.mouse.get_pressed()[0]):
                mousePosition = pygame.mouse.get_pos()
                handleMouseClick(mousePosition, Node.NodeType.UNBLOCKED)
            elif pygame.mouse.get_pressed()[0]:
                mousePosition = pygame.mouse.get_pos()
                handleMouseClick(mousePosition, Node.NodeType.BLOCKED)
            # End user input period
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                current_state = GameState.SEARCH
    elif current_state == GameState.SEARCH: # Visualize graph traversal
        pass