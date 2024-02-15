# l = []
# for x in range(10,1,-2):
#     l.append(x)
# print(l[2:4])

# def rotate_matrix(matrix, direction):
#     # Transposição da matriz
#     matrix[:] = [[row[i] for row in matrix] for i in range(len(matrix))]

#     # Reversão em linha
#     if direction == "counter-clockwise":
#         matrix[:] = [row[::-1] for row in matrix]

#     return matrix

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# rotated_matrix = rotate_matrix(matrix, "clockwise")
# print(rotated_matrix)

def Fatorial(n):
     if (n == 1) or (n == 0):
         return 1
     else:
         return n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5)
