from random import sample

class Board:
    def __init__(self):
        self.row = [3*i+r for i in change_order(range(3)) for r in change_order(range(3))]
        self.column = [3*i+c for i in change_order(range(3)) for c in change_order(range(3))]
        self.nums = change_order(range(1, 10))
        self.board = [[self.nums[pattern(c,r)] for c in self.column] for r in self.row]
        self.answer = [[num for num in row] for row in self.board]
        
    def get_question(self):
        for i in sample(range(81), 60):
             self.board[i//9][i%9] = 0
        return self.board
    
    def get_answer(self):
        return self.answer

def change_order(l):
        return sample(l, len(l))

def pattern(r, c):
     return (3*(r%3) + r//3 + c) % 9

def print_board(board):
    line0  = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    line1  = "║ - │ - │ - ║ - │ - │ - ║ - │ - │ - ║"
    line2  = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    line3  = "╠═══╪═══╪═══╠═══╪═══╪═══╠═══╪═══╪═══╣"
    line4  = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

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

def main():
    board_values = Board()
    answer = board_values.get_answer()
    question = board_values.get_question()
    prompt1 = input("List(l) or Board(b): ")
    if prompt1 == "l":
          for line in question:
               print(f"{line},", sep="")
    elif prompt1 == "b":
          print_board(question)
    prompt2 = input("Answer (y/n): ")
    if prompt2 == "y":
          print_board(answer)

if __name__ == "__main__":
     main()
