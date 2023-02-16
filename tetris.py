import random

# Define a largura e a altura do campo de jogo
WIDTH = 10
HEIGHT = 20

# Define as formas das peças do jogo
SHAPES = [
    [(1, 1, 1, 1)],
    [(1, 1, 0), (0, 1, 1)],
    [(0, 1, 1), (1, 1, 0)],
    [(1, 1), (1, 1)],
    [(1, 0, 0), (1, 1, 1)],
    [(0, 0, 1), (1, 1, 1)],
    [(1, 1, 1), (0, 1, 0)],
]

# Define a classe Piece que representa uma peça do jogo
class Piece:
    def _init_(self, shape):
        self.shape = shape
        self.x = WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

# Define a classe Board que representa o campo de jogo
class Board:
    def _init_(self):
        self.grid = [[0] * WIDTH for _ in range(HEIGHT)]

    def add_piece(self, piece):
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[piece.y + y][piece.x + x] = 1

    def remove_full_rows(self):
        rows_cleared = 0
        y = HEIGHT - 1
        while y >= 0:
            if all(self.grid[y]):
                rows_cleared += 1
                del self.grid[y]
                self.grid.insert(0, [0] * WIDTH)
            else:
                y -= 1
        return rows_cleared

    def is_game_over(self):
        return any(self.grid[0])

    def _str_(self):
        return '\n'.join(''.join(str(cell) for cell in row) for row in self.grid)

# Define a função main que executa o jogo
def main():
    board = Board()
    piece = Piece(random.choice(SHAPES))
    while not board.is_game_over():
        board.add_piece(piece)
        print(board)
        board.remove_full_rows()
        piece = Piece(random.choice(SHAPES))
        piece.move_down()
        while all(board.grid[y][x] == 0 for y, row in enumerate(piece.shape) for x, cell in enumerate(row) if cell):
            piece.move_down()
        piece.move_up()
        piece.rotate()
        while all(board.grid[y][x] == 0 for y, row in enumerate(piece.shape) for x, cell in enumerate(row) if cell):
            piece.move_left()
        piece.move_right()

if _name_ == '_main_':
    main()