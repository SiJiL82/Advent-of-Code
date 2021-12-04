test = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
challenge = [27,14,70,7,85,66,65,57,68,23,33,78,4,84,25,18,43,71,76,61,34,82,93,74,26,15,83,64,2,35,19,97,32,47,6,51,99,20,77,75,56,73,80,86,55,36,13,95,52,63,79,72,9,10,16,8,69,11,50,54,81,22,45,1,12,88,44,17,62,0,96,94,31,90,39,92,37,40,5,98,24,38,46,21,30,49,41,87,91,60,48,29,59,89,3,42,58,53,67,28]

class board:
    def __init__ (self, values):
        self.values = values

def load_boards_from_file(filename):
    boards = []
    values = []
    file = open(filename, "r")
    for line in file:
        row = list(map(int, line.split()))
        if row == []:
            new_board = board(values)
            boards.append(new_board)
            values = []
        else:
            values.append(row)
    file.close()
    return boards

def print_boards(boards):
    for board in boards:
        print_board(board.values)
        print("--------------")

def print_board(board):
    for row in board:
        print(row)


def check_board_for_number(board, number):
    for row in range(0, len(board)):
        for value in range(0, len(board[0])):
            if board[row][value] == number:
                board[row][value] = "X"
                break
        else:
            continue
        break
               

def check_board_for_win(board):
    retval = False
    for column in range(0, len(board[0])):
        column_count = 0
        for row in range(0, len(board)):
            row_count = 0
            if board[row][column] == "X":
                column_count += 1
                if column_count == len(board[0]):
                    retval = True
                    break
            if all(value == "X" for value in board[row]):
                retval = True
                break
        else:
            continue
        break
        
    return retval

def get_board_score(board, multiplier):
    score = 0
    for row in board:
        for value in row:
            if value != "X":
                score += value
    return score * multiplier
            

def calc_bingo_board_winner(numbers, boards):
    for number in numbers:
        for board in boards:
            check_board_for_number(board.values, number)
            winner = check_board_for_win(board.values)
            if winner:
                return get_board_score(board.values, number)

testboards = load_boards_from_file("./Day 4/testinput.txt")
boards = load_boards_from_file("./Day 4/input.txt")


#print(calc_bingo_board_winner(test, testboards))
# 4512            
print(calc_bingo_board_winner(challenge, boards))
64084
        

