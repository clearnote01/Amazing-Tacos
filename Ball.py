import pygame
import math
hillelakamariya = 9*32
class Ballo(pygame.sprite.Sprite):

    def __init__(self, SCREEN, inip):
        self.HMAX = 0
        self.v = 0
        self.offset = 0
        self.upright = False
        self.upleft = False
        self.left = False
        self.right = False
        self.falling = False
        self.down = False
        self.jumping = False
        self.rekt = pygame.Rect(inip[0],inip[1],32, 32)
        self.imgl = pygame.Surface((32, 32))
        self.imgl = pygame.image.load('ball.png')
        self.surf = pygame.Surface((32, 32))
        self.jump = 0
        self.v_y = 32*12
        self.v_x =2
        self.grounded = True
        self.gravity = 32*19
        self.timery = pygame.time.get_ticks()/1000.0
        self.timerz = pygame.time.get_ticks()/1000.0
        self.posy = 0
        self.posx = 0
        self.i = 0

    def timers(self, dirac):
        if dirac == 2:  #up
            self.timery = pygame.time.get_ticks()/1000.0
        if dirac == 1:  #left
            self.timerx = pygame.time.get_ticks()/1000.0
        if dirac == -1: #right
            self.timerl = pygame.time.get_ticks()/1000.0
        if dirac == 0:  #falling
            self.timerz = pygame.time.get_ticks()/1000.0

    def calc_hMAX(self):
        self.HMAX = self.posy - math.sqrt((self.v_y**2)/(2.0*self.gravity))


    def goingup(self):
        if self.rekt.bottom - self.HMAX < 0:
            return True
        else:
            return False
    def move(self):

        """if self.goingup() == False:
            if self.upright == True:
                t = pygame.time.get_ticks()/1000.0 - self.timery
                self.rekt.right +=  self.v_x
                self.rekt.bottom = self.posy - float(self.v_y*t) + (1.0/2)*float(self.gravity*t*t)
            if self.upleft == True:
                t = pygame.time.get_ticks()/1000.0 - self.timery
                self.rekt.right -=  self.v_x
                self.rekt.bottom = self.posy - float(self.v_y*t) + (1.0/2)*float(self.gravity*t*t)
        """

        if self.rekt.bottom > hillelakamariya:
            if self.upright == True:
                t = pygame.time.get_ticks()/1000.0 - self.timery
                self.rekt.right +=  self.v_x
                self.rekt.bottom = self.posy - float(self.v_y*t) + (1.0/2)*float(self.gravity*t*t)
            if self.upleft == True:
                t = pygame.time.get_ticks()/1000.0 - self.timery
                self.rekt.right -=  self.v_x
                self.rekt.bottom = self.posy - float(self.v_y*t) + (1.0/2)*float(self.gravity*t*t)
        else:
            t = pygame.time.get_ticks()/1000.0 - self.timery
            self.v = self.posy - float(self.v_y*t) + (1.0/2)*float(self.gravity*t*t)
            if self.v > hillelakamariya:
                self.rekt.bottom = self.v
            if self.upright == True:
                self.rekt.right +=  self.v_x
            if self.upleft == True:
                self.rekt.right -=  self.v_x
            if float(self.v_y*t) - (1.0)*float(self.gravity*t) < 0:
                self.offset = 5
            else:
                self.offset = 0




    def update(self, SCREEN):
        self.surf = self.imgl
        SCREEN.blit(self.surf, (self.rekt.topleft))

    def hitground(self, platform):
        for i in range(len(platform)):
            if self.rekt.colliderect(platform[i]):
                if self.rekt.bottom >= platform[i].top and self.rekt.top <= platform[i].top:
                    self.up = False
                    self.down = False
                    self.rekt.bottom = platform[i].top
                    self.jump = 0
                    self.i = i

                if self.rekt.top <= platform[i].bottom and self.rekt.bottom >= platform[i].bottom and self.down ==False:
                    self.down = True
                    self.timers(0)
                    self.rekt.top = platform[i].bottom
                    self.posx = self.rekt.bottom

                """if self.rekt.right >= platform[i].left and self.rekt.left <= platform[i].left:
                    self.down = True
                    self.timers(0)
                    self.rekt.right = platform[i].left
                    self.posx = self.rekt.bottom

                if self.rekt.left <= platform[i].right and self.rekt.right >= platform[i].left:
                    self.down = True
                    self.timers(0)
                    self.rekt.right = platform[i].left
                    self.posx = self.rekt.bottom
"""


