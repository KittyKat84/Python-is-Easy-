import numpy as np
ROW_COUNT = 6
COLUMN_COUNT = 7

def createBoard():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def validLocation(board,column):
    return board[ROW_COUNT-1][column] == 0

def get_next_open_row(board,column):
    for r in range(ROW_COUNT):
        if board[r][column]== 0:
            return r

def dropPiece(board,row,column,piece):
    board[row][column] = piece

def printBoard(board):
    print(np.flip(board,0))

def winning(board,piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    for c in range(COLUMN_COUNT):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

board = createBoard()
printBoard(board)
gameOver = False
turn = 0

while not gameOver:
    if turn == 0:
        column = int(input("Player 1 please make your selection between 0 and 6:"))
        if validLocation(board,column):
            row = get_next_open_row(board,column)
            dropPiece(board,row,column,1)
            if winning(board, 1):
                print("CONGRATULATIONS PLAYER 1 WINS!")
                gameOver = True
                break
    else:
        column = int(input("Player 2 please make your selection between 0 and 6:"))
        if validLocation(board,column):
            row = get_next_open_row(board,column)
            dropPiece(board,row,column,2)
            if winning(board, 2):
                print("CONGRATULATIONS PLAYER 2 WINS!")
                gameOver = True
                break
    printBoard(board)
    turn += 1
    turn = turn % 2