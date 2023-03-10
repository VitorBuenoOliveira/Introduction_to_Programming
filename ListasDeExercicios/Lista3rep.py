#Exerc 1
for x in range(11):
    print((x)**2)


##Jeito do Professor
for x in range(11):
    x2 = x ** 2
    print(f'O Quadrado de {x} é {x2}')
###

#Exerc 2

for x in range(2,21,2): #começa no dois e só usa numeros pares
    x ** 0.5

###

#Exerc 3
soma = 0

for x in range(1,101):
   soma += x #ele vai repetir e somar logo em seguida | equivalente a: (soma = soma + X)
print(soma)
###

#Exerc 4
soma = 0
for x in range(2,101,2):
    print(x)
    if x % 6 == 0 :
        soma += 1
print(soma)

##Jeito do Professor
contador_par = 0
contador_6 = 0

for num in range(1,101):
    if num % 2 == 0:
        contador_par += 1
    if num % 6 == 0:
        contador_6 += 1
    print(num)

print(f'Numeros Pares são {contador_par} e Numeros Divisiveis por 6 são {contador_6}')

    

##
###