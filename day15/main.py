import numpy as np
from queue import PriorityQueue

m = np.array([list(map(int, list(l.strip()))) for l in open('input.txt')])
min_m = np.min(m)
n_row, n_col = m.shape
mega_m = np.full((5*n_row, 5*n_col), 0)

for i in range(5):
    for j in range(5):
        sub_m = mega_m[i*n_row:(i+1)*n_row, j*n_col:(j+1)*n_col]
        sub_m += m + (i+j)
        sub_m[sub_m > 9] -= 9 
        mega_m[i*n_row:(i+1)*n_row, j*n_col:(j+1)*n_col] = sub_m

m = mega_m
min_m = np.min(m)
n_row, n_col = m.shape

def get_adj(node):
    offsets = [(0,1), (0,-1), (1,0), (-1,0)]
    for offset in offsets:
        new_r, new_c = node[0] + offset[0], node[1] + offset[1]
        if new_r >= 0 and new_r < n_row and new_c >= 0 and new_c < n_col:
            yield (new_r, new_c)

def get_cost(node):
    return m[node]

def heuristic(goal, node):
    return min_m * (abs(goal[0] - node[0]) + abs(goal[1] - node[1]))

start = (0, 0)
goal = (n_row-1, n_col-1)
frontier = PriorityQueue()
frontier.put(start, 0)
came_from = dict()
cost_so_far = dict()
came_from[start] = None
cost_so_far[start] = 0

while not frontier.empty():
    current = frontier.get()

    if current == goal:
        print(cost_so_far[current])
        break
    
    for next in get_adj(current):
        new_cost = cost_so_far[current] + get_cost(next)
        if next not in cost_so_far or new_cost < cost_so_far[next]:
            cost_so_far[next] = new_cost
            priority = new_cost + heuristic(goal, next)
            frontier.put(next, priority)
            came_from[next] = current
