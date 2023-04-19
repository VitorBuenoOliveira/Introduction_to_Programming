#1
#Professor
# str_in = 'string de teste'
# count = 0
# for char in str_in:
#     if char == ' ':
#         count += 1
        
# print(f'O número de espaços em branco é {count}')
############

#2
# str_in = '  876% de teste  e mais te8te       e mais teste  '
# str_in = str_in.strip()

# count = 0
# palavra = ''
# for char in str_in:
#     if char != ' ':
#         palavra += char
#     else:
#         if palavra.isalpha():
#             count += 1
#         palavra = ''
        
# print(f'O número de plavras é {count+1}')

#############

#3
# str_in = 'string de teste'
# print(str_in[::-1])

#############

#4
# str_in = 'string de teste'
# resultado = ''
# for char in str_in:
#     if char not in 'aAeEiIoOuU':
#         resultado += char
        
# print(resultado)

#5
# str_in = 'somavamos'
# str_in = str_in.lower()

# eh_palindromo = False

# if str_in == str_in[::-1]:
#     eh_palindromo = True
    
# print(eh_palindromo)
###############

#6
# str_in = 'string de teste'
# resultado = ''
# for char in str_in:
#     if char not in resultado:
#         resultado += char
# print(resultado)

###############

#7

# str_in = 'abcd'
# char_unicos = ''
# apenas_unicos = True
# for char in str_in:
#     if char not in char_unicos:
#         char_unicos += char
#     else:
#         apenas_unicos = False
#         break
        
# print(apenas_unicos)

###############

#8

# str_in = 'strrring de testte'
# resultado = ''
# for i, char in enumerate(str_in):
#     if char != str_in[i-1] or i == 0:
#         resultado += char
        
# print(resultado)

################
