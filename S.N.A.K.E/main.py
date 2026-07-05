import pygame
import random
from cobra import criar_cobra, movimento_cobra, criar_comida, detc_colisao, criar_barreiras, adicionar_barreiras
from ranking import salvar_pontos


pygame.init()
tela = pygame.display.set_mode((600,600))
tempo = pygame.time.Clock()
velocidade = 10
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
ultimo100 = 0
#facil = 1, medio = 2, dificil = 3
dif = None
#tamanho da fonte da pontuacao
fonte = pygame.font.SysFont(None, 36)
#loop da tela de nick
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
    textoconfirma = fonte.render(f'ENTER para confirmar', True, (255,255,255))
    texto_rect = texto.get_rect(center=(300, 300))
    
    tela.blit(textoconfirma, (200,350) )
    tela.blit(texto, texto_rect)
    pygame.display.flip()
    tempo.tick(60)
#loop tela de selecao dificuldade
selec_dif = True
if rodando == False:
    selec_dif = False
while selec_dif:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
            selec_dif = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                dif = 1
                velocidade = 10
                selec_dif = False
            if event.key == pygame.K_2:
                dif = 2
                velocidade = 10
                selec_dif = False
            if event.key == pygame.K_3:
                dif = 3
                velocidade = 20
                selec_dif = False
    tela.fill((0,0,0))
    texto = fonte.render(f'ESCOLHA A DIFICULDADE:', True, (0,255,0))
    texto2 = fonte.render(f'1.FACIL', True, (0,255,100))
    texto3 = fonte.render(f'2.MEDIO', True, (255,255,0))
    texto4 = fonte.render(f'3.DIFICIL', True, (255,50,50))

    tela.blit(texto, (150,200))
    tela.blit(texto2, (250, 250))
    tela.blit(texto3, (250, 300))
    tela.blit(texto4, (250,350))
    
    pygame.display.flip()
    tempo.tick(60)
if rodando == True:
    Barreiras = criar_barreiras(dif,cobra,comida,tamanhoCobra)
else:
    Barreiras = []
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
    colisao = detc_colisao(cobra,Barreiras)
    if colisao == True:
       rodando = False
    if comeu == True:
        pontuacao += 10
        if dif == 2 or dif == 3:
            if pontuacao % 100 == 0:
                nova = adicionar_barreiras(3, cobra, comida, Barreiras, tamanhoCobra)
                Barreiras.extend(nova)

    tela.fill((0,0,0))
    #desenha a pontuacao
    texto = fonte.render(f'Pontuação: {pontuacao}', True, (255,255,255))
    tela.blit(texto, (10, 10))
    #desenha as barreiras
    for j in Barreiras:
        pygame.draw.rect(tela,(210,110,255),(j[0],j[1],tamanhoCobra,tamanhoCobra)) 
    #desenha a comida
    pygame.draw.rect(tela,(0,255,0),(comida[0],comida[1],tamanhoCobra,tamanhoCobra))
   #desenha a cobra
    for i in cobra:
        pygame.draw.rect(tela,(255,0,0), (i[0],i[1],tamanhoCobra,tamanhoCobra))
    pygame.display.flip()
    #velocidade da cobra, consequentemente do jogo inteiro
    tempo.tick(velocidade)
pygame.quit()
salvar_pontos(nick,pontuacao)