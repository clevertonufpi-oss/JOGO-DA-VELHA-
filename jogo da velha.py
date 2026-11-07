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
# VALIDAÇÃO DA JOGADA
                jogada_valida = False

                while jogada_valida == False:

# LEITURA DA LINHA
                    linha_valida = False

                    while linha_valida == False:

                        entrada = input("Digite a linha (1 a 3): ")

                        for n in range(1, 4):

                            if entrada == str(n):
                                linha = n - 1
                                linha_valida = True

                        if linha_valida == False:
                            print("Linha inválida! Digite de 1 a 3.")

# LEITURA DA COLUNA
                    coluna_valida = False

                    while coluna_valida == False:

                        entrada = input("Digite a coluna (1 a 3): ")

                        for n in range(1, 4):

                            if entrada == str(n):
                                coluna = n - 1
                                coluna_valida = True

                        if coluna_valida == False:
                            print("Coluna inválida! Digite de 1 a 3.")
# VERIFICAÇÃO DA CASA
                    if tabuleiro[linha][coluna] == " ":

                        tabuleiro[linha][coluna] = jogador
                        jogada_valida = True

                    else:

                        print("\nEssa casa já está ocupada!")
                        print("Escolha outra posição.")
# VERIFICAÇÃO DE VITÓRIA
                venceu = False
# VERIFICAÇÃO DE LINHAS
                for i in range(3):
                    
                    if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:

                        venceu = True
#VERIFICAÇÃO DE COLUNAS
                for j in range(3):

                    if tabuleiro[0][j] == jogador and tabuleiro[1][j] == jogador and tabuleiro[2][j] == jogador:

                        venceu = True
#VERIFICAÇÃO DE DIAGONAIS
                if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:

                    venceu = True

                if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:

                    venceu = True
#VERIFICAÇÃO DE EMPATE
                casas_vazias = 0
                for i in range(3):

                    for j in range(3):

                        if tabuleiro[i][j] == " ":

                            casas_vazias = casas_vazias + 1

                if casas_vazias == 0 and venceu == False:

                    empate = True
#RESULTADO DA JOGADA
                if venceu == False and empate == False:

                    if jogador == "X":
                        jogador = "O"
                    else:
                        jogador = "X"

#EXIBIÇÃO DO TABULEIRO FINAL

            print  ("\n========================================")
            print  ("       TABULEIRO FINAL")
            print  ("========================================")

            print("\n   1  2  3  ")

            for i in range(3):

                print(" ",i + 1, end=" ")

                for j in range(3):

                    print(tabuleiro[i][j], end=" ")

                    if j < 2:

                        print(" | ", end="")

            print()

            if i < 2:
                print("  ---+---+---")

