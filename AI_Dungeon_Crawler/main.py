import pygame
from maze import generate_maze, place_goal, get_grid
from menu import main_menu

# Initialize Pygame
pygame.init()

# Define constants
GRID_SIZE = 40
GRID_WIDTH = 15
GRID_HEIGHT = 15
SCREEN_WIDTH = GRID_SIZE * GRID_WIDTH
SCREEN_HEIGHT = GRID_SIZE * GRID_HEIGHT

# Define colors
WALL_COLOR = (0, 0, 0)
PATH_COLOR = (255, 255, 255)
START_COLOR = (0, 255, 0)
GOAL_COLOR = (255, 0, 0)
OUTLINE_COLOR = (169, 169, 169)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeon Maze")

# Function to draw the grid
def draw_grid(grid, start_pos, goal_pos):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            if (x, y) == start_pos:
                pygame.draw.rect(screen, START_COLOR, rect)
            elif (x, y) == goal_pos:
                pygame.draw.rect(screen, GOAL_COLOR, rect)
            elif grid[y][x] == 1:
                pygame.draw.rect(screen, WALL_COLOR, rect)
            else:
                pygame.draw.rect(screen, PATH_COLOR, rect)
            pygame.draw.rect(screen, OUTLINE_COLOR, rect, 2)

# Function to start the maze
def start_maze():
    # Start position and goal position
    start_pos = (1, 1)
    goal_pos = place_goal()

    # Ensure the start is a path
    grid = get_grid()
    grid[start_pos[1]][start_pos[0]] = 0

    # Generate the maze
    generate_maze(start_pos[0], start_pos[1])

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fill the screen with white
        draw_grid(grid, start_pos, goal_pos)  # Draw the grid
        pygame.display.flip()  # Update the display

    pygame.quit()

# Run the menu first
main_menu()
start_maze()
