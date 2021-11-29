class TicTacToe:

    def __init__(self):
        self.board = [] 
        self.turn = False
        self.moves = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(' ')
            self.board.append(row)

    def insert_sign(self, position):
        position += -1
        sign = 'O' if self.turn else 'X'
        self.turn = False if self.turn else True
        if 0 <= position <= 2:
            self.board[0][position] = sign
        if 3 <= position <= 5:
            self.board[1][position-3] = sign
        if 6 <= position <= 8:
            self.board[2][position-6] = sign

    def check_win(self):
        if len(self.moves) >= 5:
            sum = 0
            # Check horizontal
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == 'X':
                        sum += 1
                    elif self.board[i][j] == 'O':
                        sum += -1
                if sum == 3:
                    print('X won')
                    return True
                elif sum == -3:
                    print('O won')
                    return True
                else:
                    sum = 0
            # Check vertical
            for i in range(3):
                for j in range(3):
                    if self.board[j][i] == 'X':
                        sum += 1
                    elif self.board[j][i] == 'O':
                        sum += -1
                if sum == 3:
                    print('X won')
                    return True
                elif sum == -3:
                    print('O won')
                    return True
                else:
                    sum = 0
            # Check 2 diagonal
            for i in range(3):
                if self.board[i][2-i] == 'X':
                    sum += 1
                elif self.board[i][2-i] == 'O':
                    sum += -1
                if sum == 3:
                    print('X won')
                    return True
                elif sum == -3:
                    print('O won')
                    return True
            sum = 0
            # Check 1 diagonal
            for i in range(3):
                if self.board[i][i] == 'X':
                    sum += 1
                elif self.board[i][i] == 'O':
                    sum += -1
                if sum == 3:
                    print('X won')
                    return True
                elif sum == -3:
                    print('O won')
                    return True
            sum = 0
            if len(self.moves) == 9 and sum == 0:
                print('Draw!!!')
                return True


    def print_board(self):
        for i in range(3):
            for j in range(3):
                print('|' + self.board[i][j], end='')
            print('|')


def startGame():
    a = TicTacToe()
    a.create_board()
    a.print_board()
    while True:
        move = int(input('Enter your move: '))
        if move in a.moves:
            print('This move is not correct')
        else:
            a.moves.append(move)
            a.insert_sign(move)
            a.print_board()
            a.check_win()


if __name__ == '__main__':
    startGame()

