import pygame
import random
from cobra import criar_cobra, movimento_cobra, criar_comida

pygame.init()
tela = pygame.display.set_mode((600,600))
tempo = pygame.time.Clock()
rodando = True
#dentro da funcao esta a posicao inicial da cobra na tela
cobra = criar_cobra()
tamanhoCobra = 20
#direcao inicial, deve ser relativa ao tamanho da cobra
direcao = [20,0]
comida = criar_comida(tamanhoCobra)

while rodando:
    nova_direcao = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                nova_direcao = [0,-20]
            if event.key == pygame.K_DOWN:
                nova_direcao = [0,20]
            if event.key == pygame.K_RIGHT:
                nova_direcao = [20,0]
            if event.key == pygame.K_LEFT:
                nova_direcao =[-20,0]
    if nova_direcao is not None and nova_direcao != [-direcao[0],-direcao[1]]:
        direcao = nova_direcao       
    cobra,comida = movimento_cobra(cobra,comida,direcao,tamanhoCobra)
    tela.fill((0,0,0))
    #desenha a comida
    pygame.draw.rect(tela,(0,255,0),(comida[0],comida[1],tamanhoCobra,tamanhoCobra))
   #desenha a cobra
    for i in cobra:
        pygame.draw.rect(tela,(255,0,0), (i[0],i[1],tamanhoCobra,tamanhoCobra))
    pygame.display.flip()
    #velocidade da cobra, consquentemente do jogo inteiro
    tempo.tick(10)
pygame.quit()