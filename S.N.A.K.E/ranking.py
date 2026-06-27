def salvar_pontos(nick, pontuacao):
    # salva o nick e a pontuacao no arquivo
    with open("ranking.txt", "a") as arquivo_escrita:
        arquivo_escrita.write(f"{nick}, {pontuacao}\n")

    print("\nJogador cadastrado:")
    print("nick:", nick)
    print("pontos:", pontuacao)
    print("\nPontuação salva com sucesso!!")

    # lê e exibe o ranking ordenado
    print("\n--- RANKING ---")
    lista_pontos = []

    try:
        with open("ranking.txt", "r") as arquivo_leitura:
            for linha in arquivo_leitura:
                if "," in linha:
                    nick_lido, pontos_lidos = linha.strip().split(",")
                    lista_pontos.append((nick_lido.strip(), int(pontos_lidos)))

        # ordena do maior para o menor
        lista_pontos.sort(key=lambda x: x[1], reverse=True)

        # imprime o ranking
        for i, (n, p) in enumerate(lista_pontos, 1):
            print(f"{i}o lugar: {n} - {p} pontos")

    except FileNotFoundError:
        print("Ainda não há pontuações registradas!")
