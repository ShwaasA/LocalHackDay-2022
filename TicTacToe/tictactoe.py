print("\nTIC TAC TOE\n")

board = [['+', '+', '+'], ['+', '+', '+'], ['+', '+', '+']]

def printBoard(board):
    for line in board:
        print(line)
    print()

def makeMove1():
    print("'X's Turn:\n")
    moveX1 = int(input("X Coordinate of 'X' (0-2): "))
    moveY1 = int(input("Y Coordinate of 'X' (0-2): "))
    if board[moveX1][moveY1] == 'O':
        print("\nINVALID MOVE, TRY AGAIN")
        makeMove1()
    else:
        board[moveX1][moveY1] = 'X'

def makeMove2():
    print("'O's Turn:\n")
    moveX2 = int(input("X Coordinate of 'O' (0-2): "))
    moveY2 = int(input("Y Coordinate of 'O' (0-2): "))
    if board[moveX2][moveY2] == 'X':
        print("\nINVALID MOVE, TRY AGAIN")
        makeMove2()
    else:
        board[moveX2][moveY2] = 'O'

def tictactoe():
    printBoard(board)
    makeMove1()
    print()
    printBoard(board)
    makeMove2()

def main():
    global board
    tictactoe()

while(True):
    main()
