print('Картинки на выставку (часть 1)')
print('Создание картин и публикация кода в GitHub')
print('Задание №1 (на дом)')
import numpy as np
import pygame
import pygame.gfxdraw
from pygame.draw import *

def draw_ellipse_angle(surface, color, rect, angle):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    ellipse(shape_surf, color, (0, 0, *target_rect.size))
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center=target_rect.center))

def igloo(x, y, size):
    circle(screen, "black", (x, y), 150 * size)
    circle(screen, (180, 180, 180), (x, y), 149 * size)
    rect(screen, "white", (x - 160 * size, y, 320 * size, 160 * size))

    line(screen, "black", (x - 150 * size, y), (x + 150 * size, y))
    line(screen, "black", (x - 140 * size, y - 50 * size), (x + 140 * size, y - 50 * size))
    line(screen, "black", (x - 112 * size, y - 100 * size), (x + 112 * size, y - 100 * size))

    line(screen, "black", (x - 70 * size, y - 100 * size), (x - 70 * size, y - 50 * size))
    line(screen, "black", (x - 0 * size, y - 100 * size), (x - 0 * size, y - 50 * size))
    line(screen, "black", (x + 70 * size, y - 100 * size), (x + 70 * size, y - 50 * size))

    line(screen, "black", (x - 90 * size, y - 50 * size), (x - 90 * size, y - 0 * size))
    line(screen, "black", (x - 30 * size, y - 50 * size), (x - 30 * size, y - 0 * size))
    line(screen, "black", (x + 30 * size, y - 50 * size), (x + 30 * size, y - 0 * size))
    line(screen, "black", (x + 90 * size, y - 50 * size), (x + 90 * size, y - 0 * size))

    line(screen, "black", (x - 35 * size, y - 147 * size), (x - 35 * size, y - 100 * size))
    line(screen, "black", (x + 35 * size, y - 147 * size), (x + 35 * size, y - 100 * size))

def fish(x, y):
    polygon(screen, (197, 102, 99), ((x, y - 60), (x - 10, y - 50), (x, y - 40)))
    polygon(screen, (153, 171, 167), ((x - 10, y - 55), (x - 10, y - 65), (x, y - 65), (x + 20, y - 35)))
    polygon(screen, (153, 171, 167), ((x + 20, y - 35), (x + 20, y - 25), (x + 30, y - 35)))
    circle(screen, "blue", (x - 5, y - 60), 3)
    circle(screen, (153, 171, 167), (x - 5, y - 60), 1)

