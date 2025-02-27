import pygame

# Initialize Pygame
pygame.init()

# Define constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169, 169, 169)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Visualizer")

# Function to draw the menu
def draw_menu():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 50)
    start_text = font.render("Start Game", True, BLACK)
    bfs_text = font.render("BFS", True, BLACK)
    bestfs_text = font.render("BestFS", True, BLACK)
    
    button_start = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, (SCREEN_HEIGHT // 2 - 140), BUTTON_WIDTH, BUTTON_HEIGHT)
    button_bfs = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, (SCREEN_HEIGHT // 2 - 60), BUTTON_WIDTH, BUTTON_HEIGHT)
    button_bestfs = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, (SCREEN_HEIGHT // 2 + 20), BUTTON_WIDTH, BUTTON_HEIGHT)
    
    pygame.draw.rect(screen, GRAY, button_start)
    pygame.draw.rect(screen, GRAY, button_bfs)
    pygame.draw.rect(screen, GRAY, button_bestfs)
    
    screen.blit(start_text, (button_start.x + (BUTTON_WIDTH - start_text.get_width()) // 2, button_start.y + (BUTTON_HEIGHT - start_text.get_height()) // 2))
    screen.blit(bfs_text, (button_bfs.x + (BUTTON_WIDTH - bfs_text.get_width()) // 2, button_bfs.y + (BUTTON_HEIGHT - bfs_text.get_height()) // 2))
    screen.blit(bestfs_text, (button_bestfs.x + (BUTTON_WIDTH - bestfs_text.get_width()) // 2, button_bestfs.y + (BUTTON_HEIGHT - bestfs_text.get_height()) // 2))
    
    pygame.display.flip()
    return button_start, button_bfs, button_bestfs

# Menu loop
running = True
menu_active = True
algorithm = None
while running:
    if menu_active:
        button_start, button_bfs, button_bestfs = draw_menu()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and menu_active:
            if button_start.collidepoint(event.pos):
                algorithm = "Start"
                menu_active = False
            elif button_bfs.collidepoint(event.pos):
                algorithm = "BFS"
                menu_active = False
            elif button_bestfs.collidepoint(event.pos):
                algorithm = "BestFS"
                menu_active = False
                
    if not menu_active and algorithm:
        from main import start_maze  # Importing only when needed to avoid circular import
        start_maze(screen, algorithm)
        running = False  # Exit the loop after starting the maze

pygame.quit()
