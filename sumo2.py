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
x1_right=False
x1_left=False
x1_accel=0
def char1 (x1,y1):
    """char1 (x1,y1) - creates char1 at given coordinates"""
    pygame.draw.circle(screen, colorRed, (x1,y1),xR)
print (x1)
print (centerX)

    

    

while True:
    screen.fill(colorBlack)
    for event in pygame.event.get():
        #Game Exit
        if event.type== QUIT:
            pygame.quit()
            sys.exit()
        
        while x1_right==True:
            x1_dir+=1
        while x1_left==True:
            x1_dir-=1
            
        if event.type==KEYDOWN:
            if event.key==K_d:
                x1_dir+=1
                x1_accel=1
                x1_right=True
            if event.key==K_a:
                x1_dir-=1
                x1_left=True
            if event.key==K_w:
                y1_dir-=1
            if event.key==K_s:
                y1_dir+=1
        if event.type==KEYUP:
            if event.key==K_d:
                x1_right=False
            if event.key==K_a:
                x1_left=False

        
        print(x1_dir)

                
    stage (centerX,centerY)
    char1 (x1,y1)
    x1_dir=x1_dir+x1_accel
    x1+=x1_dir
    y1+=y1_dir
