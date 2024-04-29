import random

def criar_tabuleiro(linhas, colunas, bombas):
    tabuleiro = [['🟦' for _ in range(colunas)] for _ in range(linhas)]
    bombas_colocadas = 0
    while bombas_colocadas < bombas:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if tabuleiro[linha][coluna] != '💣':
            tabuleiro[linha][coluna] = '💣'
            bombas_colocadas += 1
    return tabuleiro

def imprimir_tabuleiro(tabuleiro_visivel):
    for linha in tabuleiro_visivel:
        print(' '.join(linha))

def contar_bombas_vizinhas(tabuleiro, linha, coluna):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    bombas_vizinhas = 0
    for i in range(max(0, linha - 1), min(linhas, linha + 2)):
        for j in range(max(0, coluna - 1), min(colunas, coluna + 2)):
            if tabuleiro[i][j] == '💣':
                bombas_vizinhas += 1
    return bombas_vizinhas

def revelar_tabuleiro(tabuleiro, tabuleiro_visivel, linha, coluna):
    if linha < 0 or linha >= len(tabuleiro) or coluna < 0 or coluna >= len(tabuleiro[0]):
        return
    if tabuleiro_visivel[linha][coluna] != '🟦':
        return
    if tabuleiro[linha][coluna] == '💣':
        tabuleiro_visivel[linha][coluna] = '💥'
    else:
        tabuleiro_visivel[linha][coluna] = str(contar_bombas_vizinhas(tabuleiro, linha, coluna))
        if tabuleiro_visivel[linha][coluna] == '0':
            for i in range(-1, 2):
                for j in range(-1, 2):
                    revelar_tabuleiro(tabuleiro, tabuleiro_visivel, linha + i, coluna + j)

def jogar():
    linhas = int(input("Digite o número de linhas do tabuleiro: "))
    colunas = int(input("Digite o número de colunas do tabuleiro: "))
    bombas = int(input("Digite o número de bombas: "))

    tabuleiro = criar_tabuleiro(linhas, colunas, bombas)
    tabuleiro_visivel = [['🟦' for _ in range(colunas)] for _ in range(linhas)]
    bombas_marcadas = 0
    celulas_reveladas = 0
    total_celulas = linhas * colunas

    jogando = True

    while jogando:
        imprimir_tabuleiro(tabuleiro_visivel)
        linha = int(input("Digite a linha: ")) - 1
        coluna = int(input("Digite a coluna: ")) - 1
        if tabuleiro[linha][coluna] == '💣':
            revelar_tabuleiro(tabuleiro, tabuleiro_visivel, linha, coluna)
            imprimir_tabuleiro(tabuleiro_visivel)
            print("Você encontrou uma bomba! Fim de jogo!")
            jogando = False
        else:
            revelar_tabuleiro(tabuleiro, tabuleiro_visivel, linha, coluna)
            if tabuleiro_visivel[linha][coluna] == '0':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        revelar_tabuleiro(tabuleiro, tabuleiro_visivel, linha + i, coluna + j)

            celulas_reveladas += 1
            if celulas_reveladas == total_celulas - bombas:
                print("Parabéns! Você venceu!")
                jogando = False


jogar()
