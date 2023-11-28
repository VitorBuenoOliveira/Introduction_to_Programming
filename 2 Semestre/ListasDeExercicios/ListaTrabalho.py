
#Exerc1
def merge(intervals):
    if not intervals:
        return []
    merged = sorted(intervals, key=lambda x: x[0])
    result = [merged[0]]
    for i in range(1, len(merged)):
        if merged[i][0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], merged[i][1])
        else:
            result.append(merged[i])
    return result

def sum_intervals(intervals):
    merged = merge(intervals)
    return sum(x[1] - x[0] for x in merged)

intervals = [[1,2], [6, 10], [11, 15]]
print(sum_intervals(intervals))
'''
1.Introdução: A função sum_intervals calcula a soma das durações de todos os intervalos, 
utilizando um algoritmo de merge sort.

2.Definição das funções: As funções merge e sum_intervals são definidas. 
A função merge combina os intervalos e os organiza em ordem crescente. 
A função sum_intervals chama a função merge e calcula a soma das durações dos intervalos.

3.xplicação do algoritmo de merge sort: O algoritmo de merge sort divide a lista em duas metades, 
depois mescla as metades ordenadas novamente. Este processo é repetido até que a lista inteira seja mesclada.

4.Simplificação do código utilizando list comprehension: A função merge pode ser simplificada usando list 
comprehension, tornando o código mais conciso e fácil de entender.

5.Exemplo de uso: O código a seguir define os intervalos e calcula a soma das durações deles:
intervals = [[1,2], [6, 10], [11, 15]]
print(sum_intervals(intervals))

6.O algoritmo de merge sort é utilizado na organização e cálculo das durações dos intervalos. 
A list comprehension simplifica o código, tornando-o mais conciso e fácil de entender. 
O algoritmo é capaz de lidar com intervalos grandes, 
e todos os intervalos testados são subconjuntos do intervalo [-1000000000, 1000000000].
'''
#########################################

#Exerc2
def move_zeros(array):
    non_zeros = [] # armazena os elementos não-zeros
    zeros = 0 # conta a quantidade de zeros

    # percorre a lista, separando os zeros dos outros elementos
    for num in array:
        if num == 0:
            zeros += 1
        else:
            non_zeros.append(num)

    # concatena os zeros ao final da lista de outros elementos
    return non_zeros + [0] * zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3])) # retorna [1, 1, 2, 1, 3, 0, 0]

'''
1.Primeiro, ele separa os zeros dos outros elementos. 
Em seguida, ele concatena os zeros ao final da lista de outros elementos.

2.O algoritmo tem complexidade de tempo, onde n é o tamanho da lista, 
pois ele percorre a lista uma vez para separar os zeros e, em seguida, 
a concatenação dos zeros é uma operação de tempo constante. 
O algoritmo utiliza uma lista auxiliar para armazenar os 
elementos não-zeros.
'''

#####################################

#Exerc3

def rotate_matrix(matrix, direction):
    # Transposição da matriz
    matrix[:] = [[row[i] for row in matrix] for i in range(len(matrix))]

    # Reversão em linha
    if direction == "counter-clockwise":
        matrix[:] = [row[::-1] for row in matrix]

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_matrix(matrix, "counter-clockwise")
print(rotated_matrix)

'''
1.A função rotate_matrix aceita duas entradas: uma matriz de números e uma string que representa a direção da 
rotação ("clockwise" ou "counter-clockwise").

2.A matriz de entrada é um array de arrays, onde cada sub-array contém números. 
No exemplo fornecido, a matriz é composta por três linhas e três colunas.

3.A função começa executando a transposição da matriz. 
A transposição é uma operação que lê a matriz da esquerda para a direita em vez de cima para baixo. 
Em outras palavras, a matriz transposta tem as colunas da matriz original transformadas em linhas.

4.No código, a transposição é realizada usando list comprehension, 
que é uma maneira concisa e elegante de criar listas no Python. 
A função [row[i] for row in matrix] for i in range(len(matrix))] cria uma nova matriz, 
onde cada elemento é a coluna do índice i da matriz original.

5.Depois de transpor a matriz, a função verifica a direção da rotação. 
Se a direção for "counter-clockwise", a função reverterá cada linha da matriz para que ela seja 
girada no sentido anti-horário. Isso é feito usando a notação de fatiamento invertido do Python, 
que cria uma cópia reversa de uma sequência.
'''

