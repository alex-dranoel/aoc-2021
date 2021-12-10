import numpy as np

m = [list(l.strip()) for l in open('input.txt')]
m = [[int(i) for i in row] for row in m]
m = np.array(m)

n_row, n_col = m.shape
print(m)
bounded_m = np.full((n_row+2, n_col+2), np.max(m) + 1)
bounded_m[1:n_row+1, 1:n_col+1] = m
print(bounded_m)

def local_minima(array2d):
    return ((array2d < np.roll(array2d,  1, 0)) &
            (array2d < np.roll(array2d, -1, 0)) &
            (array2d < np.roll(array2d,  1, 1)) &
            (array2d < np.roll(array2d, -1, 1)))


mimina = local_minima(bounded_m)
print('N mininma:', np.sum(mimina))
print('Part 1:', np.sum(mimina*(bounded_m+1)))


bounded_m = np.full((n_row+2, n_col+2), 9)
bounded_m[1:n_row+1, 1:n_col+1] = m

minima_location = np.where(mimina)
basins_size = []


seen = np.full_like(bounded_m, False)
adj = [(-1, 0), (1, 0), (0, -1), (0, 1)]

basin_coord = []
for i,j in zip(minima_location[0], minima_location[1]):
    basin_size = 1
    basins_size.append(0)
    basin_coord.append((i,j))
    cells_to_check = [(i,j)]
    while len(cells_to_check) != 0:
        r, c = cells_to_check[-1]
        cells_to_check = cells_to_check[:-1]

        if not seen[r, c]:
            seen[r, c] = True
            basins_size[-1] += 1
            adjacents_non_nine = [(r+a, c+b) for a, b in adj if bounded_m[r+a,c+b] < 9]
            cells_to_check.extend(adjacents_non_nine)


a = sorted(basins_size)
print('Part 2:', a[-1], '*', a[-2], '*', a[-3], '=', a[-1]*a[-2]*a[-3])
print(basin_coord[basins_size.index(a[-1])])
print(basin_coord[basins_size.index(a[-2])])
print(basin_coord[basins_size.index(a[-3])])
