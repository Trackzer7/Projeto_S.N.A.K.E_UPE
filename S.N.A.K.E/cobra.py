import random

def criar_cobra():
# posicao inicial da cobra
   cobra = [[300,300],[300,300],[300,300]]
   return cobra

def movimento_cobra(cobra,comida,direcao,tamanhoCobra):
    comeu = False
    nova_cabeca = [cobra[-1][0] + direcao[0], cobra[-1][1] + direcao[1]]
    if cobra[-1] == comida:
        comida = [random.randint(0,29)*tamanhoCobra,random.randint(0,29)*tamanhoCobra]
        cobra.append(nova_cabeca)
        comeu = True
    else:
        cobra.pop(0)
        cobra.append(nova_cabeca)
    return cobra, comida, comeu

def criar_comida(tamanhoCobra):
    comida = [random.randint(0,29)*tamanhoCobra,random.randint(0,29)*tamanhoCobra]
    return comida

def detc_colisao (cobra,Barreiras):
    colisao = False
    if cobra[-1][0] < 0 or cobra[-1][0] >= 600:
        colisao = True
    if cobra[-1][1] < 0 or cobra[-1][1] >= 600:
        colisao = True
    if cobra[-1] in cobra[:-1]:
        colisao = True
    if cobra[-1] in Barreiras:
        colisao = True
    return colisao

def criar_barreiras(dif,cobra,comida,tamanhoCobra):
    quant = 0
    if dif == 1:
        quant = 0
    if dif == 2:
        quant = 15
    if dif == 3:
        quant = 25
    Barreiras = []
    for i in range(quant):
        while True:
            barreira = [random.randint(0,29)*tamanhoCobra,random.randint(0,29)*tamanhoCobra]
            if barreira not in cobra and barreira != comida:
                break
        Barreiras.append(barreira)
    return Barreiras

def adicionar_barreiras(quantidade, cobra, comida, Barreiras, tamanhoCobra):
    nova = []
    for i in range(quantidade):
        while True:
            barreira = [random.randint(0,29)*tamanhoCobra,random.randint(0,29)*tamanhoCobra]
            if barreira not in cobra and barreira != comida and barreira not in Barreiras and barreira not in nova:
                break
        nova.append(barreira)
    return nova