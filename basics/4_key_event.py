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
# Character starting position (bottom center)
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

# Coordination
to_x = 0
to_y = 0

# Event loop
running = True
while running:
    for event in pygame.event.get():  # Checking user input events
        if event.type == pygame.QUIT:
            running = False

        # If key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 0.2
            elif event.key == pygame.K_RIGHT:
                to_x += 0.2
            elif event.key == pygame.K_UP:
                to_y -= 0.2
            elif event.key == pygame.K_DOWN:
                to_y += 0.2
        # If key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # Movement
    character_x_pos += to_x
    character_y_pos += to_y

    # Restriction in Horizontal movement
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    # Restriction in Vertical movement
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > (screen_height - character_height):
        character_y_pos = (screen_height - character_height)

    # Drawing background image
    screen.blit(background, (0, 0))  # screen.fill((0, 0, 255))

    # Drawing character
    screen.blit(character, (character_x_pos, character_y_pos))

    # Updating display
    pygame.display.update()

# pygame Terminate
pygame.quit()
