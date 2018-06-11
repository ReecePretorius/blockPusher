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
HALF_WIDTH = WIDTH/2
HALF_HEIGHT = HEIGHT/2

#COLORS#
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

    imageDictionary = {'bgImage': pygame.image.load('resources/images/title_screen_temp.png')}

    title_menu(imageDictionary['bgImage'], 0, 0)

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            
            print(event)

        pygame.display.update()
        CLOCK.tick(FPS)
    
    pygame.quit()
    quit()

def text_object(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def exit_game():
    pygame.quit()
    quit()
       

def title_menu(img, x, y):
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        #background image
        gameDisplay.blit(img, (x,y))
        #new game button
        button_maker("new game", 330, 360, 470, 400, 80, game_loop)
        #continue button
        button_maker("continue", 340, 420, 460, 460, 140, load_game)
        #quit button
        button_maker("quit", 370, 480, 426, 520, 200, exit_game)
        
        pygame.display.update()
        CLOCK.tick(FPS)
                
    
def button_maker(msg, x1, y1, x2, y2, ypos, clicked = None):
    menuText_new_small = pygame.font.Font('resources/fonts/knifer_0.otf', 48)
    menuText_new_large = pygame.font.Font('resources/fonts/knifer_0.otf', 56)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(mouse)
    if x1 < mouse[0] < x2 and y1 < mouse[1] < y2:
        text, textArea = text_object(msg, menuText_new_large)
        textArea.center = (HALF_WIDTH, HALF_HEIGHT + ypos)
        if click[0] == 1 and clicked != None:
            clicked()
            
    else:
        text, textArea = text_object(msg, menuText_new_small)
        textArea.center = (HALF_WIDTH, HALF_HEIGHT + ypos)
    
    gameDisplay.blit(text, textArea)

def load_game():
    print("continue")

def game_loop():
    print("starting game")
    

if __name__ == "__main__":
    main()