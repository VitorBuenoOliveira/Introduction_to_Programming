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
#6
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
#7
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


#8
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
#########################

#10
def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("O número de colunas da matriz 1 deve ser igual ao número de linhas da matriz 2")

    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
#######################

#11
def produto_vetorial(vetor1, vetor2):
    if len(vetor1) != 3 or len(vetor2) != 3:
        raise ValueError("Ambos os vetores devem ser tridimensionais (compostos por três componentes)")

    resultado = [
        vetor1[1] * vetor2[2] - vetor1[2] * vetor2[1],
        vetor1[2] * vetor2[0] - vetor1[0] * vetor2[2],
        vetor1[0] * vetor2[1] - vetor1[1] * vetor2[0]
    ]

    return resultado    
##########

#12
import numpy as np

def encontrar_autovalores_e_autovetores(matriz):
    autovalores, autovetores = np.linalg.eig(matriz)
    return autovalores, autovetores

matriz = np.array([[2, -1],
                   [4,  3]])

autovalores, autovetores = encontrar_autovalores_e_autovetores(matriz)

print("Autovalores:")
print(autovalores)

print("\nAutovetores:")
print(autovetores)
################3
#13
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def gauss_elimination(matrix):
    n = len(matrix)

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        pivot = matrix[i][i]
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    return [row[-1] for row in matrix]

# 2x + 3y - z = 1
# 4x + y + 2z = 2
# 3x + 2y + 3z = 3

augmented_matrix = [
    [2, 3, -1, 1],
    [4, 1, 2, 2],
    [3, 2, 3, 3]
]

solution = gauss_elimination(augmented_matrix)

print("Solução do sistema:")
for i, x in enumerate(solution):
    print(f"x{i + 1} = {x}")
#############
#14
import numpy as np

def matrix_inverse(matrix):
    try:
        if matrix.shape[0] != matrix.shape[1]:
            raise ValueError("A matriz não é quadrada")

        adjoint = np.linalg.inv(matrix)

        return adjoint
    except np.linalg.LinAlgError:
        raise ValueError("A matriz não possui matriz inversa")

matrix = np.array([[2, 3, -1],
                  [4, 1, 2],
                  [3, 2, 3]])

inverse = matrix_inverse(matrix)

print("Matriz Original:")
print(matrix)

print("Matriz Inversa:")
print(inverse)
##########
#15
import numpy as np

def jacobi_eigenvalue(A, tol=1e-6, max_iter=100):
    n = len(A)
    eigenvalues = np.zeros(n)
    iterations = 0

    while True:
        max_val = 0
        for i in range(n):
            for j in range(i+1, n):
                if abs(A[i][j]) > max_val:
                    max_val = abs(A[i][j])
                    p, q = i, j

        if max_val < tol or iterations >= max_iter:
            break

        theta = 0.5 * np.arctan2(2 * A[p][q], A[q][q] - A[p][p])

        rotation = np.identity(n)
        rotation[p][p] = np.cos(theta)
        rotation[q][q] = np.cos(theta)
        rotation[p][q] = -np.sin(theta)
        rotation[q][p] = np.sin(theta)

        A = np.dot(np.dot(rotation.T, A), rotation)

        iterations += 1

    eigenvalues = np.diag(A)

    return eigenvalues

matrix = np.array([[4, -2, 2],
                   [-2, 2, -4],
                   [2, -4, 11]])

eigenvalues = jacobi_eigenvalue(matrix)

print("Autovalores:")
print(eigenvalues)
########################3
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
