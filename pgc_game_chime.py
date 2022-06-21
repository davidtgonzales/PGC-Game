#import pygame and initialize
import random
import time
import pygame, sys
import chime
chime.theme('big-sur')
from pygame.locals import *
pygame.init()
FPS=30
fpsClock=pygame.time.Clock()

#open display surface
DISPLAYSURF=pygame.display.set_mode((1000,700))
pygame.display.set_caption('MPI-CBG\’s Dr. Dee Enay')

#load colors
white=pygame.Color(255,255,255)
black=pygame.Color(0,0,0)
yellow=pygame.Color(255,255,0)
grey=pygame.Color(50,50,50)
green=pygame.Color(50,200,80)

#load images
header=pygame.image.load('./images/header.png')
main=pygame.image.load('./images/main.png')
dee_enay=pygame.image.load('./images/dee enay.png')
mouse=pygame.image.load('./images/mouse.png')
m=pygame.image.load('./images/m.png')
instructions=pygame.image.load('./images/help.png')
play1=pygame.image.load('./images/play1.png')
play2=pygame.image.load('./images/play2.png')
apicture=pygame.image.load('./images/apicture.png')
tpicture=pygame.image.load('./images/tpicture.png')
gpicture=pygame.image.load('./images/gpicture.png')
cpicture=pygame.image.load('./images/cpicture.png')
aw=pygame.image.load('./images/aw.png')
tw=pygame.image.load('./images/tw.png')
cw=pygame.image.load('./images/cw.png')
gw=pygame.image.load('./images/gw.png')
end=pygame.image.load('./images/end.png')
#load text
text70=pygame.font.Font('freesansbold.ttf',70)
text30=pygame.font.Font('freesansbold.ttf',30)
text20=pygame.font.Font('freesansbold.ttf',20)

#initial values
loop='main'
mousex=620
mousey=190
loopcount=0
points=0
mx=5
my=0
direction=0
direction1=0
amatrix=[]
tmatrix=[]
cmatrix=[]
gmatrix=[]
letters=['A','T','G','C']

#Function for coordinates
class coordinates():
    def __init__(self,xcoordinate,ycoordinate):
        self.xcoordinate=float(xcoordinate)
        self.ycoordinate=float(ycoordinate)
        
    def convert(self):
        convertedx=float(self.xcoordinate*50)+500
        convertedy=float(self.ycoordinate*50)+150
        if convertedx<500:
            convertedx=500
        elif convertedx>900:
            convertedx=900
        if convertedy<150:
            convertedy=150
        elif convertedy>600:
            convertedy=600
        return convertedx,convertedy

def aplacer():
    x=int(random.uniform(0,8))
    y=int(random.uniform(0,9))
    aplace=coordinates(x,y)
    x,y=aplace.convert()
    return x,y

def tplacer():
    x=int(random.uniform(0,8))
    y=int(random.uniform(0,9))
    tplace=coordinates(x,y)
    x,y=tplace.convert()
    return x,y

def cplacer():
    x=int(random.uniform(0,8))
    y=int(random.uniform(0,9))
    cplace=coordinates(x,y)
    x,y=cplace.convert()
    return x,y

def gplacer():
    x=int(random.uniform(0,8))
    y=int(random.uniform(0,9))
    gplace=coordinates(x,y)
    x,y=gplace.convert()
    return x,y    

