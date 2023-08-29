def isValid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    for i in range(3):
        for j in range(3):
            if board[row - row%3 + i][col - col%3 + j] == num:
                return False
    return True

def solve(board, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    
    if board[row][col] != 0:
        return solve(board, row, col + 1)
    
    for num in range(1,10):
        if isValid(board, row, col, num):
            board[row][col] = num
            if solve(board, row, col + 1):
                return True
        board[row][col] = 0
    return False

board = [[9, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 2],
        [0, 8, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 0],
        [0, 3, 0, 0, 0, 9, 4, 0, 7],
        [0, 1, 9, 0, 6, 0, 0, 0, 0],
        [1, 0, 0, 7, 0, 0, 0, 8, 5],
        [0, 0, 0, 0, 1, 0, 7, 4, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],]

if solve(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
