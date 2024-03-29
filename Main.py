import sys, pygame
from pygame.locals import *
from random import *
from pygame import rect
from pickle import FALSE


pygame.init()


size = (800, 600)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Breakout")
pygame.display.set_icon(pygame.image.load('icon.png'))



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


cores = [LIGHT_PINK,MEDIUM_BLUE,LIGHT_BLUE,LIGHT_YELLOW,SALMON]

# def brickPosition(x,y):
  
  
print(pygame.font.get_fonts())  


font = pygame.font.SysFont('inkfree',30)
placar = 0

#BLOCOS

brickPosicaoX = [360,270, 360, 450,180, 270, 360, 450, 540,180, 270, 360, 450, 540,270,360,450,360]
brickPosicaoY = [150,180, 180, 180, 210, 210, 210, 210, 210, 240, 240, 240, 240, 240,270,270,270,300]
brickVida=[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
brickCor=[cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1],cores[1]]

# print (str(len(brickVida)))
# print(str(len(brickCor)))
# print (str(len(brickPosicaoY)))
# print(str(len(brickPosicaoX)))

#PLATAFORMA
posicaoPlataforma = [350,550]
tamanhoPlataforma = [100,26]
velocidadePlataforma = 6

#JOGADOR
vidaJogador = 2
bolas = [1,1,1]



#BOLAS
posicao_bolas = [0,0]
cor = LIGHT_YELLOW
velocidadeBola = [-5,-5]


#FLAGS
telaInicial = True
rebater = False
inicio = True
vitoria = False


#TELAS
telaVitoria = " "

clock = pygame.time.Clock()


CLOCKTICK = pygame.USEREVENT+1
pygame.time.set_timer(CLOCKTICK, 1000) # configurado o timer do Pygame para execução a cada 1 segundo
temporizador = 60


#SONS

pygame.mixer.init()
# pygame.mixer.music.load('musica.wav')
# pygame.mixer.music.play()
#----------------PARTE 2-------------------------------------

# Loop principal do jogo
while True:
    
    
   
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        if event.type == CLOCKTICK:
            temporizador = temporizador -1


    if (len(bolas) == 0):
      break
   
    if (len(brickVida) == 0):
      telaVitoria = pygame.Surface.copy(screen)
      vitoria = True
      break
    
    pressed = pygame.key.get_pressed()
    
    if (inicio == True):
#       posicao_bolas= [0,0]
      posicao_bolas[0]= posicaoPlataforma[0]+50
      posicao_bolas[1]= 530
      print(str(posicao_bolas[1]))
      
    
 
    
    

    if (inicio==True):   
      if (pressed[pygame.K_SPACE]): 
        posicao_bolas[1]=posicaoPlataforma[1]+velocidadeBola[1]-5
        inicio=False
      
      
    if pressed[pygame.K_LEFT]: posicaoPlataforma[0] -= velocidadePlataforma
    if pressed[pygame.K_RIGHT]: posicaoPlataforma[0] += velocidadePlataforma
   
   
   #GARANTE QUE A PLATAFORMA NAO PASSE DOS LIMITES X DA TELA 
    if (posicaoPlataforma[0]+100 > 800):
      posicaoPlataforma[0]=700
    
    if(posicaoPlataforma[0] < 0):
      posicaoPlataforma[0]=0  
      
    

    
    screen.fill(BLACK)

   
    i = 0
    while ( i < len(brickPosicaoX)):
      brick = pygame.draw.rect(screen,(brickCor[i]),(brickPosicaoX[i],brickPosicaoY[i],80,20))
      i+=1
    
    
    #CHECA COLISAO
    j=0
    while (j < len(brickPosicaoX)):
      if ((brickPosicaoY[j]+15>= posicao_bolas[1] and brickPosicaoY[j]-15 <=posicao_bolas[1]) and (brickPosicaoX[j]+105 >= posicao_bolas[0] and brickPosicaoX[j]-15<=posicao_bolas[0])):
        brickVida[j]-=1
        pygame.mixer.music.load('ponto.wav')
        pygame.mixer.music.play()
        brickCor[j] = cores[2]
#         if (posicao_bolas[1] <= 0):
#           velocidadeBola = velocidadeBola
        if (posicao_bolas[1]> 0):
          velocidadeBola[1] = -velocidadeBola[1]
          velocidadeBola[0] = velocidadeBola[0]   
        print(str(brickVida[j]))
        
      if(brickVida[j]==0):
        del(brickPosicaoX[j])
        del(brickPosicaoY[j])
        del(brickVida[j])
        del(brickCor[j])
          
      j+=1  
    
      
    
    k=0
    posicaoVida = [670,60]
    while (k < len(bolas)):
      pygame.draw.circle(screen, LIGHT_YELLOW,(posicaoVida[0], posicaoVida[1]) ,10)
      posicaoVida[0]+=30  
      k+=1
      
      
   
    plataforma = pygame.draw.rect(screen,(LIGHT_PINK),(posicaoPlataforma[0],posicaoPlataforma[1],tamanhoPlataforma[0],tamanhoPlataforma[1]))
   
    
    
#     if rebater== False:
#         Y_vermelho += 2
#      
#      
#     if rebater==True:
#         Y_vermelho -= 2
       
       
        

    
    
    if (inicio != True):
      posicao_bolas[0] = posicao_bolas[0]+velocidadeBola[0]   
      posicao_bolas[1] = posicao_bolas[1]+velocidadeBola[1]
      
    bola = pygame.draw.circle(screen, cor, (posicao_bolas[0], posicao_bolas[1]), 10)

 
    
    if (posicaoPlataforma[1]+15>= posicao_bolas[1] and posicaoPlataforma[1]-15 <=posicao_bolas[1]) and (posicaoPlataforma[0]+115 >= posicao_bolas[0] and posicaoPlataforma[0]-15<=posicao_bolas[0]) and (inicio == False):
      print(str(posicaoPlataforma[0]))
      if (velocidadeBola[1] >0):
        velocidadeBola[1] = -velocidadeBola[1]
#
   
    if posicao_bolas[1] < 10:
      velocidadeBola[1] = -velocidadeBola[1] 
      
    if (posicao_bolas[0] < 15) or (posicao_bolas[0] > 785) :
      velocidadeBola[0] = -velocidadeBola[0]  
      
        
    if posicao_bolas[1] > 601:
      bolas.pop(vidaJogador)
      vidaJogador-=1
      
      inicio = True
   
      
    
   
    
#     score1 = font.render('Placar '+str(placar), True, (WHITE))
#     screen.blit(score1, (600, 50))

#     nome_fase = font.render("LVL 01", True, (LIGHT_YELLOW)) 
# #     timer1 = font.render('Tempo ' + str(temporizador), True, (LIGHT_YELLOW))
#     screen.blit(nome_fase, (50, 50))
        

    pygame.display.flip()

   
    clock.tick(60)
    
   
            

if (vitoria == True):
  vitoria = pygame.image.load("victory.png")
  vitoria = pygame.transform.scale(vitoria,(100,100))
  screen.fill((0,0,0))
  screen.blit(vitoria, (350, 150))
  textofinal = font.render(("Thank you for playing!"), True, (WHITE))
  screen.blit(textofinal, (260, 270)) 

if (vitoria == False):  
  pygame.mixer.music.load('fim_de_jogo.WAV')
  pygame.mixer.music.play()
  frame = pygame.draw.rect(screen, (BLACK), Rect((0, 0), (800, 600)))
  textofinal = font.render(("End game!"), True, (WHITE))
  screen.blit(textofinal, (330,270))
  


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()