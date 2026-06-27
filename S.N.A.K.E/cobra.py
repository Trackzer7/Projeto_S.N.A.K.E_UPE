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
def detc_colisao (cobra):
    colisao = False
    if cobra[-1][0] < 0 or cobra[-1][0] >= 600:
        colisao = True
    if cobra[-1][1] < 0 or cobra[-1][1] >= 600:
        colisao = True
    if cobra[-1] in cobra[:-1]:
        colisao = True
    return colisao