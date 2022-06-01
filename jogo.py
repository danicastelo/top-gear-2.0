import pygame
import time
pygame.init()
x = 200
y = 160
fundo = pygame.image.load('imagens/oie_transparent.png')
carroB = pygame.image.load('imagens/carro_branco_2_1.png')
width, height = fundo.get_width(), fundo.get_height() 
janela = pygame.display.set_mode((width, height))

pygame.display.set_caption('Top Carros')
fps = 60
janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    pygame.display.update()
    janela.blit(fundo,(0,0))
    janela.blit(carroB,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    
         




pygame.quit()