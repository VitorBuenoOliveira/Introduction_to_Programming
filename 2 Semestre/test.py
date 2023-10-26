# # def contador_letra(texto, letra):
# #     contador = 0

# #     for caractere in texto:
# #         if caractere == letra:
# #             contador += 1 
# #     return contador

# # text = 'Exemplo de texto'

# # letra_contar = 'x'

# # resultado = contador_letra(text,letra_contar)

# # print(f"A letra {letra_contar} aparece {resultado} vezes no texto. ")

# # padrao = 7

# # for i in range(1, padrao):
# #     print('*' * i)

# # for i in range(padrao, 0 , -1):
# #     print('*' * i)



# # def id_var(var):
# #     a = type(var)
# #     if a == int:
# #         b = print('int')
# #     elif a == str:
# #         b = print('string')
# #     elif a == bool:
# #         b = print('bool')
# #     elif a == float:
# #         b = print('float')
# #     else:
# #         b =print('não é nada')
# #     return b 


# # id_var(True)

# #Usanndo Enumerate
# # impares = []

# # for i in range(1,101,2):
# #     impares.append(i)
# # print(impares)
# # for i, v in enumerate(impares):#
# #     impares[i]=v+1
# # print(impares)

# # from random import randint

# # num = randint(1, 10)
# # print(num)

# import numpy as np

# def encontrar_autovalores_e_autovetores(matriz):
#     autovalores, autovetores = np.linalg.eig(matriz)
#     return autovalores, autovetores

# matriz = np.array([[2, -1],
#                    [4,  3]])

# autovalores, autovetores = encontrar_autovalores_e_autovetores(matriz)

# print("Autovalores:")
# print(autovalores)

# print("\nAutovetores:")
# print(autovetores)

# from random import randint

# def criar_campo(tamanho:int) -> list:
#     campo_minado = []
#     for i in range(tamanho):
#         linha = []
#         bomba1= randint(0,tamanho-1)
#         bomba2 = randint(0,tamanho-1)
#         for i in range(tamanho):
#             linha.append('@' if i == bomba1 or i == bomba2 else '')
#         campo_minado.append(linha)

#     return campo_minado

# def menu() -> int:
#     tamanho_matriz = 0
#     continua = True
#     while continua:
#         tamanho_matriz = int(input('Qual o tamanho da matriz: '))
#         continua = tamanho_matriz < 5
#         print('Tamanho inválido' if continua else '')
#     return tamanho_matriz

# def exibir(matriz:list) -> None:
#     for linha in matriz:
#         print(linha)

# tamanho = menu()
# cm = criar_campo(tamanho)
# exibir(cm)

