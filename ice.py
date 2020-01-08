import pygame, sys, time
from pygame.locals import *
import random


#Colors
colorRed=pygame.Color(241,59,62)
colorPurple=pygame.Color(200,254,249)
colorBlue=pygame.Color(52, 207, 235)
colorGreen=pygame.Color(100,182,100)
colorWhite=pygame.Color(255,250,250)
colorBlack=pygame.Color(0,0,0)
colorOrange=pygame.Color(242,164,0)
colorBrown=pygame.Color(148,103,58)

#Dimensions
w=800
h=600
pygame.init()
fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption ('SUMO')
centerX=w//2
centerY=h//2

#Stage
stageR=250
def stage (centerX,centerY):
    """stage (centerX,centerY) - creates a stage with given centerpoint"""
    pygame.draw.circle(screen, colorBlue, (centerX,centerY),stageR)

#Character 1
xR=int((stageR//10))
x1=int(centerX-(stageR*0.8))
y1=centerY
x1_dir=0
y1_dir=0
def char1 (x1,y1):
    """char1 (x1,y1) - creates char1 at given coordinates"""
    pygame.draw.circle(screen, colorRed, (x1,y1),xR)
print (x1)
print (centerX)

#Character 2
x2=int(centerX+(stageR*0.8))
y2=centerY
x2_dir=0
y2_dir=0
def char2 (x2,y2):
    """char2 (x2,y2) - creates char1 at given coordinates"""
    pygame.draw.circle(screen, colorGreen, (x2,y2),xR)





while True:
    screen.fill(colorBlack)
    for event in pygame.event.get():
        #Game Exit
        if event.type== QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[K_d] or keys[K_a]:
        x1_dir += 0.1 if keys[K_d] else -0.1
    else:
        x1_dir *= 0.98

    if keys[K_w] or keys[K_s]:
        y1_dir += 0.1 if keys[K_s] else -0.1
    else:
        y1_dir *= 0.98
        
#-------------------- CHAR2 MOVEMENT --------------------

    if keys[K_RIGHT] or keys[K_LEFT]:
        x2_dir += 0.1 if keys[K_RIGHT] else -0.1
    else:
        x2_dir *= 0.98

    if keys[K_UP] or keys[K_DOWN]:
        y2_dir += 0.1 if keys[K_DOWN] else -0.1
    else:
        y2_dir *= 0.98
        
        
    stage (centerX,centerY)
    char1 (round(x1),round(y1))
    char2 (round(x2),round(y2))
    x1+=x1_dir
    y1+=y1_dir
    x2+=x2_dir
    y2+=y2_dir
    pygame.display.update()
    fpsClock.tick(60)
