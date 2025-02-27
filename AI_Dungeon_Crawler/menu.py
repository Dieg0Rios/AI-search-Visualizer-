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
    text = font.render("Start", True, BLACK)
    button_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, (SCREEN_HEIGHT - BUTTON_HEIGHT) // 2, BUTTON_WIDTH, BUTTON_HEIGHT)
    pygame.draw.rect(screen, GRAY, button_rect)
    screen.blit(text, (button_rect.x + (BUTTON_WIDTH - text.get_width()) // 2, button_rect.y + (BUTTON_HEIGHT - text.get_height()) // 2))
    pygame.display.flip()
    return button_rect

# Menu loop
def main_menu():
    running = True
    button_rect = draw_menu()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Exit menu and start the maze
