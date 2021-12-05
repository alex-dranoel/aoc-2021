import re
import numpy as np

x_max = -1
y_max = -1
for l in open('input.txt'):
    x1, y1, x2, y2 = re.sub(' -> ', ',', l.strip()).split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    
    x_max = max(x1, x2, x_max)
    y_max = max(y1, y2, y_max)

print(y_max, x_max)

def solve(part):
    t = np.zeros((y_max + 1 , x_max + 1 ), dtype=int)

    for l in open('input.txt'):
        x1, y1, x2, y2 = re.sub(' -> ', ',', l.strip()).split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        if part == 1 and x1!=x2 and y1!=y2:
            continue

        sx = sy = 1
        if x1 == x2:
            sx = 0
        elif x1 > x2:
            sx = -1
        if y1 == y2:
            sy = 0
        elif y1 > y2:
            sy = -1
        for i in range(max(abs(x2-x1)+1, abs(y2-y1)+1)):
            t[y1+sy*i, x1+sx*i] += 1

    print(f'Part {part}: {(t>=2).sum()}')

solve(1)
solve(2)