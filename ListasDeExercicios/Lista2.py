#Exerc 1
dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

idade = 2024 - ano
if (idade > 16):
    if (idade < 18 or idade >= 70):
        print("Seu voto é facultativo.")
    else:
        print("Seu voto é obrigatório.")
else:
    print("Você não pode votar nas eleições de 2024.")

###

# Exerc 2
a = float(input("Digite o valor do primeiro lado: "))
b = float(input("Digite o valor do segundo lado: "))
c = float(input("Digite o valor do terceiro lado: "))

if abs(a) < abs(b) + abs(c) and abs(b) < abs(a) + abs(c) and abs(c) < abs(a) + abs(b):
    if a == b == c:
        print("Triângulo equilátero")
    elif a != b and a != c and b != c:
        print("Triângulo escaleno")
    else:
        print("Triângulo isósceles")
else:
    print("Os valores informados não formam um triângulo.")
        
###

#Exerc 3
ta1 = float(input("Digite o primeiro Angulo: "))
ta2 = float(input("Digite o segundo Angulo:"))
ta3 = float(input("Digite o segundo Angulo:"))

Soma = ta1 + ta2 + ta3

if ta1 < 90 and ta2 < 90 and ta3 < 90:
  print("Seu Triangulo é acutângulo")
elif ta1 > 90 or ta2 > 90 or ta3 > 90:
  print("Seu Triangulo é obtusângulo")
elif ta1 == 90 or ta2 == 90 or ta3 == 90:
  print("Seu Triangulo é retângulo3")
###

#Exerc 4
pay = int(input('Digite seu salário: '))
ano = int(input('Digite seus anos de trabalho: '))

a10 = pay + (10/100)
a8 = pay + (8/100)
a5 = pay + (5/100)
if ano >= 10 :
    print(f'Seu salário vai aumentar 10% {a10}')
elif ano > 6 and ano < 10:
    print(f'Seu salário vai aumentar 8% {a8}')
elif ano < 6:
    print(f'Seu salário vai aumentar 5% {a5}')
###

#Exerc 5
p1 = int(input('Digite o Primeiro Valor: '))
p2 = int(input('Digite o Segundo Valor: '))
cal = str(input('Digite um Operador: '))

soma = p1 + p2
menos = p1 - p2
divisao = p1 % p2
vezes = p1 * p2 
if cal == '+':
    print(f'Você Escolheu o Operador Soma:{p1}+{p2} = {soma}')
elif cal == '-':
    print(f'Você Escolheu o Operador Menos: {p1}-{p2} = {menos}')
elif cal == '%':
    print(f'Você Escolheu o Operador Divisão: {p1} / {p2} = {divisao}')
elif cal == '*':
    print(f'Você Escolheu o Operador Vezes: {p1} x {p2} = {vezes}')
else:
    print('Você Não Escolheu Um Operador ou Falta algum valor')


###

#Exerc 6
import random

opcoes = ['papel', 'pedra', 'tesoura']

escolha_computador = random.choice(opcoes)

escolha_computador

minha_escolha = str(input(f'Escolha uma das {opcoes}'))

if escolha_computador == 'papel' and minha_escolha == 'pedra':
    print(f'O computador ganhou {escolha_computador} X {minha_escolha}')

elif escolha_computador == 'pedra' and minha_escolha == 'papel':
    print(f'Você Ganhou {escolha_computador} X {minha_escolha}')

elif escolha_computador == 'tesoura' and minha_escolha == 'papel':
    print(f'O computador ganhou {escolha_computador} X {minha_escolha}')

elif escolha_computador == 'papel' and minha_escolha == 'tesoura':
    print(f'Você ganhou {escolha_computador} X {minha_escolha}')

elif escolha_computador == 'pedra' and minha_escolha == 'tesoura':
    print(f'O computador ganhou {escolha_computador} X {minha_escolha}')
    
elif escolha_computador == 'tesoura' and minha_escolha == 'pedra':
    print(f'Você Ganhou {escolha_computador} X {minha_escolha}')


### 