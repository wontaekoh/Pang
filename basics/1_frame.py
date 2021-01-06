import pygame

# Initialize pygame
pygame.init()

# Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Pang Game")

# Event loop
running = True
while running:
    for event in pygame.event.get():  # Checking user input events
        if event.type == pygame.QUIT:
            running = False


# pygame Terminate
pygame.quit()
