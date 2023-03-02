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
  # Jogo de Adivinhar o numero
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
##