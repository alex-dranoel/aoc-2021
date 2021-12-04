

import numpy as np

# read all
arr = [l.strip() for l in open('input.txt')]

# extract drawn numbers and boards
board_index = -1
boards = []
for i,l in enumerate(arr):
    if i == 0:
        drawn = [int(n) for n in l.split(',')]
        continue

    if l == '':
        board_index += 1
        boards.append([])
        continue

    boards[board_index].append([int(n) for n in l.split()])

# convert boards to numpy array
# and keep a same shape matrix of zeroes for checks
boards_check = []
for i,d in enumerate(boards):
    boards[i] = np.array(boards[i])
    boards_check.append(np.zeros_like(boards[i]))

# returns a tuple of list indication which
# row or col is complete (ie all its elements are True)
def check_board(b):
    rows = np.apply_along_axis(all, axis=1, arr=b)
    cols = np.apply_along_axis(all, axis=0, arr=b)
    return (rows, cols)

# when the board is winning, make the computation
# for the answer.
def compute_answer(v, b, bc, win):
    if any(win[0]):
        row = np.where(win[0] == True)
        to_remove = sum(b[row[0][0],:])

    if any(win[1]):
        col = np.where(win[1] == True)
        to_remove = sum(b[:,col[0][0]])
    
    # this line is applying the mask using 1 - bc so that
    # element that have been checked are zeroed
    # and sum all remaining
    return (np.concatenate(b * (1-bc)).sum()) * v


# Part 2: need to track the index of boards that have
# won already
n_boards = len(boards)
winning_boards = []
for i,v in enumerate(drawn):

    board_to_remove = []
    for j,b in enumerate(boards):

        # Part 2: skipping boards that have won already
        if j in winning_boards:
            continue

        # checking if the current board contains the drawn
        # number and keeping track of it
        result = np.where(b == v)
        if result:
            boards_check[j][result[0], result[1]] = 1

        # checking if the current board has win
        win = check_board(boards_check[j])
        if any(win[0]) or any(win[1]):

            # Part 1: if first winning board, get answer
            if len(winning_boards) == 0:
                part1 = compute_answer(v, b, boards_check[j], win)
                # print(part1)
                # exit()

            # Part 2: if last board to win, get answer
            if len(winning_boards) == n_boards - 1:
                part2 = compute_answer(v, b, boards_check[j], win)
                # print(part2)
                # exit()

            winning_boards.append(j)


print('Part 1:', part1)
print('Part 2:', part2)