#game loop
while True:
    for event in pygame.event.get():
        if loop=='main':
            points=0
            loop2=0
            pygame.draw.rect(DISPLAYSURF,black,(0,0,1000,700))
            DISPLAYSURF.blit(header,(0,0))   
            DISPLAYSURF.blit(main,(0,150))
            DISPLAYSURF.blit(mouse,(mousex,mousey))                
            #Selecting at the main menu of the game        
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_UP:
                    chime.info()
                    if mousey==390 or mousey==290:
                        mousey=mousey-100
                    else:
                        mousey=mousey
                        
                elif event.key==K_DOWN:
                    chime.info()
                    if mousey==190 or mousey==290:
                        mousey=mousey+100
                    else:
                        mousey=mousey     
            
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_RETURN:
                    if mousey==190:
                        chime.warning()
                        loop='play'
                    elif mousey==290:
                        chime.warning()
                        loop='help'
                    elif mousey==390:
                        chime.warning()
                        pygame.quit()
                        sys.exit()
        
        if loop=='play':
            if loopcount==0:
                starttime=time.time()            
                endtime=starttime+30
                target=letters[int(random.uniform(0,4))]    
                
            loopcount=loopcount+1
            now=time.time()
            mouseposition=coordinates(mx,my).convert()
            timer=text30.render('Time: '+str(int(endtime-now))+' secs',True,white)
            pointtext=text30.render('Score: '+str(points)+' pts',True,white)      
            pygame.draw.rect(DISPLAYSURF,black,(0,0,1000,700))
            DISPLAYSURF.blit(header,(0,0))         
            
            while len(amatrix)<5:
                a=aplacer()
                if a not in amatrix:
                    if a not in tmatrix:
                        if a not in cmatrix:
                            if a not in gmatrix:
                                amatrix.append(a)
            
            while len(tmatrix)<5:
                t=tplacer()
                if t not in amatrix:
                    if t not in tmatrix:
                        if t not in cmatrix:
                            if t not in gmatrix:
                                tmatrix.append(t)        

            while len(cmatrix)<5:
                c=cplacer()
                if c not in amatrix:
                    if c not in tmatrix:
                        if c not in cmatrix:
                            if c not in gmatrix:
                                cmatrix.append(c)

            while len(gmatrix)<5:
                g=gplacer()
                if g not in amatrix:
                    if g not in tmatrix:
                        if g not in cmatrix:
                            if g not in gmatrix:
                                gmatrix.append(g)
                    
            if loopcount%2==0:
                DISPLAYSURF.blit(play1,(0,150))
            else:
                DISPLAYSURF.blit(play2,(0,150))
            
            if target=='A':
                DISPLAYSURF.blit(aw,(290,190))
            elif target=='T':
                DISPLAYSURF.blit(tw,(290,190))
            elif target=='C':
                DISPLAYSURF.blit(cw,(290,190))
            elif target=='G':
                DISPLAYSURF.blit(gw,(290,190))
                
            pygame.draw.rect(DISPLAYSURF,grey,(490,140,480,520))
            pygame.draw.rect(DISPLAYSURF,black,(500,150,460,500))
                
            for aplace in amatrix:
                DISPLAYSURF.blit(apicture,aplace)

            for tplace in tmatrix:
                DISPLAYSURF.blit(tpicture,tplace)
                
            for cplace in cmatrix:
                DISPLAYSURF.blit(cpicture,cplace)
                
            for gplace in gmatrix:
                DISPLAYSURF.blit(gpicture,gplace)
                
            DISPLAYSURF.blit(m,mouseposition)
            DISPLAYSURF.blit(timer,(20,180))  
            DISPLAYSURF.blit(pointtext,(20,230))
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_UP:
                    chime.info() 
                    my=my-1
                elif event.key==K_DOWN:
                    chime.info() 
                    my=my+1
                if my<0:
                    my=0
                elif my>9:
                    my=9
                if event.key==K_LEFT:
                    direction1=0
                    chime.info() 
                    mx=mx-1
                elif event.key==K_RIGHT:
                    direction1=1    
                    chime.info() 
                    mx=mx+1
                if mx<0:
                    mx=0
                elif mx>8:
                    mx=8
                if direction1!=direction:
                    m=pygame.transform.flip(m,True,False)
                    direction=direction1
            
            for aplace in amatrix:
                if mouseposition==aplace:
                    if target=='T':
                        chime.success() 
                        points=points+1
                    else:
                        chime.error() 
                        points=points-1

                    amatrix.remove(aplace)
                    target=letters[int(random.uniform(0,4))]

            for tplace in tmatrix:
                if mouseposition==tplace:
                    if target=='A':
                        chime.success() 
                        points=points+1
                    else:
                        chime.error()
                        points=points-1
                    
                    tmatrix.remove(tplace)
                    target=letters[int(random.uniform(0,4))]

            for cplace in cmatrix:
                if mouseposition==cplace:
                    if target=='G':
                        chime.success() 
                        points=points+1
                    else:
                        chime.error()
                        points=points-1
                    
                    cmatrix.remove(cplace)
                    target=letters[int(random.uniform(0,4))]

            for gplace in gmatrix:
                if mouseposition==gplace:
                    if target=='C':
                        chime.success() 
                        points=points+1
                    else:
                        chime.error()
                        points=points-1
                    
                    gmatrix.remove(gplace)
                    target=letters[int(random.uniform(0,4))]

            if target=='A':
                DISPLAYSURF.blit(aw,(290,190))
            elif target=='T':
                DISPLAYSURF.blit(tw,(290,190))
            elif target=='C':
                DISPLAYSURF.blit(cw,(290,190))
            elif target=='G':
                DISPLAYSURF.blit(gw,(290,190))

            if now>endtime:
                loop='score'
                loopcount=0
                        
        if loop=='help':
            pygame.draw.rect(DISPLAYSURF,black,(0,0,1000,700))
            DISPLAYSURF.blit(header,(0,0))   
            DISPLAYSURF.blit(instructions,(0,150))
            
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_BACKSPACE:
                    chime.warning() 
                    loop='main'
                    
        elif loop=='score':
            pygame.draw.rect(DISPLAYSURF,black,(0,0,1000,700))
            DISPLAYSURF.blit(header,(0,0))
            DISPLAYSURF.blit(end,(0,150))
            totalpoints=text70.render(str(points),True,black)
            DISPLAYSURF.blit(totalpoints,(650,420))
            if loop2==0:
                chime.theme('material')
                chime.success()
                chime.theme('big-sur')
                loop2=loop2+1
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_RETURN:
                    chime.warning()
                    loop='main'
                    points=0
                    loop2=0
                    
    pygame.display.update()