def man(x, y, size, direction):
    head_1_rect = pygame.Rect(x - 40 * size, y - 100 * size, 80 * size, 50 * size)
    ellipse(screen, (220, 220, 220), head_1_rect)

    body_1_rect = pygame.Rect(x - 50 * size, y - 75 * size, 100 * size, 200 * size)
    ellipse(screen, (142, 125, 113), body_1_rect)

    rect(screen, "white", pygame.Rect(x - 50 * size, y + 10 * size, 100 * size, 120 * size))

    leg_1_rect = pygame.Rect(x - 40 * size, y + 5 * size, 30 * size, 40 * size)
    ellipse(screen, (142, 125, 113), leg_1_rect)

    leg_2_rect = pygame.Rect(x + 10 * size, y + 5 * size, 30 * size, 40 * size)
    ellipse(screen, (142, 125, 113), leg_2_rect)

    leg_3_rect = pygame.Rect(x - 50 * size, y + 35 * size, 30 * size, 15 * size)
    ellipse(screen, (142, 125, 113), leg_3_rect)

    leg_4_rect = pygame.Rect(x + 20 * size, y + 35 * size, 30 * size, 15 * size)
    ellipse(screen, (142, 125, 113), leg_4_rect)

    rect(screen, (107, 94, 84), pygame.Rect(x - 50 * size, y + 10 * size, 100 * size, 15 * size))
    rect(screen, (107, 94, 84), pygame.Rect(x - 10 * size, y - 60 * size, 20 * size, 70 * size))

    head_2_rect = pygame.Rect(x - 30 * size, y - 93 * size, 60 * size, 35 * size)
    ellipse(screen, (160, 150, 140), head_2_rect)

    head_3_rect = pygame.Rect(x - 20 * size, y - 85 * size, 40 * size, 25 * size)
    ellipse(screen, (220, 220, 220), head_3_rect)

    head_3_rect = pygame.Rect(x - 20 * size, y - 85 * size, 40 * size, 25 * size)
    ellipse(screen, (220, 220, 220), head_3_rect)

    hand_1_rect = pygame.Rect(x - 75 * size, y - 50 * size, 60 * size, 25 * size)
    ellipse(screen, (142, 125, 113), hand_1_rect)

    hand_1_rect = pygame.Rect(x + 15 * size, y - 50 * size, 60 * size, 25 * size)
    ellipse(screen, (142, 125, 113), hand_1_rect)

    if direction == "left":
        line(screen, "black", (x - 70 * size, y - 90 * size), (x - 70 * size, y + 40 * size))
    if direction == "right":
        line(screen, "black", (x + 70 * size, y - 90 * size), (x + 70 * size, y + 40 * size))

    line(screen, "black", (x - 15 * size, y - 80 * size), (x - 5 * size, y - 75 * size))

    line(screen, "black", (x + 15 * size, y - 80 * size), (x + 5 * size, y - 75 * size))

    smile_1_rect = pygame.Rect(x - 50 * size, y - 70 * size, 100 * size, 100 * size)
    arc(screen, "black", smile_1_rect, np.pi * 5 / 12, np.pi * 7 / 12)

def cat(x, y):
    body_1_rect = pygame.Rect(x + 15, y - 50, 100, 30)
    ellipse(screen, (140, 140, 140), body_1_rect)

    draw_ellipse_angle(screen, (140, 140, 140), (x + 100, y - 70, 13, 80), 70)
    draw_ellipse_angle(screen, (140, 140, 140), (x + 90, y - 60, 13, 80), 60)

    draw_ellipse_angle(screen, (140, 140, 140), (x + 10, y - 70, 13, 80), -70)
    draw_ellipse_angle(screen, (140, 140, 140), (x + 20, y - 60, 13, 80), -60)

    fish(x, y)

    polygon(screen, "white", ((x + 10, y - 60), (x + 10, y - 41), (x + 15, y - 71)))
    polygon(screen, "white", ((x + 20, y - 60), (x + 20, y - 35), (x + 25, y - 71)))

    draw_ellipse_angle(screen, (140, 140, 140), (x + 5, y - 70, 35, 30), 0)

    draw_ellipse_angle(screen, (140, 140, 140), (x + 120, y - 90, 13, 80), -60)

    circle(screen, "white", (x + 15, y - 59), 4)
    circle(screen, "white", (x + 30, y - 57), 4)

    circle(screen, "black", (x + 17, y - 59), 2)
    circle(screen, "black", (x + 32, y - 57), 2)

    polygon(screen, (140, 140, 140), ((x + 30, y - 71), (x + 40, y - 75), (x + 35, y - 60)))
    polygon(screen, (140, 140, 140), ((x + 10, y - 60), (x + 10, y - 75), (x + 15, y - 71)))

    circle(screen, "black", (x + 18, y - 47), 2)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))
screen.fill("white")

polygon(screen, (192, 192, 192), ([0, 0], [600, 0], [600, 400], [0, 400]))

igloo(200, 500, 1)

igloo(180, 550, 0.8)

igloo(260, 600, 0.8)

man(550, 430, 0.5, 'right')

man(400, 400, 0.5, 'left')

man(450, 440, 1, 'right')

man(500, 500, 1, 'right')

man(500, 700, 1.5, 'right')

cat(200, 700)

cat(130, 750)

cat(250, 760)

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
