#5.1
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_lista = input("Digite as temperaturas em Celsius separadas por espaços: ").split()

print("Temperaturas em Fahrenheit:")
for celsius in celsius_lista:
    celsius = float(celsius)
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

###################
#5.2
def fahr_para_celsius(f):
    return (5 / 9) * (f - 32)

def cria_tabela_celsius(fahr):
    celsius = [None] * len(fahr)
    
    for i, temp in enumerate(fahr):
        celsius[i] = fahr_para_celsius(fahr[i])
    
    return celsius

def main():
    inicio = int(input('Qual o início das temperaturas Fahrenheit? '))
    fim = int(input('Qual o final das temperaturas Fahrenheit? '))
    passo = int(input('Qual o passo das temperaturas Fahrenheit? '))
    
    fahr = range(fim, inicio - 1, -passo)
    
    celsius = cria_tabela_celsius(fahr)
    
    print('Tabela de conversão de Fahrenheit para Celsius')
    
    for i, temp in enumerate(fahr):
        print('{:>5d} -> {:>5.1f}'.format(temp, celsius[i]))

main()
###########################
#5.3
def fahr_para_celsius(f):
    return (5 / 9) * (f - 32)

def cria_tabela_celsius(fahr):
    celsius = [None] * len(fahr)
    
    for i, temp in enumerate(fahr):
        celsius[i] = fahr_para_celsius(fahr[i])
    
    return celsius

def obter_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um valor inteiro válido.")

def main():
    inicio = obter_inteiro('Qual o início das temperaturas Fahrenheit? ')
    fim = obter_inteiro('Qual o final das temperaturas Fahrenheit? ')
    passo = obter_inteiro('Qual o passo das temperaturas Fahrenheit? ')
    

    fahr = range(fim, inicio - 1, -passo)
    
    celsius = cria_tabela_celsius(fahr)
    
    print('Tabela de conversão de Fahrenheit para Celsius')
    
    for i, temp in enumerate(fahr):
        print('{:>5d} -> {:>5.1f}'.format(temp, celsius[i]))

main()



##########################
#5.4

def fahr_para_celsius(f):
    return (5 / 9) * (f - 32)

def cria_tabela_celsius(fahr):
    celsius = [None] * len(fahr)
    
    for i, temp in enumerate(fahr):
        celsius[i] = fahr_para_celsius(fahr[i])
    
    return celsius

def obter_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Por favor, insira um valor inteiro válido.")

def main():
    inicio = obter_inteiro('Qual o início das temperaturas Fahrenheit? ')
    fim = obter_inteiro('Qual o final das temperaturas Fahrenheit? ')
    passo = obter_inteiro('Qual o passo das temperaturas Fahrenheit? ')
    
    fahr = range(fim, inicio - 1, -passo)
    
    celsius = cria_tabela_celsius(fahr)
    
    print('Tabela de conversão de Fahrenheit para Celsius')
    
    for i, temp in enumerate(fahr):
        print('{:>5d} -> {:>5.1f}'.format(temp, celsius[i]))

main()

##########################
#5.5
numeros_impares = list(range(1, 101, 2))
for indice, valor in enumerate(numeros_impares):
    numeros_impares[indice] = valor + 1

print(numeros_impares)

##########################
#5.6
import random

def calcula_pi(num_pontos):
    dentro_circulo = 0
    
    for _ in range(num_pontos):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distancia = x**2 + y**2
        
        if distancia <= 1:
            dentro_circulo += 1
    
    return (dentro_circulo / num_pontos) * 4


valores_pi = []

for num_pontos in range(1000, 11000, 1000):  
    pi_aproximado = calcula_pi(num_pontos)
    valores_pi.append((num_pontos, pi_aproximado))

print("Número de Pontos | Valor de Pi Aproximado")
print("-" * 40)

for num_pontos, pi_aproximado in valores_pi:
    print(f"{num_pontos:<16} | {pi_aproximado:.6f}")
#############################
#5.7

quadrados_pares = []

for numero in range(10, 21):
    if numero % 2 == 0:
        quadrado = numero ** 2
        quadrados_pares.append(quadrado)
print(quadrados_pares)
###############################
#5.8
quadrados_impares = []

for numero in range(10):
    if numero % 2 != 0:
        quadrado = numero ** 2
        quadrados_impares.append(quadrado)

print(quadrados_impares)
###############################
#5.9
cubos = []

for numero in range(1, 11):
    cubo = numero ** 3
    cubos.append(cubo)

print(cubos)
###############################
#5.10
multiplos_de_sete = []
contador = 1
while len(multiplos_de_sete) < 10:
    multiplo = contador * 7
    multiplos_de_sete.append(multiplo)
    contador += 1

print(multiplos_de_sete)
#############################
#5.11
lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

maiores_ou_iguais_a_5 = [x for x in lista_original if x >= 5]
menores_que_5 = [x for x in lista_original if x < 5]

lista_reorganizada = maiores_ou_iguais_a_5 + menores_que_5

print(lista_reorganizada)
##########################
#5.12
lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numeros_impares = [x for x in lista_original if x % 2 != 0]
numeros_pares = [x for x in lista_original if x % 2 == 0]

lista_reorganizada = numeros_impares + numeros_pares

print(lista_reorganizada)
#########################
#5.13
lista = [10, 2, 32, 14, 35, 46, 17, 58, 199, 19]

print("Elementos de índices pares:")
for i in range(0, len(lista), 2):
    print(lista[i])

print("Elementos de índices ímpares:")
for i in range(1, len(lista), 2):
    print(lista[i])

print("Elementos entre os índices 2 e 4:")
for i in range(2, 4):
    print(lista[i])

print("Elemento de índice 1 e elementos distantes 3 posições:")
print(lista[1])
for i in range(4, len(lista), 3):
    print(lista[i])
##########################
#5.14
lista = list(range(100))

print("Último elemento da lista e elementos distantes 3 posições a partir do final até o início:")
print(lista[-1])
for i in range(-4, -len(lista) - 1, -3):
    print(lista[i])

print("Elementos entre os índices 87 e 34 em ordem decrescente de índices:")
for i in range(87, 33, -1):
    print(lista[i])

print("Todos os elementos, exceto os dois últimos:")
print(lista[:-2])
##########################
#5.15

lista = [1, 2, 3, 4, 5, 6, 7]
lista_inversa = lista[::-1]

print(lista_inversa)
#########################
#5.16
planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Saturno', 'Júpiter', 'Urano', 'Netuno']

planetas[4:4] = ['Fobos', 'Deimos']

planetas[0:0] = ['Sol']

resultado = planetas[6:4:-1] + planetas[4:2:-1] + planetas[3:1:-1] + planetas[0:0:-1]

print(resultado)

##########################
#5.17
"""
Quando você chama o método append() com outra lista, a lista que você forneceu como argumento é adicionada 
como um único elemento à lista original. 
Em outras palavras, a lista fornecida é anexada como um único item da lista de destino. 
Portanto, se você usar o comando primos.append([23, 29, 31]) na lista primos original, 
a lista [23, 29, 31] será adicionada como um elemento à lista primos.
"""

primos = [2, 3, 5, 7]
primos.append([23, 29, 31])

print(primos)

[2, 3, 5, 7, [23, 29, 31]]
##########################
#5.18
primos = [2, 3, 5, 7]

primos.extend([23, 29, 31])

print(primos)
###########################
#5.19
















