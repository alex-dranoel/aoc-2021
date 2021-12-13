import numpy as np
instr = [l.strip().split(' ')[-1].split('=') for l in open('input.txt') if '=' in l]
arr = [list(map(int, l.strip().split(','))) for l in open('input.txt') if ',' in l]
max_x = max(cell[0] for cell in arr)
max_y = max(cell[1] for cell in arr)

base = np.full((max_y+1, max_x+1), False)
for x,y in arr:
    base[y, x] = True

for i, (axe, v) in enumerate(instr):
    if axe == 'y':
        top = base[:int(v), :]
        bottom = base[int(v)+1:, :]
        base = top | np.flipud(bottom)
    if axe == 'x':
        left = base[:, :int(v)]
        right = base[:, int(v)+1:]
        base = left | np.fliplr(right)
    if i == 0:
        print('Part 1:', np.sum(base == True))

answ = np.full(base.shape, '.')
answ[base] = '#'
print('Part 2:\n' + '\n'.join(''.join(row) for row in answ))
