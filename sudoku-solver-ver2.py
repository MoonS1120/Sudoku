from random import sample

def pattern(r, c):
    return (3*(r % 3) + r // 3 + c) % 9

def change_order(s): 
    return sample(s, len(s)) 

nums = change_order(range(1, 10))
row = [i * 3 + r for i in change_order(range(3)) for r in change_order(range(3))]
column = [i * 3 + c for i in change_order(range(3)) for c in change_order(range(3))]
board = [[nums[pattern(r, c)] for c in column] for r in row]

def isValid(grid, row, col, number):
    for i in range(9):
        if grid[row][i] == number or grid[i][col] == number:
            return False

    corner_row = row - row%3
    corner_col = col - col%3
    for i in range(3):
        for j in range(3):
            if grid[corner_row + i][corner_col + j] == number:
                return False
    return True

def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    
    if grid[row][col] != 0:
        return solve(grid, row, col + 1)
    
    for num in range(1,10):
        if isValid(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

if solve(board, 0, 0):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
