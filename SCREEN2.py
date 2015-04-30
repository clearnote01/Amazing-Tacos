__author__ = 'utkarsh'

import pygame
from constants import *
import random
from Ball import *

pygame.init()


#thatparticularsquarewidth = 2*32

class Screens(object):
    def __init__(self):
        self.DSURF = pygame.display.set_mode((width, height))
        self.color = color['WHITE']
        self.DSURF.fill(self.color)
        pygame.display.update()
        self.rek = []

    def _update(self):
        pygame.display.update()


class Line(object):

    def __init__(self, d):
        self.color = color['RED']
        self.y = 0
        self.gap = 8*32
        self.rndy = d
        if self.rndy == 1:
            self._make_blocks_line()
        self.createdanotherline = False

    def _make_blocks_line(self):
        self.v = random.randrange(2, 13)*32

    def _draw_line(self, SURF):
        self.rek_left = pygame.Rect(0, self.y, self.v, 32)
        self.rek_right = pygame.Rect(self.v+self.gap, self.y, width-self.v-self.gap, 32)

        a = pygame.draw.rect(SURF, self.color, self.rek_left)
        pygame.draw.rect(SURF, self.color, self.rek_right)


    def _make_square_in_line(self):
        self.x_cor = random.randrange(self.sqleft, self.sqright)

    def _draw_square_line(self, SURF):
        self.square_surf = pygame.Surface((32, 32))
        self.square_rekt = pygame.Rect(0,0, 32, 32)
        pygame.draw.rect(self.square_surf, self.color, self.square_rekt)
        self.square_surf.set_alpha(50)
        SURF.blit(self.square_surf, (self.x_cor, self.y))
        self.rkt = self.y


screen = Screens()
line = []
a = 'new'

#BALL
ball= Ballo(screen.DSURF, (12*32, 12*32))
print ball.rekt.bottom
count = [1, 2, 2]
m = 0


while True:
    screen.DSURF.fill(screen.color)
    #BALL
    ball.update(screen.DSURF)

    if len(line)!= 0 and ( line[-1].y > thatparticularwidth and line[-1].createdanotherline == False):
        print 'Hallelujah'
        line[-1].createdanotherline = True
        temp = Line(count[m])
        m += 1
        if m == 3:
            m = 0
        if temp.rndy == 2:
            i = len(line) - 1
            flag = 0
            if i == 0:
                temp.sqleft, temp.sqright = line[0].rek_left.right, line[0].rek_right.left
                temp._make_square_in_line()
                line.append(temp)
                flag = 1
            while i != 0:
                if line[i].rndy == 1:
                    temp.sqleft, temp.sqright = line[i].rek_left.right, line[i].rek_right.left
                    temp._make_square_in_line()
                    line.append(temp)
                    break
                i -= 1
            if i == 0 and flag != 1:
                temp.sqleft, temp.sqright = random.randrange(0,200), random.randrange(200, 400)
                temp._make_square_in_line()
                line.append(temp)


        if temp.rndy == 1:
            line.append(temp)
    if a == 'new':
        temp = Line(1)
        m = 1
        line.append(temp)
        a = 'old'

    if a == 'kill' and len(line)!=0:
        print line.pop()

    for i, l in enumerate(line):

        l.y += ball.offset
        if l.y + 32 > height:
            line.pop(i)
        if l.rndy == 1:
            l._draw_line(screen.DSURF)
            l.linepos = l.rek_left.top
        if l.rndy == 2:
            l._draw_square_line(screen.DSURF)
            l.linepos = l.rkt
        #if ball.rekt.colliderect(l.rek_left) or ball.rekt.colliderect(l.rek_left) or  ball.rekt.colliderect(l.rek_left):

    print ball.goingup()


    for event in pygame.event.get():
        if event.type == QUIT:
            safelyexit()
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                safelyexit()

            if event.key == K_RIGHT:
                ball.timers(2)
                ball.upright = True
                ball.upleft = False
                ball.posy = ball.rekt.bottom
                ball.calc_hMAX()
                ball.offset = 0

            if event.key == K_LEFT:
                ball.timers(2)
                ball.upleft = True
                ball.upright = False
                ball.posy = ball.rekt.bottom
                ball.calc_hMAX()
                ball.offset = 0
                ball.calc_hMAX()
    ball.move()
    screen._update()
    fpsClock.tick(FPS)