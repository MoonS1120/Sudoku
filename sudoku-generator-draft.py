from random import sample

def pattern(r, c):
    # r%3 = index within 3x3 block
    # r//3 = index of block
    # ensures all value are between 0-8
    return (3*(r % 3) + r // 3 + c) % 9

def change_order(s): 
    return sample(s, len(s)) 

def print_sudoku(rows, columns, board):
    columns.insert(0, " ")
    for num in columns:
        print(str(num).center(5, " "), end="")
    print()
    for i in range(9):
        print(str(rows[i]).center(5, " "), end="")
        for j in range(9):
            print(str(board[i][j]).center(5, " "), end="")
        print()

nums = change_order(range(1, 10))
row = [i * 3 + r for i in change_order(range(3)) for r in change_order(range(3))]
column = [i * 3 + c for i in change_order(range(3)) for c in change_order(range(3))]
board = [[nums[pattern(r, c)] for c in column] for r in row]

"""
row = []
for i in change_order(range(3)):
    for row_value in change_order(range(3)):
        row.append(int(i*3+row_value))

column = []
for i in change_order(range(3)):
    for col_value in change_order(range(3)):
        column.append(int(i*3+col_value))

board = []
for row_value in row:
    row_temp =[]
    for col_value in column:
        row_temp.append(nums[pattern(row_value, col_value)])
    board.append(row_temp)
"""

print_sudoku(row, column, board)
