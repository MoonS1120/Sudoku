from random import sample

def pattern(r, c):
    return (3*(r % 3) + r // 3 + c) % 9

def change_order(s): 
    return sample(s, len(s)) 

def expandLine(line):
    return line[0]+(line[1:5]*2+line[1:4]+line[8])*2+line[1:5]*2+line[9:13]

nums = change_order(range(1, 10))
row = [i * 3 + r for i in change_order(range(3)) for r in change_order(range(3))]
column = [i * 3 + c for i in change_order(range(3)) for c in change_order(range(3))]
board = [[nums[pattern(r, c)] for c in column] for r in row]

for i in sample(range(81), 64):
    # i//9 index of row
    # i%9 index within the row (column)
    board[i//9][i%9] = 0

line0  = expandLine("╔═══╤═══╦═══╗")
line1  = expandLine("║ - │ - ║ - ║")
line2  = expandLine("╟───┼───╫───╢")
line3  = expandLine("╠═══╪═══╬═══╣")
line4  = expandLine("╚═══╧═══╩═══╝")

number_txt = " 123456789"
values = [[number_txt[n] for n in row] for row in board]

print(line0)
for i in range(9):
    number_with_line = zip(line1.split("-"), values[i])
    print( "".join(line+number for line, number in number_with_line)+" ║")
    if i//3 in [0,1,2] and i%3 != 2:
        print(line2)
    elif i//3 in [0,1] and i%3 == 2:
        print(line3)
    else:
        print(line4)
