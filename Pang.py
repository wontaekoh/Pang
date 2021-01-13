import os
import pygame

# Initializing pygame
pygame.init()

# Screen size
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("WO Pang")

# for FPS
clock = pygame.time.Clock()

# Get current file directory path
current_path = os.path.dirname(__file__)

# Join current path and images folder path
image_path = os.path.join(current_path, "images")

# Creating background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Creating stage
stage = pygame.image.load(os.path.join(image_path, "stage.jpg"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # To place character on the stage

# Creating Character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

# Character movement
to_x_LEFT = 0
to_x_RIGHT = 0
character_speed = 0.25

# Creating weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_speed = 10

# Multiple weapons
weapons = []

# Creating balloons
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png")),
    pygame.image.load(os.path.join(image_path, "balloon5.png"))]

# Balloon speed
ball_speed_y = [-18, -15, -13, -11, -9]

# Balloon initiation
balls = []
balls.append({
    "pos_x": 50,
    "pos_y": 50,
    "img_index": 0,  # biggest ball
    "to_x": 3,  # x axis movement to right
    "to_y": -6,  # y axis movement to up
    "init_speed_y": ball_speed_y[0]  # balloon init bouncing speed
})

# Remove balls and weapon variables
weapon_remove = -1
ball_remove = -1

# Font object (font, size)
game_font = pygame.font.Font(None, 40)

# Game Terminate message
game_result = "Game Over"

# Starting time tick
start_ticks = pygame.time.get_ticks()

# Total time
total_time = 100


# Event loop
running = True
while running:
    # 30 FPS
    dt = clock.tick(30)

    for event in pygame.event.get():  # Checking user input events
        if event.type == pygame.QUIT:
            running = False

        # If key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x_LEFT -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_RIGHT += character_speed
            elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                weapon_x_pos = character_x_pos + \
                    (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        # If key is released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_x_LEFT = 0
            elif event.key == pygame.K_RIGHT:
                to_x_RIGHT = 0

    # Movement (frame correction)
    character_x_pos += (to_x_LEFT + to_x_RIGHT) * dt

    # Restriction in Horizontal movement
    if character_x_pos <= 0:
        character_x_pos = 0
    elif character_x_pos > (screen_width - character_width):
        character_x_pos = (screen_width - character_width)

    # Weapon movement upward
    # w[0]: x_pos, w[1]: y_pos | only y_pos changes
    weapons = [[w[0], (w[1] - weapon_speed)] for w in weapons]
    # Removing weapon reached to the top
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # Balloon movement
    for ball_index, ball_value in enumerate(balls):
        # print(ball_index, ball_value)
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_img_idx = ball_value["img_index"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # Ball move restriction in x-axis (bounce back to left or right)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_value["to_x"] = ball_value["to_x"] * -1
        # If ball reaches to the bottom -> bounce back up
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_value["to_y"] = ball_value["init_speed_y"]
        else:
            # gravity effect -> parabola movement
            ball_value["to_y"] += 0.5

        ball_value["pos_x"] += ball_value["to_x"]
        ball_value["pos_y"] += ball_value["to_y"]

    # Collision
    # Character rect value update for collision
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # Collision check for all balls in its list
    for ball_index, ball_value in enumerate(balls):
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_img_idx = ball_value["img_index"]

        # Ball rect value update
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # Collision check (character and balls)
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # Collision check (weapons and balls)
        for weapon_index, weapon_value in enumerate(weapons):
            weapon_pos_x = weapon_value[0]
            weapon_pos_y = weapon_value[1]

            # Weapon rect value update
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y

            # Collision check
            if weapon_rect.colliderect(ball_rect):
                weapon_remove = weapon_index
                ball_remove = ball_index

                # If not the smallest ball, divide collided balls
                if ball_img_idx < 4:
                    # Current ball info
                    ball_width = ball_rect.size[0]
                    ball_height = ball_rect.size[1]

                    # Divided ball info
                    small_ball_rect = ball_images[ball_img_idx + 1].get_rect()
                    small_ball_width = ball_size[0]
                    small_ball_height = ball_size[1]

                    # Moves to left
                    balls.append({
                        "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_index": ball_img_idx + 1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_speed_y": ball_speed_y[ball_img_idx + 1]
                    })
                    # Moves to right
                    balls.append({
                        "pos_x": ball_pos_x + (ball_width / 2) - (small_ball_width / 2),
                        "pos_y": ball_pos_y + (ball_height / 2) - (small_ball_height / 2),
                        "img_index": ball_img_idx + 1,
                        "to_x": 3,
                        "to_y": -6,
                        "init_speed_y": ball_speed_y[ball_img_idx + 1]
                    })
                break  # break out second for statement
        else:
            continue
        break  # break out first for statement

    # Collide ball or weapon removal
    if ball_remove > -1:
        del balls[ball_remove]
        ball_remove = -1

    if weapon_remove > -1:
        del weapons[weapon_remove]
        weapon_remove = -1

    # Game Success
    if len(balls) == 0:
        game_result = "Mission Complete"
        running = False

    # Drawing images
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_index"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, (screen_height - stage_height)))

    screen.blit(character, (character_x_pos, character_y_pos))

    # Passby time Calculation (in sec)
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    # Timer
    timer = game_font.render("Time: {}".format(
        int(total_time - elapsed_time)), True, (255, 255, 255))

    screen.blit(timer, (10, 10))

    # Time out
    if total_time - elapsed_time <= 0:
        game_result = "Time Over"
        running = False

    # Updating display
    pygame.display.update()


# Terminate message
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center=(int(screen_width / 2), int(screen_height / 2)))
screen.blit(msg, msg_rect)
pygame.display.update()

pygame.time.delay(2000)
# pygame Terminate
pygame.quit()