def balanced_brackets(n):
    if n == 0:
        return ['']

    balanced_sub_brackets = balanced_brackets(n - 1)
    result = []

    for sub_bracket in balanced_sub_brackets:
        result.append('()' + sub_bracket)

    return result

print(balanced_brackets(4))

'''
1.O código define uma função recursiva chamada parentesis_equilibrados. 
Essa função gera uma lista de strings que representam todas as possibilidades de equilibrar n pares de parênteses.

2.Se n for 0, a função retorna uma string vazia porque não há parênteses para equilibrar.

3.Se n for maior que 0, a função calcula uma lista de parênteses equilibrados para n - 1 pares de parênteses. 
Em seguida, cria uma nova lista chamada resultado.

4.A função percorre cada string na lista parentesis_equilibrados_menos_um. 
Para cada string, ele adiciona uma nova string à lista resultado. Essa nova string 
é a string atual com um par de parênteses adicionado no início e no final.

5.Por fim, a função retorna a lista resultado.

6.Quando a função parentesis_equilibrados é chamada com um argumento de 4, 
ela imprime todas as possibilidades de equilibrar 4 pares de parênteses.
'''

def count_change(amount, denominations):
    count = [0] * (amount + 1)
    count[0] = 1

    for coin in denominations:
        for i in range(coin, amount + 1):
            count[i] += count[i - coin]

    for coin in denominations:
        if coin == amount:
            count[amount] += 1

    return count[amount]

print(count_change(4, [1,2])) # => 3
print(count_change(10, [5,2,3])) # => 4

'''
1.Introdução ao problema: Nós precisamos contar o número de maneiras diferentes de dar 
troco para uma quantidade específica usando um conjunto de denominações.

2.Abordagem: Utilizaremos a programação dinâmica para resolver o problema. 
A ideia é armazenar a contagem de maneiras diferentes de formar cada valor de 0 a amount em um array count.

3.Passo a passo: a. Inicialize o array count com todos os valores como 0, 
exceto o valor de índice 0, que é inicializado como 1. Isso ocorre porque há exatamente uma maneira de 
formar o valor 0, usando zero moedas.

b. Itere sobre cada denominação e, para cada denominação, itere sobre cada valor de coin a amount. 
Para cada par de valores (i.e., cada valor i e sua respectiva denominação), 
adicione o valor correspondente em count ao valor i - coin em count.

c. Retorne o valor em count correspondente ao índice amount, 
que representa a quantidade total de maneiras diferentes de formar a quantidade desejada usando as 
denominações disponíveis.

Exemplo de código em Python:

def count_change(amount, denominations):
    count = [0] * (amount + 1)
    count[0] = 1

    for coin in denominations:
        for i in range(coin, amount + 1):
            count[i] += count[i - coin]

    return count[amount]
4.Análise: O código resolve o problema eficientemente, com um tempo de execução de O(n * amount), 
onde n é o número de denominações.

5.Aplicações: A solução do problema é útil em muitos casos práticos, 
como sistemas de pagamento e otimização de recursos.
'''


def is_word_square(letters):
    n = int(len(letters) ** 0.5)  # Determina a ordem do quadrado

    if n * n != len(letters):
        return False  # O número de letras não forma um quadrado perfeito

    # Inicializa a matriz do quadrado
    word_square = [['' for _ in range(n)] for _ in range(n)]

    # Preenche a matriz com as letras da sequência
    for i in range(n):
        for j in range(n):
            word_square[i][j] = letters[i * n + j]

    # Verifica se as palavras formadas nas linhas são iguais às formadas nas colunas
    for i in range(n):
        row_word = ''.join(word_square[i])
        col_word = ''.join(word_square[j][i] for j in range(n))

        if row_word != col_word:
            return False

    return True

# Exemplo de uso
letters = "AAAAEEEENOOOOPPRRRRSSTTTT"
result = is_word_square(letters)
print(result)  # True

letters = "SATORAREPOTENETOPERAROTAS"
result = is_word_square(letters)
print(result)  # True

letters = "NOTSQUARE"
result = is_word_square(letters)
print(result)  # False