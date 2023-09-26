#Campo minado

from random import randint

def criar_campo(tamanho:int) -> list:
    campo_minado = []
    for i in range(tamanho):
        linha = []
        bomba1= randint(0,tamanho-1)
        bomba2 = randint(0,tamanho-1)
        for i in range(tamanho):
            linha.append('@' if i == bomba1 or i == bomba2 else '')
        campo_minado.append(linha)

    return campo_minado

def menu() -> int:
    tamanho_matriz = 0
    continua = True
    while continua:
        tamanho_matriz = int(input('Qual o tamanho da matriz: '))
        continua = tamanho_matriz < 5
        print('Tamanho inválido' if continua else '')
    return tamanho_matriz

def exibir(matriz:list) -> None:
    for linha in matriz:
        print(linha)

tamanho = menu()
cm = criar_campo(tamanho)
exibir(cm)