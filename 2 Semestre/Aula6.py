# import math

# def raiz_quadrada(numero):
#     raiz = numero ** 0.5
#     print(f'{raiz}')
#     return raiz

# def raiz(numero):
#     r = math.sqrt(numero)
#     print(f'{r}')
#     return r
# raiz(4)

#Assinatura da Função
def encontrar_primo(numero: int):
    primos = []
    for i in range(1,numero + 1):
        if e_primo(i):
            primos.append(i)
def e_primo(numero):
    for i in range(2,numero):
        divide = numero % i == 0 
        if divide:
            return False
    return True
        
lista_primos = encontrar_primo(9)
print(lista_primos)