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
def calcular_media_matriz(matriz):
    if not matriz:
        return None

    soma = 0
    contador = 0

    for linha in matriz:
        for elemento in linha:
            soma += elemento
            contador += 1

    if contador > 0:
        media = soma / contador
        return media
    else:
        return None

matriz_exemplo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

media = calcular_media_matriz(matriz_exemplo)

if media is not None:
    print(f'A média dos elementos da matriz é: {media}')
else:
    print('A matriz está vazia, a média não pode ser calculada.')

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
def multiplicar_matriz_por_escalar(matriz, escalar):
    resultado = []
    for linha in matriz:
        nova_linha = [elemento * escalar for elemento in linha]
        resultado.append(nova_linha)
    return resultado

matriz_original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

escalar = 2
resultado = multiplicar_matriz_por_escalar(matriz_original, escalar)

for linha in resultado:
    print(linha)

#3
def matriz_identidade(n):
    if n <= 0:
        raise ValueError("A ordem da matriz identidade deve ser um número inteiro positivo.")

    identidade = [[0] * n for _ in range(n)]

    for i in range(n):
        identidade[i][i] = 1

    return identidade

ordem = 3  

matriz_resultante = matriz_identidade(ordem)

for linha in matriz_resultante:
    print(linha)































##########
