# Questão 1: Escreva um programa que receba uma string como entrada e retorne a mesma string sem nenhum espaço em branco.
# t  = str(input('Digite uma frase: '))

# print(t.replace(" ",""))


############
# Questão 2: Escreva um programa que receba uma string como entrada e retorne o número de palavras na string

# texto = str(input('Digite uma frase '))
# contador = 0
# for i in range(len(texto)):
#     if texto[i] in ' ':
#         contador +=1
#         print(contador)
############

# Questão 3: Escreva um programa que receba uma string como entrada e retorne a mesma string com as letras em ordem inversa.

# f = str(input('Digite uma frase: '))
# string = f[::-1]
# print(f'A frase que você digitou invertida fica: {format(string)}')

#############

# Questão 4: Escreva um programa que remova todas as vogais de uma string.

# f = str(input("Digite uma palavra: "))

# chars = 'aeiouAEIOU'

# res = f.translate(str.maketrans('','',chars))
# print(res)

# method.translate = O translate()método retorna uma string onde alguns caracteres especificados são substituídos pelo caractere 
# descrito em um dicionário ou em uma tabela de mapeamento.
# Use o maketrans()método para criar uma tabela de mapeamento.
# Se um caractere não for especificado no dicionário/tabela, o caractere não será substituído.
# Se você usar um dicionário, deverá usar códigos ascii em vez de caracteres.
############

# Questão 5: Escreva um programa que receba uma string como entrada e verifique se ela é um palíndromo.

# f = str(input('Digite uma palavra: ')).strip().upper()

# palavras = f.split()
# junto = ''.join(palavras)
# inv = ''
# for letra in range(len(junto) - 1, -1 , -1):
#     inv +=junto[letra]
# if inv == junto:
#     print('Temos um palíndromo: ')
# else:
#     print('A frase digitada não é um palíndromo')
#############

# Questão 6 : Escreva um programa que receba uma string como entrada e retorne a mesma string com todos os caracteres duplicados removidos.
# str_in = 'string de teste'
# resultado = ''
# for char in str_in:
#     if char not in resultado:
#         resultado += char
# print(resultado)
##################

#Questão 7: Escreva um programa que receba uma string como entrada e retorne True se a string contiver apenas caracteres únicos,
#  ou False caso contrário.
# def verifica_caracteres_unicos(): # Só Funciona no Notebook
#     """
#     Verifica se uma string contém apenas caracteres únicos.

#     Retorno:
#     True se a string contém apenas caracteres únicos, False caso contrário.
#     """
#     string = input("Digite a string a ser verificada: ")
#     if len(set(string)) == len(string):
#         return True
#     else:
#         return False

# verifica_caracteres_unicos()
#################
#Questão 8 : Escreva um programa que receba uma string como entrada e retorne a mesma string com todas as letras consecutivas duplicadas reduzidas a uma única letra.
# def reduzir_consecutivas(string):
#     """
#     Reduz todas as letras consecutivas duplicadas de uma string para uma única letra.

#     Argumentos:
#     string -- a string a ser reduzida.

#     Retorno:
#     A string com todas as letras consecutivas duplicadas reduzidas a uma única letra.
#     """
#     nova_string = ''
#     for i in range(len(string)):
#         if i == 0 or string[i] != string[i-1]:
#             nova_string += string[i]
#     return nova_string

# string = input("Digite a string a ser reduzida: ")
# nova_string = reduzir_consecutivas(string)
# print(nova_string)
