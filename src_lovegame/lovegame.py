# Filename: The First Game about love

import pygame, sys, random, os

pygame.init()
pygame.mixer.init()
msc = 'msc\\花澤香菜 - 恋愛サーキュレーション.mp3'
pygame.mixer.music.load(msc)
pygame.mixer.music.play()
size = width, height = 1500, 800
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# screen = pygame.display.set_mode(size)
bg = pygame.image.load('img\\bg.jpg')
button1 = pygame.image.load('img\\button1.png')
button2 = pygame.image.load('img\\button2.png')
title1 = pygame.image.load('img\\title1.png')
button1rect = button1.get_rect()
button2rect = button2.get_rect()
button2rect.left = 900
button2rect.top = 600
flag = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if event.pos[0] in range(button2rect.left, button2rect.right) and event.pos[1] in range(button2rect.top, button2rect.bottom):
                num1 = random.randint(0, 1500)
                num2 = random.randint(0, 800)
                button2rect.center = (num1, num2)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(400, 605) and event.pos[1] in range(600, 800):
                if event.button == 1:
                    flag = True
    screen.blit(bg, [0, 0])
    screen.blit(button1, [400, 600])
    screen.blit(button2, button2rect)
    screen.blit(title1, [50, 200])
    pygame.display.update()
    if flag:
        pygame.quit()
        break

screen1 = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.mixer.init()
words = pygame.image.load('img\\words.png')
pygame.mixer.music.load(msc)
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    screen1.blit(bg, [0, 0])
    screen1.blit(words, [50, 200])
    pygame.display.update()