#Nivel Iniciante

#1.
# vetor = [1,2,3,4,5,6,7,8,9,10]

# soma = sum(vetor)

# print(soma)
#2.
def somar_vetores(vetor1, vetor2):

    if len(vetor1) != len(vetor2):
        print("Os vetores devem ter o mesmo comprimento")
    soma = []

    for i in range(len(vetor1)):
        soma.append(vetor1[i] + vetor2[i])

    return soma

vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]

resultado = somar_vetores(vetor1, vetor2)
print("A soma dos vetores é:", resultado)
#3.






























##########
