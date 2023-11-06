#1
# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n-1)

# result = fatorial(3)

# print(f'fatorial {result}')


#2
def soma_digitos(numero):
    if numero == 0:
        return 0
    else:
        ultimo_digito = numero % 10
        return ultimo_digito + soma_digitos(numero // 10)
    
t = soma_digitos(251183)
print(f'seu valor é {t}')

#3
# def soma_quadrados(n):
#     if n == 0:
#         return 0
#     else:
#         return n**2 + soma_quadrados(n - 1)

#4
# def contagem_regressiva(n):
#     if n <= 0:
#         return
#     else:
#         print(n)
#         contagem_regressiva(n - 1)

# t = contagem_regressiva()
# print(f'contagem regressiva{t}')
