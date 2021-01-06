import pygame

# Initialize pygame
pygame.init()

# Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Pang Game")

# Loading background image
background = pygame.image.load(
    "C:\\Users\\owt79\\iCloudDrive\\Computer Programming\\Projects\\Pang\\background.png")

# Event loop
running = True
while running:
    for event in pygame.event.get():  # Checking user input events
        if event.type == pygame.QUIT:
            running = False

    # Drawing background img and keep updating
    screen.blit(background, (0, 0))  # screen.fill((0, 0, 255))
    pygame.display.update()

# pygame Terminate
pygame.quit()
