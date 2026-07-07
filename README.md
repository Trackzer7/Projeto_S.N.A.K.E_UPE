# 🐍 S.N.A.K.E — UPE

Jogo da cobrinha desenvolvido em Python com Pygame como projeto de faculdade.

## 👥 Integrantes

| Integrante | Responsabilidade |
|---|---|
| Integrante 1 | Movimentação, mecânicas da cobra, comida, pontuação, dificuldade, telas de nick/dificuldade, barreiras |
| Integrante 2 | Interface gráfica geral, tela de Game Over, reiniciar o jogo |
| Integrante 3 | Cadastro do nick, sistema de ranking (salvamento e ordenação) |

## 🛠️ Requisitos

- Python 3.13 
- Pygame

## ▶️ Como rodar

**1. Instalar o pygame:**
```
pip install pygame
```

**2. Rodar o jogo:**
```
python main.py
```

## 📁 Estrutura dos arquivos

```
S.N.A.K.E/
├── main.py         # Loop principal: telas de nick, dificuldade e jogo
├── cobra.py        # Lógica da cobra, comida, colisão e barreiras
├── ranking.py       # Salvamento e exibição do ranking (arquivo ranking.txt)
└── ranking.txt        # Gerado automaticamente ao salvar a 1ª pontuação
```

## 🎮 Como jogar

1. Digite seu nick e pressione **ENTER**
2. Escolha a dificuldade (**1**, **2** ou **3**)
3. Use as **setas do teclado** para mover a cobra
4. Coma a comida verde para crescer e pontuar (+10 pontos)
5. Evite as paredes, o próprio corpo e as barreiras roxas

## 🎯 Regras de dificuldade

| Dificuldade | Tecla | Velocidade | Barreiras iniciais | Barreiras a cada 100 pontos |
|---|---|---|---|---|
| Fácil | 1 | Normal | 0 | Não |
| Médio | 2 | Normal | 0 | Sim (+3) |
| Difícil | 3 | Alta | 25 | Sim (+3) |

- A cada 100 pontos, no médio e no difícil, 3 novas barreiras surgem no tabuleiro em posições aleatórias (nunca em cima da cobra ou da comida).
- **Nota de design:** a posição da nova barreira é sorteada de forma totalmente aleatória, podendo ocasionalmente surgir próxima ou à frente da cobra. Isso foi uma decisão consciente do grupo para manter o elemento de imprevisibilidade como parte do desafio, e não um bug.
- Impedir virada de 180°: a cobra nunca pode inverter o sentido diretamente sobre si mesma.

## 🏆 Ranking

- Ao final de cada partida, o nick e a pontuação são salvos em `ranking.txt`
- O ranking completo é exibido no terminal, ordenado da maior para a menor pontuação
