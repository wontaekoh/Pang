import os
import pygame

# Initialize pygame
pygame.init()

# Screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("WO Pang")

# FPS
clock = pygame.time.Clock()

# Get current file directory path
current_path = os.path.dirname(__file__)
# Join current path and images folder path
image_path = os.path.join(current_path, "images")

# Creating background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Creating stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # To place character on the stage

# Creating Character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# Event loop
running = True
while running:
    # 30 fps
    dt = clock.tick(30)

    for event in pygame.event.get():  # Checking user input events
        if event.type == pygame.QUIT:
            running = False

    # Drawing images
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, (screen_height - stage_height)))
    screen.blit(character, (character_x_pos, character_y_pos))

    # Updating display
    pygame.display.update()

# pygame Terminate
pygame.quit()
