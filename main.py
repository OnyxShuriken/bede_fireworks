#!/usr/bin/python3
__author__ = 'Cole'

#excuse the shit code bby
#your actual bday game is almost done ;D

import pygame
from pygame.locals import *
import random

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("I'M SORRY BEDE PLEASE FORGIVE ME I HAVE NOT FINISHED YOUR GAME")

fireworks = []
explosions = []

special_dict = {1: 'red',
                2: 'cyan',
                3: 'orange',
                4: 'lime',
                5: 'amber',
                6: 'magenta',
                7: 'yellow'}

class colors:
    black = pygame.Color(0, 0, 0)
    orange = pygame.Color(255, 127, 0)
    cyan = pygame.Color(0, 255, 255)
    lime = pygame.Color(191, 255, 0)
    amber = pygame.Color(255, 191, 0)
    yellow = pygame.Color(255, 255, 0)
    red = pygame.Color(255, 0, 0)
    magenta = pygame.Color(255, 0, 255)
    white = pygame.Color(255, 255, 255)

def update():
    del_buffer = []
    if len(fireworks) != 0:
        for i in range(0, len(fireworks)):
            fireworks[i][1] += fireworks[i][3]
            fireworks[i][2] += fireworks[i][4]
            fireworks[i][6] += 1
            if fireworks[i][6] >= 60:
                if random.randint(0, 15) == 0:
                    fireworks[i][5] = True
    if len(explosions) != 0:
        for i in explosions:
            explosions[explosions.index(i)][1] += i[3]
            explosions[explosions.index(i)][2] += i[4]
            if i[1] <=0 or i[2] <= 0:
                explosions.remove(i)
        for i in del_buffer:
            explosions.remove(explosions[i])

def draw():
    if len(fireworks) != 0:
        for i in fireworks:
            if i[5]:
                rando = random.randint(0, 3)
                if rando == 0:
                    explosions.append([i[0], i[1], i[2], 0, 1])
                    explosions.append([i[0], i[1], i[2], 1, 0])
                    explosions.append([i[0], i[1], i[2], 0, -1])
                    explosions.append([i[0], i[1], i[2], -1, 0])
                elif rando == 1:
                    explosions.append([i[0], i[1], i[2], 0, 1])
                    explosions.append([i[0], i[1], i[2], 1, 0])
                    explosions.append([i[0], i[1], i[2], 0, -1])
                    explosions.append([i[0], i[1], i[2], -1, 0])
                    explosions.append([i[0], i[1], i[2], 1, 1])
                    explosions.append([i[0], i[1], i[2], 1, -1])
                    explosions.append([i[0], i[1], i[2], -1, -1])
                    explosions.append([i[0], i[1], i[2], -1, 1])
                elif rando == 2:
                    explosions.append([i[0], i[1], i[2], 0, 1])
                    explosions.append([i[0], i[1], i[2], 1, 0])
                    explosions.append([i[0], i[1], i[2], 0, -1])
                    explosions.append([i[0], i[1], i[2], -1, 0])
                    explosions.append([i[0], i[1], i[2], 1, 1])
                    explosions.append([i[0], i[1], i[2], 1, -1])
                    explosions.append([i[0], i[1], i[2], -1, -1])
                    explosions.append([i[0], i[1], i[2], -1, 1])
                    explosions.append([i[0], i[1], i[2], 0.5, 1])
                    explosions.append([i[0], i[1], i[2], 1, 0.5])
                    explosions.append([i[0], i[1], i[2], 1, -0.5])
                    explosions.append([i[0], i[1], i[2], 0.5, -1])
                    explosions.append([i[0], i[1], i[2], -0.5, -1])
                    explosions.append([i[0], i[1], i[2], -1, -0.5])
                    explosions.append([i[0], i[1], i[2], -1, 0.5])
                    explosions.append([i[0], i[1], i[2], -0.5, 1])
                elif rando == 3:
                    explosions.append([i[0], i[1], i[2], 0, 1])
                    explosions.append([i[0], i[1], i[2], 1, 0])
                    explosions.append([i[0], i[1], i[2], 0, -1])
                    explosions.append([i[0], i[1], i[2], -1, 0])
                    explosions.append([i[0], i[1], i[2], 1, 1])
                    explosions.append([i[0], i[1], i[2], 1, -1])
                    explosions.append([i[0], i[1], i[2], -1, -1])
                    explosions.append([i[0], i[1], i[2], -1, 1])
                    explosions.append([i[0], i[1], i[2], 0.5, 1])
                    explosions.append([i[0], i[1], i[2], 1, 0.5])
                    explosions.append([i[0], i[1], i[2], 1, -0.5])
                    explosions.append([i[0], i[1], i[2], 0.5, -1])
                    explosions.append([i[0], i[1], i[2], -0.5, -1])
                    explosions.append([i[0], i[1], i[2], -1, -0.5])
                    explosions.append([i[0], i[1], i[2], -1, 0.5])
                    explosions.append([i[0], i[1], i[2], -0.5, 1])
                    explosions.append([i[0], i[1], i[2], 0.25, 1])#
                    explosions.append([i[0], i[1], i[2], 0.75, 1])
                    explosions.append([i[0], i[1], i[2], 1, 0.75])
                    explosions.append([i[0], i[1], i[2], 1, 0.25])
                    explosions.append([i[0], i[1], i[2], 1, -0.25])
                    explosions.append([i[0], i[1], i[2], 1, -0.75])
                    explosions.append([i[0], i[1], i[2], -1, 0.25])
                    explosions.append([i[0], i[1], i[2], -1, 0.75])
                    explosions.append([i[0], i[1], i[2], -1, -0.25])
                    explosions.append([i[0], i[1], i[2], -1, -0.75])
                    explosions.append([i[0], i[1], i[2], -0.25, -1])
                    explosions.append([i[0], i[1], i[2], -0.75, -1])
                    explosions.append([i[0], i[1], i[2], 0.25, -1])
                    explosions.append([i[0], i[1], i[2], 0.75, -1])
                    explosions.append([i[0], i[1], i[2], -0.25, 1])
                    explosions.append([i[0], i[1], i[2], -0.75, 1])
                fireworks.remove(i)
            else:
                pygame.draw.rect(screen, colors.white, (i[1] - 5, i[2] - 5, 5, 5))
    if len(explosions) != 0:
        for i in explosions:
            color_dict = {'black': colors.black,
                          'red': colors.red,
                          'cyan': colors.cyan,
                          'orange': colors.orange,
                          'lime': colors.lime,
                          'amber': colors.amber,
                          'magenta': colors.magenta,
                          'yellow': colors.yellow}
            pygame.draw.rect(screen, color_dict[i[0]], (i[1] - 5, i[2] - 5, 5, 5))

fireworks.append(['yellow', 250, 455, 0, -5, False, 0])

while True:
    screen.fill(colors.black)

    update()

    draw()

    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    fireworks.append([special_dict[random.randint(1, 7)], random.randint(100, 400), 455, 0, -5, False, 0])

    pygame.display.update()
    clock.tick(30)
