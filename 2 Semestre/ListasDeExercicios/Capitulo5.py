#5.1
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_lista = input("Digite as temperaturas em Celsius separadas por espaços: ").split()

print("\nTemperaturas em Fahrenheit:")
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
#5.14

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
#5.15
numeros_impares = list(range(1, 101, 2))
for indice, valor in enumerate(numeros_impares):
    numeros_impares[indice] = valor + 1

print(numeros_impares)

##########################
#5.16
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
#5.17




