__author__ = 'utkarsh'

import pygame
import sys
from pygame.locals import *
color = {
            'WHITE' : (255, 255, 255),
            'BLACK' : (0, 0, 0),
            'GREEN' : (0, 255, 0),
            'RED' : (255, 0, 0),
            'RED_LIGHT' : (255,128,125),
            'BLUE' : (180, 200, 255),
            'GREY' : (121, 121, 121),
            'BROWN' : (108, 88, 90, 255),
            'DARKGREY' : (60, 60, 60),
            'LIGHT_BROWN' : (255, 176, 75),
            'SKY_BLUE' : (155, 255, 255)
        }

width, height =32*25, 32*18 # 800 x 600
FPS = 60
fpsClock = pygame.time.Clock()
#songname =
thatparticularwidth =3*32
hillelakamariya = 8*32

def safelyexit():
    pygame.quit()
    sys.exit()