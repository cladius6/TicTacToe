class TicTacToe:

    def __init__(self):
        self.board = [] 
        self.turn = False
        self.moves = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append(None)
            self.board.append(row)

    def insert_sign(self, position):
        position += -1
        sign = 1 if self.turn else 0
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
                    if self.board[i][j] == 0:
                        sum += 1
                    elif self.board[i][j] == 1:
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
                    if self.board[j][i] == 0:
                        sum += 1
                    elif self.board[j][i] == 1:
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
                if self.board[i][2-i] == 0:
                    sum += 1
                elif self.board[i][2-i] == 1:
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
                if self.board[i][i] == 0:
                    sum += 1
                elif self.board[i][i] == 1:
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
        print(' ----- ')
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == None:
                    print('|' + ' ', end='')
                elif self.board[i][j] == 0:
                    print('|' + 'X', end='')
                else:
                    print('|' + 'O', end='')

            print('|')
            print(' ----- ')


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

