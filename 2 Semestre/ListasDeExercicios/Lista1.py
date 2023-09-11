#Exerc 1
def maior_numero(lista):
    if not lista:
        return None  # Retorna None se a lista estiver vazia
    maior = lista[0]  # Inicializa com o primeiro número da lista
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
#Exerc 2
def contador_vogais(texto):
    vogais = "aeiouAEIOU"  # Lista de vogais (maiúsculas e minúsculas)
    contador = 0
    
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    
    return contador
#Exerc 3
def verificar_palindromo(texto):
    texto = texto.lower() 
    texto = texto.replace(" ", "")  
    return texto == texto[::-1]  

palindromo1 = "arara"
print(verificar_palindromo(palindromo1)) 

nao_palindromo = "python"
print(verificar_palindromo(nao_palindromo))  

palindromo2 = "A man, a plan, a canal, Panama"
print(verificar_palindromo(palindromo2))  
#Exerc 4
def calcular_media(lista):
    if not lista:
        return None  
    
    total = sum(lista)  
    media = total / len(lista)  
    
    return media
#Exerc 5
def calcular_potencia(base, expoente):
    return base ** expoente
#Exerc 6
def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def encontrar_primos(limite):
    primos = []
    for num in range(2, limite + 1):
        if eh_primo(num):
            primos.append(num)
    return primos
#Exerc 7
def contar_ocorrencias(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador
#Exerc 8
def contar_ocorrencias(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador
#Exerc 9
def verificar_anagrama(str1, str2):
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    if len(str1) != len(str2):
        return False
    
    str1_dict = {}
    str2_dict = {}
    
    for char in str1:
        if char in str1_dict:
            str1_dict[char] += 1
        else:
            str1_dict[char] = 1
    
    for char in str2:
        if char in str2_dict:
            str2_dict[char] += 1
        else:
            str2_dict[char] = 1
    
    return str1_dict == str2_dict
#Exerc 10
def encontrar_substring(string, substring):
    return substring in string
#Exerc 11
def ordenar_lista(lista):
    return sorted(lista)
#Exerc 12
def calcular_raiz_quadrada(numero):
    if numero < 0:
        raise ValueError("Não é possível calcular raiz quadrada de um número negativo")
    
    aproximacao = numero / 2.0
    
    for _ in range(10): 
        aproximacao = 0.5 * (aproximacao + numero / aproximacao)
    
    return round(aproximacao, 2)


numero = 16
raiz_quadrada = calcular_raiz_quadrada(numero)
print(f"A raiz quadrada de {numero} é aproximadamente: {raiz_quadrada}")
#Exerc 13
def quadrado(base, altura):
    for _ in range(altura):
        linha = "* " * base
        print(linha)

base = 5
altura = 3
quadrado(base, altura)
#Exerc 14
def quadrado(base, altura):
    for i in range(altura):
        if i == 0 or i == altura - 1:
            linha = "* " * base
        else:
            linha = "* " + "  " * (base - 2) + "*"
        print(linha)

base = 5
altura = 3
quadrado(base, altura)

