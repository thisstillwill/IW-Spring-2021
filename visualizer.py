import argparse
import sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from enum import Enum, auto

import solutions

# Game settings
SIZE = WIDTH, HEIGHT = 800, 800
TITLE = 'Visualizer'
ROWS = 20
COLS = 20
BORDER = 1
PADDING = 20
w = WIDTH / COLS
h = HEIGHT / ROWS
# Other constants
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(128, 128, 128)
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
PURPLE = pygame.Color(128, 0, 128)
GOLD = pygame.Color(255, 215, 0)
GOLDENROD = pygame.Color(218, 165, 32)

# All possible gamestates
class GameState(Enum):
    INPUT = auto()
    DEMO = auto()
    TEST = auto()
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
    def draw(self, screen):
        color = None
        if self.type == self.NodeType.UNBLOCKED:
            color = WHITE
        elif self.type == self.NodeType.BLOCKED:
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
def handleMouseClick(x, type, graph, screen):
    t = x[0]
    w = x[1]
    g1 = t // (WIDTH // COLS)
    g2 = w // (HEIGHT // ROWS)
    node = graph[g1][g2]
    if node.type != Node.NodeType.START and node.type != Node.NodeType.GOAL:
        node.type = type
        node.draw(screen)

# Write a message on the screen
def showMessage(text, font, screen):
    message = font.render(text, True, BLACK)
    message_rect = message.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    pygame.draw.rect(screen, WHITE, message_rect.inflate(PADDING, PADDING))
    pygame.draw.rect(screen, GREY, message_rect.inflate(PADDING, PADDING), BORDER)
    screen.blit(message, message_rect)
    pygame.display.update()

# Depth-first search that recursively explores all reachable nodes
# Adapted from an online article by Educative, Inc.
# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
# Additional references taken from COS 226: Algorithms and Data Structures
# https://www.cs.princeton.edu/courses/archive/fall13/cos226/lectures/41UndirectedGraphs.pdf
def dfs_reference(node, explored, screen):
    if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit()
    if node not in explored:
        if node.type == Node.NodeType.UNBLOCKED:
                pygame.draw.rect(screen, GOLD, (node.x * w + BORDER, node.y * h + BORDER, w - BORDER, h - BORDER))
                pygame.display.update()
        explored.append(node)
        for neighbor in node.neighbors:
            if neighbor.type == Node.NodeType.UNBLOCKED and neighbor not in explored:
                pygame.draw.rect(screen, GOLDENROD, (neighbor.x * w + BORDER, neighbor.y * h + BORDER, w - BORDER, h - BORDER))
                pygame.display.update()
            explored = dfs_reference(neighbor, explored, screen)
    return explored

# Breadth-first search to find the shortest path between two nodes
# Adapted from a blog post by Valerio Valardo on 03/18/2017
# https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
# Additional references taken from COS 226: Algorithms and Data Structures
# https://www.cs.princeton.edu/courses/archive/fall13/cos226/lectures/41UndirectedGraphs.pdf
def bfs_reference(start, goal, screen):
    explored = []
    queue = [[start]]
    if start == goal:
        raise RuntimeError('Start and Goal nodes cannot be the same!')
    while queue:
        if pygame.event.get(pygame.QUIT):
            pygame.quit()
            sys.exit()
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            if node.type == Node.NodeType.UNBLOCKED:
                pygame.draw.rect(screen, GOLD, (node.x * w + BORDER, node.y * h + BORDER, w - BORDER, h - BORDER))
                pygame.display.update()
            for neighbor in node.neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
                if neighbor.type == Node.NodeType.UNBLOCKED and neighbor not in explored:
                    pygame.draw.rect(screen, GOLDENROD, (neighbor.x * w + BORDER, neighbor.y * h + BORDER, w - BORDER, h - BORDER))
                    pygame.display.update()
            explored.append(node)
    raise RuntimeError('No path exists between start and goal nodes!')

