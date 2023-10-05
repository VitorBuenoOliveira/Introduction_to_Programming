# def como_funciona_o_enumerate(lista: list):
#     # contador = 1
#     # for item in lista:
#     #     print(f'{contador} - {item}')
#     #     contador += 1
#     for indice, item in enumerate(lista):
#         print(f'{indice + 1} - {item}')

# frutas = [
#     'laranja',
#     'goiaba',
#     'pera',
#     'maça',
#     'uva',
#     'morango',
#     'jaca',
#     'umbu'
# ]

# como_funciona_o_enumerate(frutas)

##############################
def percorrer_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f'[{i}, {j}]')
a = [50, 10 , 20]
b = [75, 89, 91]
c = [25 ,11, 83]
d = [a,b,c]

percorrer_matriz(d)

