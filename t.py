# texto = 'Amor é fogo que arde sem se ver É ferida que dói e não se sente  É um contentamento descontente  É dor que desatina sem doer'

# # print(1-len(texto))
# # for letra in texto[2:125:2]:
# #     print(letra)

# # for letra in texto[1:125:2]:
# #     print(letra)

# # print(texto[33:65])
# # c= 0 

# # for letra in texto:
# #         if letra =='s':
# #             c +=1
# #             print(c)

# #### BETA ####
# # contador_r = 0
# # palavras = texto.split()
# # for palavra in palavras:
# #     if palavra.endswith('r'):
# #         contador_r += 1
# # print("O texto tem", contador_r, "palavras que terminam com a letra 'r'.")

# ##### Minha Estrutura #####
# # cont = 0 
# # t = texto.split()

# # for texto in t:
# #     if texto.endswith('r'):
# #         cont +=1 
# # print(cont)

#Contador de 'r'
# texto = 'Amor é fogo que arde sem se ver; É ferida que dói e não se sente; É um contentamento descontente; É dor que desatina sem doer;'
# contador = 0
# for i in range(len(texto)):
#     if texto[i] in ' ;' and texto[i-1]== 'r':
#       if texto [-1 == 'r']:
#         contador +=1
#         print(contador)




















# senha_incompleta = True
# while senha_incompleta:
#   tamanho = False
#   vogal = False
#   simbolos = False
#   numeros = False
#   maiuscula = False

#   mensagem_tamanho = 'A senha deve ter entre 6 a 12 caracteres'
#   mensagem_vogal = ' A senha deve conter ao menos uma vogal'
#   mensagem_simbolos = 'A senha deve conter ao menos um simbolo(@#$%&)'
#   mensagem_numeros = ' A senha conter ao menos um digito numerico'
#   mensagem_maiuscula = ' A sena deve conter ao menos uma letra maiuscula'

#   senha = input('Senha: ')

#   if  6 <= len(senha) <= 12:
#     mensagem_tamanho = ''
#     tamanho = True
    
#   for char in senha:
#     if char in 'aeiou':
#       if not vogal:
#         vogal = True
#         mensagem_vogal = ''
#     if char.isupper():
#       if not maiuscula:
#         maiuscula = True
#         mensagem_maiuscula = ''

#     if char in '@#$%&':
#       if not simbolos:
#         simbolos = True
#         mensagem_simbolos = ''
    
#     if char in '0123456789':
#       if not numeros:
#         numeros = True
#         mensagem_numeros = '';

#   if tamanho and vogal and simbolos and numeros and maiuscula:
#     senha_incompleta = False
#   else:
#     print(mensagem_tamanho)
#     print(mensagem_vogal)
#     print(mensagem_simbolos)
#     print(mensagem_numeros)
#     print(mensagem_maiuscula)
# print('Sua senha foi criada com sucesso')