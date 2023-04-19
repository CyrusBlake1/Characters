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

Monk()