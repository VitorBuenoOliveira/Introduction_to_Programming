#Exerc1
num = int(input("Digite um número: "))

if num < 0:
    print("O número precisa ser positivo.")
else:
    print("Contando de", num, "até 0:")
for i in range(num, -1, -1):
    print(i)
#Exerc2
n = 1
t = int(input('tabuada'))
while n < 10:
    print(f'{t}*{n} = {t*n}')
    n+=1
#Exerc3

tenta = 1

while tenta <= 10:
    resp = input("Qual é a capital do Brasil? ")

    if resp.lower() == 'brasilia':
        print('Parabens, voce acertou!')
        break
    elif resp.lower() == 'desistir':
        print('A capital do Brasil é Brasília, obrigado pela participação!')
        break
    elif tenta == 3:
        des = input('Essa já é sua terceira tentativa , quer desistir? ')
        if des.lower() == 'sim':
            print('A capital do Brasil é Brasília , obrigado pela participação')
            break
        elif tenta == 10:
            print('ok, já percebi que você não sabe a resposta. A capital do Brasília')
            break
        
    else:
        print(f'Você Errou, tente novamente {tenta}')
        tenta += 1


#Exerc 4

n = int(input(''))
fatorial = 1
if n == 0:
    print(fatorial)
else:
    while n>=1:
        fatorial *= n
        n-=1

