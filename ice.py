import pygame, sys, time
from pygame.locals import *
import random
import math

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


def game():
    
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
    x1_win=0
    def char1 (x1,y1):
        """char1 (x1,y1) - creates char1 at given coordinates"""
        pygame.draw.circle(screen, colorRed, (x1,y1),xR)
    
    #Character 2
    x2=int(centerX+(stageR*0.8))
    y2=centerY
    x2_dir=0
    y2_dir=0
    x2_win=0
    def char2 (x2,y2):
        """char2 (x2,y2) - creates char1 at given coordinates"""
        pygame.draw.circle(screen, colorGreen, (x2,y2),xR)
    
    game_over=False
    
    def score ():
        pygame.draw.circle(screen, colorOrange, (50,30), (int(xR-5)))
        pygame.draw.circle(screen, colorBlack, (50,30), (int(xR-10)))
        pygame.draw.circle(screen, colorOrange, (100,30), (int(xR-5)))
        pygame.draw.circle(screen, colorBlack, (100,30), (int(xR-10)))
        pygame.draw.circle(screen, colorOrange, (150,30), (int(xR-5)))
        pygame.draw.circle(screen, colorBlack, (150,30), (int(xR-10)))
        
        pygame.draw.circle(screen, colorOrange, (750,30), (int(xR-5)))
        pygame.draw.circle(screen, colorBlack, (750,30), (int(xR-10)))
        pygame.draw.circle(screen, colorOrange, (700,30), (int(xR-5)))
        pygame.draw.circle(screen, colorBlack, (700,30), (int(xR-10)))
        pygame.draw.circle(screen, colorOrange, (650,30), (int(xR-5)))
        pygame.draw.circle(screen, colorBlack, (650,30), (int(xR-10)))
    
    def x1score ():
        if x1_win>0:
            pygame.draw.circle(screen, colorOrange, (50,30), (int(xR-5)))
        elif x1_win>1:
            pygame.draw.circle(screen, colorOrange, (100,30), (int(xR-5)))
        elif x1_win>2:
            pygame.draw.circle(screen, colorOrange, (150,30), (int(xR-5)))
            
    while game_over==False:
        screen.fill(colorBlack)
        for event in pygame.event.get():
            #Game Exit
            if event.type== QUIT:
                pygame.quit()
                sys.exit()
                
    # ~~~~~~~~~~ COLLISION DETECTION ~~~~~~~~~~~
    
        v12 = pygame.math.Vector2(x1-x2, y1-y2)
        distance = v12.length()
        hit_dist = 2*xR
        if distance <= hit_dist:
            # vector beteween center points
            nv = v12.normalize()
            # movement direction and combined relative movement
            d1 = pygame.math.Vector2(x1_dir, y1_dir)
            d2 = pygame.math.Vector2(x2_dir, y2_dir)
            dd = d1 - d2
            if dd.length() > 0:
                # normalized movement and normal distances
                ddn = dd.normalize()
                dir_dist  = ddn.dot(v12)
                norm_dist = pygame.math.Vector2(-ddn[0], ddn[1]).dot(v12)
                # minimum distance along the line of relative movement
                min_dist = math.sqrt(hit_dist*hit_dist - norm_dist*norm_dist)
                if dir_dist < min_dist:
                    # update postions of the players so that the distance is 2*xR
                    d1l, d2l = d1.length(), d2.length()
                    d1n = d1/d1l if d1l > 0 else d1
                    d2n = d2/d2l if d2l > 0 else d2
                    x1 -= d1n.x * d1l / (d1l+d2l)
                    y1 -= d1n.y * d1l / (d1l+d2l)
                    x2 -= d2n.x * d2l / (d1l+d2l)
                    y2 -= d2n.y * d2l / (d1l+d2l)
                    # recalculate vector beteween center points
                    v12 = pygame.math.Vector2(x1-x2, y1-y2)
                    nv = v12.normalize()
        
                # reflect movement vectors
                rd1 = d1.reflect(nv)
                rd2 = d2.reflect(nv)
                len1, len2 = rd1.length(), rd2.length()
                if len1 > 0:
                    rd1 = rd1 * len2 / len1
                    x1_dir, y1_dir = rd1.x, rd1.y
                else:
                    x1_dir, y1_dir = -x2_dir, -y2_dir
                if len2 > 0:
                    rd2 = rd2 * len1 / len2
                    x2_dir, y2_dir = rd2.x, rd2.y
                else:
                    x2_dir, y2_dir = -x1_dir, -y1_dir
        
    # ~~~~~~~~~~~ Borders ~~~~~~~~~~~~~~
        x1_cdist=((centerX-x1)**2+(centerY-y1)**2)**0.5
        x1_dead=False
        if x1_cdist>(stageR+30):
            x1_dead=True
            time.sleep(3)
            x1_win+=1
            game_over=True
        x2_cdist=((centerX-x2)**2+(centerY-y2)**2)**0.5
        x2_dead=False
        if x2_cdist>(stageR+30):
            x2_dead=True
            time.sleep(3)
            x2_win+=1
            game_over=True
            

        
    
        keys = pygame.key.get_pressed()
    # -------------------- CHAR1 MOVEMENT  WASD  --------------------
        if x1_dead==False:
            if keys[K_d] or keys[K_a]:
                x1_dir += 0.1 if keys[K_d] else -0.1
            else:
                x1_dir *= 0.98
        
            if keys[K_w] or keys[K_s]:
                y1_dir += 0.1 if keys[K_s] else -0.1
            else:
                y1_dir *= 0.98
            
    # -------------------- CHAR2 MOVEMENT  up/down/left/right --------------------
        if x2_dead==False:
            if keys[K_RIGHT] or keys[K_LEFT]:
                x2_dir += 0.1 if keys[K_RIGHT] else -0.1
            else:
                x2_dir *= 0.98
        
            if keys[K_UP] or keys[K_DOWN]:
                y2_dir += 0.1 if keys[K_DOWN] else -0.1
            else:
                y2_dir *= 0.98
    
        score()
        stage (centerX,centerY)
        if x1_dead==False:
            char1 (round(x1),round(y1))
        if x2_dead==False:
            char2 (round(x2),round(y2))   
        x1score() 
        x1+=x1_dir
        y1+=y1_dir
        x2+=x2_dir
        y2+=y2_dir
        pygame.display.update()
        fpsClock.tick(60)
        
while True:
    game()
    
