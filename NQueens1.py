def isSafe(board, row, col):
    # vertically up
    i, j = row-1,col 
    while(i>=0):
        if board[i][j]=='Q':
            return False
        i-=1
        

    # diagonal left up
    i, j = row-1,col-1 
    while(i>=0 and j>=0):
        if board[i][j]=='Q':
            return False
        i-=1
        j-=1

    # diagonal right up
    i, j = row-1,col+1 
    while(i>=0 and j<len(board)):
        if board[i][j]=='Q':
            return False
        i-=1
        j+=1

    return True

def NQueens(board, row):
    count = 0
    if row == len(board):
        count+=1
        print_board(board)
        return
    for j in range(len(board)):
        if isSafe(board,row,j):
            board[row][j] = 'Q'
            NQueens(board, row+1)
            board[row][j] = '.'



def print_board(board):
        print("---Chess Board---")
        for i in range(len(board)):
            for j in range(len(board)):
                print(board[i][j], end=" ")
            print()

n = 4
board = [['.']*n for _ in range(n)]
NQueens(board, 0)
