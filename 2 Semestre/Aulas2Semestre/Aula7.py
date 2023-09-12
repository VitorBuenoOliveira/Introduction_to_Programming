def divide(numerador:int,denominador:int)->float:
    if denominador == 0:
        print("Operação Invalida")
        return 0
    resultado = numerador/denominador
    return resultado
"""
lista = [] É mutável
tupla = () É imutável
dicionario = {}


vetores = lista      matrizes = lista[listas]
---------------
array
"""
#Lista
doze = []                           #items = [ 0 - 12]  | [1 - 6] | [2 - 10] [3 - 3]

                                    #Size =3
                                    #X = 10
                                
doze.append(12) # Adiciona um valor a lista
doze.append(6)
doze.append(3)
print(len(doze)) # conta quantos caracteres tem na variavel
# doze.pop(0)# remove o valor pela casa 
# doze.remove(3)# remove o valor 12
indice = doze.index(6) #Ele localiza o valor da variavel
print(doze)
print(indice)
doze.reverse()# Ele inverte os caracteres
doze.sort()# Ordena os caracteres da variavel
doze.insert(2,10)
dez = doze
dez[2] = 15
print(doze[2])
onze  = doze.copy()
print(onze)