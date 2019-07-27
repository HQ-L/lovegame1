# Filename: The First Game about love
# author: Huiqi Li

# import these package
import pygame, sys, random, os

# INIT pygame and pygame's music player
pygame.init()
pygame.mixer.init()
# music's path
msc = 'msc\\花澤香菜 - 恋愛サーキュレーション.mp3'
# load it
pygame.mixer.music.load(msc)
# start playing
pygame.mixer.music.play()
# set the size of screen and set Fullscreen
size = width, height = 1500, 800
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# debug now it is useless
# screen = pygame.display.set_mode(size)
# set the background picture and the first page's element, and then load them
bg = pygame.image.load('img\\bg.jpg')
button1 = pygame.image.load('img\\button1.png')
button2 = pygame.image.load('img\\button2.png')
title1 = pygame.image.load('img\\title1.png')
button1rect = button1.get_rect()
button2rect = button2.get_rect()
# Initializes a position
button2rect.left = 900
button2rect.top = 600
# this flag is responsible for jumping pages
flag = False

# infinite loop
while True:
    # traversal events
    for event in pygame.event.get():
        # if the operation is to press the keyboard
        if event.type == pygame.KEYDOWN:
            # if the operation is to press "Esc"
            if event.key == pygame.K_ESCAPE:
                # exit
                sys.exit()
        # if the operation is moving the mouse
        if event.type == pygame.MOUSEMOTION:
            # when mouse is in button2
            if event.pos[0] in range(button2rect.left, button2rect.right) and event.pos[1] in range(button2rect.top, button2rect.bottom):
                num1 = random.randint(0, 1500)
                num2 = random.randint(0, 800)
                # move button2
                button2rect.center = (num1, num2)
        # if the operation is click mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse in button1
            if event.pos[0] in range(400, 605) and event.pos[1] in range(600, 800):
                # if the operation is clicking the left key
                if event.button == 1:
                    # falg = True
                    flag = True
    # set these element
    screen.blit(bg, [0, 0])
    screen.blit(button1, [400, 600])
    screen.blit(button2, button2rect)
    screen.blit(title1, [50, 200])
    # update
    pygame.display.update()
    # if flag == true, then strat jumping pages
    if flag:
        pygame.quit()
        break

# INIT and set the page two's element
screen1 = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.mixer.init()
words = pygame.image.load('img\\words.png')
pygame.mixer.music.load(msc)
pygame.mixer.music.play()

# same as above
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()

    screen1.blit(bg, [0, 0])
    screen1.blit(words, [50, 200])
    pygame.display.update()
