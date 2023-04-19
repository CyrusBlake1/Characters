import pygame
import time
import math

RUN_TIME = 100
Width, Height = 1200, 600
surf = pygame.display.set_mode((Width, Height))
surf.fill((0, 0, 0))

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

Box()
