from functools import lru_cache
import math
# hall-way and rooms
#start_board = ((None,)*11, ('B', 'A'), ('C', 'D'), ('B', 'C'), ('D', 'A'))
#start_board = ((None,)*11, ('C', 'B'), ('B', 'D'), ('D', 'A'), ('A', 'C'))
room_size = 2
#start_board = ((None,)*11, ('B', 'D', 'D', 'A'), ('C', 'C', 'B', 'D'), ('B', 'B', 'A', 'C'), ('D', 'A', 'C', 'A'))
start_board = ((None,)*11, ('C', 'D', 'D', 'B'), ('B', 'C', 'B', 'D'), ('D', 'B', 'A', 'A'), ('A', 'A', 'C', 'C'))
room_size = 4

end_board = ((None,)*11, ('A',)*room_size, ('B',)*room_size, ('C',)*room_size, ('D',)*room_size)

target_room = {'A':1, 'B':2, 'C':3, 'D':4}
amphipod_costs = {'A':1, 'B':10, 'C':100, 'D':1000}

@lru_cache(maxsize=None)
def solve_next(board):
    if board == end_board:
        return 0

    # can we move something that is on the hall-way to its room
    min_cost = float(math.inf)
    for i, amphipod in enumerate(board[0]):
        if (i%2 == 0 and i != 0 and i != 10) or amphipod is None:
            continue

        v = target_room[amphipod]
        # as soon as there is a different amphipod in the target room, then it's a no go
        if any(a is not None and a != amphipod for a in board[v]):
            continue
        
        # is the hall-way to the room free of amphipod ?
        # target is to the left
        if not all(c is None for c in board[0][min(2*v, i+1):max(i, 2*v+1)]):
            continue

        n_empty_in_room = sum(c is None for c in board[v])
        cost = (abs(i-2*v) + n_empty_in_room)*amphipod_costs[amphipod]
        hall_way = board[0][:i] + (None,) + board[0][i+1:]
        new_room = (None,) * (n_empty_in_room - 1) + (amphipod,) * (room_size - n_empty_in_room + 1)
        next_cost = solve_next((hall_way,) + board[1:v] + (new_room,) + board[v+1:])
        new_cost = cost + next_cost
        min_cost = min(min_cost, new_cost)
    
    # can we move something from its room to the hall-way or to its proper room
    for i, room in enumerate(board):
        # if i is the hall-way
        if i == 0:
            continue

        # as soon as one amphipod is found and its not the right room, then it's a good move
        if not any(a is not None and target_room[a] != i for a in room):
            continue

        n_empty_in_room = sum(c is None for c in room)
        amphipod = room[n_empty_in_room]
        # can it go somewhere on the right
        for j in range(0, 11):
            # cannot stop on rooms door
            if j % 2 == 0 and j != 0 and j!= 10:
                continue

            if all(c is None for c in board[0][ min(j, 2*i): max(j, 2*i) + 1 ] ):
                cost = (n_empty_in_room + (abs(j-2*i) + 1))*amphipod_costs[amphipod]
                new_src_room = (None,) * (n_empty_in_room + 1) + room[n_empty_in_room+1:]
                hall_way = board[0][:j] + (amphipod,) + board[0][j+1:]
                next_cost = solve_next((hall_way,) + board[1:i] + (new_src_room,) + board[i+1:])
                new_cost = cost + next_cost
                min_cost = min(min_cost, new_cost)

    return min_cost

print(solve_next(start_board))