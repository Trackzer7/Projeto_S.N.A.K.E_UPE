#cadastro de novo jogador
nick = str(input("Digite seu nick: "))
pontos = int(input("Digite sua pontuação: "))

#salva no arquivo
with open ("ranking.txt", "a") as arquivo:
    arquivo.write(f"{nick}, {pontos}\n")

print("\nJogador cadastrado: ")
print("nick:", nick)
print("pontos:", pontos)

print("\nPontuação salva com sucesso!!")

#ranking ordenado
print("\n--- RANKING ---")

lista_pontos = []

#lê os dados do arquivo
try:
 with open ("ranking.txt", "r") as arquivo:
    for linha in arquivo:
        if "," in linha:
            nick_lido, pontos_lidos = linha.strip().split(",")
            lista_pontos.append((nick_lido.strip(), int(pontos_lidos)))
    #ordena a lista pelo segundo item da tupla(pontos), do maior para o menor
    lista_pontos.sort(key=lambda x: x[1], reverse=True)

    #imprime o ranking
    for i, (nick, pontos) in enumerate(lista_pontos, 1):
        print(f"{i}o lugar: {nick} - {pontos} pontos")
except FileNotFoundError:
    print("Ainda não há pontuações registradas!")