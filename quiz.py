import pygame
###########################################################################################
# 기본 초기화
# Initialize pygame
pygame.init()

# Screen size
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()
###########################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트, 속도 등)

# Event loop
running = True
while running:
    # fps = 30
    dt = clock.tick(30)
    # print("fps: " + str(clock.get_fps()))

    # 2. 이벤트 처리 (키보드, 마우스 등)
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

    # 3. 게임 케릭터 위치 정의
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

    # 4. 충돌 처리

    # 5. 화면에 그리기
    # Drawing background image
    # screen.blit(image, (x_pos, y_pos))

    # Updating display
    pygame.display.update()

# pygame Terminate
pygame.quit()
