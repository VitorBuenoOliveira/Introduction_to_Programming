# def maior_numero(lista_numeros):
#     maior = max(lista_numeros)
#     return maior

# lista= [3,2,4,1,2]
# x = maior_numero(lista)
# print(f'O maior numero da lista {x}')



#O mesmo código que o de cima mas sem a biblioteca
# import math
# def maior_numero(lista_numeros):
#     maior = -math.inf
#     for item in lista_numeros:
#         maior = item
#         if maior < item:
#             maior = item
#     return maior
    
# lista = [-1,-2,-3,-4,-5,-6,-17,-18,-20]
# maior = maior_numero(lista)
# print(maior)

#########################
#contador de vogais
                  #Os dois pontos serve para forçar a variavel virar aquele tipo
# def contador_vogais(texto:str):
#     formato = texto.lower()
#     vogais = ['a','e','i','o','u']
#     contador = 0
#     for letra in formato: # pode colocar também texto.lower()
#         if letra in vogais:
#             contador += 1
#     return contador

# total = contador_vogais('Vitor Bueno Oliveira')
# print(f'Quantidade de vogais é : {total}')

###########################################
# para descobrir o numero minimo de uma lista
# import math

# min_value = math.inf

# numbers = [5, 2, 8, 1, 9]

# for num in numbers:
#     if num < min_value:
#         min_value = num

# print("O valor mínimo é:", min_value)
