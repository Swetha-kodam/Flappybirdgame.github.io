from msilib.schema import Class
import pygame
import random

class Pipe(object):
    def __init__(self ,x,y):
        self.x=x
        self.y=y
        self.width=75
        self.height=400
    def draw(self):
        color=(50,105,50)
        return pygame.draw.rect(screen,color,pygame.Rect(self.x,self.y,self.width,self.height))
    def move(self):
        self.x-=1

class PipePair(object):
    def __init__(self ,x):
        self.topPipe=Pipe(x,random.randrange(-350,0))
        self.bottomPipe=Pipe(x,self.topPipe.y + 600)
    def draw(self):
        return [self.topPipe.draw(),self.bottomPipe.draw()]
    def move(self):
        self.topPipe.move()
        self.bottomPipe.move()
        if self.topPipe.x<-100:
            self.topPipe.x=900
            self.bottomPipe.x=900
            self.topPipe.y=random.randrange(-350,0)
            self.bottomPipe.y=self.topPipe.y + 600

class Bird():
    def __init__(self):
        self.x=100
        self.y=250
        self.radius=25
    def draw(self):
        color=(240,230,140)
        pygame.draw.circle(screen,color,(self.x,self.y),25)
    def move(self):
        self.y+=.5
pygame.init()
screen=pygame.display.set_mode([800,600])

#variables
pairs=[PipePair(700),PipePair(900),PipePair(1400)]
bird=Bird()
cooldown=0
gameOver=False


running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    screen.fill((255,255,255))
    if gameOver==False:
        for pair in pairs:
            pairData=pair.draw()#pairData =list containing data for top n bottom pipe
            pair.move()
            for pipe in pairData:
                if pipe.collidepoint(bird.x,bird.y):
                    gameOver=True

                
            
        bird.draw()
        bird.move()

        key_input=pygame.key.get_pressed()
        cooldown-=1
        if key_input[pygame.K_UP] and cooldown<0:
            bird.y-=60
            cooldown=30

    else:
        font=pygame.font.Font('freesansbold.ttf',32)
        text=font.render('GAMEOVER',True,(100,255,0),(255,0,0))  
        textGameover=text.get_rect()
        textGameover.center=(400,300)
        screen.blit(text, textGameover)  
    
   # pygame.draw.circle(screen,(0,0,255),(250,250),75)
   # pygame.draw.rect(screen,(50,205,50),pygame.Rect(50,300,75,500))
    #have everything actually visible

    pygame.display.update()
pygame.quit()