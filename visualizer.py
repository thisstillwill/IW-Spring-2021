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
GREEN = pygame.Color(0, 255, 0)

# All possible gamestates
class GameState(Enum):
    INPUT = auto()
    SEARCH = auto()
    END = auto()

# A single vertex in the graph
class Node:
    # All possible node types
    class NodeType(Enum):
        UNBLOCKED = auto()
        BLOCKED = auto()
        START = auto()
        GOAL = auto()
    # Create a new node
    def __init__(self, x, y) -> None:
        # Position on screen
        self.x = x
        self.y = y
        # Neighboring vertices
        self.neighbors = []
        # Type of node
        self.type = self.NodeType.UNBLOCKED
    # Draw the node on the screen
    def draw(self):
        color = WHITE
        if self.type == self.NodeType.BLOCKED:
            color = BLACK
        elif self.type == self.NodeType.START:
            color = RED
        elif self.type == self.NodeType.GOAL:
            color = BLUE
        pygame.draw.rect(screen, color, (self.x * w + BORDER, self.y * h + BORDER, w - BORDER, h - BORDER))
        pygame.display.update()
    # Connect the node to each of its neighbors
    def addNeighbors(self, graph):
        x = self.x
        y = self.y
        if x < COLS-1 and graph[self.x + 1][y].type != Node.NodeType.BLOCKED:
            self.neighbors.append(graph[self.x + 1][y])
        if x > 0 and graph[self.x - 1][y].type != Node.NodeType.BLOCKED:
            self.neighbors.append(graph[self.x - 1][y])
        if y < ROWS-1 and graph[self.x][y + 1].type != Node.NodeType.BLOCKED:
            self.neighbors.append(graph[self.x][y + 1])
        if y > 0 and graph[self.x][y - 1].type != Node.NodeType.BLOCKED:
            self.neighbors.append(graph[self.x][y - 1])

# Interact with selected node
def handleMouseClick(x, type, graph):
    t = x[0]
    w = x[1]
    g1 = t // (WIDTH // COLS)
    g2 = w // (HEIGHT // ROWS)
    node = graph[g1][g2]
    if node.type != node.NodeType.START and node.type != node.NodeType.GOAL:
        node.type = type
        node.draw()

# Breadth-first search to find the shortest path between two nodes
# Adapted from a blog post by Valerio Valardo on 03/18/2017
# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
def bfs_shortest_path(start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        raise RuntimeError('Start and Goal nodes cannot be the same!')
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            for neighbor in node.neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            explored.append(node)
    raise RuntimeError('No path exists between start and goal nodes!')

# Initialize game
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Create graph
screen.fill(GREY)
graph = [[0 for c in range(COLS)] for r in range(ROWS)]
for i in range(COLS):
        for j in range(ROWS):
            graph[i][j] = Node(i, j)
            graph[i][j].draw()

# Set start and end nodes
start = graph[0][COLS - 1]
start.type = Node.NodeType.START
start.draw()
goal = graph[ROWS - 1][0]
goal.type = Node.NodeType.GOAL
goal.draw()

# Main game loop
current_state = GameState.INPUT
while True:
    events = pygame.event.get()
    # Handle current game state
    if current_state == GameState.INPUT: # Allow user input to edit playfield
        for event in events:
            # Check if user quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Set type of selected node
            elif (pygame.mouse.get_pressed()[1] or pygame.key.get_mods() & 
            pygame.KMOD_CTRL and pygame.mouse.get_pressed()[0]):
                mousePosition = pygame.mouse.get_pos()
                handleMouseClick(mousePosition, Node.NodeType.UNBLOCKED, graph)
            elif pygame.mouse.get_pressed()[0]:
                mousePosition = pygame.mouse.get_pos()
                handleMouseClick(mousePosition, Node.NodeType.BLOCKED, graph)
            # End user input period
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Set neighbors of each node
                for i in range(COLS):
                    for j in range(ROWS):
                        graph[i][j].addNeighbors(graph)
                current_state = GameState.SEARCH
    elif current_state == GameState.SEARCH: # Visualize graph traversal
        for event in events:
            # Check if user quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                path = bfs_shortest_path(start, goal)
                for node in path:
                    if node != start and node != goal:
                        pygame.draw.rect(screen, GREEN, (node.x * w + BORDER, node.y * h + BORDER, w - BORDER, h - BORDER))
                        pygame.display.update()
                current_state = GameState.END
    elif current_state == GameState.END: # End the game
        for event in events:
            # Check if user quits the game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                pass
