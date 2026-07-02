import pygame
import random
from cobra import criar_cobra, movimento_cobra, criar_comida, detc_colisao
from ranking import salvar_pontos


pygame.init()
tela = pygame.display.set_mode((600,600))
tempo = pygame.time.Clock()
#cadastro de novo jogador
nick = ''
rodando = True
inserindo_nick = True
#dentro da funcao esta a posicao inicial da cobra na tela
cobra = criar_cobra()
tamanhoCobra = 20
#direcao inicial, deve ser relativa ao tamanho da cobra
direcao = [20,0]
comida = criar_comida(tamanhoCobra)
pontuacao = 0
#tamanho da fonte da pontuacao
fonte = pygame.font.SysFont(None, 36)

while inserindo_nick:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            inserindo_nick = False
        if event.type == pygame.KEYDOWN:
            carac = event.unicode
            if event.key == pygame.K_BACKSPACE:
                nick = nick[:-1]
            elif event.key == pygame.K_RETURN:
                inserindo_nick = False
            else:
                if carac != '':
                   nick += carac
    tela.fill((0,0,0))
    texto = fonte.render(f'Digite seu nick: {nick}', True, (255,255,255))
    texto_rect = texto.get_rect(center=(300, 300))
    tela.blit(texto, texto_rect)
    pygame.display.flip()
    tempo.tick(60)

#loop do jogo
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
    cobra,comida,comeu = movimento_cobra(cobra,comida,direcao,tamanhoCobra)
    colisao = detc_colisao(cobra)
    if colisao == True:
       rodando = False
    if comeu == True:
        pontuacao += 10
    tela.fill((0,0,0))
    #desenha a pontuacao
    texto = fonte.render(f'Pontuação: {pontuacao}', True, (255,255,255))
    tela.blit(texto, (10, 10))
    #desenha a comida
    pygame.draw.rect(tela,(0,255,0),(comida[0],comida[1],tamanhoCobra,tamanhoCobra))
   #desenha a cobra
    for i in cobra:
        pygame.draw.rect(tela,(255,0,0), (i[0],i[1],tamanhoCobra,tamanhoCobra))
    pygame.display.flip()
    #velocidade da cobra, consequentemente do jogo inteiro
    tempo.tick(10)
pygame.quit()
salvar_pontos(nick,pontuacao)