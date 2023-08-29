#Exercicio 4.1
# import math

# def print_table():
#     print("| {:<13} | {:<9} | {:<10} | {:<13} |".format("Ângulo (graus)", "Seno", "Cosseno", "Tangente"))
#     print("|--------------|---------|------------|--------------|")

#     for angle in range(0, 361, 30):
#         radians = math.radians(angle)
#         sin_val = math.sin(radians)
#         cos_val = math.cos(radians)

#         if angle == 90:
#             tangent_val = math.inf
#         elif angle == 270:
#             tangent_val = -math.inf
#         else:
#             tangent_val = math.tan(radians)

#         print("| {:<13} | {:<9.3f} | {:<10.3f} | {:<13}".format(angle, sin_val, cos_val, tangent_val))

# print_table()

#####################
#Exerc 4.2
import math

def print_square_root_table():
    print("| {:<5} | {:<15} |".format("Número", "Raiz Quadrada"))
    print("|-------|----------------|")

    for number in range(1, 101, 10):
        square_root = math.sqrt(number)
        print("| {:<5} | {:<15.5f} |".format(number, square_root))

print_square_root_table()
#####################
#Exerc 4.3
def main():
    try:
        number = float(input("Digite um número: "))
        square = number ** 2
        cube = number ** 3

        print(f"Número: {number:.2f}")
        print(f"Quadrado: {square:.2f}")
        print(f"Cubo: {cube:.2f}")
    except ValueError:
        print("Entrada inválida. Insira um número válido.")

if __name__ == "__main__":
    main()
######################
#Exerc 4.5
def print_triangle(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))

def print_square(side_length):
    for i in range(side_length):
        print("*" * side_length)

def main():
    shape = input("Digite 'triangulo' ou 'quadrado' para escolher a forma: ")

    if shape == "triangulo":
        height = int(input("Digite a altura do triângulo: "))
        print_triangle(height)
    elif shape == "quadrado":
        side_length = int(input("Digite o comprimento do lado do quadrado: "))
        print_square(side_length)
    else:
        print("Forma não reconhecida.")

if __name__ == "__main__":
    main()
##############################
#exerc 4.6
def print_tree(height):
    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

def main():
    tree_height = int(input("Digite a altura da árvore de Natal: "))
    trunk_height = tree_height // 3

    for i in range(1, tree_height - trunk_height + 1):
        print_tree(i)

    for i in range(trunk_height):
        print(" " * (tree_height - trunk_height) + "*" * (trunk_height * 2 - 1))

if __name__ == "__main__":
    main()
############################
#Exerc 4.7
def imprimir_conceito(nota):
    if nota >= 9.0:
        conceito = 'A'
    elif nota >= 8.0:
        conceito = 'B'
    elif nota >= 7.0:
        conceito = 'C'
    elif nota >= 5.0:
        conceito = 'D'
    else:
        conceito = 'E'

    print(f"Conceito: {conceito}")

def main():
    try:
        nota = float(input("Digite a nota (entre 0.0 e 10.0): "))
        if 0.0 <= nota <= 10.0:
            imprimir_conceito(nota)
        else:
            print("Nota fora do intervalo permitido.")
    except ValueError:
        print("Entrada inválida. Insira uma nota válida.")

if __name__ == "__main__":
    main()
################################
#Exerc 4.8
def calcular_quadrado(numero):
    quadrado = numero ** 2
    return quadrado

def main():
    try:
        valor = int(input("Digite um valor inteiro: "))
        resultado = calcular_quadrado(valor)
        print(f"O quadrado de {valor} é {resultado}.")
    except ValueError:
        print("Entrada inválida. Insira um valor inteiro.")

if __name__ == "__main__":
    main()
#################################
#Exerc 4.9
def fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("| {:<10} | {:<10} |".format("Celsius", "Fahrenheit"))
    print("|------------|------------|")

    for celsius in range(0, 101, 10):
        fahrenheit_value = fahrenheit(celsius)
        print("| {:<10} | {:<10.2f} |".format(celsius, fahrenheit_value))

if __name__ == "__main__":
    main()
#############################
#Exerc 4.10
def celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        inicio = int(input("Digite o valor de início (em Fahrenheit): "))
        fim = int(input("Digite o valor de fim (em Fahrenheit): "))
        passo = int(input("Digite o valor do passo: "))

        print("| {:<12} | {:<12} |".format("Fahrenheit", "Celsius"))
        print("|--------------|--------------|")

        for fahrenheit in range(inicio, fim + 1, passo):
            celsius_value = celsius(fahrenheit)
            print("| {:<12} | {:<12.2f} |".format(fahrenheit, celsius_value))

    except ValueError:
        print("Entrada inválida. Certifique-se de inserir valores numéricos.")

if __name__ == "__main__":
    main()
############################
#Exerc 4.11
import math

def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    try:
        x1 = float(input("Digite a coordenada x do primeiro ponto: "))
        y1 = float(input("Digite a coordenada y do primeiro ponto: "))
        x2 = float(input("Digite a coordenada x do segundo ponto: "))
        y2 = float(input("Digite a coordenada y do segundo ponto: "))

        dist = distancia(x1, y1, x2, y2)
        print(f"A distância entre os pontos é: {dist:.2f}")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir coordenadas numéricas.")

if __name__ == "__main__":
    main()
############################
#Exerc 4.12
import random

def calcular_pi(num_pontos):
    dentro_circulo = 0

    for _ in range(num_pontos):
        x = random.random()
        y = random.random()

        distancia = x**2 + y**2

        if distancia <= 1:
            dentro_circulo += 1

    pi_aproximado = (dentro_circulo / num_pontos) * 4
    return pi_aproximado

def main():
    while True:
        try:
            num_pontos = int(input("Digite o número de pontos a serem sorteados (0 para sair): "))
            
            if num_pontos == 0:
                print("Programa encerrado.")
                break
            
            pi_estimado = calcular_pi(num_pontos)
            print(f"Estimativa de pi com {num_pontos} pontos: {pi_estimado:.6f}")
        except ValueError:
            print("Entrada inválida. Insira um número inteiro.")

if __name__ == "__main__":
    main()
#########################
#Exerc 4.13
import random

def lancar_dado():
    return random.randint(1, 6)

def main():
    num_lancamentos = int(input("Digite o número de lançamentos: "))

    for _ in range(num_lancamentos):
        resultado = lancar_dado()
        print(f"Resultado do lançamento: {resultado}")

if __name__ == "__main__":
    main()
########################
#Exerc 4.14
#Exerc 4.15
########################
#Exerc 4.16
def main():
    minha_lista = [10, 20, 30]

    try:
        indice = int(input("Digite o índice (0, 1 ou 2) para imprimir um elemento: "))
        
        if 0 <= indice <= 2:
            elemento = minha_lista[indice]
            print(f"Elemento no índice {indice}: {elemento}")
        else:
            raise IndexError("Índice fora da faixa permitida (0 a 2).")
    
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
    except IndexError as e:
        print(e)

if __name__ == "__main__":
    main()
########################
#Exerc 4.17
def main():
    minha_lista = [10, 20, 30]

    try:
        indice = int(input("Digite o índice (0, 1 ou 2) para imprimir um elemento: "))
        
        if 0 <= indice <= 2:
            elemento = minha_lista[indice]
            print(f"Elemento no índice {indice}: {elemento}")
        else:
            raise IndexError("Índice fora da faixa permitida (0 a 2).")
    
    except ValueError:
        print("Entrada inválida. Insira um número inteiro.")
    except IndexError as e:
        print(e)

if __name__ == "__main__":
    main()
#######################

