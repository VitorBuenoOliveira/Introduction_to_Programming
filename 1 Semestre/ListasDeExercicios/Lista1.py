val1 = 12
val2 = 3.75

texto = "O valor da soma é: "

soma = val1 + val2
print(type(val1))
print(type(val2))
print(type(texto))
print(soma)
print(texto,soma)


#
#Calculo de Fahrenheit
Temp = float(input("Digite sua Temperatura: ")) 
Fah = 1.8 * Temp + 32
Cel = (Temp - 32) / 1.8

print(type(Fah),Fah,type(Cel),Cel)
#

#
#Area do Circulo
r = float(input("Digite o raio: "))

P = 2 * 3.14 * r
A = 3.14 * (r*r)

print(P,A)


#Jeito do Professor

raio = 10
pi = 3.14
#Operação
perimetro = 2 * pi * raio
area = pi * (raio ** 2)

print(f'o perimetro da circunferencia é {perimetro}')
print(f' A area do circulo é {area}')
#


#

#
#Conversor de horas e minutos
min = float(input("Digite os minutos: "))

horas = min // 60

minutos = min % 60

print("Horas:",horas,"Minutos",minutos,)


#



