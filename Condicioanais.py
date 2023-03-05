massa = float(input("Digite Sua Massa: "))
h = float(input("Digite Sua Altura: "))
Cal = massa / (h**2)

if 18.5 < Cal > 24.9:
  print('Seu Peso é normal')



  ###
massa = float(input("Digite Sua Massa: "))
Altura = float(input("Digite Sua Altura: "))

Cal =  massa / (Altura**2)

if Cal < 17:
  print("Você Está Abaixo do Peso ;-;")
if 17.5 < Cal < 18.49:
  print("Você Está no Peso normal")
if 18.50 < Cal < 25:
  print("Você Está Acima do Peso")
if 25 < Cal < 30:
  print("Você Está Com Obesidade I")
if 31 < Cal < 35:
  print("Você Está Com Obesidade II (!!!Severa)")
if 39.99 < Cal < 40:
  print("Você Está Com Obesidade III (!!!Mórbida!!!)")



###


###
#Jogo de Adivinhar o numero
from random import randint

num = randint(1, 10)
num

val = int(input("Chute um numero: "))
if val > num:
  print("Seu numero é maior que o num")
if val < num:
  print("Seu numero é menor que o num")
if val == num:
  print("Você Ganhou o jogo")

print(num)
###
#1
num = float(input("Digite um numero de 1 a 5: "))


if num == 1:
    print("Seu numero não é primo: ")
elif num == 4:
    print("Seu numero não é primo")
else:
    print("Seu numero é primo")
###

###
#2
from random import randint

num1 = randint(1,10)

print(num1)
num2 = float(input("Digite seu numero: "))

if num1 > num2:
   print("O valor numero1 é maior que o numero2")
if num2 > num1:
   print("O valor numero2 é maior que o numero1")
else:
   print("Eles são iguais")
###

###

###
#3 Jogo do Impar e par sem o operador (+)
from random import randint
escolha_paridade = input('escolha seu impar ou par: ')

num_computador = randint(1, 100)

num_usuario = int(input('Escolha seu número: '))

paridade_computador = num_computador % 2

paridade_usuario = num_usuario % 2

paridade_final = 'par'

if(paridade_computador == 0 and paridade_usuario !=0) or (paridade_computador !=0 and paridade_usuario == 0):
  paridade_final = 'impar'

if paridade_computador !=paridade_usuario:
  paridade_final = 'impar'
if paridade_final == escolha_paridade:
  print('Você ganhou')
else:
  print('eu ganhei')

print(num_computador,num_usuario)

###

###
#4
temperatura = float(input("Digite a temperatura da água em graus Celsius: "))

if temperatura < 0:
    print("A água está no estado sólido (gelada)")
elif temperatura >= 0 and temperatura < 100:
    print("A água está no estado líquido")
else:
    print("A água está no estado gasoso (vapor)")


###

###
#5

s = str(input("Digite uma palavra: "))

if 'a'or 'e'or 'i'or 'o' or'u' in s:
    print('tem vogal')
else:
    print('não tem vogal')
###

