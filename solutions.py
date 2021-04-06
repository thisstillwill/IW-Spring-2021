# Breadth-first search
def bfs(start, goal):
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