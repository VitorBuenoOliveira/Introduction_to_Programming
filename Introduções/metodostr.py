t = str(input('Digite um texto: '))

print(t.lower()) # deixa as letras minusculas
print(t.upper()) # deixa as letras maiusculas
print(t.swapcase())# deixa as letras letras minusculas maiusculas e vice e versa
print(t.capitalize())# deixa padrão 
print(t.title())# Deixa toda letra inicial de cada palavra maiuscula
print(t.strip())# Tira os caracteres invisiveis
print(t.rstrip())# Tira todos os espaços a direita
print(t.lstrip())# Tira todos os espaços a esquerda
print(t.center(3))# Centraliza a palavra
print(t.ljust(6))# Centraliza para direita 
print(t.rjust(6))# Centraliza para esquerda
#################

poema = 'Todos esses que aí estão;atravancando meu caminho, Eles passarão...; Eu passarinho!'
print(poema.find('passa')) #Procura a palavra | Se der -1 quer dizer que não existe
print(poema.index('passa')) # Difereça para o find é que da erro 