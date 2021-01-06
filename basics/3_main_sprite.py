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

# Loading Character(Sprite)
character = pygame.image.load(
    "C:\\Users\\owt79\\iCloudDrive\\Computer Programming\\Projects\\Pang\\character.png")
# Character size
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
# Character position (bottom center)
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height


# Event loop
running = True
while running:
    for event in pygame.event.get():  # Checking user input events
        if event.type == pygame.QUIT:
            running = False

    # Drawing background img
    screen.blit(background, (0, 0))  # screen.fill((0, 0, 255))

    # Drawing character
    screen.blit(character, (character_x_pos, character_y_pos))

    # Updating display
    pygame.display.update()

# pygame Terminate
pygame.quit()
