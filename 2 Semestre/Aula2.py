# Cria um programa para calcular média e decidir se passou


nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
nota3 = float(input('Digitee sua terceira nota: '))

Total = (nota1 + nota2 + nota3) / 3 

if Total > 6 :
    print('Você foi aprovado!!')
else:
    print('Você foi reprovado :( ')

