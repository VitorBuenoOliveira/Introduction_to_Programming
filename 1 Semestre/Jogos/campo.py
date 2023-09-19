import random

def criar_campo_minado(linhas, colunas, num_minas):
    # Crie um tabuleiro vazio preenchido com zeros
    tabuleiro = [[0 for _ in range(colunas)] for _ in range(linhas)]

    # Coloque minas aleatoriamente no tabuleiro
    minas_colocadas = 0
    while minas_colocadas < num_minas:
        linha = random.randint(0, linhas - 1)
        coluna = random.randint(0, colunas - 1)
        if tabuleiro[linha][coluna] != -1:
            tabuleiro[linha][coluna] = -1
            minas_colocadas += 1

    # Preencha as dicas (números)
    for linha in range(linhas):
        for coluna in range(colunas):
            if tabuleiro[linha][coluna] != -1:
                num_minas_vizinhas = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= linha + i < linhas and 0 <= coluna + j < colunas:
                            if tabuleiro[linha + i][coluna + j] == -1:
                                num_minas_vizinhas += 1
                tabuleiro[linha][coluna] = num_minas_vizinhas

    return tabuleiro

def exibir_campo_minado(tabuleiro):
    for linha in tabuleiro:
        for celula in linha:
            if celula == -1:
                print("*", end=" ")
            else:
                print(celula, end=" ")
        print()

# Tamanho personalizado do campo minado
linhas = 5
colunas = 5
num_minas = 5

campo_minado = criar_campo_minado(linhas, colunas, num_minas)
exibir_campo_minado(campo_minado)
