import pygame

# Initialize pygame
pygame.init()

# Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Pang Game")

# FPS
clock = pygame.time.Clock()

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

# Movement speed
character_speed = 0.5

# Balloon
balloon = pygame.image.load(
    "C:\\Users\\owt79\\iCloudDrive\\Computer Programming\\Projects\\Pang\\balloon.png")
# balloon size
balloon_size = balloon.get_rect().size
balloon_width = balloon_size[0]
balloon_height = balloon_size[1]
# balloon starting position (bottom center)
balloon_x_pos = (screen_width - balloon_width) / 2
balloon_y_pos = (screen_height - balloon_height) / 2

# Font
# Created font object (font, size)
game_font = pygame.font.Font(None, 40)

# Total time
total_time = 60

# Getting start time tick
start_ticks = pygame.time.get_ticks()


# Event loop
running = True
while running:
    # fps = 60
    dt = clock.tick(60)
    # print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get():  # Checking user input events
        if event.type == pygame.QUIT:
            running = False

        # If key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        # If key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # Movement (frame correction)
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

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

    # Rect value update for collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    balloon_rect = balloon.get_rect()
    balloon_rect.left = balloon_x_pos
    balloon_rect.top = balloon_y_pos

    # Collision check
    if character_rect.colliderect(balloon_rect):
        print("Game Over")
        running = False

    # Passby time Calculation (in sec)
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    # Timer
    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))

    # Time out
    if total_time - elapsed_time <= 0:
        print("Time out")
        running = False

    # Drawing background image
    screen.blit(background, (0, 0))  # screen.fill((0, 0, 255))

    # Drawing character
    screen.blit(character, (character_x_pos, character_y_pos))

    # Drawing balloon
    screen.blit(balloon, (balloon_x_pos, balloon_y_pos))

    # Drawing timer
    screen.blit(timer, (10, 10))

    # Updating display
    pygame.display.update()

pygame.time.delay(1000)
# pygame Terminate
pygame.quit()
