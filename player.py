import pygame

class Player:
    def __init__(self, screen):
        self.x = 200
        self.y = 300

        self.ani_speed_init = 5
        self.ani_speed = self.ani_speed_init
        self.aniL = ['resources/characters/triangle/left1.png','resources/characters/triangle/left2.png','resources/characters/triangle/left3.png','resources/characters/triangle/left4.png']
        self.aniR = ['resources/characters/triangle/right1.png','resources/characters/triangle/right2.png','resources/characters/triangle/right3.png','resources/characters/triangle/right4.png']
        self.aniL.sort()
        self.aniR.sort()
        self.ani_pos = 0
        self.ani_max = len(self.aniL) - 1
        self.img = pygame.image.load(self.aniL[0])
        self.update(0, screen, 'left')

    def update(self, pos, screen, direction):
        if pos != 0:
            self.ani_speed -= 1
            self.x += pos
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
        return(screen.blit(self.img, (self.x, self.y)))
