# ==========================================
# JOGO DA VELHA 3x3
# Trabalho avaliativo - Coding
# ==========================================

import os

# PLACAR GERAL
vitorias_x = 0
vitorias_o = 0
empates = 0
total_partidas = 0


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_placar():
    print("\n===== PLACAR GERAL =====")
    print(f"Jogador X: {vitorias_x}")
    print(f"Jogador O: {vitorias_o}")
    print(f"Empates: {empates}")
    print(f"Total de partidas: {total_partidas}")
    print("========================\n")


def exibir_tabuleiro(tabuleiro):
    print("\n   1   2   3")
    for i in range(0, 9, 3):
        print(f" {tabuleiro[i]} | {tabuleiro[i + 1]} | {tabuleiro[i + 2]} ")
        if i < 6:
            print("---+---+---")
    print()


def verificar_vencedor(tabuleiro):
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinacoes:
        if tabuleiro[a] != ' ' and tabuleiro[a] == tabuleiro[b] == tabuleiro[c]:
            return tabuleiro[a]

    return None


def partida_nova():
    global vitorias_x, vitorias_o, empates, total_partidas

    tabuleiro = [' '] * 9
    jogador_atual = 'X'

    while True:
        limpar_tela()
        mostrar_placar()
        exibir_tabuleiro(tabuleiro)

        print(f"Vez do jogador {jogador_atual}")
        escolha = input("Escolha uma posição de 1 a 9 (ou 0 para sair): ")

        if escolha == '0':
            return False

        if not escolha.isdigit():
            print("Entrada inválida! Digite um número de 1 a 9.")
            input("Pressione Enter para continuar...")
            continue

        posicao = int(escolha) - 1

        if not 0 <= posicao <= 8:
            print("Posição fora do intervalo.")
            input("Pressione Enter para continuar...")
            continue

        if tabuleiro[posicao] != ' ':
            print("Essa posição já está ocupada.")
            input("Pressione Enter para continuar...")
            continue

        tabuleiro[posicao] = jogador_atual
        vencedor = verificar_vencedor(tabuleiro)

        if vencedor:
            total_partidas += 1

            if vencedor == 'X':
                vitorias_x += 1
                mensagem = "Jogador X venceu!"
            else:
                vitorias_o += 1
                mensagem = "Jogador O venceu!"

            limpar_tela()
            mostrar_placar()
            exibir_tabuleiro(tabuleiro)
            print(mensagem)
            input("Pressione Enter para continuar...")
            return True

        if ' ' not in tabuleiro:
            total_partidas += 1
            empates += 1

            limpar_tela()
            mostrar_placar()
            exibir_tabuleiro(tabuleiro)
            print("Empate! Ninguém venceu.")
            input("Pressione Enter para continuar...")
            return True

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'


if __name__ == "__main__":
    while True:
        continuar = partida_nova()
        if not continuar:
            limpar_tela()
            print("Jogo encerrado. Obrigado por jogar!")
            break

        resposta = input("Deseja jogar outra partida? (S/N): ").strip().lower()
        if resposta not in ('s', 'sim'):
            limpar_tela()
            print("Jogo encerrado. Obrigado por jogar!")
            break