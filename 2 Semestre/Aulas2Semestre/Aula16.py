def mix(s1, s2):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    listaS1 = list(s1) 
    listaS2 = list(s2)

    dicionario = {}

    for i in listaS1:
        if i in alfabeto:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1

    for i in listaS2:
        if i in alfabeto:
            if i in dicionario:
                dicionario[i] += 1
            else:
                dicionario[i] = 1
    filtros1={}
    for K in sorted(dicionario,key=dicionario.get,reverse=True):
        if dicionario[K]>1:
            filtros1[K]=dicionario[K]


    return filtros1

s1 = 'eduardo'
s2 = 'mendes'
print(mix(s1, s2))


# def count(s):
#     count_dict = {}
#     for char in s:
#         if char in count_dict:
#             count_dict[char] += 1
#         else:
#             count_dict[char] = 1
#     return count_dict

# # Testing the function
# print(count("test")) # Output: {'a': 2, 'b': 1}
# print(count(""))     # Output: {}