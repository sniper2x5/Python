import pygame, sys, time
from pygame.locals import *
import random

#Colors
colorRed=pygame.Color(241,59,62)
colorPurple=pygame.Color(200,254,249)
colorBlue=pygame.Color(107,0,173)
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
pygame.display.set_caption ('Fight')
centerX=w//2
centerY=h//2
#Floor
floor=h-(h//10)
#Character 1
char_height=h//6
x1=centerX//4
y1=floor-(char_height/2)
x1_dir=0
jump1= False
jumpcount1=10
def char1 (x1,y1):
    """char1 (x1,y1) - creates char1 with given dimensions"""
    #hitbox
    pygame.draw.rect(screen, colorRed,(x1,(floor-h//6),w//15,h//6))
print (floor)


while True:
    screen.fill(colorBlack)
    for event in pygame.event.get():
        #Game Exit
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_d:
                x1_dir=10
            if event.key==K_a:
                x1_dir=-10
        if event.type==KEYUP:
            if event.key==K_d:
                if x1_dir<0:
                    pass
                else:
                    x1_dir=0 
            if event.key==K_a:
                if x1_dir>0:
                    pass
                else:
                    x1_dir=0 
                    
                   
                    
#Jump
        if not jump1:
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    jump1=True

    else:
        if jump1==True:
            if jumpcount1>=-10:
                neg1=1
                if jumpcount1<0:
                    neg1=-1
                y1 -=(jumpcount1**2)*0.3*neg1
                jumpcount1-=1
            else:
                jump1= False
                jumpcount1=10
        
        
    char1(x1, y1)
    x1+=x1_dir
    
    pygame.draw.rect(screen, colorWhite, (0,floor,w,h))
    pygame.display.update()
    fpsClock.tick(60)
