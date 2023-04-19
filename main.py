import pygame
import time
import math

RUN_TIME = 100
Width, Height = 1200, 600
surf = pygame.display.set_mode((Width, Height))
surf.fill((0, 0, 0))


def Monk():
    Old_man1 = pygame.image.load('Old_Man_1.3.PNG')
    Old_man2 = pygame.image.load('Old_Man2.png')
    Old_man3 = pygame.image.load('Old_Man3.png')
    OM_Walk1 = pygame.image.load('OM_Walk1.2.png')
    Old_man = [Old_man1, Old_man2, Old_man3, OM_Walk1]
    Old_man_stand = [Old_man1, Old_man2, Old_man3]

    half_size = (int(Old_man1.get_width() / 2), int(Old_man1.get_height() / 2))

    Old_man1 = pygame.transform.smoothscale(Old_man1, half_size)
    Old_man2 = pygame.transform.smoothscale(Old_man2, half_size)
    Old_man3 = pygame.transform.smoothscale(Old_man3, half_size)

    x = 500
    y = 100
    current_image = 1
    speed = 20
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y -= speed
            surf.fill((0, 0, 0))
            surf.blit(Old_man[current_image], (x, y))
            current_image = (current_image + 1) % len(Old_man)
            pygame.display.update()
            pygame.time.delay(50)
        if keys[pygame.K_s]:
            y += speed
            surf.fill((0, 0, 0))
            surf.blit(Old_man[current_image], (x, y))
            current_image = (current_image + 1) % len(Old_man)
            pygame.display.update()
            pygame.time.delay(50)
        if keys[pygame.K_a]:
            x -= speed
            surf.fill((0, 0, 0))
            surf.blit(Old_man[current_image], (x, y))
            current_image = (current_image + 1) % len(Old_man)
            pygame.display.update()
            pygame.time.delay(50)
        if keys[pygame.K_d]:
            x += speed
            surf.fill((0, 0, 0))
            surf.blit(Old_man[current_image], (x, y))
            current_image = (current_image + 1) % len(Old_man)
            pygame.display.update()
            pygame.time.delay(50)
        surf.fill((0, 0, 0))
        surf.blit(Old_man_stand[current_image], (x, y))
        current_image = (current_image + 1) % len(Old_man_stand)
        pygame.display.update()
        pygame.time.delay(200)

# Monk()

def Robot():
    pygame.init()
    Robot_N1 = pygame.image.load('Robot_Neutral.png')
    Robot_N2 = pygame.image.load('Robot_Neutral2.png')
    Robot_N3 = pygame.image.load('Robot_Neutral3.png')
    Finger_N1 = pygame.image.load('Robot_Finger.png')
    Finger_N2 = pygame.image.load('Robot_Slap.png')
    Robot_N = [Robot_N1, Robot_N2, Robot_N3, Robot_N2]
    Finger_N = Finger_N1

    scale_width = 0.5
    scale_height = 0.5

    for idx, robot in enumerate(Robot_N):
        Robot_N[idx] = pygame.transform.scale(robot,
                                              (scale_width * robot.get_width(), scale_height * robot.get_height()))

    bob_speed = 0.25
    bob_amplitude = 20
    bob_counter = 0

    x = 500
    y = 100
    current_image = 1

    dx = (100 - x) / 100  # Distance to travel in x direction per frame
    dy = (100 - y) / 100  # Distance to travel in y direction per frame

    clock = pygame.time.Clock()
    fps_limit = 30

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        #x += dx
        #y += dy

        bob_counter += bob_speed
        bob_offset = bob_amplitude * math.sin(bob_counter)

        surf.fill((0, 0, 0))
        surf.blit(Robot_N[current_image // 8], (x, y + bob_offset))
        current_image = (current_image + 1) % (8 * len(Robot_N))

        pygame.display.update()
        clock.tick(fps_limit)

# Robot()


def Box():
    pygame.init()
    text_box = pygame.image.load('Text_Box.png')
    font = pygame.font.Font('PixeloidMono-VGj6x.ttf', 36)
    text = "Welcome to the game"
    text_surface = font.render('', True, (0, 0, 0))

    w, h = text_box.get_width(), text_box.get_height()
    new_h, new_w = text_box.get_height() / 2, text_box.get_width() / 2
    text_box = pygame.transform.scale(text_box, (new_w, new_h))

    x = 375
    y = 450
    current_char = 0
    current_word = ""
    text_complete = False
    char_timer = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        surf.fill((100, 75, 175))

        if not text_complete:
            char_timer += 5
            if char_timer >= 10:
                current_word += text[current_char]
                text_surface = font.render(current_word, True, (0, 0, 0))
                current_char += 1
                char_timer = 0
                if current_char == len(text):
                    text_complete = True

        surf.blit(text_box, (x, y))
        surf.blit(text_surface, (x + 50, y + 30))
        pygame.display.update()
        pygame.time.delay(50)

# Box()

