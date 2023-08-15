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

salario = 1000


if salario == 1000:
    salario*0.20
    print(f'Seu novo Salario é {salario}')
else:
    print('nada mudou :3')
