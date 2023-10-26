#6.1
def exibir_frase():
    for _ in range(100):
        print('Romani ite domum')

exibir_frase()

#6.3
def contar_espacos(string):
    contador = 0
    for caractere in string:
        if caractere.isspace():
            contador += 1
    return contador

minha_string = "Este é um exemplo de frase com espaços em branco."
quantidade_espacos = contar_espacos(minha_string)
print(f"A quantidade de espaços em branco na string é: {quantidade_espacos}")

#6.4
def inverter_string(string):
    string_invertida = string[::-1]
    print(string_invertida)

minha_string = "celacanto provoca maremoto"
inverter_string(minha_string)

#6.5
def eh_palindromo(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

palavra = "arara"
if eh_palindromo(palavra):
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")

#6.6
def eh_palindromo(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]

palavra = "Ovo"
if eh_palindromo(palavra):
    print(f"'{palavra}' é um palíndromo.")
else:
    print(f"'{palavra}' não é um palíndromo.")

#6.7
def eh_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    return frase == frase[::-1]

frase = "Seco de raiva coloco no colo caviar e doces"
if eh_palindromo(frase):
    print(f"A frase '{frase}' é um palíndromo.")
else:
    print(f"A frase '{frase}' não é um palíndromo.")

#6.8
def nome_completo():
    partes_nome = []

    while True:
        parte = input("Digite uma parte do nome (ou deixe em branco para encerrar): ")
        if parte:
            partes_nome.append(parte)
        else:
            break

    nome_composto = " ".join(partes_nome)
    print(f"Nome completo: {nome_composto}")

nome_completo()
#6.9
def nome_completo():
    partes_nome = []

    while True:
        parte = input("Digite uma parte do nome (ou deixe em branco para encerrar): ")
        if parte:
            partes_nome.append(parte)
        elif len(partes_nome) >= 2:
            break
        else:
            print("Você deve inserir pelo menos duas partes para formar um nome completo.")

    nome_composto = " ".join(partes_nome)
    print(f"Nome completo: {nome_composto}")

nome_completo()

#6.10
nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

    conteudo_maiusculas = conteudo.upper()

    print("Conteúdo do arquivo em maiúsculas:")
    print(conteudo_maiusculas)
except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#6.11
nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

    conteudo_minusculas = conteudo.lower()

    print("Conteúdo do arquivo em minúsculas:")
    print(conteudo_minusculas)
except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#6.12
nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

    conteudo_com_primeira_letra_maiuscula = conteudo.title()

    print("Conteúdo do arquivo com a primeira letra de cada palavra em maiúscula:")
    print(conteudo_com_primeira_letra_maiuscula)
except FileNotFoundError:
    print(f"Arquivo '{nome_arquivo}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
#6.13
import csv

tabela = []

for celsius in range(301):
    fahrenheit = (celsius * 9/5) + 32
    tabela.append([celsius, fahrenheit])

nome_arquivo = "tabela_temperaturas.csv"

with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["Celsius", "Fahrenheit"])
    for linha in tabela:
        escritor.writerow(linha)

print(f"Tabela de conversão de temperaturas salva em '{nome_arquivo}'.")

#6.14
def copiar_arquivo(origem, destino):
    try:
        with open(origem, 'r') as arquivo_origem:
            conteudo = arquivo_origem.read()

        if not verificar_arquivo(destino):
            with open(destino, 'w') as arquivo_destino:
                arquivo_destino.write(conteudo)
            print(f"Conteúdo de '{origem}' copiado com sucesso para '{destino}'.")
        else:
            resposta = input(f"O arquivo '{destino}' já existe. Deseja sobrescrevê-lo? (S/N): ").strip().lower()
            if resposta == 's':
                with open(destino, 'w') as arquivo_destino:
                    arquivo_destino.write(conteudo)
                print(f"Conteúdo de '{origem}' copiado com sucesso para '{destino}'.")
            else:
                print("Operação cancelada. O arquivo de destino não foi alterado.")
    except FileNotFoundError:
        print(f"Arquivo '{origem}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def verificar_arquivo(arquivo):
    try:
        with open(arquivo, 'r'):
            return True
    except FileNotFoundError:
        return False

arquivo_origem = input("Digite o nome do arquivo de origem: ")
arquivo_destino = input("Digite o nome do arquivo de destino: ")

copiar_arquivo(arquivo_origem, arquivo_destino)

#6.15
import random

def calcular_pi(num_pontos):
    dentro_circulo = 0

    with open("pontos_pi.txt", "w") as arquivo:
        for _ in range(num_pontos):
            x = random.random()
            y = random.random()
            arquivo.write(f"{x} {y}\n")
            if x**2 + y**2 <= 1:
                dentro_circulo += 1

    valor_pi = (dentro_circulo / num_pontos) * 4
    return valor_pi

num_pontos = 100000
valor_pi = calcular_pi(num_pontos)

print(f"Valor estimado de pi com {num_pontos} pontos: {valor_pi}")












