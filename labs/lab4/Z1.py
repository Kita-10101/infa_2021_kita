print('Картинки на выставку (часть 1)')
print('Создание картин и публикация кода в GitHub')
print('Задание №1 (пробное)')
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (230, 230, 230), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
circle(screen, (255, 0, 0), (160, 175), 22.5)
circle(screen, (0, 0, 0), (160, 175), 22.5, 1)
circle(screen, (255, 0, 0), (240, 175), 20)
circle(screen, (0, 0, 0), (240, 175), 20, 1)
circle(screen, (0, 0, 0), (160, 175), 10)
circle(screen, (0, 0, 0), (240, 175), 10)
polygon(screen, (0, 0, 0), [(115, 100), (125, 90), (205, 170), (195, 180)])
polygon(screen, (0, 0, 0), [(400 - 115, 100), (400 - 125, 90),
                            (400 - 205, 170), (400 - 195, 180)])
polygon(screen, (0, 0, 0), [(175, 275), (175, 285), (225, 285), (225, 275)])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
print()
