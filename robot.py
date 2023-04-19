import pygame
import time
import math

RUN_TIME = 100
Width, Height = 1200, 600
surf = pygame.display.set_mode((Width, Height))
surf.fill((0, 0, 0))


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

        # x += dx
        # y += dy

        bob_counter += bob_speed
        bob_offset = bob_amplitude * math.sin(bob_counter)

        surf.fill((0, 0, 0))
        surf.blit(Robot_N[current_image // 8], (x, y + bob_offset))
        current_image = (current_image + 1) % (8 * len(Robot_N))

        pygame.display.update()
        clock.tick(fps_limit)


Robot()
