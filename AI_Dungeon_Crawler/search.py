from collections import deque

def bfs(start, goal, grid):
    """Perform BFS to find the path from start to goal."""
    queue = deque([start])
    parent = {start: None}
    visited = set([start])

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            if 0 <= neighbor[0] < len(grid[0]) and 0 <= neighbor[1] < len(grid):
                if grid[neighbor[1]][neighbor[0]] == 0 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    path.reverse()

    return path