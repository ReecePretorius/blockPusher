import pygame

class Player:
    def __init__(self, screen):
        self.x = 360
        self.y = 240

        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.aniL = ['resources/characters/tim/tim_left.png','resources/characters/tim/tim_left2.png']
        self.aniR = ['resources/characters/tim/tim_right.png','resources/characters/tim/tim_right2.png']
        self.aniU = ['resources/characters/tim/tim_up.png','resources/characters/tim/tim_up2.png']
        self.aniD = ['resources/characters/tim/tim_left.png','resources/characters/tim/tim_left2.png']

        #sprite width and hight
        self.sprite = pygame.image.load(self.aniL[0])
        self.s_width = self.sprite.get_size()[0]
        self.s_height = self.sprite.get_size()[1]

        self.ani_pos = 0
        self.ani_max = len(self.aniL) - 1
        self.img = pygame.image.load(self.aniU[0])
        self.update(0, 0, screen, 'up')

    def get_dimensions(self, dim):
        if dim == 'w':
            return self.s_width
        else:
            return self.s_height

    def update(self, xpos, ypos, screen, direction):
        if xpos != 0 or ypos != 0:
            self.ani_speed -= 1
            self.x += xpos
            self.y += ypos
            if self.ani_speed == 0:
                if direction == 'right':
                    self.img = pygame.image.load(self.aniR[self.ani_pos])
                    self.ani_speed = self.ani_speed_init
                    if self.ani_pos == self.ani_max:
                        self.ani_pos = 0
                    else:
                        self.ani_pos += 1
                elif direction == 'left':
                    self.img = pygame.image.load(self.aniL[self.ani_pos])
                    self.ani_speed = self.ani_speed_init
                    if self.ani_pos == self.ani_max:
                        self.ani_pos = 0
                    else:
                        self.ani_pos += 1
                elif direction == 'up':
                    self.img = pygame.image.load(self.aniU[self.ani_pos])
                    self.ani_speed = self.ani_speed_init
                    if self.ani_pos == self.ani_max:
                        self.ani_pos = 0
                    else:
                        self.ani_pos += 1
                elif direction == 'down':
                    self.img = pygame.image.load(self.aniD[self.ani_pos])
                    self.ani_speed = self.ani_speed_init
                    if self.ani_pos == self.ani_max:
                        self.ani_pos = 0
                    else:
                        self.ani_pos += 1                        
        return(screen.blit(self.img, (self.x, self.y)))
