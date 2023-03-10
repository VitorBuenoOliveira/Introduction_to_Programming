v =  1
for x in range(2,11,2):#range(start(Aonde começa),stop(Aonde termina !sempre vai teminar no numero anterior),step(quantidade de passos))
    print(v+x)

list(range()) # Usado para listar 


#Exer1
for x in range(11):
    print((x)**2)


##Jeito do Professor
for x in range(11):
    x2 = x ** 2
    print(f'O Quadrado de {x} é {x2}')
###

######################

# Imagine que você tenha um intervalo de números inteiro que 
# vai de 1 até 1000000 e sua tarefa é encontrar o milésimo maior número que seja ímpar e divisível por 17
#%%time = !DECORADOR!
n = 0
for numero in range(1, 1000001):
    if numero % 17 == 0 and numero % 2 != 0:
        n += 1
        if n == 1000:
            print(numero)

#####################



#Break
#Em Python, a palavra-chave break possibilita sair de um loop sempre que essa palavra-chave é executada.
#%%time = !DECORADOR!
n = 0
for numero in range(1, 1000001):
    if numero % 17 == 0 and numero % 2 != 0:
        n += 1
        if n == 1000:
            print(numero)
            break
# #Estrutura for-else
# Eventualmente é necessário que o programa execute algo no caso do loop não ser encerrado pela palavra-chave break. Para casos assim, existe a estrutura for-else.

# Por exemplo, imagine que você queira encontrar o menor número que seja divisível por 11, e diferente deste, dentro de um intervalo de números inteiros. 
# Caso o número seja encontrado, o programa deve imprimir o valor do número. Porém, caso nenhum número seja encontrado, o programa deve imprimir a mensagem 
# "nenhum número foi encontrado".
intervalo = 20
for num in range(1, intervalo+1):
    if num % 11 == 0 and num != 11:
        print(num)
        break
else:
    print('nenhum número foi encontrado')


# Escreva um programa que pede para o usuário acertar o nome de uma fruta em 10 tentativas. 
# A cada interação, o programa deve imprimir o número de tentativas e pedir para que o usuário escolha uma fruta. 
# Caso o usuário acerte a fruta, o programa deve imprimir "Parabéns, você acertou!". 
# Caso o usuário escreva "desisto", o programa deve imprimir "ok, 
# obrigado pela participação". No caso de todas as tentativas se esgotarem, 
# o programa deve imprimir "Suas tentativas acabaram e você não acertou".

### Fase Beta ###
frutas = ["abacaxi","banana"]
tenta = 0
for x in range(10):
    tenta += 1
    escolha =  input(f"Tentativa {tenta}.Escolha uma fruta: ")

    if escolha.lower() == "desisto":
        print("Obrigado pela participação")
        break
    if escolha.lower() in frutas:
        print("Parabéns, você acertou!")
        break