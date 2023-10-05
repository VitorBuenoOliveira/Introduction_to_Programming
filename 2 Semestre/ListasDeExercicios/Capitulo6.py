#6.1
def imprimir_frase():
    for _ in range(100):
        print("Romani ite domum")

imprimir_frase()

#6.3
def contar_espacos_em_branco(string):
    contador = 0
    for caractere in string:
        if caractere == ' ':
            contador += 1
    return contador

minha_string = "Esta é uma string com espaços em branco."
quantidade_espacos = contar_espacos_em_branco(minha_string)
print(f"A quantidade de espaços em branco na string é: {quantidade_espacos}")

#6.4
def imprimir_string_invertida(string):
    string_invertida = string[::-1]
    print(string_invertida)

# Exemplo de uso:
minha_string = "celacanto provoca maremoto"
imprimir_string_invertida(minha_string)

#6.5
def eh_palindromo(palavra):
    palavra = palavra.lower()
    palavra_sem_espacos = palavra.replace(" ", "")
    palavra_invertida = palavra_sem_espacos[::-1]

    return palavra_sem_espacos == palavra_invertida

print(eh_palindromo("ovo"))  
print(eh_palindromo("arara")) 
print(eh_palindromo("Python"))
print(eh_palindromo("A man a plan a canal Panama"))

#6.6
def eh_palindromo(palavra):
    palavra = palavra.lower()
    palavra_sem_espacos = palavra.replace(" ", "")
    palavra_invertida = palavra_sem_espacos[::-1]

    return palavra_sem_espacos == palavra_invertida

print(eh_palindromo("Ovo")) 
print(eh_palindromo("arara")) 
print(eh_palindromo("Python")) 
print(eh_palindromo("A man a plan a canal Panama"))

#6.7
def nome_abreviado(nome_completo):
    partes = nome_completo.split()
    abreviacao = ''

    for parte in partes:
        abreviacao += parte[0].upper()

    return abreviacao

nome = "José de Alencar da Silva"
abreviado = nome_abreviado(nome)
print("Nome abreviado:", abreviado)

#6.8
def nome_abreviado(nome_completo):
    partes = nome_completo.split()
    abreviacao = ''

    for parte in partes:
        abreviacao += parte[0].upper()

    return abreviacao

nome = "José de Alencar da Silva"
abreviado = nome_abreviado(nome)
print("Nome abreviado:", abreviado)

#6.9
def nome_abreviado(nome_completo):
    partes = nome_completo.split()
    abreviacao = ''

    if len(partes) >= 2:
        for parte in partes:
            abreviacao += parte[0].upper()
        return abreviacao
    else:
        return "Nome inválido"
    
nome1 = "José de Alencar da Silva"
abreviado1 = nome_abreviado(nome1)
print("Nome abreviado 1:", abreviado1)

nome2 = "Maria Silva"
abreviado2 = nome_abreviado(nome2)
print("Nome abreviado 2:", abreviado2)

nome3 = "Ana"
abreviado3 = nome_abreviado(nome3)
print("Nome abreviado 3:", abreviado3)

#6.10
nome_arquivo = "seu_arquivo.txt"

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read().upper()
        print(conteudo)
        
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

#6.11
nome_arquivo = "seu_arquivo.txt"

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        
        conteudo_minusculo = conteudo.lower()
        
        print(conteudo_minusculo)
        
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")


#6.12
nome_arquivo = "seu_arquivo.txt"

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        
        conteudo_formatado = conteudo.title()
        
        print(conteudo_formatado)
        
except FileNotFoundError:
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

#6.13
nome_arquivo_origem = "arquivo_origem.txt"

nome_arquivo_destino = "arquivo_destino.txt"

try:
    with open(nome_arquivo_origem, 'r') as arquivo_origem:

        with open(nome_arquivo_destino, 'w') as arquivo_destino:
            arquivo_destino.write(arquivo_origem.read())
        print(f"Conteúdo do arquivo de origem '{nome_arquivo_origem}' foi copiado para o arquivo de destino '{nome_arquivo_destino}'.")
except FileNotFoundError:
    print(f"O arquivo de origem '{nome_arquivo_origem}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")

#6.14
nome_arquivo_origem = "arquivo_origem.txt"


nome_arquivo_destino = "arquivo_destino.txt"

try:
    with open(nome_arquivo_origem, 'r') as arquivo_origem:
        with open(nome_arquivo_destino, 'w') as arquivo_destino:
            arquivo_destino.write(arquivo_origem.read())
        print(f"Conteúdo do arquivo de origem '{nome_arquivo_origem}' foi copiado para o arquivo de destino '{nome_arquivo_destino}'.")
except FileNotFoundError:
    print(f"O arquivo de origem '{nome_arquivo_origem}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")


#6.15
import random
import math

nome_arquivo = "pontos.txt"

num_pontos = 1000

def dentro_circulo(x, y):
    return x**2 + y**2 <= 1

try:
    with open(nome_arquivo, 'w') as arquivo:
        pontos_dentro = 0
        
        for _ in range(num_pontos):
            x = random.uniform(0, 1)
            y = random.uniform(0, 1)
            
            if dentro_circulo(x, y):
                pontos_dentro += 1
            
            arquivo.write(f"{x} {y}\n")
        
        valor_pi = 4 * (pontos_dentro / num_pontos)
        
        arquivo.write(f"Valor de pi: {valor_pi}")
        
        print(f"{num_pontos} pontos gerados e armazenados em '{nome_arquivo}'")
        print(f"Valor calculado de pi: {valor_pi}")
except Exception as e:
    print(f"Ocorreu um erro: {str(e)}")








