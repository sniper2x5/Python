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
colorBlue2=pygame.Color(37, 45, 204)

#Dimensions
w=800
h=600
pygame.init()
fpsClock=pygame.time.Clock()
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption ('Ice Fighters')
centerX=w//2
centerY=h//2
point=3
pointx=240
gameEnd_p=1
gameEnd_px=340
option=False

# ~~~~~~~~~~~~~~~~~~~~~ TEXT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
bigFont = pygame.font.Font('shark_party.ttf',64)
smallFont = pygame.font.Font("shark_party.ttf",32)
tinyFont = pygame.font.Font('shark_party.ttf', 16)
titleText = bigFont.render("Ice Fighters", True, colorBlue)
multiplayerText=smallFont.render("Multiplayer", True, colorBlue2,)
singleplayerText=smallFont.render("Singleplayer", True, colorBlue2)
intructionsText=smallFont.render("How to Play", True, colorBlue2)
leaderboardText=smallFont.render("Leaderboard", True, colorBlue2)
game_endText=bigFont.render("GAME OVER", True, colorRed)
replayText=smallFont.render ("Play Again", True, colorBlue)
returnText=smallFont.render ("Main Menu", True, colorBlue)
menu_upText=tinyFont.render ("= Menu Up", True, colorBlack)
menu_downText=tinyFont.render ('= Menu Down',True, colorBlack)
menu_returnText=tinyFont.render ('= ENTER', True, colorBlack)

def game_end():
    while True:
        screen.fill(colorBlack)
        for event in pygame.event.get():
            #Game Exit
            if event.type== QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_s:
                    global gameEnd_p
                    global gameEnd_px
                    if gameEnd_p==1:
                        gameEnd_px+=75
                        gameEnd_p-=1
                    elif gameEnd_p==0:
                        gameEnd_px-=75
                        gameEnd_p+=1 
                if event.key==K_w:
                    if gameEnd_p==1:
                        gameEnd_px+=75
                        gameEnd_p-=1
                    elif gameEnd_p==0:
                        gameEnd_px-=75
                        gameEnd_p+=1
                if event.key==K_RETURN:
                    if gameEnd_p==0:
                        title()
        screen.blit(game_endText,(230,50))
        screen.blit(replayText,(300,325))
        screen.blit(returnText,(300,400))
        pygame.draw.circle(screen,colorRed,(280,gameEnd_px),10)
        pygame.display.update()
        fpsClock.tick(60)

        
def title():
    while True:
        screen.fill(colorBlack)
        for event in pygame.event.get():
            #Game Exit
            if event.type== QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_s:
                    global point
                    global pointx
                    if point==3:
                        pointx+=75
                        point-=1
                    elif point==2:
                        pointx+=75
                        point-=1
                    elif point==1:
                        pointx+=75
                        point-=1
                    elif point==0:
                        pointx-=225
                        point+=3
                if event.key==K_w:
                    if point==3:
                        pointx+=225
                        point-=3
                    elif point==2:
                        pointx-=75
                        point+=1
                    elif point==1:
                        pointx-=75
                        point+=1
                    elif point==0:
                        pointx-=75
                        point+=1
                if event.key==K_RETURN:
                    if point==2:
                        option=True
                        game()
                    elif point==1:
                        option=True
                        instruct()
                    
                    
        #Background
        title_bg=pygame.image.load("icebiome3.png")
        screen.blit(title_bg,(0,0))
        screen.blit(titleText, (200,50))
        screen.blit(singleplayerText, (300,225))
        screen.blit(multiplayerText, (300,300))
        screen.blit(intructionsText, (300,375))
        screen.blit(leaderboardText, (300,450))
        screen.blit(menu_upText, (700,450))
        screen.blit(menu_downText, (700,475))
        screen.blit(menu_returnText, (700,500))
        pygame.draw.circle(screen,colorRed,(280,pointx),10)
        pygame.draw.circle(screen,colorWhite,(685,460),10)
        pygame.draw.circle(screen,colorRed,(685,485),10)
        pygame.draw.circle(screen,colorBlue2,(685,510),10)
        pygame.display.update()
        fpsClock.tick(60)

def instruct():
    while True:
        screen.fill(colorBlack)
        for event in pygame.event.get():
            #Game Exit
            if event.type== QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_RETURN:
                    title()
        instruct_bg=pygame.image.load('instruct.png')
        instruct_sprite=pygame.image.load('instructsprite.png')
        
        screen.blit(instruct_bg,(0,0))
        screen.blit(returnText, (325,550))
        pygame.draw.circle(screen,colorRed,(310,568),10)
        pygame.display.update()
        fpsClock.tick(60)
        
        
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
        if x1_win>1:
            pygame.draw.circle(screen, colorOrange, (100,30), (int(xR-5)))
        if x1_win>2:
            pygame.draw.circle(screen, colorOrange, (150,30), (int(xR-5)))
    
    def x2score ():
        if x2_win>0:
            pygame.draw.circle(screen, colorOrange, (750,30), (int(xR-5)))
        if x2_win>1:
            pygame.draw.circle(screen, colorOrange, (700,30), (int(xR-5)))
        if x2_win>2:
            pygame.draw.circle(screen, colorOrange, (650,30), (int(xR-5)))
            
    while x1_win!=3 or x2_win!=3:
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
        if x1_cdist>(stageR+30):
            time.sleep(3)
            x2=int(centerX+(stageR*0.8))
            y2=centerY
            x1=int(centerX-(stageR*0.8))
            y1=centerY
            x2_win+=1
            x1_dir=0
            y1_dir=0
            print (x2_win)

            
        x2_cdist=((centerX-x2)**2+(centerY-y2)**2)**0.5
        if x2_cdist>(stageR+30):
            time.sleep(3)
            x2=int(centerX+(stageR*0.8))
            y2=centerY
            x1=int(centerX-(stageR*0.8))
            y1=centerY
            x1_win+=1
            x2_dir=0
            y2_dir=0
            print (x1_win)

            

        
    #MOVEMENT
        keys = pygame.key.get_pressed()
    # -------------------- CHAR1 MOVEMENT  WASD  --------------------
        if keys[K_d] or keys[K_a]:
            x1_dir += 0.1 if keys[K_d] else -0.1
        else:
            x1_dir *= 0.98
    
        if keys[K_w] or keys[K_s]:
            y1_dir += 0.1 if keys[K_s] else -0.1
        else:
            y1_dir *= 0.98
            
    # -------------------- CHAR2 MOVEMENT  up/down/left/right --------------------
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
        char1 (round(x1),round(y1))
        char2 (round(x2),round(y2))   
        x1score()
        x2score() 
        x1+=x1_dir
        y1+=y1_dir
        x2+=x2_dir
        y2+=y2_dir
        pygame.display.update()
        fpsClock.tick(60)
        
while True:
    #game_end()
    title()
