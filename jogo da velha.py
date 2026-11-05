# ==========================================
# JOGO DA VELHA 3x3
# Trabalho avaliativo - Coding
# ==========================================

# PLACAR GERAL
vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0
# CONTROLE DO MENU
opcao = ""

while opcao != "4":

    print("\n================================")
    print("       JOGO DA VELHA 3x3")
    print("================================")
    print("1 - Jogar uma partida")
    print("2 - Iniciar campeonato")
    print("3 - Ver placar")
    print("4 - Sair")
    print("================================")

    opcao = input("Escolha uma opção: ")
 # ======================================
    # OPÇÃO 1 - PARTIDA INDIVIDUAL
    # ======================================

    if opcao == "1" or opcao == "2":

        campeonato = False
        numero_partidas = 1
        pontos_x = 0
        pontos_o = 0

        if opcao == "2":

            campeonato = True

            print("\n===== CAMPEONATO =====")
            print("1 - Melhor de 3")
            print("2 - Melhor de 5")

            escolha = ""

            while escolha != "1" and escolha != "2":

                escolha = input("Escolha o campeonato: ")

                if escolha != "1" and escolha != "2":
                    print("Opção inválida!")

            if escolha == "1":
                numero_partidas = 3
            else:
                numero_partidas = 5

            maioria = (numero_partidas // 2) + 1

            print("\nCampeonato iniciado!")
            print("Número máximo de partidas:", numero_partidas)
            print("Vitórias necessárias:", maioria)
   # CONTROLE DAS PARTIDAS
        partida_atual = 0

        while partida_atual < numero_partidas and pontos_x < ((numero_partidas // 2) + 1) and pontos_o < ((numero_partidas // 2) + 1):

            partida_atual = partida_atual + 1
              # MATRIZ DO TABULEIRO
            tabuleiro = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ]

            jogador = "X"
            venceu = False
            empate = False

            print("\n================================")
            print("PARTIDA", partida_atual)
            print("================================")

            print("\nRegras:")
            print("Os jogadores alternam as jogadas.")
            print("Vence quem completar 3 símbolos iguais.")
            print("Se o tabuleiro encher, ocorre empate.")
     # REPETIÇÃO DAS JOGADAS
            while venceu == False and empate == False:

                # EXIBIÇÃO DO TABULEIRO 

                print("\n    1   2   3")

                for i in range(3):

                    print(" ", i + 1, end=" ")

                    for j in range(3):

                        print(tabuleiro[i][j], end="")

                        if j < 2:
                            print(" | ", end="")

                    print()

                    if i < 2:
                        print("   ---+---+---")
                     # IDENTIFICAÇÃO DO JOGADOR
                print("\nVez do jogador:", jogador)

                
            