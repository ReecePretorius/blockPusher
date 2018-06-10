import sys
import pygame
import random
import os
import copy

from pygame.locals import *

#GLOBALS#
FPS = 30
WIDTH = 800
HEIGHT = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
#########

def main():
    global gameDisplay, CLOCK
    pygame.init()

    gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT)) # window size
    pygame.display.set_caption('blockpusher') # window title
    CLOCK = pygame.time.Clock() #used for framerate, specific game clock

    bgImage = pygame.image.load('title_screen_temp.png')

    title_menu(bgImage, 0, 0)

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            # print(event)

        pygame.display.update()
        CLOCK.tick(FPS)
    
    pygame.quit()
    quit()        

def title_menu(img, x, y):
    gameDisplay.blit(img, (x,y))
    

if __name__ == "__main__":
    main()