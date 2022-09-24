import random

class Game:
    def __init__(self) -> None:
        self.cells = []
    def create_cells(self):
        for i in range(3):
            row = []
            for c in range(3):
                row.append('~')
            self.cells.append(row)
    def player_randomizer(self):
        return random.randint(0,1)
    def action(self, row, col, player):
        self.board[row][col] = player