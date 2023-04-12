# Escreva um programa que receba uma string como entrada e retorne a mesma string sem nenhum espaço em branco.
# t  = str(input('Digite uma frase: '))

# print(t.replace(" ",""))



# Escreva um programa que receba uma string como entrada e retorne o número de palavras na string

# texto = str(input('Digite uma frase '))
# contador = 0
# for i in range(len(texto)):
#     if texto[i] in ' ':
#         contador +=1
#         print(contador)

# Escreva um programa que receba uma string como entrada e retorne a mesma string com as letras em ordem inversa.

# f = str(input('Digite uma frase: '))
# string = f[::-1]
# print(f'A frase que você digitou invertida fica: {format(string)}')

# Escreva um programa que remova todas as vogais de uma string.

# f = str(input("Digite uma palavra: "))

# chars = 'aeiouAEIOU'

# res = f.translate(str.maketrans('','',chars))
# print(res)

# method.translate = O translate()método retorna uma string onde alguns caracteres especificados são substituídos pelo caractere descrito em um dicionário ou em uma tabela de mapeamento.

# Use o maketrans()método para criar uma tabela de mapeamento.

# Se um caractere não for especificado no dicionário/tabela, o caractere não será substituído.

# Se você usar um dicionário, deverá usar códigos ascii em vez de caracteres.


# Escreva um programa que receba uma string como entrada e verifique se ela é um palíndromo.

# f = str(input('Digite uma palavra: ')).strip().upper()

# palavras = f.split()
# junto = ''.join(palavras)
# inv = ''
# for letra in range(len(junto) - 1, -1 , -1):
#     inv +=junto[letra]
# if inv == junto:
#     print('Temos um palíndromo: ')
# else:
#     print('A frase digitada não é um palíndromo')



