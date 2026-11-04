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
