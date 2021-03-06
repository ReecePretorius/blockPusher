import sys
import pygame
import random
import os
import copy

import player

from pygame.locals import *

#GLOBALS#
FPS = 60
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
    global gameDisplay, CLOCK, levelDict
    levelDict = {}
    pygame.init()

    gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT)) # window size
    pygame.display.set_caption('blockpusher') # window title
    CLOCK = pygame.time.Clock() #used for framerate, specific game clock
    
    #Dictionary of images used to construct menus and playing fields
    imageDictionary = {'bgImage': pygame.image.load('resources/images/title_screen.png'),
                       'grid': pygame.image.load('resources/images/40x40Grid.png'),
                       'back_wall': pygame.image.load('resources/images/wall_pieces/back_wall.png'),
                       'left_wall': pygame.image.load('resources/images/wall_pieces/left_wall.png'),
                       'bottom_wall': pygame.image.load('resources/images/wall_pieces/bottom_wall.png'),
                       'right_wall': pygame.image.load('resources/images/wall_pieces/right_wall.png'),
                       'floor': pygame.image.load('resources/images/wall_pieces/floor.png')}
    
    #construct dictionary of levels
    getLevels = read_level_file()
    for i in range(3):
        levelDict[i] = getLevels[i + 1]

    print(levelDict)    

    title_menu(imageDictionary['bgImage'], 0, 0)
    
    player1 = player.Player(gameDisplay)
    xpos, ypos = 0, 0
    xspeed, yspeed = 0, 0
    direction = 'up'

    player_width = player1.get_dimensions('w')
    player_height = player1.get_dimensions('h')

    print(player_width,player_height)

    #main game loop#############################################
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    #walk right
                    print('walking right')
                    xspeed = 2
                    direction = 'right'
                elif event.key == pygame.K_a:
                    #walk left
                    print('walking left')
                    xspeed = -2
                    direction = 'left'
                elif event.key == pygame.K_w:
                    #walk forward
                    print('walking forward')
                    yspeed = -2
                    direction = 'up'
                elif event.key == pygame.K_s:
                    #walk down
                    print('walking down')
                    yspeed = 2
                    direction = 'down'
                elif event.key == pygame.K_ESCAPE:
                    print('closing')
                    pygame.quit()
                    quit()
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    #walk right
                    xpos = 0
                    xspeed = 0
                    direction = 'right'    
                elif event.key == pygame.K_a:
                    #walk left
                    xpos = 0
                    xspeed = 0
                    direction = 'left'
                elif event.key == pygame.K_w:
                    #walk forward
                    ypos = 0
                    yspeed = 0
                    direction = 'up'
                elif event.key == pygame.K_s:
                    #walk down
                    ypos = 0
                    yspeed = 0
                    direction = 'down'        
            print(event)

        xpos = xspeed
        ypos = yspeed

        build_level(imageDictionary, 0, 0)
        player1.update(xpos, ypos, gameDisplay, direction)
        pygame.display.update()
        CLOCK.tick(FPS)
    pygame.quit()
    quit()
    #############################################################

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
                pygame.quit()
                quit()
        
        #background image
        gameDisplay.blit(img, (x,y))
        #new game button
        press = button_maker("new game", 330, 360, 470, 400, 80, None)
        #continue button
        button_maker("continue", 340, 420, 460, 460, 140, load_game)
        #quit button
        button_maker("quit", 370, 480, 426, 520, 200, exit_game)
        
        if press == 'start':
            return

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
            text, textArea = text_object(msg, menuText_new_small)
            textArea.center = (HALF_WIDTH, HALF_HEIGHT + ypos)
            gameDisplay.blit(text, textArea)
            clicked()
        elif click[0] == 1 and clicked == None:
            return('start')   
            
    else:
        text, textArea = text_object(msg, menuText_new_small)
        textArea.center = (HALF_WIDTH, HALF_HEIGHT + ypos)
    
    gameDisplay.blit(text, textArea)

def read_level_file():
    levelsFile = open("resources/levels/levels.txt", "r")
    templevel = []
    levelObject = []

    for line in levelsFile:
        line = line.rstrip()
        templevel.append(line)
        levelObject = [l.split(',') for l in ','.join(templevel).split('::')]  

    levelObject.remove([''])
    #print(levelObject) 
    levelsFile.close()
    return levelObject   

def get_character():
    pass

def build_level(dict, x, y):
    gameDisplay.blit(dict['floor'], (40,80))
    gameDisplay.blit(dict['back_wall'], (x,y))
    gameDisplay.blit(dict['left_wall'], (x,y))
    gameDisplay.blit(dict['right_wall'], (760,y))
    gameDisplay.blit(dict['bottom_wall'], (40,560))

def is_wall():
    pass

def run_level():
    pass    

def redraw_level():
    pass        

def load_game():
    print("continue")
    
if __name__ == "__main__":
    main()