import random
def criar_cobra():
# posicao inicial da cobra
   cobra = [[300,300],[300,300],[300,300]]
   return cobra

def movimento_cobra(cobra,comida,direcao,tamanhoCobra):
    nova_cabeca = [cobra[-1][0] + direcao[0], cobra[-1][1] + direcao[1]]
    if cobra[-1] == comida:
        comida = [random.randint(0,29)*tamanhoCobra,random.randint(0,29)*tamanhoCobra]
        cobra.append(nova_cabeca)
    else:
        cobra.pop(0)
        cobra.append(nova_cabeca)
    return cobra, comida

def criar_comida(tamanhoCobra):
    comida = [random.randint(0,29)*tamanhoCobra,random.randint(0,29)*tamanhoCobra]
    return comida

