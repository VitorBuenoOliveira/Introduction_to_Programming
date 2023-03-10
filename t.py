f = str(input('Adivinhe uma fruta: '))
tentativas = 10

for t in range(tentativas+1):
    if f == 'banana':
        print('Você Ganhou o Jogo')
        break
    if f !='banana':
        print('Você Errou a fruta')
        tentativas += 1
    if tentativas == 10:
        print('Acabou suas tentativas')
    if f == 'desistir':
        print('Obrigado')
        break
    
