# Indexação
# Como as strings são compostas por uma sequência de caracteres, você pode determinar o valor de um caractere em uma determinada posição na string. 
# Chamado de indexação em uma string, esta é a operação mais básica que você pode fazer com este objeto.
# Em ciência da computação, você começa a contar pelo número 0. 
# A figura abaixo mostra um objeto string cujo valor é "Aula de Python". 
# Cada caractere está localizado em um índice. 
# O primeiro caractere em uma string está sempre no índice 0. Para a string "Aula de Python", o último caractere está no índice 13.
# Também é possível fazer a contagem reversa. O último caractere em qualquer string está sempre no índice -1 quando contado de forma reversa. 
# Para a string "Aula de Python", o primeiro caractere, A, está no índice -14. Observe que o espaço também é um caractere.

# string = 'Aula de Python'

# print(string[0]) # retorna o caractere que está na posição com o índice igual a 0 
# print(string[5])
# print(string[8])
# print(string[-1])
# print(string[-8])

# Slicing
# Até o momento, sabemos como obter o caractere localizado em um determinado índice na string. 
# Mas às vezes queremos saber o valor de um grupo de caracteres, começando por um índice e terminando com outro. 
# Digamos que você seja um professor e tenha informações sobre todos os alunos do seu curso no formato “##### PrimeiroNome ÚltimoNome”. 
# Você só está interessado nos nomes e percebe que os seis primeiros caracteres são sempre os mesmos: cinco dígitos e depois um espaço. 
# Você pode extrair os dados que deseja olhando para a parte da string que começa no sétimo caractere até o final da string.
# Extrair dados dessa maneira é chamado de obter uma substring da string. Os colchetes podem ser usados de maneira mais sofisticada. 
# Você pode usá-los para cortar (slicing) a string entre dois índices e obter uma substring, de acordo com certas regras. Para cortar uma string, 
# você pode colocar até três inteiros, separados por dois pontos, entre colchetes:

## [start_index : stop_index : step]
## start_index representa o índice do primeiro caractere a ser usado.
## stop_index representa o índice até o qual você leva os caracteres, mas não incluindo aquele que está na posição indicada pelo stop_index.

# # step representa quantos caracteres pular (por exemplo, considerar cada segundo caractere ou a cada quatro caracteres). 
# # Um step positivo significa que você está indo da esquerda para a direita através da string e vice-versa para um passo negativo. 
# # Não é necessário fornecer explicitamente o valor do step. Se omitido, o step é 1, o que significa que você considera cada caractere.

# Estrutura de Dados

# Exemplos:
# texto = 'Aula de Python' #texto

# print(texto[2]) #escreve só a letra | depende do numero da letra
# print(texto[:4])#Começo
# print(texto[8:])# Final

# for letra in texto:#Escreve tudo
#     print(letra)
    
# for letra in texto[2 : 7 : 0]:
#     print(letra)


# for letra in texto[2:32:2]:
#     print(letra)

# #Escrever em forma alternada
# for x in texto[::2]:
#     print(x)

# c= 'banana' in texto
# print(c)

# print(len(texto))