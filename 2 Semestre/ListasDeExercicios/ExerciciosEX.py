#Nivel Iniciante

#1.
# vetor = [1,2,3,4,5,6,7,8,9,10]

# soma = sum(vetor)

# print(soma)
#2.
def somar_vetores(vetor1, vetor2):

    if len(vetor1) != len(vetor2):
        print("Os vetores devem ter o mesmo comprimento")
    soma = []

    for i in range(len(vetor1)):
        soma.append(vetor1[i] + vetor2[i])

    return soma

vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

resultado = somar_vetores(vetor1, vetor2)
print("A soma dos vetores é:", resultado)
#3.
def matriz_transposta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

matriz_original = [
    [1, 2, 3],
    [4, 5, 6]
]

resultado = matriz_transposta(matriz_original)
for linha in resultado:
    print(linha)


#4
#jeito do professor
# def e_simetrica(matriz:list) -> bool:
#     tam = len(matriz)
#     for i in range(tam):
#         for j in range(tam):
#             if i !=j and matriz[i][j] != matriz[j][i]:
#                 return False
#     return True
# matriz = [
#     [1,2,4],
#     [2,5,6],
#     [4,6,7]
# ]

# print(e_simetrica(matriz))

########################

def matriz_simetrica(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    if num_linhas != num_colunas:
        return False

    for i in range(num_linhas):
        for j in range(num_colunas):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True

matriz_simetrica1 = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

matriz_simetrica2 = [
    [1, 2, 3],
    [2, 4, 2],
    [3, 2, 5]
]

print(matriz_simetrica(matriz_simetrica1))
print(matriz_simetrica(matriz_simetrica2)) 

#5
def media_matriz(matriz:list) -> float:
    qtd = 0
    soma = 0
    for linha in matriz:
        soma += sum(linha)
        qtd += len(linha)
    media = soma / qtd
    return media
#intermediario
#1
def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo comprimento")

    resultado = 0

    for i in range(len(vetor1)):
        resultado += vetor1[i] * vetor2[i]

    return resultado

vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

resultado = produto_escalar(vetor1, vetor2)
print(f'O produto escalar entre os vetores é: {resultado}')
#2
#Jeito do Professor
#def produto_escalar(matriz:list,escalar:int) -> list:
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             matriz[i][j] *= escalar

#     return matriz

# matriz = [
#     [1,2,4],
#     [2,5,6],
#     [4,6,7]
# ]

# print(produto_escalar(matriz,5))
#####################################       

# def multiplicar_matriz_por_escalar(matriz, escalar):
#     resultado = []
#     for linha in matriz:
#         nova_linha = [elemento * escalar for elemento in linha]
#         resultado.append(nova_linha)
#     return resultado

# matriz_original = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# escalar = 2
# resultado = multiplicar_matriz_por_escalar(matriz_original, escalar)

# for linha in resultado:
#     print(linha)
#################################


#3
# def matriz_identidade(n):
#     if n <= 0:
#         raise ValueError("A ordem da matriz identidade deve ser um número inteiro positivo.")

#     identidade = [[0] * n for _ in range(n)]

#     for i in range(n):
#         identidade[i][i] = 1

#     return identidade

# ordem = 3  

# matriz_resultante = matriz_identidade(ordem)

# for linha in matriz_resultante:
#     print(linha)


#Exerc9
def determinante(matriz:list) -> int:
    dp = 1
    ds = 1
    for i, l in enumerate(matriz):
        for j, v in enumerate(l):
            if i == j:
                dp *= matriz[i][j]
            else:
                ds *= matriz[i][j]
    return dp - ds

matriz = [
    [1,2],
    [3,4],
]

print(determinante(matriz))































##########
