# Faça um programa em Python que calcule a área de um quadrado. Exerc 2.9

# Exerc 3.1

# lado_base = int(2)

# lado_altura= int(2)

# formula = lado_base * lado_altura


# print(formula)
# ===============
#3.2
# lado_base = float(2)

# lado_altura= float(2)

# formula = lado_base * lado_altura


# print(formula)
#===================
# 3.3
# o numero com int é sem valor, já o float é com virgula, portanto se colocarmos um valor quebrado no int ira dar erro

#==================
#3.4
# valor_1 = 37

# decifra = valor_1 % 2

# if decifra == 0:
#     print("Seu Valor é Par")
# else:
#     print("Seu valor é Impar")
#===================
#3.5
# numero1 = int(input("Digite seu primeiro numero: "))
# numero2 = int(input("Digite seu segundo numero: "))

# if numero2 % numero1 == 0:
#     print(f"{numero2} é um multiplo de {numero1}")
# else:
#     print(f"{numero2} não é um múltiplo de {numero1}")
#===================
#3.6
# valor1 = int(input("Digite seu valor: "))

# if (valor1 % 3) == 0:
#     print("Seu valor é divisivel por 3")
# if (valor1 % 5) == 0:
#     print("Seu valor é divisivel por 5")
# if (valor1 % 7) == 0:
#     print("Seu valor é divisivel por 7")
# else:
#     print("Não é multiplo de 3,5,7")
#===================
#3.7
# Uma empresa vai conceder um aumento diferenciado a seus funcionários, 
# segundo os seguintes critérios: quem ganha até 1000 reais (inclusive) terá aumento de 20 %; 
# entre 1000 e 2000 (inclusive), aumento de 18 %; entre 2000 e 4000 (inclusive) 
# aumento de 15 % e acima de 4000 aumento de 10 %. Escreva um programa que, 
# dado um valor de salário, calcule o novo valor após o aumento.

# salario = 2700

# if salario <= 1000:
#     salario_novo=salario*0.20
#     print(f'Seu salario terá um aumento de {salario_novo}')

# elif salario <= 2000:
#     salario_novo=salario*0.18
#     print(f'Seu salario terá um aumento de {salario_novo}')


# elif salario <= 4000:
#     salario_novo=salario*0.20
#     print(f'Seu salario terá um aumento de {salario_novo}')

# else:
#     salario_novo = salario * 0.10
#     print(salario_novo)

#===========================

#3.8
# ang1 = float(input("Digite o primeiro angulo: "))
# ang2 = float(input("Digite o segundo angulo: "))
# ang3 = float(input("Digite o terceiro angulo: "))

# if ang1 == ang2 and ang2 == ang3:
#     print('Seu triangulo é equilátero')
# elif ang1 == ang2 or ang1==ang3 or ang2 == ang3:
#     print('Seu triangulo é isóceles')
# else:
#     print('escaleno')
#==========================
#3.9
# idade = int(input('Digite sua idade: '))

# if idade <=3:
#     print('Bebê')
# elif idade <=7:
#     print('Criança')
# elif idade <=12:
#     print('Pré-Adolescente')
# elif idade <=20:
#     print('Adolescente')
# elif idade <=40:
#     print('Jovem')
# elif idade <=64:
#     print('Meia-idade')
# else:
#     print('Idoso')
#========================
#3.10
# idade = int(input('Digite a idade do seu cachorro: '))
# peso = int(input('Digite o peso do seu cachorro: '))
# if idade <= 2:
#     if peso <= 3:
#         idade_humana = idade * 12.5
#     elif 10 <= peso <= 23:
#         idade_humana = idade * 10.5
#     else:
#         idade_humana = idade * 9
# else:
#     if peso <= 3:
#         idade_humana = 2 * 12.5 + (idade - 2) * 5.2
#     elif 10 <= peso <= 23:
#         idade_humana = 2 * 10.5 + (idade - 2) * 5.7
#     else:
#         idade_humana = 2 * 9 + (idade - 2) * 7.8
#====================
#3.11
# n = int(input('Digite um valor: '))
# soma = 0 
# for i in range(n):
#     soma+= i ** 2

# print(soma)
# numeros_digitados = []
# numero = float(input("Digite um número (ou 0 para finalizar): "))

# while numero != 0:
#     numeros_digitados.append(numero)
#     numero = float(input("Digite um número (ou 0 para finalizar): "))

# if numeros_digitados:
#     soma = sum(numeros_digitados)
#     media = soma / len(numeros_digitados)
#     print(f"A média dos números digitados é: {media:.2f}")
# else:
#     print("Nenhum número foi digitado.")
#=====================
#3.12
# numeros_digitados = []

# while True:
#     numero = float(input("Digite um número (ou 0 para finalizar): "))
#     if numero == 0:
#         break
#     numeros_digitados.append(numero)

# if numeros_digitados:
#     soma = sum(numeros_digitados)
#     media = soma / len(numeros_digitados)
#     print(f"A média dos números digitados é: {media:.2f}")
# else:
#     print("Nenhum número foi digitado.")
#=====================
#3.13
# n = int(input('Digite um valor: '))
# soma = 0 
# for i in range(n):
#     soma+= i ** 2

# print(soma)
# numeros_digitados = []
# numero = float(input("Digite um número (ou 0 para finalizar): "))

# while numero != 0:
#     numeros_digitados.append(numero)
#     numero = float(input("Digite um número (ou 0 para finalizar): "))

# if numeros_digitados:
#     soma = sum(numeros_digitados)
#     media = soma / len(numeros_digitados)
#     print(f"A média dos números digitados é: {media:.2f}")
# else:
#     print("Nenhum número foi digitado.")
#======================
#3.14
# celsius = int(input('Digite a temperatura em celcius: '))
# for celsius in range(0, 101, 10):
#     fahrenheit = celsius * 9/5 + 32
#     print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")
#3.15
# tamanho = 5

# for i in range(1, tamanho * 2):
#     if i <= tamanho:
#         print("* " * i)
#     else:
#         print("* " * (2 * tamanho - i))