def main():
    # Set and parse argumennts
    parser = argparse.ArgumentParser(description='Visualize graph traversal')
    parser.add_argument('algorithm', help="the algorithm to use", choices=['bfs', 'dfs'])
    parser.add_argument('-t', '--test', help='test the selected algorithm', default=False, action='store_true')
    args = parser.parse_args()

    # Initialize game
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(TITLE)

    # Initialize font for messages
    font = pygame.font.SysFont(['systemfont'], 36)

    # Create graph
    screen.fill(GREY)
    graph = [[0 for c in range(COLS)] for r in range(ROWS)]
    for i in range(COLS):
            for j in range(ROWS):
                graph[i][j] = Node(i, j)
                graph[i][j].draw(screen)

    # Set start and end nodes
    start = graph[0][COLS - 1]
    start.type = Node.NodeType.START
    start.draw(screen)
    goal = None
    if args.algorithm == 'bfs':
        goal = graph[ROWS - 1][0]
        goal.type = Node.NodeType.GOAL
        goal.draw(screen)

    # Main game loop
    reference_path = None
    reference_explored = None
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
                elif (pygame.mouse.get_pressed()[2] or (pygame.key.get_mods() & 
                pygame.KMOD_CTRL and pygame.mouse.get_pressed()[0])):
                    mousePosition = pygame.mouse.get_pos()
                    handleMouseClick(mousePosition, Node.NodeType.UNBLOCKED, graph, screen)
                elif pygame.mouse.get_pressed()[0]:
                    mousePosition = pygame.mouse.get_pos()
                    handleMouseClick(mousePosition, Node.NodeType.BLOCKED, graph, screen)
                # End user input period
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Set neighbors of each node
                    for i in range(COLS):
                        for j in range(ROWS):
                            graph[i][j].addNeighbors(graph)
                    current_state = GameState.DEMO
        elif current_state == GameState.DEMO: # Visualize graph traversal
            for event in events:
                # Check if user quits the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    # Select reference algorithm to use
                    if (args.algorithm == 'dfs'):
                        reference_explored = dfs_reference(start, [], screen)
                    elif (args.algorithm == 'bfs'):
                        # Test if no path exists
                        try:
                            reference_path = bfs_reference(start, goal, screen)
                        except RuntimeError as e:
                            showMessage(str(e), font, screen)
                            current_state = GameState.END
                            continue
                        for node in reference_path:
                            if node.type == Node.NodeType.UNBLOCKED:
                                pygame.draw.rect(screen, GREEN, (node.x * w + BORDER, node.y * h + BORDER, w - BORDER, h - BORDER))
                            pygame.display.update()
                    if (args.test):
                            current_state = GameState.TEST
                    else:
                        current_state = GameState.END
        elif current_state == GameState.TEST: # Test student solution
            for event in events:
                # Check if user quits the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Select student algorithm to use
                    if (args.algorithm == 'dfs'):
                        try:
                            solution_explored = solutions.dfs(start, [])
                            # Test for incorrect return type
                            if not all(isinstance(node, Node) for node in solution_explored):
                                raise TypeError
                        except AttributeError:
                            showMessage('Missing solution for ' + args.algorithm + '!', font, screen)
                            current_state = GameState.END
                            continue
                        except TypeError:
                            showMessage('Returned list type is incorrect!', font, screen)
                            current_state = GameState.END
                            continue
                        # Test student solution
                        try:
                            # Test for incorrect list length
                            if len(solution_explored) < len(reference_explored):
                                raise Exception('Student list shorter than expected!')
                            elif len(solution_explored) > len(reference_explored):
                                raise Exception('Student list longer than expected!')
                            # Test all unique reachable nodes found
                            if len(solution_explored) != len(set(solution_explored)):
                                raise Exception('Duplicate nodes found!')
                            for solution_node in solution_explored:
                                # Check if user quits the game
                                if pygame.event.get(pygame.QUIT):
                                    pygame.quit()
                                    sys.exit()
                                if solution_node.type == Node.NodeType.UNBLOCKED:
                                    pygame.draw.rect(screen, PURPLE, (solution_node.x * w + BORDER, solution_node.y * h + BORDER, w - BORDER, h - BORDER))
                                    pygame.display.update()
                        except Exception as e:
                            showMessage(str(e), font, screen)
                        else:
                            showMessage('All tests passed!', font, screen)
                        finally:
                            current_state = GameState.END
                    elif (args.algorithm == 'bfs'):
                        # Run student solution
                        try:
                            solution_path = solutions.bfs(start, goal)
                            # Test for incorrect return type
                            if not all(isinstance(node, Node) for node in solution_path):
                                raise TypeError
                        except AttributeError:
                            showMessage('Missing solution for ' + args.algorithm + '!', font, screen)
                            current_state = GameState.END
                            continue
                        except TypeError:
                            showMessage('Returned path type is incorrect!', font, screen)
                            current_state = GameState.END
                            continue
                        # Test student solution
                        try:
                            # Test for incorrect path length
                            if len(solution_path) < len(reference_path):
                                raise Exception('Student path shorter than expected!')
                            elif len(solution_path) > len(reference_path):
                                raise Exception('Student path longer than expected!')
                            for reference_node, solution_node in zip(reference_path, solution_path):
                                # Test for incorrect node in student path
                                if reference_node != solution_node:
                                    raise Exception('Incorrect node in path!')
                                if solution_node.type == Node.NodeType.UNBLOCKED:
                                    pygame.draw.rect(screen, PURPLE, (solution_node.x * w + BORDER, solution_node.y * h + BORDER, w - BORDER, h - BORDER))
                                    pygame.display.update()
                        except Exception as e:
                            showMessage(str(e), font, screen)
                        else:
                            showMessage('All tests passed!', font, screen)
                        finally:
                            current_state = GameState.END
        elif current_state == GameState.END: # End the game
            for event in events:
                # Check if user quits the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
                else:
                    pass

if __name__ == '__main__':
    main()
