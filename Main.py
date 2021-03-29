import sys, pygame
from pygame.locals import *
from random import *
from pygame import rect


pygame.init()


size = (800, 600)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Papa Bolinhas")


#CORES BASICAS
BLACK  = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)


#CORES TEMA
LIGHT_PINK = (233,91,94)
MEDIUM_BLUE = (3,76,140)
LIGHT_BLUE = (155,202,242)
LIGHT_YELLOW = (250,205,9)
SALMON = (217, 93, 48) 

brickVector=[]
cores = [LIGHT_PINK,MEDIUM_BLUE,LIGHT_BLUE,LIGHT_YELLOW,SALMON]

# def brickPosition(x,y):
  
  
  


font = pygame.font.SysFont('sans',40)
placar = 0

#FASE1

brickPosicaoX = [180, 270, 360, 450, 540, 90  , 180, 270, 360, 450, 540, 630 ,180, 270, 360, 450, 540]
brickPosicaoY = [200, 200, 200, 200, 200, 230, 230, 230, 230, 230, 230, 230 ,260, 260, 260, 260, 260]
brickVida=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
brickCor=[cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1]]


posicaoPlataforma = [350,550]
tamanhoPlataforma = [100,30]
velocidadePlataforma = 5



criar = True
rebater = False

X_vermelho = 0
Y_vermelho = 0

cor = RED



clock = pygame.time.Clock()


CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # configurado o timer do Pygame para execuÃ§Ã£o a cada 1 segundo
temporizador = 60

#----------------PARTE 2-------------------------------------

# Loop principal do jogo
while True:
    
    
   
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type == CLOCKTICK:
            temporizador = temporizador -1


    if temporizador == 0:
        
        break

    
    pressed = pygame.key.get_pressed()

   
    
    if pressed[pygame.K_LEFT]: posicaoPlataforma[0] -= velocidadePlataforma
    if pressed[pygame.K_RIGHT]: posicaoPlataforma[0] += velocidadePlataforma
    
    if (posicaoPlataforma[0]+100 > 800):
      posicaoPlataforma[0]=posicaoPlataforma[0]-5
    
    if(posicaoPlataforma[0] < 0):
      posicaoPlataforma[0]=posicaoPlataforma[0]+5  
      
    

    
    screen.fill(BLACK)

   
    i = 0
    while ( i < len(brickPosicaoX)):
      brick = pygame.draw.rect(screen,(brickCor[i]),(brickPosicaoX[i],brickPosicaoY[i],80,20))
      i+=1
    
    j=0
    while (j < len(brickPosicaoX)):
      if (brickPosicaoY[j]+15>= Y_vermelho and brickPosicaoY[j]-15 <=Y_vermelho) and (brickPosicaoX[j]+105 >= X_vermelho and brickPosicaoX[j]-15<=X_vermelho):
        brickVida[j]-=1
        brickCor[j] = cores[2]
        rebater = True
        print(str(brickVida[j]))
        if(brickVida[j]==0):
          del(brickPosicaoX[j])
          del(brickPosicaoY[j])
          del(brickVida[j])
          del(brickCor[j])
      j+=1  
    
      
     
    plataforma = pygame.draw.rect(screen,(LIGHT_PINK),(posicaoPlataforma[0],posicaoPlataforma[1],tamanhoPlataforma[0],tamanhoPlataforma[1]))
   
    
    
    if rebater== False:
      Y_vermelho += 2
    
    
    if rebater==True:
      Y_vermelho -= 2
      
       
    
    if criar == True:
        X_vermelho = randint(40,760)
        Y_vermelho = 20
        cor = LIGHT_YELLOW
        criar = False
        

    
   
   
    posicaoBolasVermelhas = [X_vermelho,Y_vermelho]
   
   
    bola = pygame.draw.circle(screen, cor, posicaoBolasVermelhas, 10)

   
    

    
    
    if (posicaoPlataforma[1]+15>= Y_vermelho and posicaoPlataforma[1]-15 <=Y_vermelho) and (posicaoPlataforma[0]+115 >= X_vermelho and posicaoPlataforma[0]-15<=X_vermelho):
      print(str(posicaoPlataforma[0]))
      print(str(X_vermelho))
      rebater = True
        
        

    
   
    
    score1 = font.render('Placar '+str(placar), True, (WHITE))
    screen.blit(score1, (600, 50))

   
    timer1 = font.render('Tempo ' + str(temporizador), True, (LIGHT_YELLOW))
    screen.blit(timer1, (50, 50))
        

    pygame.display.flip()

   
    clock.tick(60)
    
    if (Y_vermelho >600 or Y_vermelho<0):
      rebater = False
      criar = True


frame = pygame.draw.rect(screen, (WHITE), Rect((0, 0), (800, 600)))


textofinal = font.render('Fim de Jogo - Placar final: ' + str(placar), True, (RED))
size = font.size(str(textofinal))
screen.blit(textofinal, (size[0]/2., size[1]/2.))



pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
