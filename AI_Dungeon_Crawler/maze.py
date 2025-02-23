# maze.py
import random

GRID_WIDTH = 15
GRID_HEIGHT = 15

# Create a grid of walls (1 = wall, 0 = open space)
grid = [[1 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Recursive backtracking maze generation
def generate_maze(x, y):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    random.shuffle(directions)

    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2
        if 0 <= nx < GRID_WIDTH and 0 <= ny < GRID_HEIGHT and grid[ny][nx] == 1:
            grid[ny][nx] = 0
            grid[y + dy][x + dx] = 0
            generate_maze(nx, ny)

# Function to find a valid goal position
def place_goal():
    for _ in range(100):
        goal_x = random.randint(1, GRID_WIDTH - 2)
        goal_y = random.randint(1, GRID_HEIGHT - 2)
        if grid[goal_y][goal_x] == 0:
            return (goal_x, goal_y)
    return (GRID_WIDTH - 2, GRID_HEIGHT - 2)

# Function to return the grid
def get_grid():
    return grid
